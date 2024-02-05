import sys
input = sys.stdin.readline

# 삭제해야하는 노드 -2로 수정
# nodeInfo[i]가 -2라면 삭제 노드의 자식. -> 얘도 dfs 돌림

# 리프노드 조건
# nodeInfo[i]가 -2가 아님.
# nodeInfo중에 i 가 없어야 함.

n = int(input())
nodeInfo = list(map(int, input().split()))
# index 번의 부모 번호
delNode = int(input())

def dfs(delNum, nodeInfo):
    nodeInfo[delNum] = -2 # 삭제 노드 처리
    for i in range(n):
        if nodeInfo[i] == delNum:
            dfs(i, nodeInfo)

dfs(delNode, nodeInfo)
# print(nodeInfo)

ans = 0
for i in range(n):
    # 어떤 노드의 부모가 아니고, 해당 노드가 삭제노드가 아닐때
    if  i not in nodeInfo and nodeInfo[i] != -2:
        ans += 1
print(ans)
