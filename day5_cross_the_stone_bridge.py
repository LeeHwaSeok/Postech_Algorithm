'''
돌다리 건너기
'''
initial_condition = 1904101441
t = int(input())

for _ in range(t):
    n = int(input())
    test_case = [0]*(n+1)

    for i in range(1,n+1):
        if i == 1:
            test_case[i] =1
        elif i == 2:
            test_case[i] =2
        elif i == 3:
            test_case[i] =4
        else:
            test_case[i] =(test_case[i-1] + test_case[i-2] + test_case[i-3])% initial_condition
    print(test_case[n]) # print에 test_case[n] % 1904101441 이러면 time limit이 발생
                        # 엄청 큰 수가 됩니다.


