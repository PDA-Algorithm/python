import sys 
from collections import deque

input = sys.stdin.readline 

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    arr = []

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(graph, node, visited, arr):
        q = deque([node])
        visited[node] = 1

        while q:
            v = q.popleft()

            arr.append(v)

            for i in graph[v]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1

    bfs(graph, 1, visited, arr)

    print(len(arr)-1)
    
