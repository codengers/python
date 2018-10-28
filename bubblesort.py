'''Bubble sort is a sorting algorithm by using adjesent elements to
compare swap it'''
#Ascending order
#create list of number
numList = [3,2,5,1,10,34,15,23,44,54,56,76,54,67,45,90,111,36]
listLength = len(numList)
for i in range(listLength):
    for j in range(0,listLength-i-1):
        print(i, j)
        if numList[j] < numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
print(numList)
