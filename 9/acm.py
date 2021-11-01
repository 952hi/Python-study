'''
ACM Craft https://www.acmicpc.net/problem/1005 
위상정렬 

건설해야하는 건물의 수와 건설시간 그리고 선수건물의 규칙을 받아와서
최종적으로 원하는 건물의 번호를 입력받아 최소시간을 출력해주는 문제

# 느낀점
9월 커리큘럼 문제와 다를게 없어서 어렵지 않게 풀 수 있었다.
'''
import sys 
from collections import deque

t = int(sys.stdin.readline()) 

for _ in range(t): 
    n, k = map(int, sys.stdin.readline().split())
    cost = [0] + list(map(int, sys.stdin.readline().split()))
    tree = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    dp = [0] * (n + 1)
    
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        # 선수 건설이 있으면 진입차수 +1
        in_degree[b] += 1
        tree[a].append(b)
        
    q = deque()
        
    for i in range(1, n + 1):
        #진입차수가 0인 건물 있으면 큐 삽입 
        #건설시간 코스트 리스트에 삽입 
        if in_degree[i] == 0: 
            q.append(i)
            dp[i] = cost[i]
        
    while q: 
        now = q.popleft() 
        for i in tree[now]:
            in_degree[i] -= 1
            dp[i] = max(dp[now] + cost[i], dp[i])
            if in_degree[i] == 0:
                q.append(i) 
                
    answer = int(sys.stdin.readline())
    print(dp[answer])