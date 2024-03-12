import sys

n,k = map(int,sys.stdin.readline().split())
m = str(sys.stdin.readline())
res = []

for i in range(n):
  while res and k>0 and res[-1]<m[i]:
    res.pop()
    k -= 1
  res.append(m[i])
while k>0:
  res.pop()
  k-=1
print(''.join(res))
