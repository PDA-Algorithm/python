import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [None for _ in range(N+1)]

def DFS(graph, v, visited):
    for i in graph[v]:
        # 방문하지 않았을 경우
        if not visited[i]:
            visited[i] = v
            DFS(graph, i, visited)
        
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(tree, 1, parent)

for i in range(2, N+1):
    print(parent[i])
