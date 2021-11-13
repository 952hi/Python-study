  
'''
https://www.acmicpc.net/problem/14888 
백준 14888번 
page 349 연사자 끼워 넣기 문제

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 
둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

입력예시

3
3 4 5
1 0 1 0

'''
import sys
import math

input = sys.stdin.readline

n = int(input())
digit = list(map(int,input().split()))
add,sub,mul,div = map(int , input().split())

# 비교할 변수에 무한대 값 대입
comp_min = sys.maxsize
comp_max = -sys.maxsize

#사용한 숫자의 개수 , 첫번째숫자값
def dfs(i,now):
    global add,sub,mul,div,comp_max,comp_min

    if  i == n:
        comp_min = min(comp_min,now)
        comp_max = max(comp_max,now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+digit[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-digit[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now*digit[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,int(now /digit[i]))
            div += 1

dfs(1, digit[0])

print(comp_max)
print(comp_min)

'''
느낀점
from itertools import permutations < 모든 순열의 조합을 만들어주는 함수를 사용하면
DFS를 사용하지 않고 만들수 있을것 같은느낌이다.
'''
