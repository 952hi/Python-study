import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []
wall = [[0]*m for _ in range(n)]
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def point():
    score = 0
    for i in range(n):
        for j in range(m):
            if wall[i][j] == 0:
                score += 1
    return score

def worm(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < n and nx >= 0 and ny >= 0 and ny < m :
            if wall[nx][ny] == 1:
                wall[nx][ny] == 2
                worm(nx,ny)

def dfs(count):
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                wall[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if wall[i][j] == 2:
                    worm(i,j)

        result = max(result,point())
        return result

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
                graph[i][j] = 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
    
print(dfs(0))