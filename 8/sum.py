T = int(input())

for a in range(T):
    hap = 0
    data = list(map(int, input().split()))
    for i in data:
        if i % 2 ==1 :
            hap+= i
    print("#%d %d" % (a+1,hap))
