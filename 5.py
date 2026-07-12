t = int(input())
for k in range(t):
    n, m = map(int, input().split())
    profits = []
    for l in range(n):
        row = list(map(int, input().split()))
        profits.append([0] + row)
    
    dp = [0] * (m + 1)
    
    for i in range(n):
        new_dp = [0] * (m + 1)
        for s in range(m + 1):
            best = 0
            for j in range(s + 1):
                best = max(best, dp[s - j] + profits[i][j])
            new_dp[s] = best
        dp = new_dp
    
    print(dp[m])
