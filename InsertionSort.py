def insertionSort(L):
    for x in range(1, len(L)):
        while L[x] < L[x-1] and x != 0:
            L[x],L[x-1] = L[x-1],L[x]
            x -= 1

myList = [3,1,34,5,2,8,9,0]
insertionSort(myList)
print(myList)