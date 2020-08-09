import numpy as np


def EditDis(a,b):
    EDP = np.array([[0 for j in range(len(a)+1)] for i in range(len(b)+1)])
    i = 0
    j = 0
    while i <= len(b):
        j=0
        while j <= len(a):
            if j == 0:
                EDP[i][j] = i
            elif i == 0:
                EDP[i][j] = j
            elif a[j-1] == b[i-1]:
                EDP[i][j] = EDP[i-1][j-1]
            else:
                EDP[i][j] = min(EDP[i-1][j],EDP[i][j-1],EDP[i-1][j-1])+1
            j+=1
        i+=1

    print(EDP[i-1][j-1])


EditDis('march','cart')