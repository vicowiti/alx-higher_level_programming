#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    all_args = sys.argv
    all_args.pop(0)
    args_number = len(all_args)
    # check number of args conditionally
    if args_number == 0:
        print("{:d} arguments.".format(args_number))
    if args_number == 1:
        print("{:d} argument:".format(args_number))
        for arg in all_args:
            for index in range(0, args_number):
                print("{:d}: {:s}".format(index + 1, all_args[index]))
    # for more arguments than 1
    if args_number > 1:
        print("{:d} arguments:".format(args_number))
        for arg in all_args:
            print("{:d}: {:s}".format(all_args.index(arg) + 1, arg))
