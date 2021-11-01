def dfs(graph,visited, v):
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, visited, i)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [0]*9

dfs(graph, visited, 1)
