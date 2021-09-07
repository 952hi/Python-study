n = int(input())
a= []
result = 0
  
for _ in range(n):
    a.append(list(map(int, input().split())))
      
    for i in range(10):
        if a[i] % 2 == 1:
            result = result + a[i]

    print(result)