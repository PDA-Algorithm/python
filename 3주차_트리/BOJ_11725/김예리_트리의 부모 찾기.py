import sys


input = sys.stdin.readline

tree = {}
n = int(input())
for _ in range(n-1):
  a, b = map(int, input().split())
  tree[b]=a

for i in range(n):
  print(tree[i+1])