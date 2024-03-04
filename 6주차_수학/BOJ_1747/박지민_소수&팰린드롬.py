# 1747 소수&팰린드롬
import sys, math
input = sys.stdin.readline

# 소수 판별 함수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

# 팰린드롬 판별 함수
def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False


N = int(input())
answer = 0

while True:
    if isPrime(N) and isPalindrome(N): # 소수이면서 팰린드롬이면 종료
        print(N)
        break
    N += 1
