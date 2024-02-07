import sys
input = sys.stdin.readline
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)
i = 0
for i in range(N):
    if i+schedule[i][0] <= N:
        dp[i+schedule[i][0]] = max(dp[i+schedule[i][0]], dp[i]+schedule[i][1])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[-1])