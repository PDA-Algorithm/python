import sys
input = sys.stdin.readline
print = sys.stdout.write

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
     
    elif dp[a][b][c]:
        return dp[a][b][c]
    
    elif a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

dp = [[[[] for i in range(21)] for j in range(21)] for k in range(21)]
    
while True:
    # 입력
    a, b, c = map(int, input().split())
    
    # 종료조건
    if a == b == c == -1:
        exit()
    
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}\n')