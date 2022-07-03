#전체 힌트
# *Hint : input() 함수를 사용할 때에 괄호 안에 문구가 있으면 해당문구가 출력으로 인식되어 Wrong answer
# - input('enter 2 input') => X
# - input() => O


'''
# 1. A+B 구하기 
#  두 수를 입력 받아 그 합을 출력하는 프로그램을 제출합시다.
'''

a,b = map(int, input().split())
print(a+b)


'''
# 2. A+B LV.2
#  테스트 케이스만큼 입력받아서 A+B를 전부 구하는 프로그램을 구현합시다.
'''
t = int(input())
for _ in range(t):
  a,b = list(map(int, input().split()))
  print(a+b)

#해설 
# 변수 t에 몇번 반복할것인지 입력 [= 테스트 케이스만큼 ]
# 받아온 값을 a b 형식으로 받아서 split하여 계산


'''
# 3. 리스트 합
#   테스트 케이스만큼 리스트를 입력 받고, 그 리스트를 합하여 출력
'''

def _sum(l):
  s = 0
  for i in l:
    s = s+i
  return s

t = int(input())
for _ in range(t):
  l = list(map(int, input().split()))
  print(_sum(l))

#해설
# list(map(int, input().split()))을 사용하면 자동으로 매핑하여 list로 만들어줌
# _sum(l) => 리스트의 요소의 총합 출력

'''
# 4. 최댓값과 최솟값의 차이 구하기
#  테스트 케이스만큼 리스트를 입력받습니다.
#  리스트에서 최댓값과 최솟값을 구하고, 그 차이를 출력하는 프로그램 작성
'''

#min, max 함수로 구현
def Max(l):
    m = l[0]
    for i in l:
        if m < i:
            m = i
    return m

def Min(l):
    m  = l[0]
    for i in l:
        if m > i:
            m = i
    return m

# 밑에는 내장함수 사용
t = int(input())
for _ in range(t):
  i = list(map(int, input().split()))
  print(max(i)-min(i))



'''
# 5. 스택 구현하기
#  가장 기본적이고 중요한 자료 구조인 스택을 구현합니다.
*Hint : list의 pop() 함수를 사용합시다.

LIFO = 후입선출
맨 뒤에 넣은게 맨 먼저 나옴
=> 프링글스 과자 
'''

f = int(input())

for _ in range(f):
    t = int(input())
    stack = []  
    for _ in range(t):
        x = int(input())
        if x == -1:
            print(stack.pop())
        else :
            stack.append(x)



#해설
# 테스트 케이스를 항상 초기화 해야함 [for 안에 작성]
# 리스트를 받아옴 
# ex) 1 2 3 4 -1 
#  -1일경우 stack - pop 하고, 프린트 출력
#  이 외 경우 append

# 2   ... 테스트 케이스 2번 사용
# 10  ... 리스트에 요소를 10번 추가합니다.
# 1
# -1
# 2
# 7
# 3
# -1
# 4
# -1
# 5
# -1
## list [1,-1,2, 7, 3, -1, 4, -1, 5, -1]
### 결과
    # list [2,7]
    # 출력 1, 3, 4, 5
# 6   ... 리스트에 요소를 10번 추가합니다.
# 3
# 4
# 2
# 1
# 5
# -1
## list [3, 4, 2, 1, 5, -1]
### 결과
    #list [3, 4, 2 ,1]
    #출력 5
'''
# 6. 큐 구현하기
# 가장 기본적이고 중요한 자료 구조인 큐를 구현합니다.

FIFO = 선입 선출
맨 처음에 넣은게 맨 먼저나옴
롤 queue
'''

import collections
f = int(input())

for _ in range(f):
    t = int(input())
    queue=collections.deque([]) 
    for _ in range(t):
        x = int(input())
        if x == -1:
            print(queue.popleft())    
        else :
            queue.append(x)

#해설
# collections 라이브러리를 사용해서 deque 리스트를 생성합니다.
# deque는 popleft를 사용할 수 있는데, 이러면 리스트의 맨 앞자리부터 끊어서 사용 가능

# 2  ... 테스트 케이스를 2번 사용합니다.
# 10 ... 리스트에 요소를 10번 추가합니다.
# 1
# -1
# 2
# 7
# 3
# -1
# 4
# -1
# 5
# -1
## list [1 , -1, 2, 7, 3 , -1, 4, -1, 5, -1] 
### 결과 : 
    #list [4, 5]
    #출력 : 1, 2, 7, 3 
# 6 ... 리스트에 요소를 6번 추가합니다.
# 3
# 4
# 2
# 1
# 5
# -1
## list [3, 4, 2, 1, 5, -1]
### 결과 : 
    #list [4, 2, 1, 5]
    #출력 : 3




'''
#7. 우선순위 큐 구현하기
# 가장 기본적이고 중요한 자료 구조인 우선순위 큐를 사용합니다.

*heapq를 이용하자
*주의 : 일반적으로 숫자가 작을수록 우선순위가 높다고 얘기합니다.
'''

import heapq 
f = int(input())

for _ in range(f):
    t = int(input())
    hq = []  
    for _ in range(t):
        x = int(input())
        if x == -1:
            print(heapq.heappop(hq))
        else :
            heapq.heappush(hq, x)



#해설
# heapq 라이브러리를 사용합니다.
# 받아온 값을 리스트에서 크기 비교하여 정렬 후 저장합니다.

# 입력형식
# 2 ... 테스트 케이스 2번 사용하겠다.
# 10 ... 리스트 요소를 10번 추가합니다.
# 1
# -1
# 2
# 7
# 3
# -1
# 4
# -1
# 5
# -1
## list [ 1,-1,2,7,3,-1,4,-1,5,-1] 
### 결과 
    # list [5, 7]
    # 출력 1,2,3,4

# 6 ... 리스트 요소를 6번 추가합니다.
# 3
# 4
# 2
# 1
# 5
# -1
##list [3,4,2,1,5,-1] -1 1번 => 1 출력
### 결과
    # list [2,3,4,5]
    # 출력 1


'''
# 8 피보나치 수열
#피보나치 수열은 첫째 항과 둘째 항이 1이고, 셋째 항부터는 아래 공식에 따라 만들어집니다.
Fn = F(n-1) + F(n-2)

'''

def FIB1(n):
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  return FIB1(n-1) + FIB1(n-2)

x = int(input())

for _ in range(x):
  n = int(input())
  print(FIB1(n))

#해설
## fib1 함수를 만들어서 n이 0 혹은 1이면 각각 리턴
## 그외에는 공식 리턴

#입력
# 6   ... 테스트 6번 반복
# 입력 => 결과
# 1  => 1
# 2  => 1
# 3  => 2
# 4  => 3
# 5  => 5
# 6  => 8