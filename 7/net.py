# 공유기 설치
# page 369
# 입력받은 집의 좌표를 통해 인접한 공유기 사이 거리를 가능한 크게 설치
# 
# 조건
# 한 집에 최대 한개 설치 가능
# 가장 인접한 두 공유기 사이의 거리를 최대로 하기
# 
# 집의 좌표와 공유기 수를 입력받고
# 가장 인접한 두 공유기 사이의 최대 거리를 출력하라  


# 집 좌표, 공유기 수 입력받기
adress,net = map(int,input().split())

# 집 좌표 리시트 초기화
home = []

# 좌표 추가
for i in range(adress):
    home.append(int(input()))

# sort()를 통해 정렬
home.sort()

# 최소 최대 거리 지정
fisrt_range = 1
max_range = home[-1] - home[0]

result = 0


while(fisrt_range <= max_range):

    #최소 최대 크기를 통해 중간 크기 도출
    mid_range = (fisrt_range + max_range)//2
    
    # 홈 리스트 첫번재를 첫 번째 공유기로 지정
    value = home[0]
    count = 1 

    # 좌표리스트의 두번째 부터 끝까지 
    # 중앙값과 첫번째값보다 크면 그자리에 공유기 설치
    for i in range(1,adress):
        if home[i] >= value + mid_range :
            value = home[i]
            count += 1

    # 공유기가 같거나 많이 설치 되면
    # 더 큰 거리가 가능한지 검사하기 위해 초기값 증가        
    if count >= net :
        fisrt_range = mid_range + 1
        result = mid_range

    # 정해진 공유기 수를 채우지 못했을 경우
    # 최대 범위 감소
    else:
        max_range = mid_range - 1

print(result)

# 느낀점
# 저번주에 비해 쉽게 느껴졌고 확실히 푸는데 걸린 시간도 적었습니다.
# 최소값과 최대값의 중앙값을 통해 계산해 쉽게 풀 수 있엇다. 

