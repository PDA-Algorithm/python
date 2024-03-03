import sys
import math

a, b = map(int,sys.stdin.readline().split())
check = [True for i in range(10000001)]
cnt = 0
def prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if check[i] == True:
      j = 2
      while (i * j <= n):
        check[i * j] = False
        j += 1
prime(10000000)

for i in range(2,10000001):
    if check[i] == True:
        tmp=i
        while i<=b/tmp:
            if i>=a/tmp:
                cnt+=1
            tmp=tmp*i
print(cnt)
