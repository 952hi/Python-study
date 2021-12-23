'''
page 262
전보

도시의 개수와 통로를 입력받아 메세지를 전달한 도시의 수와 걸린시간을 출력하는문제

n -> 도시의 개수
m -> 통로의 개수

입력예시
3 2 1  첫째줄은 n,m, 출발도시
1 2 4
1 3 2

출력예시
2 4   2-> 전달한 도시의수 4 -> 걸린시간

느낀점
전형적인 다익스트라 알고리즘 문제였다
'''
import sys
import heapq

input = sys.stdin.readline
inf = sys.maxsize


n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != inf:
        count += 1
        max_distance = max(max_distance, d)

print(count-1,max_distance)