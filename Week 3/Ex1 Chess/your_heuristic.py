import numpy as np
import chess
import random

# your_heuristic function should return a heuristic value based on the
# board state. the value should be the higher the more likely white
# is to win the game.

# hint: the below example assigns value +1 to each white piece on the
# board irrespective of where on the board and what piece it is, and
# likewise, value -1 to each black piece. it is probably a good idea
# to assign higher values to more important pieces. also, you may want
# to let the score depend on where on the board the pieces are
# located: usually the central squares are considered more important


def your_heuristic(board: chess.Board, verbose=False, piece_values=None):
    # the pieces are encoded as integers as follows:
    # pawn = 1, knight = 2, bishop = 3, rook = 4, queen = 4, king = 5
    # you can use these integers to index the below array
    piece_value = piece_values if piece_values else [None, 0.2, 1, 1, 1, 2, 5]

    score = 0
    pmap = board.piece_map()  # a dictionary with all the pieces of the board
    for square, piece in pmap.items():
        # assign a score to each piece depending (possibly) on the piece
        # type and the square it is in. the square is an integer between
        # 1-64.
        # hints:
        # * you can get the file (the horizontal position, usually labeled
        # as a,b,c,...,h), which is an integer between 0,...,7 by
        # function chess.square_file(square).
        # * you can get the rank (the vertical position, usually labeled
        # as 1,2,3,...,8), which is an integer between 0,...,7 by
        # function chess.square_rank(square)
        # * you can get the type of the piece, which is represented as
        # an integer, see above, in the variable piece.piece_type

        if board.is_fivefold_repetition():
            return 0

        # pawn
        if piece.piece_type == 1:
            if piece.color == chess.WHITE:
                if chess.square_rank(square) >= 6:
                    multiplier = 2.1
                if chess.square_rank(square) == 5:
                    multiplier = 1.3
                if chess.square_rank(square) == 4:
                    multiplier = 1.05
                print(piece)
            piece_score = (
                (1 if piece.color == chess.WHITE else -1) * multiplier * piece_value[1]
            )
        else:
            piece_score = (1 if piece.color == chess.WHITE else -1) * piece_value[
                piece.piece_type
            ]

        # you can use this for debugging
        if verbose:
            print((square, chess.square_rank(square), piece, piece_score))

        score += piece_score

    return score * random.uniform(0.9, 1.1)
