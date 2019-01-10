#Find area of triangle using pi of math module.
#area of triangle  = pi*r*r

import argparse
import math

#create argument parser object
parser = argparse.ArgumentParser(description="This program used to calculates area of triangle using argparse module")
parser.add_argument("r", type=float, help="Enter radius value in float type.")
args = parser.parse_args()
result = (math.pi*args.r**2)
print("Area of triangle of {} and {} is : {}".format(math.pi, (args.r**2), result))

