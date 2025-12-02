"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):

    small_list = list_one
    big_list = list_two

    if len(small_list) > len(big_list):
        small_list = list_two
        big_list = list_one

    def list_a_in_list_b(list_a, list_b, index_b):
        if len(list_a) == 0:
            return True

        if len(list_a) > index_b + len(list_b):
            return False

        for index in range(len(list_a)):
            if list_a[index] !=  list_b[index_b + index]:
                return False
                
        return True

    for index in range(len(big_list)-len(small_list)+1):
        if list_a_in_list_b(small_list, big_list, index):
            if len(list_one) == len(list_two):
                return EQUAL
            if len(list_one) < len(list_two):
                return SUBLIST
            return SUPERLIST

    return UNEQUAL
    
