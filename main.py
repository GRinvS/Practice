
[n,m,k] = [int(i) for i in input().split()]
 
dan = [[0]*(n+1) for i in range((m+1))]
for i in range(k):
    x,y=map(int,input().split())
    dan[x][y]=1
mod = 10**9+7
 
dp = [[0]*(m+1) for i in range(n+1)]
dp[0][0] = 1
 
for i in range(0, n+1):
    for j in range(0, m+1):
        if not dan[i][j]:
            if i > 0:
                dp[i][j] = (dp[i-1][j]+ dp[i][j]) % mod
            if j > 0:
                dp[i][j] = (dp[i][j-1]+  dp[i][j]) % mod
        else:
            continue
        
 
print(dp[n][m]%mod)