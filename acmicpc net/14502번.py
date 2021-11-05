import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
wall = [[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0

def corona(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < n and nx >= 0 and ny >= 0 and ny < m :
            if wall[nx][ny] == 0:
                wall[nx][ny] = 2
                corona(nx,ny)
                
def get_point():
    score = 0
    for i,j in [(x,y) for x in range(n) for y in range(m)]:
        if wall[i][j] == 0:
            score += 1
    return score
    
def dfs(count):
    global result
    if count == 3:
        for i,j in [(x,y) for x in range(n) for y in range(m)]:
            wall[i][j] = graph[i][j]

        for i,j in [(x,y) for x in range(n) for y in range(m)]:
            if wall[i][j] == 2:
                corona(i,j)

        result = max(result,get_point())
        return 

    for i,j in [(x,y) for x in range(n) for y in range(m)]:
        if graph[i][j] == 0:
            graph[i][j] = 1
            count += 1
            dfs(count)
            graph[i][j] = 0
            count -= 1
dfs(0)
print(result)