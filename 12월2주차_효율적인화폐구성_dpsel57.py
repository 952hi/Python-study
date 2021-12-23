'''
page226 
효율적인화폐구성
n,m을 입력받아
n -> 화폐의 개수
m -> 돈의 값
 
돈 m을 화폐로 표현할때 최소의 화폐 수를 출력하는 문제
 
입력예시
2 15 => 2개의 화폐 , 15원
2 => 2원짜리 화폐
3 => 3원짜리 화페 

만약 주어진 화폐로 출력하지 못할경우 -1 출력

느낀점
예외처리 부분만 잡으면 쉽게 풀 수 있는 문제
크게 어려움이 없었다.
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
money_size = []
for _ in range(n):
    money_size.append(int(input()))
    
money_size.sort()

check = 0

for i in range(n-1,-1,-1):
    
    if money_size[i] > m :
        continue
    
    a = m//money_size[i]
    
    if m % money_size[i] == 0 :
        check = check + a
        m = 0
    else:
        check = check + a
        m = m - a *money_size[i]
        
if m > 0 :
    print(-1)
else:
    print(check)
        
        