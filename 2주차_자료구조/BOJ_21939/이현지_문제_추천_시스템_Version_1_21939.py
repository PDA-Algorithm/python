#heap
import heapq
import sys
input=sys.stdin.readline
arr=[]
heap1=[]
heap2=[]
t1=int(input())
for i in range(t1):
    u,v=map(int,input().split())
    heapq.heappush(heap1,(v,u))
    heapq.heappush(heap2,(-1*v,-1*u))
t2=int(input())
for i in range(t2):
    line=input().split()
    if "add" in line:
        u,v=int(line[1]),int(line[2])
        heapq.heappush(heap1,(v,u))
        heapq.heappush(heap2, (-1*v, -1*u))
    else:
        temp = int(line[1])
        if "recommend" in line:
            if temp==-1:
                #min
                for m in range(len(arr)):
                    if heap1[0][1]== arr[m]:
                        heapq.heappop(heap1)
                print(heap1[0][1])
            elif temp==1:
                for m in range(len(arr)):
                    if -heap2[0][1]==arr[m]:
                        heapq.heappop(heap2)
                print(-heap2[0][1])
        elif "solved" in line:
            arr.append(temp)



