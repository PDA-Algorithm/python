import sys; input = sys.stdin.readline

# 최대 회의 개수
# 끝나는 시간으로 정렬

n = int(input())
lst = []
for _ in range(n):
    time = list(map(int, input().split()))
    lst.append(time)

lst.sort(key = lambda x:[x[1], x[0]]) # 정렬 기준을 2개로 해줘야 하네!!
# 1순위. 일찍 끝나는 순
# 2순위. 일찍 시작하는 순

startTime = 0
count = 0

for i in lst:
    if i[0] >= startTime:
        startTime = i[1] # 종료시간을 시작시간으로 넣고 비교
        count += 1

print(count)
