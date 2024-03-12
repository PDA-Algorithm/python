import sys
n, x = map(int,sys.stdin.readline().split())
visit = list(map(int,sys.stdin.readline().split()))

tmp = sum(visit[:x])
max_val = tmp
cnt = 1
for i in range(x,n):
  tmp = tmp - visit[i-x] + visit[i]
  if tmp > max_val:
    max_val = tmp
    cnt = 1
  elif tmp == max_val:
    cnt += 1

if max_val != 0:
  print(max_val)
  print(cnt)
else:
  print('SAD')
