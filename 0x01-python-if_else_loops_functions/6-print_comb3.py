#!/usr/bin/python3

for i in range(10):
    for j in range(i, 10):
        if i > j or i == j:
            continue

        print("{}".format(i), end='')
        print("{}".format(j), end=', ')

print('\n')
