#!/usr/bin/python
if __name__ == "__main__":
    import sys
    a = sys.argv
    if len(a) == 1:
        print("0 arguments.\n")
    elif len(a) == 2:
        print("1 argument:")
        print("1: {}".format(a[1]))
    else:
        print("{} argument:".format(len(a)-1))
        for i in range(int(len(a)-1)):
            print("{}: {}".format(i+1, a[i+1]))
