'''
page 300
도시 분할 계획

도시에 연결된 길을 입력받아
도서를 두개의 2개의 구역으로 나누었을때 
최소 유지비용을 출력하시오

같은 도시간에 경로가 여러가지 존재하면안됨
모든 도시는 연결되어야함 
=> 사이클이 존재하지않고 모든 길이 연결되어야함
=> 크루스칼

n,m은 도시의개수와 길의개수
a,b,c a는 출발도시 b는 도착도시 , c는 비용

입력예시

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

느낀점
두개의 구역을나눌때 최소비용이 드는것은
크루스칼을 통해 모든 간선을 연결하고 마지막간선을 제거하면 가장 적은 비용으로 만들 수 있었다.
'''
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

edges = []
score = 0

for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
max_edgedigit = 0

for edge in edges:
    cost,a,b =edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        score += cost
        last = cost

print(score-last)    