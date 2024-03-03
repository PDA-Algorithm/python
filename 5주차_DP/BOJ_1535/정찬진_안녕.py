import sys
from itertools import combinations

N = int(sys.stdin.readline())
health = list(map(int, sys.stdin.readline().split()))
happy = list(map(int, sys.stdin.readline().split()))

if sum(health) < 100:
    print(sum(happy))
    
else:
    li = list()
    for i in range(N):
        li.append((health[i], happy[i]))

    max_happy = 0
    for i in range(N):
        comb = list(combinations(li, i + 1))

        for j in comb:
            hp = 0
            ha = 0
            for k in range(len(j)):
                hp += j[k][0]
                ha += j[k][1]
            if hp < 100 and ha > max_happy:
                max_happy = ha
    print(max_happy)
