#heap
import sys
import heapq

input=sys.stdin.readline
test=int(input())
for t in range(test):
    k=int(input())
    maxheap = []
    minheap = []
    visited = [False] * k
    for i in range(k):
        ind,num=input().split()
        num=int(num)
        if 'I'==ind:
            heapq.heappush(minheap,(num,i))
            heapq.heappush(maxheap, (-num,i))
            visited[i] = True
        elif 'D'==ind:
            if num==1:
                while maxheap and not visited[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heapq.heappop(maxheap)
            elif num==-1:
                while minheap and not visited[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visited[minheap[0][1]] = False
                    heapq.heappop(minheap)
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)

    if not minheap or not maxheap:
        print("EMPTY")
    else:
        print(-maxheap[0][0],minheap[0][0])
