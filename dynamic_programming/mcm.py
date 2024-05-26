def mcm(arr):
    def helper(i, j):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for k in range(i, j):
            val = (arr[i - 1] * arr[k] * arr[j]) + helper(i, k) + helper(k + 1, j)
            mini = min(mini, val)
        dp[i][j] = mini
        return dp[i][j]

    N = len(arr)
    dp = [[-1 for _ in range(N)] for _ in range(N - 1)]
    print(dp)
    return helper(1, N - 1)


print(mcm([10, 30, 5, 60]))
