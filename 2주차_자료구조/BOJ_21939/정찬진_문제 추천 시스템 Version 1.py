import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []
check = dict()
for i in range(N):
  num, val = map(int,sys.stdin.readline().split())
  heapq.heappush(min_heap,(val,num))
  heapq.heappush(max_heap,(-val,-num))
  check[num] = 1
T = int(sys.stdin.readline())
for j in range(N,N+T):
  op = list(sys.stdin.readline().split())

  if op[0] == 'add':
    heapq.heappush(min_heap,(int(op[2]),int(op[1])))
    heapq.heappush(max_heap,(-int(op[2]),-int(op[1])))
    if check.get(int(op[1])) == None:
      check[int(op[1])] = 1
    else:
      check[int(op[1])] += 1
      
  elif op[0] == 'recommend':
    dec = int(op[1])
    if dec == 1:
      while max_heap and check[-max_heap[0][1]] == 0:
        heapq.heappop(max_heap)
      print(-max_heap[0][1])
    else:
      while min_heap and check[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)
      print(min_heap[0][1])

  elif op[0] == 'solved':
    check[int(op[1])] = 0

    while max_heap and check[-max_heap[0][1]] == 0:
      heapq.heappop(max_heap)
    while min_heap and check[min_heap[0][1]] == 0:
      heapq.heappop(min_heap)
