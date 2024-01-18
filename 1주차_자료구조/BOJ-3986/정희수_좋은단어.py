n = int(input())
arr =[]
for _ in range(n):
    arr.append(input())

def check(string):
    temp = []
    for s in string:
        if temp == []:
            temp.append(s)
        elif temp[-1] == s:
            temp.pop()
        else:
            temp.append(s)
    if len(temp) == 0:
        return True
    else:
        return False
3
ans = 0
for a in arr:
    if check(a):
        ans+=1

print(ans) 