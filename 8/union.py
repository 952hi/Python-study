'''
page298 팀 결성

입력값 예시)
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

첫줄 n,m을 입력한다 
m개 명령을 추가적으로 입력한다
0 1 3 명령형식 0 -> 합치는 명령 
1 1 7 명령형식 1 -> 같은 집합인지 확인  맞다면 YES 출력 아니면 NO 출력

느낀점
그래프에 겁먹어서 어렵게 느껴졌다.
문제를 이해할때 그림을 그리면서 하니 이해하기 편했다.


'''
def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    
    # 작은 값을 가르키도록 하여 하나의 집합을 이루게 함
    if a>b :
        parent[a] = b
    else:
        parent[b] = a


def find(parent, x):

    # 루트노드를 찾을때까지 재귀호출 수행
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


# 각 값 입력받기
n,m = map(int, input().split())

# 부모 리스트 초기화
parent = [0] * (n+1)

# 자기 부모를 자신으로 초기화
# 자신으로 초기화하면 원소가 하나인 집합이 됨
for i in range(n+1):
    parent[i] = i

for j in range(m):
    order_type,a,b = map(int, input().split())
    
    # 0 이면 합치는 명령
    if order_type == 0:
    
        union(parent, a, b)

    # 1 이면 확인하는 명령
    elif order_type == 1:

        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")


