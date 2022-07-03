'''
01 동전 챠징 -- 1
'''
def Divide_banknotes(money, cnt, charges,mc_num):
    Money_Changes = [50000,10000,5000,1000,500,100]

    if money >= Money_Changes[mc_num]:
        charges = money // Money_Changes[mc_num]
        money = money % Money_Changes[mc_num]
        cnt = cnt+charges
        if mc_num == 5:
            return cnt
    mc_num = mc_num + 1
    return Divide_banknotes(money, cnt, charges,mc_num)

t = int(input())

for _ in range(t):
    money = int(input())
    cnt, charges,mc_num = 0,0, 0

    print(Divide_banknotes(money, cnt, charges,mc_num))

## 포문 사용 풀기
'''
01 동전 챠징 -- 2
'''
def Divide_banknotes(money):
    Money_Changes = [50000,10000,5000,1000,500,100]
    charges, cnt = 0, 0
    for x in range(len(Money_Changes)):
        if money >= Money_Changes[x]:
            charges = money // Money_Changes[x]
            money = money % Money_Changes[x]
            cnt = cnt+charges
    return cnt

t = int(input())

for _ in range(t):
    money = int(input())
    print(Divide_banknotes(money))


