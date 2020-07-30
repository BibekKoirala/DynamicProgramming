# Fibonacci series using Tabulation
# Time complexity Big O of this method is n

LookupTable = [None for i in range(6)]


def fib_tab(n):
    LookupTable[0]=0
    LookupTable[1]=1
    for i in range(2,6):
        LookupTable[i] = LookupTable[i-1] + LookupTable[i-2]


fib_tab(5)
print(LookupTable)

