'''
https://www.acmicpc.net/problem/18428
감시피하기

입력예시
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

느낀점
DFS 문제 푼게 대부분 4방향 탐색햇는데 이번 문제는 같은 행 열 끝까지 탐색해야했다.
DFS -> 4방향 이라고 생각하는 고정관념때문에 오래걸렸던것 같다.

'''
import sys
input = sys.stdin.readline
from itertools import combinations

def watch():
    for teacher in teacher_list:
        x, y = teacher
        # 상
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if hallway[nx][ny] == 'S':
                return False

            if hallway[nx][ny] == 'O':
                break
        # 하
        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 좌
        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 우
        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
    return True

N = int(input())
hallway = [input().split() for _ in range(N)]

empty_list = []
teacher_list = []
for i in range(N):
    for j in range(N):
        if hallway[i][j] == 'X':
            empty_list.append((i, j))
        elif hallway[i][j] == 'T':
            teacher_list.append((i, j))

# 벽 3개 뽑기
for walls in combinations(empty_list, 3):

    # 벽 세우기
    for wall in walls:
        x, y = wall
        hallway[x][y] = 'O'
    # 감시하기
    if watch():
        print('YES')
        break
    # 벽 허물기
    for wall in walls:
        x, y = wall
        hallway[x][y] = 'X'
else:
    print('NO')