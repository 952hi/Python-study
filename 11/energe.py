import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
score = 0
comp = 0

def search(a):
    global score
    if len(temp) == 2:
        if a > score :
            score = a
        return
    else:
        for i in range(1,len(temp)-1):
            comp = temp[i-1]*temp[i+1]
            digit = temp[i]
            
            del temp[i]
            
            search(a+comp)
            temp.insert(i, digit)

search(0)
print(score)