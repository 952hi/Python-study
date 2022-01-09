'''
https://www.acmicpc.net/problem/11375
11375번 열혈강호

강호네 회사에는 직원이 N명이 있고, 해야할 일이 M개가 있다. 직원은 1번부터 N번까지 번호가 매겨져 있고, 일은 1번부터 M번까지 번호가 매겨져 있다.
각 직원은 한 개의 일만 할 수 있고, 각각의 일을 담당하는 사람은 1명이어야 한다.
각각의 직원이 할 수 있는 일의 목록이 주어졌을 때, M개의 일 중에서 최대 몇 개를 할 수 있는지 구하는 프로그램을 작성하시오.

입력예시
5 5
2 1 2
1 1
2 2 3
3 3 4 5
1 1

출력예시
4

느낀점
이분매칭 개념을 이해할 수 있어서 좋았습니다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
d = [0 for i in range(m + 1)]
cnt = 0

def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in a[1:]:
        s[i].append(j)
        
for i in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    if dfs(i):
        cnt += 1

print(cnt)