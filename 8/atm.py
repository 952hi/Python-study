human = int(input())
wait = list(map(int, input().split()))
wait.sort()
def time(a):
    hap = 0
    for j in range(a):
        hap = hap + wait[j]
    return hap
 

last = 0


for i in range(human):
    last = last + time(i)

print(last)