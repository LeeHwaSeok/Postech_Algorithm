'''
최대 합 부분 연속 수열 2
'''

def dynamic_programming(arr):
    dp = [None] * len(arr)
    dp[0] = arr[0]

    for x in range(1,len(arr)):
        dp[x] =  max(0,dp[x-1]) + arr[x]
    return max(dp)

_repeat = int(input())

for _ in range(_repeat):
    arr = list(map(int,input().split()))
    print(dynamic_programming(arr))


