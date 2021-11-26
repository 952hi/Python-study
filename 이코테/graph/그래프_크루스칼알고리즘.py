'''
https://www.acmicpc.net/problem/1197
최소스패닝 트리

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력예시
3 3
1 2 1
2 3 2
1 3 3

출력 -> 3

느낀점
사이클을 생각안하고 다익스트라 알고리즘으로 착각해서 시간이 오래걸렸습니다.
예전에 MST 문제를 프림알고리즘으로 풀었는데 이번에는 크루스칼로 풀어봤습니다.
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
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0] * (v+1)

edges = []
result = 0
for i in range(1,v+1):
    parent[i] = i
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        
print(result)