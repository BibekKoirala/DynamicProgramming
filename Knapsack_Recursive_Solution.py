
# MaxWt ------> Maximum wt the Knapsack can currently contain
# n ----------> Length of arry being processed
# wt ---------> Array with weight of all the values
# val --------> Values  that can be stored in knapsack
# Knapsack is a recursive function. Here we calculate the maximum value that the Knapsack contain

def Knapsack(MaxWt, n, wt, val):
    if MaxWt == 0 or n == 0:
        return 0

    if wt[n-1] > MaxWt:
        return Knapsack(MaxWt, n-1, wt, val)
    else:
        return  max(val[n-1]+Knapsack(MaxWt - wt[n-1], n-1, wt, val), Knapsack(MaxWt,n-1, wt, val))


print(Knapsack(70,4,[10,40,30,20], [60,180,120,100]))
