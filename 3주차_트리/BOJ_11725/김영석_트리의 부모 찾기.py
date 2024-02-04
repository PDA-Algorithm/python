import sys
from collections import deque as d
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    
parent = [0]*(n+1)

q = d([1])
v = [0]*(n+1)
parent[1] = 1
while q:
    now = q.popleft()
    for e in edge[now]:
        if not parent[e]:
            q.append(e)
            parent[e] = now
for i in range(2, n+1):
    print(str(parent[i])+'\n')