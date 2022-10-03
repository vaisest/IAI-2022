from perceptron import Perceptron

IMGS_FILE = "mnist-x.data"
CHARS_FILE = "mnist-y.data"


def main():
    """
    Implement the perceptron algorithm in the Perceptron class. After that you can try out the
    values of different number pairs by changing the values of the 'target_char' and
    'opposite_char' variables.
    """
    perc = Perceptron(IMGS_FILE, CHARS_FILE)
    perc.train("7", "5", 100)
    print(perc.test("7", "5"))
    perc.save_weights("weights.bmp")

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    combinations = [(x, y) for x in numbers for y in numbers]
    for x, y in combinations:
        perc.train(x, y, 100)
        rate = perc.test(x, y)
        print(
            f"{x} vs {y}, hit rate {rate:.2f}, error {(1-rate)*100:.2f} %",
            "!!!" if rate < 0.8 else "",
        )


if __name__ == "__main__":
    main()
