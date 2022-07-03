"""
01. 랜선웨어
컴퓨터 개수 - pc_node  
랜선의 개수 - pc_edge
시작 번호 - st_pc

감염된 컴퓨터1 - len_pc1
감연된 컴퓨터2 - len_pc2

감염된 컴퓨터 리스트 - visit
감염된 랜선 체크 리스트 - queue

2중 리스트 => timelimit

변경안 => dict

"""
def lanWare(lan_ware, st_pc):
    visit, queue = [],[]

    queue.append(st_pc)
    
    while queue:
        node = queue.pop(0)

        if node not in visit:
            visit.append(node)
            queue.extend(lan_ware[node])

    return len(lan_ware) - len(visit)

test_case = int(input())

for _ in range(test_case):
    pc_node, pc_edge, st_pc = map(int,input().split())
    
    lan_ware = [ []*pc_node for _ in range(pc_node)]
    for _ in range(pc_edge):
        len_pc1, len_pc2 = map(int,input().split())
        lan_ware[len_pc1].append(len_pc2)
        lan_ware[len_pc2].append(len_pc1)

    print(lanWare(lan_ware,st_pc))

'''
야발
'''
from collections import deque

t = int(input())

for _ in range(t):
    n,m,ll = map(int,input().split())
    List = [[] for _ in range(n)]
    for i in range(m):
        u,v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    for i in range(n):
        List[i].sort()
    
    check = [False]*n
    Queue = deque([ll])

    while Queue : 
        v = Queue.popleft()
        if check[v] == True:
            continue
        check[v] = True
        
        for i in List[v]:
            if check[i] == False:
                Queue.append(i)
        
    print(check.count(False))