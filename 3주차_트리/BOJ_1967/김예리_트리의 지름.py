import sys
sys.setrecursionlimit(10**5)

"""
dfs 총 두 번
1. 루트에서 가장 먼 노드 찾기
2. 찾은 노드에서 가장 먼 노드 찾기
visited에 가중치 더한 값 저장해서 지름 구하기
"""

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)] 
for _ in range(n-1):
  parent, child, weight = map(int, input().split())
  tree[parent].append([child, weight])
  tree[child].append([parent, weight])

def dfs (v, weight):
  for i, j in tree[v]: # i는 연결 노드, j는 가중치
    cal_weight = weight + j
    if visited[i] == -1:
      visited[i] = cal_weight
      dfs(i, cal_weight)


visited = [-1] * (n+1)
visited[1] = 0

dfs(1,0)

index = visited.index(max(visited))

visited = [-1] * (n+1) # visited 초기화
visited[index] = 0 
dfs(index, 0)

print(max(visited))
