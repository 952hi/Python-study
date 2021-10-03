'''
a = input().split('-')
num = []
for i in a:
    ## 작성 부분 ##
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
    print(n)
    
55-50+40
'''

a = input().split('-')
num = []
for i in a:
    ## 작성 부분 ##
    hap = 0
    b = i.split('+')
    for j in b:
        hap = int(j) + hap
    num.append(hap)
    
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
    print(n)
