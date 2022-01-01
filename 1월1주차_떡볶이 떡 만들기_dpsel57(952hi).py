'''
page 201
떡볶이 떡 만들기

떡의수 N와 필요한 떡의 길이 M 그리고 가진떡의 정보를 입력받아
떡의길이를 맞출 수 있는 가장 크게 자를수 있는 크기를 출력하는 문제
 
입력예시
4 6
19 15 10 17

출력예시
15

느낀점
전형적인 이진탐색문제였습니다.
범위설정만 신경써서 한다면 어렵지않게 풀수 있었습니다.
'''

n,m = map(int,input().split())
ricecake = list(map(int, input().split()))
ricecake.sort()

left = 0
right = max(ricecake)

while left <= right:
    result = 0
    mid = (left + right)//2
    
    for rice in ricecake:
        if rice > mid :
            result += rice - mid
    
    if result < m:
        right = mid - 1
    
    else:
        left = mid + 1
        score = mid

         
print(score)
            
    