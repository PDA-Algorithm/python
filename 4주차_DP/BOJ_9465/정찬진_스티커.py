import sys
T = int(sys.stdin.readline())

for _ in range(T):
  n = int(sys.stdin.readline())
  seal = []
  for _ in range(2):
    seal.append(list(map(int,sys.stdin.readline().rstrip().split())))

  # seal[0].insert(0,0)
  # seal[1].insert(0,0)
  dp = [[0 for _ in range(100000)] for _ in range(2)]
  dp[0][0] = seal[0][0]
  dp[1][0] = seal[1][0]
  if n == 1:
    print(max(max(dp[0]),max(dp[1])))
  else:
    dp[0][1] = seal[0][1] + seal[1][0]
    dp[1][1] = seal[0][0] + seal[1][1]
    for i in range(2,n):
      for j in range(2):
        dp[j][i] = seal[j][i] + max(dp[1-j][i-1],dp[1-j][i-2])
    print(max(max(dp[0]),max(dp[1])))
