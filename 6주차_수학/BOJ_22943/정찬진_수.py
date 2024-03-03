import sys
import math
import itertools

m,k = map(int,sys.stdin.readline().split())

check = [True for i in range(pow(10,m)+1)]
prime = set()
one = []
for i in range(2,int(math.sqrt(pow(10,m)))+1):
  if check[i] == True:
    j = 2
    while (i * j<=pow(10,m)):
      check[i*j] = False
      j += 1
for i in range(2,pow(10,m)+1):
  if check[i] == True:
    prime.add(i)

# print(prime)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(itertools.permutations(numbers, m))
lst = []
for perm in result:
  if perm[0] == 0:
    continue
  N = int(''.join(map(str, perm)))
  tmp = N
  while tmp % k == 0:
    tmp //= k
  i = 2
  while(i<=int(math.sqrt(tmp))):
    if tmp % i == 0:
      if i in prime and tmp//i in prime:
        j = 2
        while j < N // 2:
          if j in prime and N-j in prime:
            lst.append(N)
            break
          j += 1
      break
    i+= 1
print(len(lst))
