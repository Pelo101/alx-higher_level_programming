#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        i = 0
        counter = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            counter = counter + 1
    except IndexError:
        pass
    finally:
        print()
    return counter
