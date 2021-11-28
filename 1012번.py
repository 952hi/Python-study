'''
https://www.acmicpc.net/problem/1012
유기농배추

dfs문제로 
배추가 심겨져있는 리스트를 입력받아
배추흰지렁이의 최소 개수를 출력하는 문제

흰지렁이는 인접한 배추에 이동할수 있음
인접 - > 상하좌우에 배추가있다면 인접한상태

느낀점
크게 막히는 부분없이 문제를 풀었습니다.
백준에 제출할때 재귀제한을 해제를 안해주니 오류가 나서 당황했습니다.
'''
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            if temp[nx][ny] == 1:
                temp[nx][ny] = 2
                dfs(nx,ny)
    return

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    temp = [[0]*m for _ in range(n)]
    count = 0
    
    for i in range(k):
        a,b = map(int,input().split())
        temp[a][b] = 1
        
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:

                dfs(i,j)
                count += 1

    print(count) 
