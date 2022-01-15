'''
https://www.acmicpc.net/problem/1697
숨바꼭질

n,k의 좌표값을 통해
n에서 k로 이동할때
최소이동횟수를 출력하는 문제

이동가능 방법 +-1 or *2

느낀점
1로만들기랑 비슷한 문제라고 생각이 들었습니다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q= deque()
    q.append(n)
    while q:
        x = q.popleft()

        if x == k:
            print(temp[x])
            break
        
        for i in (x-1,x+1,x*2):
            if 0 <= i <= max and not temp[i]:
                temp[i] = temp[x] + 1
                q.append(i)
max =10**5
temp=[0]*(max+1)

n,k = map(int,input().split())

bfs()