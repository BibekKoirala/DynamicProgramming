
def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1


def maxLengthChain(arr):
    mergeSort(arr)
    LIC = [1 for _ in range(len(arr))]
    i = 1
    while i < len(arr):
        j = 0
        while j < i:
            if arr[j][1] < arr[i][0]:
                LIC[i] = max(LIC[j] + 1, LIC[i])
            j += 1
        i += 1
    print(arr)
    print(LIC)


maxLengthChain([(5,24),(15,25),(27,40),(50,60)])