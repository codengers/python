#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#import datetime
import datetime

name = raw_input("Please enter your name: ")
age = int(raw_input("Please ente your age: "))

#get age diff
ageDiff = 100 - age

now = datetime.datetime.now()
completedAge = now.year+ageDiff

print("#"*60)
print("Hi "+name+",you will complete 100 years in "+ str(completedAge))
print("#"*60)

