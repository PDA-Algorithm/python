import sys
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  coin = list(map(int,sys.stdin.readline().split()))
  value = int(sys.stdin.readline())
  dp = [0 for _ in range(value+1)]

  dp[0] = 1
  for i in coin:
    for j in range(i,value+1):
      dp[j] = dp[j] + dp[j-i]
  print(dp[-1])
