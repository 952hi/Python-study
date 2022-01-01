'''
page 388 이코테 교재
화성탐사문제
반복 횟수 T와 그래프의 크기 N 그리고 그래프 정보를 입력받아
0,0 에서 n-1,n-1로 이동할때의 최소비용을 출력하시오

입력예시
3  
3  
5 5 4  
3 9 1  
3 2 7  
5  
3 7 2 0 1  
2 8 0 9 1  
1 2 1 8 1  
9 8 9 2 0  
3 6 5 1 5  
7  
9 0 5 1 1 5 3  
4 1 2 1 6 5 3  
0 7 6 1 6 8 5  
1 1 7 8 3 2 3  
9 4 0 7 6 4 1  
5 8 3 2 4 8 3  
7 4 8 4 8 3 4 

출력예시
28
19
36

느낀점
BFS로 해결해보려 했으나 중복으로 처리되는부분을 생각하지않아서 새로풀었습니다.
다익스트라로 최소값만 다음칸으로 전달해서 문제를 해결했습니다.
'''
import sys
input = sys.stdin.readline
inf = sys.maxsize
import heapq

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(int(input())):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split()))) 
    distance = [[inf]*n for _ in range(n)]
    
    x,y = 0,0
    q = []
    
    heapq.heappush(q, (graph[x][y],x,y))
    distance[x][y] = 0
    
    while q:
        dist,x,y = heapq.heappop(q)
        
        if x != 0 and y != 0:
            if distance[x][y] < dist:
                continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))
    print(distance[n-1][n-1]) 