'''
page 149 
음료수 얼려 먹기

얼음틀의 가로 M 세로 N 을 입력받고
얼음틀의 막혀있는 부분의 정보를 바탕으로
아이스크림의 수를 출력하는 문제
 
입력예시
4 5
00110
00011
11111
00000

출력예시
3

느낀점
n,m 을 보통 좌표값을 x,y로 주는데 y,x로 줘서 별거아니지만 헷갈렸다. 
'''

import sys
from collections import deque
m,n = map(int, input().split())
ice = []
score = 0
dx =[1,-1,0,0]
dy =[0,0,1,-1]

for i in range(m):
    ice.append(list(map(int, input())))
    
def bfs(x,y):
    q = deque()
    q.append((x,y))
    ice[x][y] = 2
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if ice[nx][ny] == 0:
                    ice[nx][ny] = 2
                    q.append((nx,ny))      

for i in range(m):
    for j in range(n):
        if ice[i][j] == 0:
            bfs(i,j)
            score += 1

print(score)
