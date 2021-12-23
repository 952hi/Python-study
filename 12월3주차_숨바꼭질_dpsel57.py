'''
page 390 숨바꼭질

헛간의 수 N, 길의수 M을 입력받고
통로를 입력받아 1번헛간에서 최단거리가 가장먼곳으로 이동했을때
숨는 헛간과 거리 그리고 같은거리를 가진 헛간의 수를 출력하는 문제

입력예시
6 7 
3 6
4 3
3 2
1 3
1 2
2 4
5 2

출력예시
4 2 3

느낀점
다익스트라로 풀었는데 bfs로 풀어도 가능할거같다

'''
import sys
input = sys.stdin.readline
inf = sys.maxsize
import heapq

n,m = map(int,input().split())

distance = [inf] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q :
        value, node = heapq.heappop(q)
        if distance[node] < value:
            continue
        
        for i in graph[node]:
            cost = value + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
     
dijkstra(1)

max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result= [max_node]
    elif max_distance == distance[i]:
        result.append(max_node)
print(max_node,max_distance,len(result))