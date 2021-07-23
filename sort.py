# 카드정렬하기 백준1715번
# 정렬된 카드 묶음  A B C 를 -> A+B+C로 만들때 
# 최소의 비교횟수를 출력하는 문제이다

# 10 20 40 
# 10+20 -> 30 30+40 -> 70 30+70 -> 100
# 20+40 -> 60 60+10 -> 70 60+70 -> 130

# 위의 예를 통해 최소숫자를 더했을때
# 최소 비교횟수가 나온다는 것을 알게됨
# 제한조건 중 시간제한이 2초이기에
 
import heapq

n = int(input())
compare = []
data = 0
a,b= 0 , 0
result = 0

for i in range(n):
    data = int(input())
    heapq.heappush(compare, data)

while len(compare)>1:
    a = heapq.heappop(compare)
    b = heapq.heappop(compare)
    heapq.heappush(compare, a+b)

    result = result + (a+b)

print(result)
    
