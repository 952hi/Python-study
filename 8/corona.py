# 경쟁적 전염
# 교재 page 344 백준 18405번 

# 시험관의 크기 N
# 바이러스 개수 K
# 시간 S
# 좌표값 X,Y  

# 문제설명
# 시험관의 크기 받고 그 크기만큼 리스트생성
# 1초에 한번 모든 바이러스가 전염함 
# #바이러스 1~K까지 바이러스를 작은수부터 순서대로 전염시킴 
# 전염은 동서남북 방향으로 4곳 전염시킴
# 리스트 0이면 바이러스 존재하지않음
# 0이 아니고 1~K라면 그곳은 이미 전염되있음
# 이미 바이러스1이 전염되있는상태에서 바이러스2가 전염시킬수 없음
# 정해진 시간에 받아온 XY좌표값에 있는 값을 출력하는 문제

# 시험관의 크기와 바이러스의 개수를 입력받음   
n, k = map(int, input().split())

# 시험관
tube = []
# 바이러스
virus = []

# 입력받은 시험관의 원소를 리스트에 추가
for i in range(n):
    tube.append(list(map(int, input().split()))) 
    for j in range(n):
        # 0이 아닌값은 바이러스이므로 바이러스 리스트에 추가함
        if tube[i][j] != 0:
            virus.append((tube[i][j], 0 , i , j))

# 작은수부터 사용해야하기에 정렬            
virus.sort()

# 시간, 출력해야하는 XY 값 입력받음
time, search_x , search_y = map(int, input().split())

# 동남서북
dx = [1,0,-1,0] 
dy = [0,1,0,-1]

while len(virus)>0:
    # 왼쪽부터 바이러스, 시간 , 좌표 xy 값
    germ , s ,x ,y = virus.pop(0)

    # 출력해야할 시간이라면 반복문 탈출
    if s == time:
        break
    
    # 동남서북으로 전염시키고 전염이 가능하다면 시험관에 추가
    # 다음 전염을 위해 바이러스 리스트에도 추가 
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0<= next_x and next_x < n and 0 <= next_y and next_y <n :
            if tube[next_x][next_y] == 0:
                tube[next_x][next_y] = germ
                virus.append((germ,s+1,next_x,next_y))

print(tube[search_x-1][search_y-1])

# 느낀점
# 
# 다른 스터디원께서 풀이를 한번해주시기도 했고 7월 3주차 연구소 문제와 비슷해 이해하기 편했습니다.





