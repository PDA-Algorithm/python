import sys

input = sys.stdin.readline

sushi=[]

n,d,k,c = map(int, input().split())

for _ in range(n):
  x = int(input())
  sushi.append(x)

max_len = 0

for i in range(0,n):
  check = set()
  for j in range(k):
    check.add(sushi[(i+j)%n])
  if c not in check:
    check.add(c)
  max_len=max(max_len, len(check))

print(max_len)
