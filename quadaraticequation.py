# quadratic equation program
# standard quadratic equation is ax**2+bx+c=0
# d = (b**2)-4ac
# x1 = (-b+sqrt(d))/2a
# x2 = (-b-sqrt(d))/2a

import cmath

def quadEq1(a,b,c):
    d = (b**2)-(4*a*c)
    x1 = (-b-cmath.sqrt(d))/(2*a)
    return x1

def quadEq2(a,b,c):
    d = (b**2)-(4*a*c)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    return x2


#input a, b, c
a = float(raw_input("Please enter a value for 'a': "))
b = float(raw_input("Please enter a value for 'b': "))
c = float(raw_input("Please enter a value for 'c': "))

x1 = quadEq1(a,b,c)
x2 = quadEq2(a,b,c)
print("The solutions are {0} and {1}".format(x1, x2))
