#Palindrome

string = raw_input("Please enter string: ")
halfLen = len(string) / 2

#for i in range(halfLen):
#    end = -(i+1)
#    if(string[i] =="" and string[end]==""):
#        print(i, end)
#    elif(string[i] == string[end]):
#        print("This is a palidrome: "+string[i]+"="+string[end])
#    else:
#        print("this is not palindrome")

reversedString = string[::-1]
if reversedString[:halfLen] == string[:halfLen]:
    print("This is palidrome string")
else:
    print("This is not palindrome")
 
#print(reversedString[:halfLen]+"="+string[:halfLen])

