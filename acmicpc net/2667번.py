'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys
from collections import deque

input = sys.stdin.readline
numbering = []
result = []
n = int(input())

for _ in range(n):
    numbering.append(list(map(int,input().rstrip())))



dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    numbering[x][y] = 2
    score = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx >= 0 and nx < n and ny>= 0 and ny < n:
                if numbering[nx][ny] ==1:
                    numbering[nx][ny] = 2
                    q.append((nx,ny))
                    score += 1
    return score

for i in range(n):
    for j in range(n):
        if numbering[i][j] == 1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in result:
    print(i)