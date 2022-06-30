#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    # initialize the arguments array and remove the filename at index 0
    args_array = sys.argv
    args_array.pop(0)
    # loop through array while updating the total variable
    for arg in args_array:
        total += int(arg)
    print(total)
