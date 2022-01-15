'''
https://www.acmicpc.net/problem/14888
연산자 끼워넣기

수의 갯수 n
수의 값 리스트
연산자의 덧셈 뺄셈 곱셈 나눗셈 갯수 를 입력받아

최댓값과 최소값을 출력하는 문제

느낀점
간단하게 dfs로 풀수 잇는 문제였습니다.
'''
import sys
input = sys.stdin.readline

n = int(input())
digit = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())
max_digit = -sys.maxsize
min_digit = sys.maxsize

def dfs(i,now):
    global n,digit,plus,minus,mul,div,max_digit,min_digit
    if i == n:
        max_digit = max(max_digit,now)
        min_digit = min(min_digit,now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1,now+digit[i])
            plus += 1
        if minus > 0:
            minus -=1
            dfs(i+1,now-digit[i])
            minus +=1
        
        if mul  > 0 :
            mul -= 1
            dfs(i+1,now*digit[i])
            mul += 1
        
        if div > 0 :
            div -= 1
            dfs(i+1,int(now/digit[i]))
            div += 1

dfs(1,digit[0])
print(max_digit)
print(min_digit)