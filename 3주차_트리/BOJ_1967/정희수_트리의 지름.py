import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)] 
for _ in range(2, n+1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

dist = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(node, graph, val, visited):
    visited[node] = 1
    for i in graph[node]:
        next = i[0]
        w = i[1]
        if visited[next] == 0:
            dist[next] = val + w
            dfs(next, graph, val + w, visited)

dfs(1, graph, 0, visited)
pos_node = dist.index(max(dist))

visited = [0 for _ in range(n+1)]
dfs(pos_node, graph, 0, visited)
print(max(dist))
