#this is to find area of triangle program
#formula area=1/2 * b * h, b= breadth and h= height


#define and declare b
breadth = float(raw_input("Please enter breadth: "))
height  = float(raw_input("Please enter height: "))


def areaOfTriangle(b,h):
    print('print breadth: %0.2f' %b)
    print('print height: %0.2f' %h)
    a= (b * h)/2
    return a


areaIs = areaOfTriangle(breadth,height)
print('Area of triangle is %0.2f:' %areaIs)
