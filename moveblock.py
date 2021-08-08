# 블록 이동하기
# page355 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/60063

# 문제설명
# 로봇개발자 "무지"는 한 달 앞으로 다가온 "카카오배 로봇경진대회"에 출품할 로봇을 준비하고 있습니다. 
# 준비 중인 로봇은 2 x 1 크기의 로봇으로 "무지"는 "0"과 "1"로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여 
# (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 로봇이 이동하는 지도는 가장 왼쪽
# 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 "0"은 빈칸을 "1"은 벽을 나타냅니다. 
# 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 
# 로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다 
# 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.
# 장애물을 피해 로봇을 최단거리로 최소한의 시간으로 목적지로 보내고 걸린시간을 출력하는 문제

from collections import deque

def get_next_pos(pos, board):
    
    # 이동가능한 위치
    next_pos = [] 

    # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos = list(pos) 
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:

        # 위쪽으로 회전하거나, 아래쪽으로 회전
        for i in [-1, 1]:

            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면 
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: 
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:

        # 왼쪽으로 회전하거나, 오른쪽으로 회전
        for i in [-1, 1]: 

            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: 
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):

    # 입력된 맵에 추가적으로 2칸씩 더 집어넣어 
    # 로봇이 맵안에 있는지 판단하기 쉬워짐

    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    # 너비 우선 탐색 수행
    q = deque()

    # 최단거리를 구해야하므로 거친자리를 체크하기
    visited = []

    # 튜플을 사용해 {(1,1) (1,2)} , {(1,2) (1,1)}를 
    # 같은 객체로 취급하기에 두칸을 차지하는 로봇이 같은 곳을 방문하지않도록 함  
    pos = {(1, 1), (1, 2)} 

    # 큐에 로봇 위치 시간을 저장
    q.append((pos, 0)) 
    # 로봇이 있는자리 방문처리
    visited.append(pos) 
    
    # 큐가 빌 때까지 반복    
    while q:
        pos, cost = q.popleft()

        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):

            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

# 느낀점
# 로봇이 한칸이 아니고 두칸을 움직이고 체크해야해서 이해하기 힘들었다
# 튜플을 사용했을때 특성 공부가 필요한것 같다