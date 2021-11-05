'''
https://www.acmicpc.net/problem/15686
page 332
치킨 배달

리스트를 받아 집이면 1 치킨집이면 2 빈곳이면 0 

치킨집 n개 중 m개를 선택 했을때
치킨거리 -> 집에서 치킨집까지의 최소거리를 모든 집별로 구해 합산해 출력
 
'''
import itertools, sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 탐색
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
            arr[i][j] = 0  # 빈 칸으로 수정

# 치킨집 중에 M개 고르기(조합)
result = list(itertools.combinations(chicken, M))

# 탐색
# 정수최대값 대입
min_distance = sys.maxsize
for i in range(len(result)):
    distance = 0
    
    for m in range(N):
        for n in range(N):
            # 집이 위치 했으면 거리계산
            
            if arr[m][n] == 1:
                temp = sys.maxsize
                
                for j in range(M):
                    temp = min(temp, abs(m - result[i][j][0]) + abs(n - result[i][j][1]))
                # 모든집을 합산
                distance += temp
                
    # 조합으로 생성된 치킨집 별 최소거리를 비교해 최소값인지 확인
    min_distance = min(min_distance, distance)

# 출력
print(min_distance)

'''
느낀점
sys.maxsize -> 정수 최댓값
itertools.combinations 조합 ,itertools.permutations 순열
좌표값에 순서가 중요하지않기 때문에 조합을 사용
for문 내포함수

'''