import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
comp = []
for _ in range(n):
    comp.append(int(input()))


for i in range(m+k):
    a,b,c = map(int, input().split())
    temp = 0
    if a == 1:
        comp[b-1] = c
    else:
        for j in comp[b-1:c]:
            temp += j
    print(temp)

