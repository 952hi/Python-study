'''
https://www.acmicpc.net/problem/1149
RGB

문제간단설명
i = 2일때
2번집은 1번집과 3번집의 색상과 같으면 안된다 
규칙을 참고해서 

집의수와 집의 색상을 칠하는데 드는비용 정보를 입력받아
각집을 칠했을때 최소비용을 출력하는 문제

입력예시
3
(R  G  B ) 색상 순서
26 40 83
49 60 57
13 89 99

출력예시
96

느낀점
시간을 생각해서 문제 푸는연습이 필수적일것 같습니다.

'''
# import sys
# input = sys.stdin.readline
# n = int(input())
# paintcost = []
# for i in range(n):
#     paintcost.append(list(map(int,input().split())))

# home = [0 for _ in range(n)]



# def painting(color):
#     home[0] = paintcost[0][color]
#     cnt = 1
#     sum = 0
    
#     while cnt<n:
#         if cnt >= 2:
#             if home[cnt-1] == 0:
#                 home[cnt] = min(paintcost[cnt][1],paintcost[cnt][2])
#             elif home[cnt-1] == 1:
#                 home[cnt] = min(paintcost[cnt][0],paintcost[cnt][2])
#             else:
#                 home[cnt] = min(paintcost[cnt][0],paintcost[cnt][1])
#             return 0
#         else:    
#             if home[cnt-1] == 0:
#                 home[cnt] = min(paintcost[cnt][1],paintcost[cnt][2])
#             elif home[cnt-1] == 1:
#                 home[cnt] = min(paintcost[cnt][0],paintcost[cnt][2])
#             else:
#                 home[cnt] = min(paintcost[cnt][0],paintcost[cnt][1])
#         cnt +=1
#     for i in home:
#         sum += i
        
#     return sum

# first_red =painting(0)
# print(home)
# first_blue = painting(1)
# print(home)
# first_green = painting(2)
# print(home)
# print(min(first_red,first_green,first_blue))

import sys
input = sys.stdin.readline

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    a[i][0]=a[i][0]+min(a[i-1][1],a[i-1][2])
    a[i][1]=a[i][1]+min(a[i-1][0],a[i-1][2])
    a[i][2]=a[i][2]+min(a[i-1][0],a[i-1][1])

print(min(a[n-1]))