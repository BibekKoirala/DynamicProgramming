import numpy as np


def EDP(e,f):
    arr = np.array([[1000000 for i in range(f+1)] for j in range(e+1)])
    i = 1
    while i <= e:
        arr[i][0] = 0
        arr[i][1] = 1
        i += 1

    for j in range(f+1):
        arr[0][j] = 0
        arr[1][j] = j

    i = 2
    while i <= e:
        j = 2
        while j <= f:
            x = 1
            while x <= j:
                res = 1 + max(arr[i-1][x-1], arr[i][j-x])
                if res < arr[i][j]:
                    arr[i][j] = res
                x += 1
            j += 1
        i += 1

    print(arr)


EDP(2,4)
