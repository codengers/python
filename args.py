#To find sum of two given numbers. Save this as args.py
import argparse

#create ArgumentParse class object
parser = argparse.ArgumentParser(description="This program calculates sum of two numbers")

#add two numbers with the names n1 and n2 and type as float
parser.add_argument("n1", type=float, help="Input first number")
parser.add_argument("n2", type=float, help="Input first number")

#retrive the arguments passed to the program
args = parser.parse_args()

#convert n1 and n2 values into float and add them.
result = float(args.n1)+float(args.n2)
print("Sum of two= ", result)