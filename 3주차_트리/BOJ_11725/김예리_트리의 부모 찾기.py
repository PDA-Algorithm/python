import sys
# recursion error 방지
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(v):
  for i in graph[v]:
    if visited[i] == 0:
      visited[i] = v
      dfs(i)

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


dfs(1)

for i in range(2, n+1):
  print(visited[i])
