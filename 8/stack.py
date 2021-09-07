N = int(input())
dp= []
order = []
comp = 0

for i in range(N):
    order.append(input().split())

for j in range(N):

    if order[j][0] == "push" :
        comp = order[j][1]
        dp.append(comp)

    elif order[j][0] == "pop":
        if len(dp) ==0 :
            print(-1)
        else:
            print(dp.pop())
    
    elif order[j][0] == "size":
        print(len(dp))
    
    elif order[j][0] == "empty":
        if len(dp) == 0:
            print(1)
        else: print(0)

    elif order[j][0] == "top":
        if len(dp) == 0:
            print(-1)
        else:
            print(dp[-1])
