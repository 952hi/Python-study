'''
https://www.acmicpc.net/problem/2667
단지번호붙이기

배열의 크기 N과 그래프의 정보를 받아와
단지가 있는 구역의 개수 구역별 단지의 수를 오름차순으로 출력하는 문제


단지가 있는 부분은 1 없는부분 2
입력예시
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력예시
3
7
8
9

느낀점
오랜만에 BFS를 사용해서 다시 숙지 할 수 있어서 좋았습니다.
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 2
    score = 1
    while q:
        a,b = q.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    score += 1
                    q.append((nx,ny))
    return score
                    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

digit = len(result)
print(digit)
result.sort()
for i in range(digit):
    print(result[i])