from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    graph[v].sort()
    
    for i in graph[v]:
        if visited[i]== 0:
            visited[i] = 1
            dfs(i)
def bfs(v):
    visited[v] = 1
    
    
    q = deque()
    q.append(v)
    
    while q:
        a = q.popleft()
        graph[a].sort()
        print(a,end=" ")
        
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] =1
                q.append(i)
                
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]* (n+1)

for i in range(n+1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
print()
visited = [0]*(n+1)
bfs(v)

