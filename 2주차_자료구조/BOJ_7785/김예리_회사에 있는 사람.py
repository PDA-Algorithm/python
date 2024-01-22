import sys

name_list = dict()

n = int(sys.stdin.readline())

for i in range(n):
  order = sys.stdin.readline().split()
  if order[1] == "enter":
    name_list[order[0]]="in"
  else:
    del name_list[order[0]]

answer = sorted(name_list, reverse=True)
for i in answer:
  print(i)