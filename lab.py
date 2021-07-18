# 구현 16 연구소
# 깊이우선탐색 강의 
# 행과 열 각각 받아 연구소 크기를 결정합니다.
# 그 후 벽과 바이러스 그리고 빈칸의 위치를 받아 들입니다.
# 벽을 3개 세워 안전영역의 최댓값을 구합니다.
# 바이러스가 있으면 2
# 벽이 있으면 1
# 빈칸이면 0
# 바이러스는 십자가 형태로 퍼짐
# 벽은 최대 3개까지만 설치할 수 있고 무조건 3개를 세워야 한다



n, m = map(int, input().split())
# 초기 연구소 영역
data = []

# 벽을 설치한 뒤의 연구소 영역
temp = [[0] * m for _ in range(n)] 

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향 
# 동 남 서 북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


result = 0

# 깊이 우선 탐색(DFS)을 이용해 
# 각 바이러스가 사방으로 퍼지도록 하기

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 동서남북 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 0의 갯수를 세어 안전영역을 크기를 계산
def score():
    point = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                point += 1
    return point


# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def fence(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최대값 계산
        result = max(result, score())
        return

    # 울타리를 3개 만들기
    # 모든경우에수
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                fence(count)
                data[i][j] = 0
                count -= 1

fence(0)
print(result)

# 느낀점
# DFS를 구현해보니 BFS은 어떨까 라는 생각이 들었고 
# 문제가 어려워서 많이 노력해야 할것 같다는 느낌을 받았습니다. 







