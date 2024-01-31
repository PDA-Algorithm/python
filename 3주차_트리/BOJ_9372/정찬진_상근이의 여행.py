import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(val):
  q = deque()
  q.append(val)
  cnt = 0
  visited = [0 for _ in range(N+1)]

  while q:
    alpha = q.popleft()
    if sum(visited) == N: # 여행국가로 채워지면 return
      return cnt
    visited[alpha] = 1

    for nx in graph[alpha]:
      if visited[nx] == 0:
        q.append(nx)
        visited[nx] = 1
        cnt += 1
      
for _ in range(T):
  N,M = map(int,sys.stdin.readline().split())
  graph = [[] for _ in range(N+1)]
  res = []
  for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
  print(bfs(1))
