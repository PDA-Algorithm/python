#stack
import sys
input=sys.stdin.readline

arr=list(map(str,input().rstrip()))
answer=0
a1=arr.count('(')
a2=arr.count(')')
b1=arr.count(']')
b2=arr.count('[')
if a1!=a2 or b1!=b2:
    print(0)
    exit()
stack=[]
temp=1
for i in range(len(arr)):
    if arr[i]=='(':
        stack.append(arr[i])
        temp*=2
    elif arr[i]=='[':
        stack.append(arr[i])
        temp*=3
    elif arr[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        if arr[i-1]=='(':
            answer+=temp
        stack.pop()
        temp//=2
    elif arr[i]==']':
        if not stack or stack[-1]=='(':
            answer=0
            break
        if arr[i-1]=='[':
            answer+=temp
        stack.pop()
        temp //= 3
print(answer)