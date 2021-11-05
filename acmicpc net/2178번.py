import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        a,b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>= 0 and nx <n and ny >= 0 and ny <m :
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[a][b] + 1
                    q.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))