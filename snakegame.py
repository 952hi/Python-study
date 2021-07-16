snake_mapsize = int(input())
apple = int(input())
snake_data = []
snake_map = [[0]*(snake_mapsize) for i in range(snake_mapsize)]

for i in range(apple):
    r,l = map(int, input().split())
    snake_map[r][l] = 1

direction = int(input())

for i in range(direction):
    x,c = input().split()
    snake_data.append(int(x))


// https://kom-story.tistory.com/188
print(snake_map) 


