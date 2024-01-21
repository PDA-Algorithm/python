sticks = input()
ans = cnt = 0
s = []

for stick in sticks:
    if stick == '(':
        cnt += 1
        s.append('(')
    else:
        is_stick = False
        while s and s[-1] == 1:
            s.pop()
            is_stick = True
        
        if is_stick:
            cnt -= 1
            s.pop()
            s.append(1)
            ans += 1
        else:
            cnt -= 1
            ans += cnt
            s[-1] = 1

print(ans)