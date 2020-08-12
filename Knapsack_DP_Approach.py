
# Dynamic problem solution to the Knapsack probem
# This has some limitation. for higher value of max wt the arbitary space required is increased
# So to solve that issue greedy approach is used.


def Knapsack(val,wt,mxwt):
    n = len(val)
    knapsack = [[0 for i in range(mxwt+1)] for j in range(n+1)]
    i = 0
    while i <= n:
        j = 0
        while j <= mxwt:
            if j == 0 or i == 0:
                knapsack[i][j] = 0
            elif wt[i-1] > j:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(val[i-1]+knapsack[i-1][j-wt[i-1]], knapsack[i-1][j])

            j += 1
        i += 1
    for i in knapsack:
        print(i)
        print('\n')
    print('Maximum value is ', knapsack[n][mxwt])


Knapsack([60, 100, 120], [10,20,30], 50)