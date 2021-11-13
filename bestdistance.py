'''
미래도시
이코테 page259

문제설명
1번회사에서 X회사로 가야합니다.
가는 도중 K번 회사로가 소개팅에 참석해야합니다.
1번 회사에서 K번 회사에서 소개팅한 후 X회사로 갈때 최소 이동시간을 출력하시오
하나의 회사를 이동하면 1의 시간이 소요됨

1번에서 X회사로 도달할수없는 경우 -1 출력

5 7 -> n, m 회사수 , 연결도로수
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5 -> 최종 회사 X ,소개팅 장소 K

느낀점
지난주 BFS를 완벽하게 이해해서 쉽게 해결할 수 있었습니다.

'''
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
score = [0] * (n+1)
check = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
x , k = map(int,input().split())

q = deque()
q.append(1)


def bfs():
    while q:
        a = q.popleft()
        for i in graph[a]:
            if score[i] == 0:
                q.append(i)
                score[i] = score[a] + 1

bfs()
if score[k] == 0:
    check = 1
temp = score[k]


score = [0] * (n+1)

q.append(k)
bfs()
if score[x] == 0:
    check = 1
    
if check != 1:
    temp = temp + score[x]
    print(temp)
else:
    print(-1)