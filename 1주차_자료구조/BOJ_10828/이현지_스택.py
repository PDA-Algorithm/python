#STACK
#first in last out
import sys
input=sys.stdin.readline

n=int(input())
#command=['push','pop','size','empty','top']
arr=[]
for i in range(n):
    temp=list(map(str, input().split()))
    if 'push' in temp:
        arr.append(temp[1])
    elif 'pop' in temp:
        m=len(arr)
        if m==0:
            print(-1)
        else:
            print(arr.pop())
    elif 'size' in temp:
        print(len(arr))
    elif 'empty' in temp:
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif 'top' in temp:
        m = len(arr)
        if m == 0:
            print(-1)
        else:
            print(arr[-1])

