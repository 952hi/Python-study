n,m = map(int,input().split())
ice=[]
for _ in range(n):
    ice.append(list(map(int,input())))


def dfs(x,y):
    if x <= -1 or x >=n or y<=-1 or y>=m:
        return 0
    
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return 1

    return 0

score = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == 1:
            score += 1

print(score)
