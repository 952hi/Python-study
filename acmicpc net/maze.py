'''
입력예시
5 6
101010
111111
000001
111111
111111

정답 : 10
'''
from collections import deque

n,m = map(int,input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    score = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[a][b] +1
                q.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(0,0))