# Recursive non DP approach
def BCP(n, k):
    if k == 0 or n <= k:
        return 1
    else:
        return BCP(n - 1, k) + BCP(n - 1, k - 1)


print(BCP(4, 2))


# Dynamic Programming Approach

def DynamicBCP(n, k):
    DPA = [[0 for i in range(n + 1)] for j in range(k + 1)]
    i = 0
    while i <= k:
        j = 0
        while j <= n:
            if j == i or i == 0:
                DPA[i][j] = 1
            elif j < i:
                DPA[i][j] = 0
            else:
                DPA[i][j] = DPA[i][j - 1] + DPA[i - 1][j - 1]
            j += 1
        i += 1

    print(DPA[i - 1][j - 1])


DynamicBCP(4, 2)

# Space Optimised Dynamic Programming Approach


def SpaceBCP(n, k):
    SBCP = [0 for i in range(k + 1)]
    SBCP[0] = 1
    i = 0
    while i <= n:
        j = k
        while j > 0:
            if i == j:
                SBCP[j] = 1
            elif i > j:
                SBCP[j] = SBCP[j] + SBCP[j-1]
            j -= 1
        i += 1
    print(SBCP)


SpaceBCP(5, 2)