'''
숫자 카드 게임
이코테 PAGE 96

숫자가 쓰여진 N*M 행렬을 입력받아
각 행에서 가장작은 수 뽑아 그중에서 가장 큰 수를 출력하는 문제

'''

import sys
input=sys.stdin.readline

n,m = map(int,input().split())

result = 0
for i in range(n):
    comp = list(map(int,input().split()))
    min_digit = min(comp)
    result = max(result,min_digit)

print(result)
        