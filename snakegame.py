# 구현 11번 뱀

# 주어진 크기의 게임판에서 주어진 사과와 명령을 바탕으로 
# 게임이 몇초에 끝나는지 출력하는 문제
# L 왼쪽 90도 회전 D 오른쪽 90도 회전
# 뱀은 매초 머리를 다음칸으로 이동시킨다.
# 이동한 칸에 사과가 있다면 그 칸의 사과는 없어지고 꼬리는 움직이지 않는다
# 이동한 칸에 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워준다 //몸길이는 변하지 않는다//

# 게임판 크기를 입력받는다
n = int(input())
# 사과의 갯수를 입력받는다
k = int(input())

# 사과위치를 입력받을 통을 초기화한다.
data = [[0] * (n + 1) for _ in range(n + 1)]
# 명령을 입력받을 통을 만든다
info = []


for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동 남 서 북
# L명령 +1 
# D명령 -1

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

# ex -1 % 4 -> (-1 * 4 +3) % 4 = 3
# 들어온 명령에 따라 방향을 바꾼다
 
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
        print(direction)
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    # 머리위치
    x, y = 1, 1
    # 뱀이 xy 좌표값에 위치하면 2로 표시

    data[x][y] = 2
    direction = 0 
    time = 0

    #명령을 카운트하는      
    index = 0

    q = [(x, y)] 
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0 
            
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 예외처리 벽에 부딪치거나 꼬리에 머리가 닿았을때
        else:
            time += 1
            break        
        x, y = nx, ny 
        time += 1

        # 회전정보가 명령갯수보다 작거나 명령시간과 시간이 같으면 턴 함수실행
        if index < l and time == info[index][0]: 
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())

# 느낀점
# pop(0), -1 % 4, map함수