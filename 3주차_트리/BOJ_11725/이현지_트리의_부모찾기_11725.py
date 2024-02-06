#DFS BFS
#이문제는 부모를 찾는 것이기 때문에 깊이 우선이 좋음
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
nums=[list(map(int,input().split())) for _ in range(n-1)]
graph=[[]*(n+1) for _ in range(n+1)]
chk=[0]*(n+1)
for i,j in nums:
    graph[i].append(j)
    graph[j].append(i)
q=deque()
q.append(1)
def bfs():
    while q:
        now=q.popleft()
        for next in graph[now]:
            if chk[next]==0:
                #now를 현재에 저장하면 부모 노드 저장고 같음
                chk[next]=now
                q.append(next)
#dfs
# def dfs(start):
#     for i in graph[start]:
#         if chk[i]==0:
#             chk[i]=start
#             dfs(i)
# dfs(1)
bfs()
for i in range(2,n+1):
    print(chk[i])
