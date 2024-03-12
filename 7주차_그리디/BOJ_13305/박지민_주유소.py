# 13305 주유소
import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))  # 이동 거리 = 필요한 기름
cost = list(map(int, input().split()))     # 도시 별 기름 가격
answer = 0
current = cost[0]

for i in range(N-1):
    if current > cost[i]:
        current = cost[i]
    answer += current * distance[i]

print(answer)
