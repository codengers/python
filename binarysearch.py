#Binary Search
#Fast search algorithm with time complexity of O(logn).
#Based on divide and conquer.
#data item should be sorted order.

#list of elements
listOfElements = [10, 14, 19, 26, 31, 42, 44]
low = listOfElements.index(min(listOfElements))
high = listOfElements.index(max(listOfElements))
val = 44
while low <= high:
    mid = (low+high)//2
    if val == listOfElements[mid]:
        print(mid)
    if val > listOfElements[mid]:
        low=mid+1
    else:
        high=mid-1

    

