import sys
import heapq

T = int(sys.stdin.readline())

q = []

for i in range(T):
  k = int(sys.stdin.readline())
  for i in range(k):
    order, n = sys.stdin.readline().split()
    
