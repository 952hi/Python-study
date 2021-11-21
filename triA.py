'''
Page 376
정수 삼각형
https://www.acmicpc.net/problem/1932

줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

느낀점
규칙을 찾기가 어렵지만 코드로 짜는것은 쉽게 해결할 수 있었습니다.

'''
import sys
input = sys.stdin.readline

n = int(input())
temp = []

for _ in range(n):
    temp.append(list(map(int,input().split())))


for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            temp[i][j] = temp[i-1][j] + temp[i][j]
        elif i == j:
            temp[i][j] = temp[i-1][j-1] + temp[i][j]
        else:
            temp[i][j] = max(temp[i-1][j]+ temp[i][j],temp[i-1][j-1]+ temp[i][j])
            
print(max(temp[n-1]))