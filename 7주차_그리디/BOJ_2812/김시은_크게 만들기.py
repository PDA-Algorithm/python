import sys; input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input().rstrip())
# k_cnt = 0

# for i in range(n-1):
#     if int(num[i]) < int(num[i+1]):
#         num[i] = ''
#         k_cnt +=1 
#     if k_cnt == k:
#         break
    
# # 리스트 하나로 합쳐주기
# print(''.join(num))

stack = [num[0]]
for i in range(1, len(num)):
    while len(stack) > 0 and k > 0:
        if stack[-1] < num[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num[i])

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
