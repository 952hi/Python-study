'''
https://www.acmicpc.net/problem/3665
최종순위

입력예시
3

5
5-> 4 -> 3->2 -> 1 
2
2 4
3 4

3
2 3 1
0

4
1 2 3 4
3
1 2
3 4
2 3

느낀점 
문제가 이해가 안돼서 어려웠고 인접행렬을 많이 사용안해봐서 어려웠다

'''
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    indegree = [0] * (n+1)
    
    graph = [[False] * (n+1) for i in range(n+1)]
    data = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    m = int(input())
    
    for i in range(m):
        a,b = map(int, input().split())
        
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            
            indegree[a] -= 1
            indegree[b] += 1
    
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
 
    check = False
    cycle = False
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
        
        if len(q) >= 2:
            check = True
            break

        now = q.popleft()
        result.append(now)
        
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                
                if indegree[j] == 0:
                    q.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif check:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
            