'''
04 DFS 깊이 우선 탐색
'''
def dfs(graph, start_node):
    visit,stack = [], []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


t = int(input())

for _ in range(t):
    node, edge = map(int, input().split())
    graph = [ []*node for _ in range(node)]

    for _ in range(edge):
        m, n = map(int, input().split())
        graph[m].append(n) 
        graph[n].append(m)
    for i in range(node):
        graph[i].sort(reverse=True)
    print(*dfs(graph,0))