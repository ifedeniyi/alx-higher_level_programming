#!/usr/bin/python3

for i in range(10):
    for j in range(i, 10):
        if i > j or i == j:
            continue

        if not(i == 0 and j < 2):
            print(', ', end='')

        print("{}{}".format(i, j), end='')

print('\n')
