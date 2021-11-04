import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int, input().split())
box = []
result = -2
for _ in range(n):
    box.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [-1,1,0,0]

q = deque()

def bfs():
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <n and nx >=0 and ny <m and ny >=0 :
                if box[nx][ny] == 0:
                    box[nx][ny] = box[a][b] + 1
                    q.append((nx,ny))
       
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i,j))

bfs()
check = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            box[i][j] = -1
            check += 1
        result = max(result,box[i][j])
        
if check != 0:
    print(-1)
else:
    print(result-1)