def lcs(X, Y):
    m = len(X)
    n = len(Y)

    dp = []
    for i in range(m + 1):
        row = []
        for i in range(n + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                