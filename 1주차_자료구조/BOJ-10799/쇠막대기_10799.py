#STACK
import sys
input=sys.stdin.readline

total=list(input())
ans=0
rs=[]
for i in range(len(total)):
    if total[i]=='(':
        rs.append('(')
    elif total[i]==')':
        if total[i-1]=='(':
            rs.pop()
            ans+=len(rs)
        else:
            rs.pop()
            ans+=1
print(ans)
