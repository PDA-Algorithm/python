import sys
import math

input = sys.stdin.readline

def isPrime(x):
  if x == 1:
    return False
  for i in range(2,int(math.sqrt(x)+1)):
    if x%i==0:
      return False
  return True

n = int(input())

while True:
  if isPrime(n):
    if str(n) == str(n)[::-1]:
      print(n)
      break
  n+=1
