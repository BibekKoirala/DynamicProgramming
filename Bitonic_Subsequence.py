

# Bitonic Subsequence is the longest subsequence with previously increaing and then decreasing subsequence
# We can find longest increasing subsequence and longest decreasing subsequence for each index and
# Add the index values of each to find one
def bitonic(s):

    LIS = [1 for _ in range(len(s))]
    LDS = [1 for _ in range(len(s))]

    i = 1
    while i < len(s):
        j = 0
        while j < i:
            if s[i] > s[j]:
                LIS[i] = max(LIS[j]+1,LIS[i])
            j += 1
        i += 1

    i = len(s) - 2
    while i >= 0:
        j = len(s) - 1
        while j > i:
            if s[i] > s[j]:
                LDS[i] = max(LDS[j] + 1, LDS[i])
            j -= 1
        i -= 1

    print(LIS)
    print(LDS)
    output = 0
    i = 0
    while i < len(LIS):
        output = max(LIS[i] + LDS[i] - 1, output)
        i += 1

    print(output)


bitonic([1,11,2,10,4,5,2,1])

