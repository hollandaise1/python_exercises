import numpy as np


def main():

    largest_odd_number(5.7, 8, 11)


def largest_odd_number(x, y, z):
    """Write a program that examines three variables x, y, z
    and prints the largest odd number among them.
    If none of them are odd, it should print a message
    to that effect. """

    odd_number_list = []
    try:
        if int(x) == x and x % 2 != 0:
            odd_number_list.append(x)
        else:
            if int(y) == y and y % 2 != 0:
                odd_number_list.append(y)
            else:
                if int(z) == z and z % 2 != 0:
                    odd_number_list.append(z)
        print(max(odd_number_list))
    except ValueError:
        print("No odd integers are found!")


def larger_odd_number(x, y):
    """Write a program that compares the two numbers and prints the larger odd number"""
    if x == y:
        print("Cannot compare 'cause the two numbers are equal!")
    elif x % 2 != 0 and y % 2 != 0:
        if x > y:
            print("The larger number is: ", x)
        else:
            print("The larger number is: ", y)
    else:
        if x % 2 != 0 and y % 2 == 0:
            print(x)
        elif x % 2 == 0 and y % 2 != 0:
            print("The larger number is: ", y)
        else:
            print("Both numbers are not odd numbers, try another two numbers!")


if __name__ == '__main__':
    main()
