def mergeSort(L):
    if len(L) > 1:
        mid = len(L)//2
        left = L[:mid]
        right = L[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1


        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1

myList = [4,3,8,5,7,2,1,6]
mergeSort(myList)
print(myList)









