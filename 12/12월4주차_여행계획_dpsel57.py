'''
page 393 여행계획문제

여행지의 수 N과 여행계획의 도시의 수 M
여행지간 연결된 정보를 받아와 여행계획이 수행이 가능한지 여부를 출력하는 문제

느낀점
간단한 서로소 알고리즘 문제였습니다.

입력예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

출력예시
YES
'''
import sys
input = sys.stdin.readline

def findparent(parent,x):
    if parent[x] != x:
        parent[x] = findparent(parent, parent[x])
    return parent[x]

def unionparent(parent,a,b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    
    if a>b :
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int, input().split())
data = []
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1 :
            unionparent(parent, i+1, j+1)

travel = list(map(int,input().split()))
result = 0
for i in range(m-1):
    if findparent(parent, travel[i]) != findparent(parent, travel[i+1]):
        result = 1

if result == 1:
    print("NO")
else:
    print("YES")        