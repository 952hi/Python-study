def dfs(a):
    visited[a] = True
    for j in graph[a]:
        if not visited[j]:
            dfs(j)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False]*(N+1)
count = 0

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)