'''
위에서 아래로 page 178
정수 N을 입력받아 N만큼 정수를 입력받는다
내림차순으로 출력한다 즉 큰수 먼저 출력한다 

느낀점
range 범위 많이 틀렸었는데 이 문제를 통해서 많이 익혔다
이론으로 다 알고 있어도 코드로 구현해보고 안해보고 차이가 큰것 같다

'''


def selection_sort(a):

    for i in range(N):
        for j in range(i+1,N):
            if temp[j] < temp[i]:
                comp = temp[i]
                temp[i] = temp[j]
                temp[j] = comp

    return a

def bubble_sort(b):

    for _ in range(N):
        for i in range(N-1):

            if b[i] > b[i+1]:
                comp = b[i+1]
                b[i+1] = b[i]
                b[i] = comp
    return b

def insertion_sort(c):

    for i in range(1,N):
        idx = c[i]

        for j in range(i,0,-1):
            if idx < c[j-1]:
                c[j], c[j-1] = c[j-1],c[j]
    return c

def heap_sort(d):

    a = len(d)

    for i in range(1, a):
        c = i

        # 루트노드가 될때까지 반복
        while c > 0:

            # 트리에서 부모와 자식 관계 왼쪽자식 = 루트*2+1 부모 = (자식-1) // 2
            root = (c - 1) // 2

            # 자식이 루트보다 크면 교환 
            if d[c] > d[root]:
                d[c], d[root] = d[root], d[c]

            # 자식을 루트로 바꿔 그 위 부모와 다시비교
            c = root
    
    for i in range(a - 1, -1, -1):

        #최대힙이므로 큰값인 루트값을 빼서 마지막으로 이동
        d[0], d[i] = d[i], d[0]
        root, c = 0, 1

        # 리프노드가 될때까지 반복
        while c < i:

            c = root * 2 + 1

            # 왼쪽 오른쪽 자식 비교 우측이 크면 자식 값 증가
            if c < i - 1 and d[c] < d[c + 1]:
                c += 1

            # 자식이 루트보다 크면 자식 부모 교환
            if c < i and d[c] > d[root]:
                d[c], d[root] = d[root], d[c]
            root = c

    return d
    

N = int(input())
temp = []
comp = 0

for _ in range(N):
    temp.append(int(input()))

heap_sort(temp)
print()
for _ in range(N):
    print(temp.pop())