''' 
page 118 게임개발

문제설명
크기 N*M 으로 구성된 직사각형 맵에서 캐릭터의 좌표 x,y 를 받아 
아래 메뉴얼에 따라 상하좌우로 이동시켜 캐릭터가 방문한 칸의 수를 출력하시오.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 90도 회전 )부터 차례대로 갈 곳을 정한다

2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진한다. 
   왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.

3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 
   단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다 

맵에서 0이면 육지 1이면 바다 바다는 통행할 수 없음
캐릭터는 처음 방향은 입력받는다 
0 북쪽 1 동쪽 2 남쪽 3 서쪽

'''
def turn_character(a):
    a = a-1
    if a == -1:
        a= 3
    return a

# 맵크기와 x,y 그리고 방향을 입력받음
n,m = map(int, input().split())
x,y,direction = map(int, input().split())

# 육지와 바다의 정보를 가진 리스트 입력받음
map_sl = []
for _ in range(n):
    map_sl.append(list(map(int, input().split())))

# 북 동 남 서 순서로 변화량 
dxdy = [(-1,0),(0,1),(1,0),(0,-1)]

# 다녀간 곳을 체크하기위한 리스트 선언
# 처음 위치인 x,y는 다녀간 것이므로 1을 넣어줌
map_check = [[0]*m for _ in range(n)]
map_check[x][y] = 1

# 북 동 남 서 중 못 가는 상황 카운트
impossible_count = 0

# 방문한 횟수 카운트
count = 1
nx,ny = 0,0

while True:
    
    # 반시계회전 
    direction = turn_character(direction)
    
    # x,y값 변화
    nx= x+dxdy[direction][0]
    ny= y+dxdy[direction][1]
    
    # 육지이고 안가본 곳이라면
    # 간곳으로 체크 하고 x,y에 그 nx ,ny 값을 넣어 그곳에서 4방향체크
    # nx ny로 이동했기에 불가능카운트 0으로 초기화

    if map_sl[nx][ny] ==0 and map_check[nx][ny]==0:
        map_check[nx][ny] = 1
        x,y = nx, ny
        count = count+1
        impossible_count = 0
        continue

    # 이미가본곳이거나 바다라면
    # 불가능 카운트 +1
    else:
        impossible_count = impossible_count + 1

    # 4방향이 모두 못갈경우
    if impossible_count == 4:

        # 뒷칸으로 이동
        nx = x-dxdy[direction][0]
        ny = y-dxdy[direction][1]

        # 육지라면 그다음 x,y값에 넣어 다시 4방향 체크
        if map_sl[nx][nx] == 0:
            x,y = nx,ny
        else:
            break
        # 뒷칸으로 이동했기때문에 불가능카운트 초기화
        impossible_count = 0

print(count)

"""

느낀점 
dfs와 유사하다고 생각이 들었다.
저번주 블록이동하기에서 두칸을 이동시키다가 한칸을 이동시키니 구현하기 쉬웠다.
새로운칸으로 이동시킬때 불가능카운트 초기화를 해줘야하는데
마지막부분에 impossible_count = 0 를 빠트려서 제대로 실행이 안되서 오래걸렸다.
바로 코드짜는게 아니라 그림이나 손코딩을 하는 습관 길러야겠다고 생각했습니다.
"""