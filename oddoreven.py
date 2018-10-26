#this function is used to find even and odd number
#provide lower and upper number. it will list all even and odd numbers

evenNumbers = [];
oddNumbers = [];
def evenOdd(lower, upper):
    for i in range(lower, upper+1):
        if i%2 ==0:
           evenNumbers.append(i)
        else:
           oddNumbers.append(i)
    dictofNumbers={}
    dictofNumbers["Even numbers"] =evenNumbers
    dictofNumbers["Odd numbers"] =oddNumbers

    return dictofNumbers

lowLimit = int(raw_input("Enter lower limit :")) 
upperLimit = int(raw_input("Enter upper limit :"))
print("Here are numbers",evenOdd(lowLimit, upperLimit)) 
