import sys, math
input = sys.stdin.readline

a,b = map(int, input().split())

prime=[True] * (int(math.sqrt(b))+1)
prime[1]=False

for i in range(2, int(math.sqrt(b))+1):
  if prime[i]:
    if i**2 > int(math.sqrt(b)):
      break
    for j in range(i**2, int(math.sqrt(b))+1, i):
      prime[j]=False

cnt = 0

for i in range(1, len(prime)):
  if prime[i]:
    tmp = i**2
    while True:
      if tmp<a:
        tmp*=i
        continue
      if tmp>b:
        break
      tmp *= i
      cnt += 1

print(cnt)
