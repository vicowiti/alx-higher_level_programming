#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for i in set_1:
        if i in set_2:
            my_list.append(i)
    for j in set_2:
        if j in set_1:
            my_list.append(j)
    return set(my_list)
