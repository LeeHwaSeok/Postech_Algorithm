'''
세계 암기대회
'''
test_case = int(input())

for _ in range(test_case):
    column,row = map(int,input().split())
    pointer = []

    for x in range(column):
        pointer.append(list(map(int,input().split())))

    my_step = [ [0]*row for _ in range(column)]
    for i in range(column):
        for j in range(row):
            if i == 0 and j ==0:
                my_step[i][j] = pointer[i][j]
            elif i == 0:
                my_step[i][j] = my_step[i][j-1] + pointer[i][j]
            elif j == 0:
                my_step[i][j] = my_step[i-1][j] + pointer[i][j]
            else:
                my_step[i][j] = min(my_step[i-1][j-1], my_step[i-1][j], my_step[i][j-1]) + pointer[i][j]
    print(my_step[column-1][row-1])