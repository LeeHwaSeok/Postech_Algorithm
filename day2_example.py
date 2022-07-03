# 예제 a~b까지 더하는 프로그램

def _sum(a,b):
    if a==b:
        return a
    
    mid = (a+b)//2
    sa = _sum(a,mid)
    sb = _sum(mid+1,b)

    return sa+sb

_sum(5,7)
print(_sum)
# 18

# 설명
# 1. 해결할 문제를 함수로 정의
#     _sum(a,b) : a~b까지의 합
# 2. 분할 (재귀함수)
#     a~b를 절반으로 나눔
#         => 재귀함수로 부분 문제들 해결
# 3. 정복(분할에 의한 결과들 합치기)
#     Sa와 Sb로 _sum(a,b)를 구함
#         => Sa+SB
# 4. 종료 조건(초기값)
#     a와 b가 같을 때 Sum(a,b) = a

'''
#01 n^k mod m효율적으로 계산하기
'''

def Power(n,k,m):
    if k == 0:
        return 1
    if k == 1:
        return n
    
    half = Power(n,k//2,m)

    if k % 2 == 0:
        return (half * half) % m
    else:
        return (half * half * n ) % m

t = int(input())
for _ in range(t):
    n,k,mod = map(int, input().split())
    print(Power(n,k,mod))


'''
#02 이진함수
'''
def binary(data, left, right, q):
    if left > right:
        return -1
    
    mid = (left + right) //2
    
    if data[mid] == q:
        return mid
    
    if data[mid] > q:
        subproblem = binary(data,left,mid-1,q)
    
    elif data[mid] < q:
        subproblem = binary(data,mid+1,right,q)
    
    return subproblem

t = int(input())
for _ in range(t):
    data = list(map(int,input().split()))
    query = list(map(int,input().split()))
    answer = []

    for q in query:
        answer.append(binary(data,0,len(data)-1,q))

    print(*answer)


'''
2번 방식
'''

import bisect

def find(l,x):
    i = bisect.bisect_left(l,x)
    if i != len(l) and l[i] ==x:
        return i
    return -1

t = int(input())

for _ in range(t):
    data = list(map(int,input().split()))
    query = list(map(int,input().split()))
    answer = [find(data,x) for x in query]
    answer = []
    for x in query:
        answer.append(find(data,x))
    print(*answer)



'''
03. 최대 합 부분 연속 수열

'''
