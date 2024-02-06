import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
  a,b,l = map(int,sys.stdin.readline().split())
  graph[a].append((b,l))
  graph[b].append((a,l))

def bfs(x):
  q = deque()
  q.append(x)
  visited = [-1 for _ in range(N+1)]
  visited[x] = 0

  while q:
    alpha = q.popleft()
    for nx,tmp in graph[alpha]:
      if visited[nx] == -1:
        q.append(nx)
        visited[nx] = visited[alpha] + tmp
        
  return [max(visited),visited.index(max(visited))]
max_val = 0
print(bfs(bfs(1)[1])[0]) #1번 노드의 최댓값의 인덱스로 다시 최댓값을 구한다.
