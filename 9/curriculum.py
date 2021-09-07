'''
교재 page 303 
커리큘럼

문제설명
N개의 강의를 듣고자 할때
모든강의는 1번 부터 ~ N번까지 번호를 가진다
또한 동시에 여러개의 강의를 들을 수 있다고 가정한다.
N개의 강의정보를 입력받고 N개의 강의를 모두 수강하는데까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

첫째줄은 강의의 수 N이 주어진다
다음 N줄에는 각 강의시간과 강의를 듣기위한 선수강의 번호가 자연수로 지정된다
각줄은 -1로 끝난다.

입력예시 
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1 

느낀점
for i in data[1:-1] 에서 원소가 2개이면 pass되는 사실
copy.deepcopy() 깊은복사 b에 a리스트를 복사해 넣고 b를 수정하면 a에는 변경되지 않는다.
'''

from collections import deque
import copy
                     
# 강의 수 입력
N = int(input())

# 진입차수 리스트, 강의 수강시간, 그래프 초기화
indegree = [0] * (N+1)
time = [0] * (N+1)
graph = [[] for _ in range(N+1)]



for i in range(1,N+1):
    # data -> 시간, 선수강의번호 , 끝표시 -1
    data = list(map(int, input().split()))
    time[i] = data[0]
    
    for j in data[1:-1]:
        # 선수강의수당 진입차수 1 증가
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q=deque()
    
    # 진입차수 0인 강의 큐에 삽입
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌때까지
    while q:
        now = q.popleft()
        
        # 진입차수가 1인 노드를 0으로 바꿔줌
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            
            # 진입차수 0인 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1,N+1):
        print(result[i])

topology_sort()      
