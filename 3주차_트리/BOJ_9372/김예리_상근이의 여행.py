import sys

input = sys.stdin.readline

def dfs (graph, v, visited, cnt):
  visited[v] = True
  for i in graph[v]:
    if visited[i] == False:
      cnt = dfs(graph, i, visited, cnt+1)
  return cnt


T = int(input())

for _ in range(T):
  n, m = map(int, input().split())
  visited = [False] * (n+1)
  graph = [[] for _ in range(n+1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  cnt = dfs(graph, 1, visited, 0)
  print(cnt)


