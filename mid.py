a = int(input())
compare= []
temp = 0

for i in range(a):
    compare.append(int(input()))
    compare.sort()
    temp = len(compare)//2
    
    if len(compare) == 1:
        print(compare[0])
        
    else:
        if len(compare)%2 == 0:
        
            if compare[temp-1] > compare[temp]:
                print(compare[temp])
            else:
                print(compare[temp-1])
    
        if len(compare)%2 ==1:
            print(compare[temp])
