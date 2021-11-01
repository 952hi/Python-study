from collections import deque
  
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]

visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)


for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited_dfs[v] = 1
    print(v,end=' ')
    
    graph[v].sort()
    
    for i in graph[v]:
        if visited_dfs[i] == 0:
            dfs(i)
        
def bfs(v):
    visited_bfs[v] = 1
        
    q = deque()
    q.append(v)
    
    while q:
        a = q.popleft()
        print(a,end=" ")
        
        graph[a].sort()
        
        for i in graph[a]:
            if visited_bfs[i] == 0:
                visited_bfs[i] =1
                q.append(i)

dfs(v)
print()
bfs(v)