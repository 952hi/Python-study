'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
import sys
input = sys.stdin.readline
from collections import deque
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(v):
    visited[v] =1
    print(v,end=' ')
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(v)
print()
visited= [0] * (n+1)

def bfs(v):
    q = deque()
    visited[v] = 1
    q.append(v)

    while q:
        a = q.popleft()
        print(a,end=" ")
        graph[a].sort()
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
bfs(v)
