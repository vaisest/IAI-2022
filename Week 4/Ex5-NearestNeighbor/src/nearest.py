import os
import random

import numpy as np

# from PIL import Image

NUMBER_OF_PIXELS = 28 * 28
IMAGE_SIZE = 28


def get_chars(filename):
    """
    Reads the classes of characters
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, "..", filename)) as file:
            chars = [line[0] for line in file]

        return chars

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


def get_images(filename):
    """
    Reads the images (black pixel is 1, white pixel is 0 in the input)
    Trasnforms (0, 1) values to (-1.0, 1.0)
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vectors = []

    try:
        with open(os.path.join(dir_path, "..", filename)) as file:
            for line in file:
                vectors.append([1 if int(v) == 1 else 0 for v in line.strip().split(",")])

        return vectors

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class Nearest:
    def __init__(self, images, chars):
        idata = get_images(images)
        cdata = get_chars(chars)

        self.data = [{"vector": v, "char": c} for (v, c) in zip(idata, cdata)]
        random.seed()

    def train(self, target_char, opposite_char):
        dataset = self.data[0:5000]
        dataset = [x for x in dataset if x["char"] in (target_char, opposite_char)]

        self.points = dataset

    def test(self, target_char, opposite_char):
        success = 0
        examples = self.data[5000:]

        examples = [e for e in examples if e["char"] in (target_char, opposite_char)]

        dist_sum = 0
        for e in examples:
            min_dist = NUMBER_OF_PIXELS
            closest_point = None
            for point in self.points:
                distance = np.count_nonzero(np.not_equal(point["vector"], e["vector"]))
                if distance < min_dist:
                    min_dist = distance
                    closest_point = point

                    # !!!
                    # without 99%, with 98%, but twice as fast
                    # if distance <= 60:
                    #     break
            if closest_point["char"] == e["char"]:
                dist_sum += min_dist
                success += 1

        # print(dist_sum / len(examples))
        return float(success) / len(examples)

    # def save_weights(self, filename):
    #     """Draws a 28x28 grayscale picture of the weights

    #     :param filename: Name of the file where weights will be saved
    #     """
    #     pixels = [0.01 + 0.98 / (1.0 + float(math.exp(-w))) for w in self.weights]

    #     Image.fromarray(np.array(pixels).reshape(IMAGE_SIZE, IMAGE_SIZE), mode="L").save(
    #         filename
    #     )
