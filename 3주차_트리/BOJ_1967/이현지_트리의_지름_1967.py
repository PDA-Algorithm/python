#bfs
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    pnode,cnode,cost=map(int,input().split())
    graph[pnode].append((cnode,cost))
    graph[cnode].append((pnode,cost))

def bfs(start):
    chk = [-1] * (n + 1)
    chk[start]=0
    q=deque()
    q.append(start)
    while q:
        node=q.popleft()
        for nx,nc in graph[node]:
            if chk[nx]==-1:
                q.append(nx)
                chk[nx]=chk[node]+nc
    maxv=max(chk)
    return [chk.index(maxv),maxv]
print(bfs(bfs(1)[0])[1])
