import math

su = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

max_su = max(su)

for i in su:

    if math.sqrt(i) < max_su:

        for j in su:

            if j > i and j % i == 0:
                print(i, j)

                su.remove(j)

print(su)

