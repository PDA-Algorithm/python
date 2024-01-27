import sys
n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
  a = sys.stdin.readline().split()
  if a[1] == "enter":
    arr.add(a[0])
  else:
    arr.remove(a[0])
arr = sorted(arr, reverse=True)
for i in arr:
  print(i)
