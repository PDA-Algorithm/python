'''
1. 테스트 케이스마다 입력을 받는다
2. 입력을 한글자씩 스택에 넣는다. 단, 마지막 글자가 현재 글자와 같으면 넣지말고 pop
3. 마지막 글자까지 넣었을 때, 스택이 비어있으면 ans += 1
'''

import sys
input = sys.stdin.readline

ans = 0

for testcase in range(int(input())):
    word = input().rstrip()
    s = []
    
    for i in range(len(word)):
        
        now = word[i]
        
        if s and s[-1] == now:
            s.pop()
        
        else:
            s.append(now)
        
    if not s:
        ans += 1

print(ans)