#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = []
    for i in my_list:
        if i not in unique_values:
            unique_values.append(i)
    total = 0
    for z in unique_values:
        total += z
    return total
