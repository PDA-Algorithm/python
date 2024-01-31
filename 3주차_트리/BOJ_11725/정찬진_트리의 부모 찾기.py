from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
node = [0 for _ in range(n+1)]

node[1] = 1

def bfs(a):
  q = deque()
  q.append(a)
  visited[a] = 1
  while q:
    alpha = q.popleft()

    for nx in graph[alpha]:
      if visited[nx] == 0:
        visited[nx] = 1
        q.append(nx)
        node[nx] = alpha # 노드에 부모의 노드값을 저장

for _ in range(n-1):
  a,b = map(int,sys.stdin.readline().split())
  graph[a] += [b]
  graph[b] += [a]
bfs(1)
# for i in range(2,n+1):
#   for j in graph[i]:
#     if node[j]<node[i]:
#       print(j)
for i in range(2,n+1):
  print(node[i])
