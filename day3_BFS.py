'''
03. BFS 너비 우선 탐색
'''

def bfs(graph, start_node):
    visit,queue = [], []

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        # print('node',node)

        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            # print('visit',visit)
            # print('queue',queue)

    return visit



t = int(input())

for _ in range(t):
    node, edge = map(int, input().split())

    #노드 크기만한 그래프 생성
    graph = [ []*node for _ in range(node)]

    for _ in range(edge):
        m, n = map(int, input().split())
        # graph[n].append(m) // 한 방향성 노드라 n->m 필요없음
        graph[m].append(n) 

    for i in range(node):
        graph[i].sort()
    # print('graph',graph)
    print(*bfs(graph,0))