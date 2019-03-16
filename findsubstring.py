#find sub string using find, rfind, index, rindex.
#These methods are useful to locate sub strings in a string.

#Ask user to enter the string input.
str = input("Please enter string: ")
sub = input("Please enter sub string: ")

# Now find substring from string.
try:
  n = str.rindex(sub, 0, len(str))
except ValueError:
  print("Sub string not found")
else:
  print("Sub string found at position: ", n+1)