import random


def generate_dicts(N):
    ds = []
    for _ in range(N):
        E = random.random() < 1 / 111
        B = random.random() < 1 / 365

        if E and not B:
            A = random.random() < 0.81
        elif not E and B:
            A = random.random() < 0.92
        elif E and not B:
            A = random.random() < 0.97
        else:
            A = random.random() < 0.0095

        d = {"E": E, "B": B, "A": A}
        ds.append(d)
    return ds


n = 100000
dicts = generate_dicts(n)

# Among the tuples with A=1, what is the fraction where B=1?
filtered_A_true = [x for x in dicts if x["A"]]
count_B_if_A = len([x for x in filtered_A_true if x["B"]])
share_B_if_A = count_B_if_A / len(filtered_A_true)

# Among the tuples with A=1 and E=1, what is the fraction where B=1?
filtered_A_and_E_true = [x for x in dicts if x["A"] and x["E"]]
count_B_if_A_and_E = len([x for x in filtered_A_and_E_true if x["B"]])
share_B_if_A_and_E = count_B_if_A_and_E / len(filtered_A_and_E_true)

print(f"{share_B_if_A=}, {share_B_if_A_and_E=}")

# print(len([x for x in dicts if x["A"] and not x["B"] and not x["E"]]) / len(dicts))
# print(len([x for x in dicts if not x["A"] and not x["B"] and not x["E"]]) / len(dicts))
