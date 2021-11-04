import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())

graph =[[] for _ in range(n+1)]
virus= [0] * (n+1)
virus[1] = 1

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in graph[x]:
        if virus[i] == 0:
            virus[i] = 1
            q.append(i)
count = 0
for i in range(2,n+1):
    if virus[i] == 1:
        count += 1

print(count)