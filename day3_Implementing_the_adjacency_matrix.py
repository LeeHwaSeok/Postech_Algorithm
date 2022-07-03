'''
01. 인접 행렬 구현하기
'''

t = int(input())

for _ in range(t):
    n,m= map(int, input().split())
    g = [[0]*n for _ in range(n)]


    for i in range(m) :
        u,v,c = map(int, input().split())
        g[u][v] = c

    for i in range(n):
        print(*g[i])