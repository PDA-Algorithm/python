import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(idx, cnt):
    visited[idx] = 1
    
    for i in graph[idx]:
        if visited[i] == 0:
            cnt = dfs(i, cnt+1)
    
    return cnt

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    visited = [0] * (n+1)
    
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print(dfs(1,0))