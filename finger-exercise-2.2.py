
def main():

   largestOddNumber(4, 2, 3)

def largestOddNumber(x, y, z):
    """Write a program that examines three variables x, y, z
    and prints the largest odd number among them.
    If none of them are odd, it should print a message
    to that effect. """
    largest_num = None
    if x % 2 != 0:
        largest_num = x
    if y % 2 != 0 and y > x:
        largest_num = y
        if z % 2 != 0 and z > y:
            largest_num = z
        else:
            print("The largest odd number among the three is: ", largest_num)
    else:
        print("None of the numbers are odd!")
    return x, y, z


if __name__ == '__main__':
    main()