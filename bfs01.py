from collections import deque

def bfs(graph, visited, v):
    q = deque()
    q.append(v)
    
    visited[v] = 1
    
    while q:
        a = q.popleft()
        print(a,end=" ")
        for i in graph[a]:
            if visited[i] == 0 :
                 visited[i] = 1
                 q.append(i)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [0]*9

bfs(graph, visited, 1)