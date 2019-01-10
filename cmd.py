#A Python program to disp;ay command line arguments.
import sys

args = sys.argv[1:]
n = len(args)
print("no. of command line args: {}".format(n))
print("The args are : {}".format(args))
print("The args one by one:")
for a in args:
    print(a)
