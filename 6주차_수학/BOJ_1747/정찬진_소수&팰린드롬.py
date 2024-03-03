import sys
import math
N = int(sys.stdin.readline())
check = [True for i in range(1100001)]
def prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if check[i] == True:
      j = 2
      while (i * j <= n):
        check[i*j] = False
        j += 1
    
prime(1100000)
while True:
  if check[N] == True:
    if N == 1:
      print(N+1)
      break
    is_palin = True
    tmp = str(N)
    for i in range(int(len(tmp)/2)):
      if tmp[i] != tmp[len(tmp)-1-i]:
        is_palin = False
        break
      
    if is_palin:
      print(N)
      break
  N += 1
