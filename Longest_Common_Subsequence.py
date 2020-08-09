import numpy as np


def Subsequence(a,b):
    LCS = np.array([[0 for j in range(len(a)+1)]for i in range(len(b)+1)])
    i = 1
    while i <= len(b):
        j = 1
        while j <= len(a):
            print('running')
            if b[i-1] == a[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
            j += 1
        i += 1

    print(LCS)


Subsequence('aggtab','gxtxayb')