from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    
    # 입력
    n = int(input())
    parent = [[] for _ in range(n+1)]
    ans = 0
    
    # 리프노드들
    is_leaf = [True]*(n+1)
    leaves = deque([])
    
    # 자식 노드 수
    child_cnt = [0]*(n+1)
    
    for i in range(n-1):
        a, b, c = map(int, input().split())
        parent[b].append((a,c))  # b의 부모가 a고, 거리가 c다
        is_leaf[a] = False
        child_cnt[a] += 1
            
    distance = [0]*(n+1)
    
    for i in range(1, n+1):
        if is_leaf[i]:
            leaves.append(i)
    
    # bfs
    while leaves:
        now = leaves.popleft()
        # 부모에 대해
        for node in parent[now]:
            par, dis = node
            before, after = distance[par], distance[now] + dis  # 기존 부모까지의 최대 거리, 지금 들어가는 거리
            ans = max(ans, before + after)  # 부모에서 만나는 경우
            distance[par] = max(distance[par], distance[now] + dis)  # 부모 갱신
            
            # 모든 자식을 고려했다면 본인이 리프노드가 된다
            child_cnt[par] -= 1
            if not child_cnt[par]:
                leaves.append(par)
                
    return ans
        
print(bfs())