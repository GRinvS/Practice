n = int(input())
c = []
for i in range(n):
    row = list(map(int, input().split()))
    c.append(row)
dp = [[0] * n for i in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = 1
for mask in range(1 << n):
    for last in range(n):
        if dp[mask][last] == 0:
            continue
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            if c[last][nxt] == 1:
                new = mask | (1 << nxt)
                dp[new][nxt] += dp[mask][last]
full = (1 << n) - 1
ans = sum(dp[full][i] for i in range(n))
print(ans)
