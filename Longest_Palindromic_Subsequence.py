def LPS(s):
    Lookup = [[0 if i != j else 1 for i in range(len(s))] for j in range(len(s))]

    k = 1
    while k < len(s):
        i = 0
        j = k
        while j < len(s):
            if s[i] == s[j]:
                Lookup[i][j] = Lookup[i + 1][j - 1] + 2
            else:
                Lookup[i][j] = max(Lookup[i][j - 1], Lookup[i + 1][j])
            j += 1
            i += 1
        k += 1
    for i in Lookup:
        print(i)


LPS('BABCBAB')
