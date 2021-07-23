adress,net = map(int,input().split())

home = []


for i in range(adress):
    home.append(int(input()))

home.sort()

fisrt_range = 1
max_range = home[-1] - home[0]
result = 0

while(fisrt_range <= max_range):
    mid_range = (fisrt_range + max_range)//2
    value = home[0]
    count = 1 

    for i in range(1,adress):
        if home[i] >= value + mid_range :
            value = home[i]
            count += 1
    if count >= net :
        fisrt_range = mid_range + 1
        result = mid_range
    else:
        max_range = mid_range - 1

print(result)   
