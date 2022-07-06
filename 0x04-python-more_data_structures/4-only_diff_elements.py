#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_list = []
    for i in set_1:
        all_list.append(i)
    for j in set_2:
        all_list.append(j)
    return set(all_list)
