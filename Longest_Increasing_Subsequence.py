# Solution to Longest Increasing Subsequence

arr = [10,22,9,33,21,50,41,60]
length = len(arr)
LIS = [1 for i in range(length)]


def Longest_Increasing_Subsequence():
    i = j = 0
    for i in range(length):
        for j in range(i+1):
            if arr[i] > arr[j] and LIS[i] < LIS[j]+1:
                LIS[i] = LIS[j] + 1


Longest_Increasing_Subsequence()
print(LIS)
