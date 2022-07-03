'''
Project 05 최단 경로 구하기
'''
from cmath import inf
import heapq
import sys

def dijkstra(v,start,adj):
    dist = [inf] * (v + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cost, node = heapq.heappop(heap)
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(heap, [c, n])
    return dist


repeat = int(input())

for _ in range(repeat):
    node, edge = map(int,input().split())

    graph = [ []*node for _ in range(node+1)]

    for _ in range(edge):
        depart_node, arrival_node, cost = map(int,input().split())
        graph[depart_node].append([arrival_node,cost])
    dst_ls =[]

    for res in dijkstra(node, 0, graph)[1:]:
        dst_ls.append(res if res != inf else -1)
    print(dst_ls[len(dst_ls)-2])
