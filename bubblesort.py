'''Bubble sort is a sorting algorithm by using adjesent elements to
compare swap it'''
#Ascending order
#create list of number
import datetime
def bubble_sort_one(numList):
    a = datetime.datetime.now()
    print(a)
    listLength = len(numList)
    for i in range(listLength):
        for j in range(0,listLength-i-1):
            #print(j,numList[j], numList[j+1], "=", numList[j+1],numList[j])
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
    b = datetime.datetime.now()
    print(b)
    print("time difference", b-a)
    print(numList)    



def bubble_sort_two(numList):
    a = datetime.datetime.now()
    print(a)
    listLength = len(numList)
    for i in range(listLength-1, 0, -1):
        for j in range(i):
            print(i,j,numList[j], numList[j+1], "=", numList[j+1],numList[j])
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
    b = datetime.datetime.now()
    print(b)
    print("time difference", b-a)
    print(numList)


numList = [54,26,93,17,77,31,44,55,20]
bubble_sort_one(numList)
bubble_sort_two(numList)
