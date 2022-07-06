#!/usr/bin/bash
def print_sorted_dictionary(a_dictionary):
    new_list = []
    for i in a_dictionary:
        new_list.append(i)
    new_list = sorted(new_list, reverse=False)
    for i in new_list:
        print("{:s}: {}".format(i, a_dictionary[i]))
