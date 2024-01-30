#Heap
import sys
import heapq
input=sys.stdin.readline

T=int(input())
heap=[]
for i in range(0,T):
    temp=int(input())
    if temp==0:
        if not heap:
            print(0)
        else:
            answer=heapq.heappop(heap)
            print(answer*(-1))
    else:
        heapq.heappush(heap,temp*(-1))
