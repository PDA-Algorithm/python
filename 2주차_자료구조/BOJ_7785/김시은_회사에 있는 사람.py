import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    name, state = input().rstrip().split(' ')
    if state == 'enter':
        s.add(name)
    if state == 'leave':
        s.remove(name) #

for i in sorted(s, reverse=True):
    print(i)