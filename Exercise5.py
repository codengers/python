#Guess Game One

import random
numberInput = int(raw_input("Please enter numbers between 1 and 9 :"))
randomNumber = random.randint(1, 9)
if numberInput == randomNumber:
   print("You are correct")
elif numberInput < randomNumber:
   print("You guessed low number")
else:
   print("You guessed high number")


