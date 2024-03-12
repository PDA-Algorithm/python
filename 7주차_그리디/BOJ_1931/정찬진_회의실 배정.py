import sys

N = int(sys.stdin.readline())
num = []
res = 0
temp = 0
for _ in range(N):
  tmp = list(map(int,sys.stdin.readline().split()))
  num.append(tmp)
num.sort(key=lambda x: (x[1],x[0]))

for n in num:
  if temp <= n[0]:
    temp = n[1]
    res += 1
    
print(res)
