from iai_chess import play_game
from your_heuristic import your_heuristic


def wins_share(arr):
    wins = [x for x in arr if x]
    return len(wins) / len(arr)


def losses_share(arr):
    losses = [x for x in arr if not x and x is not None]
    return len(losses) / len(arr)


def draws_share(arr):
    draws = [x for x in arr if x is None]
    return len(draws) / len(arr)


def simulate(values):
    values = [None, 0.2, 1, 1, 1, 2, 5]

    def heuristic_gen(board, verbose=False):
        return your_heuristic(board, verbose=verbose, piece_values=values)

    results = []
    while True:
        results.append(play_game(depth=3, quiet=True, black_heuristic=heuristic_gen))
        print(results, values)
        print(
            f"Wins: {wins_share(results)} Losses: {losses_share(results)} Draws: {draws_share(results)}"
        )


if __name__ == "__main__":
    play_game(depth=3)  # to run a quick game

    # play_game()  # default depth=4, which may take up to 20 minutes
    # play_game(black_heuristic=our_heuristic)  # an even game between two good bots
    # print("asd")
