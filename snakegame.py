snake_mapsize = int(input())
apple = int(input())

snake_map = [[0]*(snake_mapsize) for i in range(snake_mapsize)]

for i in range(apple):
    r,l = map(int, input().split())
    snake_map[r][l] = 1


    

print(snake_map) 


