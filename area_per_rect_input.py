#!/usr/bin/env python3
# Created By: Beni
# Date: February 24, 2025
# Calculates the area and perimeter of a rectangle.


def main():

    L = float(input("Give a length "))
    W = float(input("Now give a width "))
    print("Area is s{}cm^2".format(L * W))
    print("Perimeter is {}cm".format(L + L + W + W))


if __name__ == "__main__":
    main()
