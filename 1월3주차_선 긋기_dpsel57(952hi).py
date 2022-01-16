'''
https://www.acmicpc.net/problem/2170
선 긋기

선을 긋는 정보를 받아와 중복을 제외하고
선을 그은 길이를 출력하는 문제

느낀점
튜플형식으로 하지않으면 시간초과가 나서 당황했다. 

입력예시
4
1 3
2 5
3 5
6 7

출력예시
5
'''
import sys
input = sys.stdin.readline

n = int(input())
line = []
length = 0
for _ in range(n):
    a,b = map(int,input().split())
    line.append((a,b))

line.sort()

start = line[0][0]
end = line[0][1]

for i in range(1,n):
    istart,iend = line[i][0],line[i][1]
    
    if istart < end:
        end = max(end,iend)
    else:
        length += end - start
        start , end = istart, iend

length += end - start
            
print(length)