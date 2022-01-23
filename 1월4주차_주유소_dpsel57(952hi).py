'''
https://www.acmicpc.net/problem/13305
주유소

도시의 수 n
도시간 거리 값
도시별 1L당 가격
정보를 입력받아

최소 비용을 출력하는 문제

입력예제
4
2 3 1   <도시간 간격
5 2 4 1 <도시별 주유소 가격 정보
출력예제
18

느낀점
직관적으로 생각하면 시간낭비가 심하고 
코드최적화의 중요성을 느꼈습니다.
'''
import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

result = distance[0]*price[0]
minPrice = price[0]

for i in range(1,len(distance)):
    if minPrice>price[i]:
        result += price[i]*distance[i]
        minPrice = price[i]
    else:
        result += distance[i]*minPrice

print(result)

# import sys
# input = sys.stdin.readline

# n = int(input())
# distance = list(map(int,input().split()))
# price = list(map(int,input().split()))
# price.pop()

# allDistance = 0
# result = 0

# for i in range(len(distance)):
#     allDistance += distance[i]
                
# for i in range(len(distance)-1):
#     if allDistance ==0 :
#         break
    
#     if min(price)==price[i]:
#         result += (price[i]*allDistance)
#         break
#     else:
#         allDistance -= distance[i]
#         result += distance[i]*price[i] 

# print(result)