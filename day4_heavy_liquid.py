'''
02 무거운 용액
'''
t = int(input())

for _ in range(t):
    cnt,volume = map(int,input().split())
    case_list = []

    for _ in range(cnt):
        volume_result, n = 0, 0
        case_weight, case_volume = map(int,input().split())
        density = case_weight / case_volume
        case_list.append((density,case_weight,case_volume))
    case_list.sort(reverse=True)

    while volume :
        if volume < case_list[n][2]:
            volume_result += volume*case_list[n][0]
            break

        volume = volume - case_list[n][2]
        volume_result += case_list[n][1]
        n += 1
    print(int (volume_result))
