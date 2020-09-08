# coding: utf-8
import sys

if __name__ == '__main__':
    print(type(sys.argv))
    for i in range(len(sys.argv)):
        print('arg[{}]: {}'.format(i, sys.argv[i]))
