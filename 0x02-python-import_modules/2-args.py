#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    counter = len(arg) - 1
    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
    for i in range(counter):
        print("{}: {}".format(counter, arg[counter]))