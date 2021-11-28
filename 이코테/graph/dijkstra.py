'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
import sys
input = sys.stdin.readline
inf = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def get_small_node():
    min_value = inf
    index = 0
    for i in range(n+1):
        if distance[i] < min_value and visited[i] == 0:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for _ in range(n-1):
        next_node = get_small_node()
        visited[next_node] = 1
        
        for j in graph[next_node]:
            cost = distance[next_node] + j[1]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
    
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == inf:
        print("No")
    else:
        print(distance[i])
    
