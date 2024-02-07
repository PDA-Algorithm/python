for tc in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    dp = [[0,0,0] for _ in range(n)] # (위에거 때기 / 아래거 때기 / 안때기)
    dp[0] = [arr1[0], arr2[0], 0]
    for i in range(n-1):
        dp[i+1][0] = max(dp[i][1], dp[i][2]) + arr1[i+1]
        dp[i+1][1] = max(dp[i][0]+arr2[i+1], dp[i][2]+arr2[i+1])
        dp[i+1][2] = max(dp[i])
    print(max(dp[n-1]))
