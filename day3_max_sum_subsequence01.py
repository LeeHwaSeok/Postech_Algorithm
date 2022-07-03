'''
03. 최대 합 부분 연속 수열

'''

from tracemalloc import start


def mls(l):
    n = len(l)

    if n == 1:
        return l[0]

    left = mls(l[:n//2])
    right = mls(l[n//2:])

    lindex = n // 2-1
    lmax = l[lindex]
    lsum = l[lindex]

    for i in range(lindex-1,-1,-1):
        lsum += l[i]
        if lsum > lmax:
            lmax = lsum
    rindex = n //2

    rindex = n // 2-1
    rmax = l[rindex]
    rsum = l[rindex]

    for i in range(rindex+1,n):
        rsum += l[i]
        if rsum > rmax:
            rmax = rsum
    return max(lmax+rmax, left, right)



t = int(input())

for _ in range(t):
    l = list(map(int,input().split()))
    print(mls(l))