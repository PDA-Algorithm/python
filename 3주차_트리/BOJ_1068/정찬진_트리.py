# 주의해야할 점
# 부모노드는 항상 바뀔 수 있다.(0으로 고정이 아님)
# 부모노드가 0이고 자식노드가 1일 때 지워주는 노드의 값이 1이면 결과는 1이 나와야 한다. 지워주는 노드의 값이 0이면 결과는 0이다.
# 백준서버에서 런타임에러(nameError)라는 것을 처음 봤다.
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)] # 연결 리스트(0부터 시작하므로 N+1 해줄 필요 없음)
visited = [0 for _ in range(N)]
cnt = 0
node = list(map(int,sys.stdin.readline().split())) # 부모 노드 리스트 받아주기
D = int(sys.stdin.readline()) # 지워줄 노드

for i in range(N):
  if node[i] == -1: # 부모노드의 값이 1일 때 val로 값을 받아준다.
      val = i
      pass
  elif i == D or node[i] == D: # 그래프에 넣어줄 때 지워줄 노드가 부모노드에 들어가거나 지워줄 노드가 부모노드일 경우 넣지 않는다.
    pass
  else:
    graph[node[i]] += [i] # 위 두 경우를 제외하고 부모노드에 자식노드를 저장해 단방향 트리를 만들어준다.

visited[D] = 2

def bfs(x):
  q = deque()
  q.append(x)
  global cnt
  
  while q:
    alpha = q.popleft()

    if len(graph[alpha]) == 0 and alpha != D: # 자식을 가지고 있지 않고 지워진 노드가 아니면 카운트해준다.
      cnt += 1
      continue

    for nx in graph[alpha]:
      if visited[nx] == 0:
        q.append(nx)
        visited[nx] = 1
bfs(val)
if val == D:
  print(0)
else:
  print(cnt)
