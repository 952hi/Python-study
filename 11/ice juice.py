'''
입력예시
4 5
00110
00011
11111
00000

정답
3
'''
        
n,m = map(int, input().split())
ice = []

for _ in range(n):
    ice.append(list(map(int, input())))
    
score = 0

def dfs(x,y):
    if x<=-1 or x >= n or y <= -1 or y>= m:
        return
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return 1
    
    return 



for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            score += 1
print(score)