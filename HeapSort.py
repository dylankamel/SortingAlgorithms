def heapify(L, N , i):
    largest = i
    #setting up children nodes
    l = 2 * i + 1
    r = 2 * i + 2
    # checking if a child node is greater than parent node
    if l < N and L[largest] < L[l]:
        largest = l
    if r < N and L[largest] < L[r]:
        largest = r
    #changing root if one of if statements is met and swapping if so
    if largest != i:
        L[i],L[largest] = L[largest],L[i]
        heapify(L,N, largest)

def heapSort(L):
    N = len(L)
    for i in range(N // 2 - 1, -1, -1):
        heapify(L, N, i)
    for i in range(N - 1, 0, -1):
        L[i], L[0] = L[0], L[i]  # swap
        heapify(L, i, 0)


myList = [3,2,5,8,1,4]
heapSort(myList)
print(myList)