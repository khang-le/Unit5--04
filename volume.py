#!/usr/bin/env python3

# Created by: Khang Le
# Created on: November 2019
# This program uses Multiple Parameters

import math


def volume(height, radius):
    # formula

    volume1 = math.pi * radius * radius * height

    return volume1


def main():
    # get user input

    height_value = input("Enter the height of cylinder: ")
    radius_value = input("Enter the radius of cylinder: ")
    try:
        height1 = int(height_value)
        radius1 = int(radius_value)
        calculated = volume(radius=radius1, height=height1)
        print("The volume of the cylinder is: {} cm^3".format(calculated))
    except Exception:
        print("These are not integer")


if __name__ == "__main__":
    main()
