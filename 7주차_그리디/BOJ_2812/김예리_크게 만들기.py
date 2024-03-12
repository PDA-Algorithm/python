import sys

input = sys.stdin.readline

n = int(input())
road_len = list(map(int, input().split()))
price = list(map(int, input().split()))

tmp = price[0] # 기준 가격
answer = 0
for i in range(n-1):
  if tmp > price[i]: # 기준 가격이 비교 가격보다 커진다면
    tmp = price[i] # 기준 가격을 비교 가격으로 두고
  answer += tmp*road_len[i] # 기준 가격이랑 거리랑 곱해서 결과에 더해줌
print(answer)
