#Python uses else suite with for loop and while loop.
grp = [1, 2, 3, 4, 5, 6]
search = int(input('Please enter the number: '))
for element in grp:
    if search == element:
        print('{}'.format('The element is found'))
        break
else:
    print('{}'.format('The element is not found'))