# 카드정렬하기 백준1715번
# 정렬된 카드 묶음  A B C 를 -> A+B+C로 만들때 
# 최소의 비교횟수를 출력하는 문제이다

# 10 20 40 
# 10+20 -> 30 30+40 -> 70 30+70 -> 100
# 20+40 -> 60 60+10 -> 70 60+70 -> 130

# 위의 예를 통해 최소숫자를 더했을때
# 최소 비교횟수가 나온다는 것을 알게됨
# 제한조건 중 시간제한이 2초이기
# 수행시간이 적은 힙정렬을 사용하기로함

# 힙정렬 사용위한 라이브러리 불러오기 
import heapq

# 비교할 값 받기
n = int(input())

# 비교 리스트 및 변수 초기화
compare = []
data = 0
a,b= 0 , 0
result = 0

# 받은 값 최소 힙에
for i in range(n):
    data = int(input())
    heapq.heappush(compare, data)

# 트리에 남은게 없을때까지 반복
while len(compare)>1:

    # 가장 작은 두 수를 가져옴
    a = heapq.heappop(compare)
    b = heapq.heappop(compare)
    # 합하여 넣어줌
    heapq.heappush(compare, a+b)

    # 결과에 넣어줌
    result = result + (a+b)

print(result)

# 느낀점
# 1. 엄청나게 간단하지만 2초라는 제한시간이 걸려있어 당황했다
# 2. 파이썬은 라이브러리를 통해 쉽고 간편하게 이용할수있어서 좋은것 같다 

