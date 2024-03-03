import sys

n = int(sys.stdin.readline())
price = list(map(int,sys.stdin.readline().split()))
price.insert(0,0)
dp = [0] * 10001
for i in range(1,n+1):
  for k in range(1,i+1):
    dp[i] = max(dp[i],(dp[i-k] + price[k]))
print(dp[n])
