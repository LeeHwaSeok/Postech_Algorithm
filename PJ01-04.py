'''
Project 01. 합병

문제 : 
    리스트를 2개를 받아온다
    1. 리스트 각 요소를 비교하여 작은 것을 리스트에 담는다
    2. 요소에 담긴 리스트는 다음 인덱스를 가르킨다
    3. 반복
    4. 마지막으로 남은 리스트는 그냥 붙여준다
    끝. 

출력 : 
    1. 갖고온 요소가 1번 리스트의 경우 1 or 2를 한 줄에 출력한다.
'''
    # 출력용 프린터
    # print("fe",fe)
    # print("se",se)
    # print(first_arr)
    # print(second_arr)

    # print("len(fa)",len(first_arr))
    # print("len(sa)",len(second_arr))

'''
# 1try => timelimit 사실 print 때문이였음
'''
def Merge_sort(first, second):
    global fe, se
    # print("fe",fe)
    # print("se",se)

    if len(first_arr) == fe:
        return 2
    elif len(second_arr) == se:
        return 1

    if first[fe] > second[se]:
        se += 1
        return 2
    elif first[fe] < second[se]:
        fe += 1
        return 1
    # else :
    #     fe +=1
    #     se +=1
    #     return 1



t = int(input())
for _ in range(t):
  first_arr = list(map(int, input().split()))
  second_arr = list(map(int, input().split()))
  answer = []
  fe, se = 0,0
  for _ in range(len(first_arr)+len(second_arr)):
    answer.append(Merge_sort(first_arr,second_arr))
  print(*answer)

'''
    # 함수 없이 포문으로만
'''
t = int(input())
for _ in range(t):
  first_arr = list(map(int, input().split()))
  second_arr = list(map(int, input().split()))
  answer = []
  fe, se = 0,0

  for _ in range(len(first_arr)+len(second_arr)):

    if len(first_arr) == fe:
        answer.append(2)
        continue

    elif len(second_arr) == se:
        answer.append(1)
        continue

    if first_arr[fe] > second_arr[se]:
        se += 1
        answer.append(2)
    elif first_arr[fe] < second_arr[se]:
        fe += 1
        answer.append(1)

  print(*answer)


'''
Project 02. 이진탐색 2
    bisect left or right를 쓰면 좋다.
문제 : 
    리스트 2개를 받아온다
    1. 1개는 탐색해야할 리스트 또 하나는 찾아야할 리스트를 받아온다
    2. 리스트에서 일치하는 값을 찾으면 바로 출력
    3. 리스트에서 일치하는 값이 없으면 가장 가까운 값을 출력

'''

import bisect


def binary_finder(arr, target):
    i = bisect.bisect_left(arr,target)

    if i != len(arr) and arr[i] == target:
        return arr[i]
    elif i == len(arr):
        return arr[-1]
    elif i == 0:
        return arr[0]
    else:
        if arr[i] - target < target - arr[i-1] :
            return arr[i]
        else :
            return arr[i-1]



t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    find_arr = list(map(int,input().split()))
    answer = []

    for target in find_arr:
        answer.append(binary_finder(arr, target))
    print(*answer)
