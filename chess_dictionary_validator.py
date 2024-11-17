"""
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
'5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named
isValidChessBoard() that takes a dictionary argument and returns True or False depending on
if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can
only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from
'1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w'
or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or
'king'. This function should detect when a bug has resulted in an improper chess board.
"""


def check_board_bounds(board):
    chess_board_spaces = [f"{row}{col}" for row in '12345678' for col in 'abcdefgh']
    for space in board.keys():
        if space not in chess_board_spaces:
            return False
    return True


def check_number_of_kings(board):
    if "wking" in board.values() and "bking" in board.values():
        return True
    return False


def check_number_of_pieces(board):
    white_pieces = []
    black_pieces = []

    for piece in board.values():
        if piece[0] == 'w':
            white_pieces.append(piece)
        elif piece[0] == 'b':
            black_pieces.append(piece)

    if len(white_pieces) > 16 or len(black_pieces) > 16:
        return False

    if white_pieces.count('wpawn') > 8 or black_pieces.count('bpawn') > 8:
        return False

    return True


def check_prefix(board):
    prefixes = ['b', 'w']
    for piece in board.values():
        if piece[0] not in prefixes:
            return False
    return True


def is_valid_chess_board(board):
    condition1 = check_board_bounds(board)
    condition2 = check_number_of_kings(board)
    condition3 = check_prefix(board)
    condition4 = check_number_of_pieces(board)

    return condition1 and condition2 and condition3 and condition4