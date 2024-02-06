#DFS
import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
m=int(input())

def dfs(arr,delid):
    arr[delid]=-2
    for i in range(len(arr)):
        if arr[i]==delid:
            dfs(arr,i)

count=0
dfs(arr,m)
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)
