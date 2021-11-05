from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
visited[x] = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
q = deque([x])
while q:
    a = q.popleft()   
    for i in graph[a]:
        if visited[i] == -1 :
            q.append(i)
            visited[i] = visited[a] +1
for i in range(1,n+1):
    if k == visited[i]:
        print(i)
if k not in visited:
    print(-1)