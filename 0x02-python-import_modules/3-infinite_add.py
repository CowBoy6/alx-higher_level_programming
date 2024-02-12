#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = sys.argv
    if len(a) == 1:
        print("0")
    else:
        sum = 0
        for i in range(len(a)):
            if i != 0:
                sum += int(a[i])
        print("{}".format(sum))
