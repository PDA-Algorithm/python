import sys

input = sys.stdin.readline
"""
지그재그로 최댓값 계산하기
X O O O O
O O X O O
이런식으로 건너뛰어서 선택될 수도 있기 때문에
max(i-1, i-2) 확인해주면서 최댓값 계산
"""

t = int(input())

for _ in range(t):
  n = int(input())
  dp = [list(map(int, input().split())) for _ in range(2)]
  # 1 <= n <- 100,000 이기 때문에
  # n > 1 일 때, index 0,1 처리해주기
  if n > 1:
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
  
  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + dp[0][i]
    dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + dp[1][i]

  # 두 줄 중에 max 값 출력하기
  answer = max(dp[0][n-1], dp[1][n-1])
  print(answer)
