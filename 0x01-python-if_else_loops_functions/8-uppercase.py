#!/usr/bin/python3

def uppercase(str):
    for i in str:
        islower = ord(i) >= 97 and ord(i) <= 122
        print(chr(ord(i) - 32) if islower else i, end='')
    print('\n')
