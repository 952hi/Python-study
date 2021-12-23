'''
page 386
정확한순위 문제

학생 N명 과 학생간 성적비교횟수 M을 입력받아
성적순위를 정확히 알수 있는 학생이 몇명인지 출력하는 문제

입력예시
6 6
1 5 --> 1번학생은 5번학생보다 성적이 낮다는 의미
3 4
4 2
4 6
5 2
5 4

출력예시
1
느낀점
플로이드 워셜 알고리즘 문제를 너무오랜만에 풀어봐서
답지보면서 문제를 풀었습니다.
'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로는 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 성적비교값 입력받아 초기화
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

count = 0

for i in range(1,n+1):
    check = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            check += 1
    if check == n :
        count += 1

print(count)