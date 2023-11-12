import math

for a1 in range(2):
    for a2 in range(3):
        for a3 in range(4):
            for a4 in range(5):
                for a5 in range(6):
                    if a1 * 1 + a2 * 2 + a3 * 6 + a4 * 24 + a5 * 120 == 695:
                        print(a1 + a2 + a3 + a4 + a5)
                        print(a1, a2, a3, a4, a5)


