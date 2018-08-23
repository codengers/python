num=raw_input("enter number: ")
num=int(num)
factorial=1
if(num<0):
    print("Factorial doesn't have negative number")
elif(num==0):
    print("Factorial for 0 is 1")
else:
    for i in range(1,num+1):
        print("i = "+str(i))
        factorial = factorial*i
    print("factorial number for "+str(num)+"is:"+str(factorial))
