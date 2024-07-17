"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    solution = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                solution.add((i, j))
    return solution


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_c = copy.deepcopy(board)
    if action not in actions(board):
        raise ValueError
    turn = player(board)
    board_c[action[0]][action[1]] = turn
    return board_c


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]       
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count += 1
    return count == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    value = -2
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
        return value
    

def min_value(board):
    value = 2
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
        return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value = -2
            for action in actions(board):
                maxi = min_value(result(board, action))
                if maxi > value:
                    value = maxi
                    optimal = action
        elif player(board) == O:
            value = 2
            for action in actions(board):
                mini = max_value(result(board, action))
                if mini < value:
                    value = mini
                    optimal = action
        return optimal
