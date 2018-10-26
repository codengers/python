lower=int(raw_input("Enter a lower number: "))
upper=int(raw_input("Enter a upper number: "))

print("Prime numbers between ",lower, " and ", upper, " are: ")
for num in range(lower, upper+1):
   if num>1:
      for i in range(2, num):
          #print("I am here", i)
          if num%i==0:
             #print(str(num)+" is not a prime number")
             #print(i,"times",num//i,"is",num)
             break
      else:
          print(num, "is a prime number")

    #else:
     #   print(num, "is not a prime number")
    
