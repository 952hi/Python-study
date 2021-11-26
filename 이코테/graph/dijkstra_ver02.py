import sys
input = sys.stdin.readline
import heapq
inf = int(1e9)

n,m = map(int,input().split())
start_node = int(input())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

print(graph)

def dijkstra(start):
    q = []
    print(start)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        value, node = heapq.heappop(q)
        
        if distance[node] < value:
            continue
        
        for i in graph[node]:
            cost = value + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(start_node)

for i in range(1,n+1):
    if distance[i] == inf :
        print("no")
    else:
        print(distance[i])
            