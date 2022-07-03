'''
zero one neckset
'''
repeat = int(input())

for _ in range(repeat):
    n,C = map(int,input().split())
    w = list(map(int,input().split()))
    v = list(map(int,input().split()))

    T = [[0]*(C+1) for _ in range(n)]

    for i in range(n):
        for j in range(1, C+1):
            if i == 0:  
                if w[i] > j:
                    T[i][j] = 0
                else:
                    T[i][j] = v[i]
            else:
                if w[i] > j:
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = max(T[i-1][j], T[i-1][j-w[i]]+v[i])
    print(T[n-1][C])

