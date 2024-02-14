import sys

input = sys.stdin.readline

n = int(input())
t_list = []
p_list = []
dp = [0] * (n+1) # i번째 날까지 일 했을 때 최대 수익
for _ in range(n):
  t, p = map(int, input().split())
  t_list.append(t)
  p_list.append(p)

for i in range(n-1, -1, -1): #뒤에서부터 확인
  if i+t_list[i] <= n:
    # 오늘 상담 안할 때, 상담 할 경우 중 큰 값
    """
    상담을 할 경우에는
    오늘 날짜의 상담 금액과 p_list[i],
    오늘 날짜 + 오늘 날짜의 상담 기간 i+t_list[i]의 dp 값,
    즉, 오늘 상담을 진행했을 경우,
    상담이 끝났을 때의 최대 수익(dp[i+t_list[i]])값과 (오늘 상담을 진행했으므로)
    오늘의 상담 보수 값을 더해준 값이 최대 수익이다.

    상담을 진행하지 않았을 경우와 오늘의 상담 최대 수익의 max값이 dp[i]값이 된다.
    """
    dp[i] = max(dp[i+1], p_list[i] + dp[i+t_list[i]])
  else:
    dp[i] = dp[i+1]

print(dp[0])