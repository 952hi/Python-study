'''
이코테 page 99
1이 될때까지


어떠한 수 N을 입력받아

1. n에서 1을 뺀다
2. n을 k로 나눈다

두 가지 규칙을 바탕으로 1로만들때 최소횟수를 출력하는 문제
'''

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
check = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // 5
        check += 1
    else:
        n = n -1
        check += 1
        
print(check)
    