n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
dp = [0] * n
dp[0] = price[0]
for i in range(n - 1):
    dp[i + 1] = min(dp[i], price[i + 1])
idx = n - 1
ans = 0
while idx:
    ans += dp[idx - 1] * dis[idx - 1]
    idx -= 1
print(ans)
