'''
02. 인접 리스트 구현하기
'''

t = int(input())

for _ in range(t):
    node, edge = map(int, input().split())

    # 노드 만큼 배열 생성
    graph = [ []*node for _ in range(node)]

    for _ in range(edge):
        m, n = map(int, input().split())
        graph[n].append(m)
        graph[m].append(n)
    
    for i in range(node):
        graph.sort(i)
        print(*graph)
        # print(*sorted(graph[i]))