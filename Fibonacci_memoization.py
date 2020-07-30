# Fibonacci series using memoization
# Big O of this algorithm is n


MemoTable = [None for i in range(41)]


def fib_memo(n):
    if MemoTable[n] is not None:
        return MemoTable[n]
    elif n <= 1:
        MemoTable[n] = n
        return n
    else:
        MemoTable[n] = fib_memo(n-1) + fib_memo(n-2)
        return MemoTable[n]


fib_memo(40)
print(MemoTable)

