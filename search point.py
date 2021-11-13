'''
이코테 page 368
고정점 찾기

N개의 원소로 이루어진 오름차순으로 정렬된 순열을 받아드려
인덱스값과 원소의 값이 같은 고정점을 출력하시오

ex) a[2] = 2 -> 고정점

5
15 -6 1 3 7

고정점이 있다면 고정점 출력
고정점이 없다면 -1 출력

느낀점
이진탐색의 종료 예외처리가 헷갈린거 빼고
쉽게 해결할 수 있었습니다.

'''

'''
1회차

import sys
input = sys.stdin.readline
n = int(input())
temp = list(map(int,input().split()))

a = 0
for i in range(n):
    if i == temp[i] :
        a = i

if a == 0 :
    print(-1)
else:
    print(a)
        
'''

# 2회차
import sys
input = sys.stdin.readline
n = int(input())
temp = list(map(int,input().split()))

left = 0
right = n -1

while True:
    mid = (left + right)//2 
    
    if left > right :
        print(-1)
        break
    
    if temp[mid] == mid :
        print(mid)
        break
    
    if temp[mid]  > mid :
        right = mid -1
    else:
        left = mid + 1 