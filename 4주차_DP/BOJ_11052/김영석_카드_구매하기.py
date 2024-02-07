n = int(input())
p = list(map(int, input().split()))
dp = [0]*(n+1)
i = 0
while i < n:
    for j in range(min(n-i, len(p))):
        dp[i+j+1] = max(dp[i+j+1], dp[i] + p[j])
    i += 1
    
print(dp[n])