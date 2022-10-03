import random


def generate_dicts(N):
    ds = []
    for _ in range(N):
        B = random.random() < 0.9

        R = B and random.random() < 0.9

        I = B and random.random() < 0.95

        G = random.random() < 0.95

        S = I and G and random.random() < 0.99

        M = S and random.random() < 0.99

        # v = [B, R, I, G, S, M]
        d = {"B": B, "R": R, "I": I, "G": G, "S": S, "M": M}
        ds.append(d)
    return ds


n = 100000
dicts = generate_dicts(n)

first_filtered = [x for x in dicts if x["R"] and x["G"] and not x["S"]]
first_B_count = len([x for x in first_filtered if x["B"]])
first_B_share = first_B_count / len(first_filtered)

second_filtered = [x for x in dicts if x["R"] and x["I"] and x["G"]]
second_S_count = len([x for x in second_filtered if x["S"]])
second_S_share = second_S_count / len(second_filtered)

third_filtered = [x for x in dicts if not x["R"] and x["I"] and x["G"]]
third_S_count = len([x for x in third_filtered if x["S"]])
third_S_share = third_S_count / len(third_filtered)


print(f"{first_B_share=}, {second_S_share=}, {third_S_share=}")
