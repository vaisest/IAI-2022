import os
import math

SMALL_NUMBER = 0.00001


def get_occurrences(filename):
    results = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, "..", filename)) as file:
            for line in file:
                count, word = line.strip().split(" ")
                results[word] = int(count)

        return results

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s" % str(e))
        raise


def get_words(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, "..", filename)) as file:
            words = [word for line in file for word in line.split()]

        return words

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class SpamHam:
    """Naive Bayes spam filter
    :attr spam: dictionary of occurrences for spam messages {word: count}
    :attr ham: dictionary of occurrences for ham messages {word: count}
    """

    def __init__(self, spam_file, ham_file):
        self.spam = get_occurrences(spam_file)
        self.ham = get_occurrences(ham_file)

    def evaluate_from_file(self, filename):
        words = get_words(filename)
        return self.evaluate(words)

    def evaluate_from_input(self):
        words = input().split()
        return self.evaluate(words)

    def evaluate(self, words):
        """
        :param words: Array of str
        :return: probability that the message is spam (float)
        """
        # Implement me

        spam_total = sum(self.spam.values())

        def spam_probability(word):
            if word not in self.spam:
                return SMALL_NUMBER
            return self.spam[word] / spam_total

        ham_total = sum(self.ham.values())

        def ham_probability(word):
            if word not in self.ham:
                return SMALL_NUMBER
            return self.ham[word] / ham_total

        # no bias
        log_spamicity = math.log(0.5) - math.log(0.5)

        for word in words:
            log_spamicity += math.log(spam_probability(word)) - math.log(ham_probability(word))

        spamicity = math.exp(log_spamicity)

        # return scaled to 0-1
        return spamicity / (1 + spamicity)  # R / (R + 1)
