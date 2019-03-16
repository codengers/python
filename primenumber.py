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
    


#another pgm to find 10 prime numbers
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
    
num = int(input("Please enter number:" ))
c=1
j=2
while True:
    if prime(j):
        print(j)
        c+=1
    j+=1
    if c>num:
        break
print("total prime number count: {}".format(c))
