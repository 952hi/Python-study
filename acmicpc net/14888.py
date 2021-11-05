import sys
import math
input = sys.stdin.readline

n = int(input())
digit = list(map(int,input().split()))
add,sub,mul,div = map(int , input().split())

print(n,digit,sub)

comp_min = math.inf
comp_max = -math.inf

def dfs(i,now):
    global add,sub,mul,div,comp_max,comp_min

    if  i == n:
        comp_min = min(comp_min,now)
        comp_max = max(comp_max,now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+digit[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-digit[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now*digit[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,int(now /digit[i]))
            div += 1

dfs(1, digit[0])

print(comp_max)
print(comp_min)