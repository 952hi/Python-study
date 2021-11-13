n = 5
lost = [2, 4]
reserve = [1,3,5]

answer = [1 for _ in range(n+1)]
answer[0] = 0
for i in lost:
    answer[i] = 0

for i in reserve:
    answer[i] = 2


temp = [0 for _ in range(n+1)]

    
count = 0
for i in range(1,n):
    if answer[i] == 0:
        if answer[i-1] == 2:
            count += 1
        if answer[i+1] == 2:
            count += 1
    temp[i] = count
    count = 0
    
print(answer)
print(temp)
        
