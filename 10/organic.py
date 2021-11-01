from collections import deque

def bfs(graph, Ox, Oy):
    q = deque()
    q.append((Ox, Oy))
    graph[Ox][Oy] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 2
digit = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(digit):
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                bfs(graph,i,j)
    print(graph)
    print(count)
