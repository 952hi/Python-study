'''
page 395 탑승구
탑승구의 수 N과 비행기의 수M
각비행기별 원하는 탑승구를 입력받아
최대수용가능한 탑승구의 수를 출력하는 문제
느낀점
문제자체는 어려운게 없었지만 문제의 조건이 이해가 안돼서 다른사람이 설명해놓은 걸 보고 문제를 풀었습니다.
입력예시
4
3
4
1
1
출력예시
2
'''
import sys
input = sys.stdin.readline

def find_p(parent,x):
    if parent[x] != x:
        parent[x] = find_p(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find_p(parent,a)
    b = find_p(parent,b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
result = 0


for i in range(m):
    data = find_p(parent, int(input()))
    if data == 0:
        break
    union(parent, data-1, data)
    result +=1

print(result)