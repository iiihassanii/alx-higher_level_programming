#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argslen = len(sys.argv) - 1
    counter = 0
    for i in range(argslen):
        counter += int(sys.argv[i + 1])
    print(counter)
