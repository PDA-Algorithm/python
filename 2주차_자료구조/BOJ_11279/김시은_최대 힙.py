import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)