import sys
N = int(sys.stdin.readline())
row = []
res = 0
for _ in range(N):
  tmp = int(sys.stdin.readline())
  row.append(tmp)
row.sort(reverse=True)
for i in range(len(row)-2):
  if row[i] < row[i+1] + row[i+2]:
    res = row[i] + row[i+1] + row[i+2]
    break
if res == 0:
  print(-1)
else:
  print(res)
