#stack
import sys
input=sys.stdin.readline

test=int(input())
count=0
words=[input().rstrip() for _ in range(test)]
for word in words:
    arr=[]
    for i in range(len(word)):
        if len(arr)==0:
            arr.append(word[i])
        else:
            if arr[-1]==word[i]:
                arr.pop()
            else:
                arr.append(word[i])
    if len(arr)==0:
        count+=1
print(count)