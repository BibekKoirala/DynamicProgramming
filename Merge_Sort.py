import random
res = [None for i in range(6)]


def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res[k] = L[i]
                i += 1
            else:
                res[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            res[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            res[k] = R[j]
            j += 1
            k += 1


merge_sort([12, 11, 13, 5, 6, 7])
print(res)
