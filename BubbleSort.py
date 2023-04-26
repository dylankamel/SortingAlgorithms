def bubbleSort(L):
    n = len(L)

    for i in range(n):

        for j in range(0,n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j + 1], L[j]

myList = [3,6,2,4,1,5]
sortedList = BubbleSort(myList,0)