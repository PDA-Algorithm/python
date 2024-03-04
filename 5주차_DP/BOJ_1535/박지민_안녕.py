# 1535 안녕

import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

L = [0] + L     # 인덱스 1부터 쓰기 위해 가장 앞에 0 추가
J = [0] + J

# i번째 사람까지 고려하고 체력이 j일 때 얻을 수 있는 최대 기쁨
# 2차원 배열 / N명의 사람(행), 100까지의 체력(열)
dp = [[0 for _ in range(101)] for _ in range(N+1)]

# 모든 인원과 체력에 대해 최대 기쁨 계산
for i in range(1, N+1):
    for hp in range(1, 101):
        if L[i] <= hp:
            dp[i][hp] = max(dp[i-1][hp], dp[i-1][hp-L[i]] + J[i])
        else:
            dp[i][hp] = dp[i-1][hp]
    
print(dp[N][99])    # N명의 사람을 고려하고, 체력이 99일 때의 최대 기쁨
