import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(node, cnt):
    checked[node] = 1
    
    for adj_node in graph[node]:
        if checked[adj_node] == 0:
            cnt = DFS(adj_node, cnt+1)
    
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    checked = [0]*(N+1)
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(DFS(1, 0))
