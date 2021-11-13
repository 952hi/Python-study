'''
이코테 page375

n*m 리스트를 입력받아 최대로 캘수 있는 금의 양을 출력하는 문제

1 2  3  4 
5 6  7  8
9 10 11 12

규칙 
첫 번째 열 어디서든 출발가능 ->1, 5, 9 번에서 시작가능 
오른쪽 한칸 오른쪽위 한칸 오른쪽 아래 세가지 방법으로 이동가능 -> 5번이라면 2 6 10 이동가능

입력예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

'''
import sys
input = sys.stdin.readline

t = int(input())

gold = []

dy = [-1,0,1]

for _ in range(t):
    n,m = map(int, input().split())
    gold = list(map(int, input().split()))
    arr = []
    comp = 0
    for i in range(n):
        arr.append(gold[comp:m+comp])
        comp +=m
    for j in range(1,m):
        for i in range(n):
            if i==0:
                top = 0
            else:
                top = arr[i-1][j-1]
            if i == n-1 :
                bottom = 0
            else:
                bottom = arr[i+1][j-1]
            right = arr[i][j-1]
            arr[i][j] = arr[i][j] + max(top, bottom, right)
    max_comp = -sys.maxsize
    for i in range(n):
        max_comp = max(max_comp, arr[i][m-1])
    print(max_comp)

'''
느낀점
매우간단하게 조건문으로 해결할 수 있었다
x,y 좌표값을 반대로 생각해야하는 부분이 있어서 어려웠다
'''

