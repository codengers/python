#Sequential or Linear Search
#Sequential search starts at the begining of the list and checks
#every elements of the list.
#Sequential search compares the element with all other elements given in the list.
#If the element is matched, it returns the value index, else it returns -1.

listOfElements = [12, 14, 11, 15, 16]
value = 20
for val in listOfElements:
    if value == val:
        print(listOfElements.index(value))
        break
    else:
        print("Index is not found.")

    
