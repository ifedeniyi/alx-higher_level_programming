#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
sq2 = my_square.square(4)
print("Area: {} - Perimeter: {}".format(
    my_square.area(), my_square.perimeter()))
print("Area: {} - Perimeter: {}".format(
    sq2.area(), sq2.perimeter()))
print(my_square)
print(sq2)
