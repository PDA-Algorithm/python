import sys
import heapq

heap = []
N = int(sys.stdin.readline())

for i in range(N):
  value = int(sys.stdin.readline())
  if value == 0:
    if not heap:
      print(0)

    else:
      print(heapq.heappop(heap)[1])

  else:
    heapq.heappush(heap,(-value,value))
