import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a>0:
        heapq.heappush(heap, (-a, a))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
