# issue => 최소힙과 최대힙을 동기화하는 것, 중복된 값을 지우기 위해 서로 다른 id를 배정해야하는 것
import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
  min_heap = []
  max_heap = []
  N = int(sys.stdin.readline().strip())
  check = dict()

  for i in range(N):
    cal, num = sys.stdin.readline().split()
    num = int(num)
    
    if cal == "I":
      heapq.heappush(min_heap,(num,i))
      heapq.heappush(max_heap,(-num,i))
      check[i] = 1
    else:
      if num == -1:
        if min_heap:
          check[heapq.heappop(min_heap)[1]] = 0 # 최소힙에서 제거한 후 값을 0으로 변경

      elif num == 1:
        if max_heap:
          check[heapq.heappop(max_heap)[1]] = 0 # 최대힙에서 제거한 후 값을 0으로 변경

    while min_heap and check[min_heap[0][1]] == 0: # 출력하려는 값의 사전번호가 0인 경우 계속 제거
      heapq.heappop(min_heap)
    while max_heap and check[max_heap[0][1]] == 0:
      heapq.heappop(max_heap)
      
  if len(min_heap) == 0 or len(max_heap) ==0:
    print("EMPTY")
  else:
    print(-max_heap[0][0], min_heap[0][0])
