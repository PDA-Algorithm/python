#set
import sys
input=sys.stdin.readline

test=int(input())
arr=set()
for i in range(test):
    name, state=map(str,input().split())
    if state=="leave":
        arr.discard(name)
    else:
        arr.add(name)
arr=list(arr)
arr=sorted(arr,reverse=True)
print(' '.join(map(str, arr)))
