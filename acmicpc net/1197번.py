'''
https://www.acmicpc.net/problem/1197
최소 스패닝 트리

그래프를 입력받아 
사이클이 생기지 않고 모든 노드를 방문 했을때의
간선의 가중치의 합의 최소값을 출력하는 문제

입력예시 
3 3
1 2 1
2 3 2
1 3 3

'''

import sys
input = sys.stdin.readline
import heapq
inf = sys.maxsize

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        value , node = heapq.heappop(q)
        
        if value > distance[node]:
            continue
        
        for i in graph[node]:
            cost = value + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(value,node))

dijkstra(1)
result = 0

for i in range(1,n+1):
    if distance[i] != inf:
        result = max(result, distance[i])

print(result)