n = int(input())
lose = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * 100
for i in range(n):
    for j in range(99, lose[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - lose[i]] + joy[i])

print(max(dp))
