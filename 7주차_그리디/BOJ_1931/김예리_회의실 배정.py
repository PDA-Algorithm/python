import sys

input = sys.stdin.readline

times = []
answer = 0

n = int(input())
for _ in range(n):
  times.append(list(map(int, input().split())))

# 종료시각 먼저 오름차순 정렬,
# 시작시각 오름차순 정렬 -> 3 3 처럼 시각 같을 경우 때문에 처리
times.sort(key = lambda x:(x[1],x[0]))
tmp = times[0][1]
for i in range(1, n):
  if tmp <= times[i][0]:
    tmp = times[i][1]
    answer += 1
print(answer+1)
