import sys
input = sys.stdin.readline

"""
트리 연결 관계에서 deleted_node의 자식들을 dfs로 다 처리해준다.
다시 트리 연결 관계에서 자식이 없는 리프 노드를 찾아준다.
"""

n = int(input())
tree_node = list(map(int, input().split()))
deleted_node = int(input())
tree = [[] for _ in range(n)] # 노드가 0부터 시작
visited = [False] * (n)
answer = 0

for i in range(len(tree_node)):
  for j in range(0, len(tree_node)):
    if tree_node[j] == i:
      tree[i].append(j) # 자식만 연결 관계에 추가

def dfs(v):
  visited[v] = True # 삭제할 노드와 그 노드의 자손들 모두 방문 처리
  for i in tree[v]:
    if not visited[i]:
      dfs(i)

dfs(deleted_node)

for i in range(n):
  if not visited[i] and not tree[i]: 
    answer += 1
  elif not visited[i] and len(tree[i])==1 and tree[i][0] == deleted_node:
    answer += 1

print(answer)

"""
deleted_node를 자식으로 갖고 있는 노드 리프노드 처리 해야함
"""