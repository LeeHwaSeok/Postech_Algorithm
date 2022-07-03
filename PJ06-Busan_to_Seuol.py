'''
06 부산에서 서울
T =  repeat
G = 기름양, L = 최종 거리
'''
_repeat = int(input())
for _ in range(_repeat):
    G, L= map(int, input().split())
    gasStation = list(map(int,input().split()))
    present = 0
    visited = 0
    if(G >=L):
        print(0)
    else:
        before_point=0
        gasStation.append(L)
        for node in gasStation:
            if (node>present+G):
                if(node-before_point>G):
                    visited = -1
                    break
                present = before_point
                visited +=1  
            before_point = node
        print(visited)

