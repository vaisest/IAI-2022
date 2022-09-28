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


def your_heuristic(board: chess.Board, verbose=False):
    # the pieces are encoded as integers as follows:
    # pawn = 1, knight = 2, bishop = 3, rook = 4, queen = 4, king = 5
    # you can use these integers to index the below array

    # statistics:
    # [None, 1, 1, 1, 1, 1, 1]               Wins: 0.0     Losses: 1.0     Draws: 0.0     n: 54
    # [None, 0.2, 1, 1, 1, 2, 5]             Wins: 0.5325  Losses: 0.38    Draws: 0.0875  n: 400
    # [None, 1, 3.05, 3.33, 5.63, 9.5, 20]   Wins: 0.5756  Losses: 0.3195  Draws: 0.1049  n: 410
    # [None, 1, 2.97, 3.13, 5.02, 9.49, 20]  Wins: 0.6025  Losses: 0.2975  Draws: 0.1     n: 400
    # [None, 1, 3.2, 3.33, 5.1, 8.8, 20]     Wins: 0.6204  Losses: 0.2968  Draws: 0.0827  n: 411
    # [None, 1, 3.2, 3.33, 5.1, 8.8, 12]     Wins: 0.6383  Losses: 0.2793  Draws: 0.0824  n: 376
    # [None, 1, 3.2, 3.33, 5.1, 8.8, 100]    Wins: 0.6016  Losses: 0.3034  Draws: 0.0950  n: 379

    piece_value = [None, 1, 3.2, 3.33, 5.1, 8.8, 12]

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
                else:
                    multiplier = 1
            elif piece.color == chess.BLACK:
                if chess.square_rank(square) >= 4:
                    multiplier = 2.1
                if chess.square_rank(square) == 5:
                    multiplier = 1.3
                if chess.square_rank(square) == 6:
                    multiplier = 1.05
                else:
                    multiplier = 1
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

    return score * random.uniform(0.97, 1.03)
