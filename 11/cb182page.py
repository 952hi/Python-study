a,b = map(int, input().split())
comp1 = list(map(int, input().split()))
comp2 = list(map(int, input().split()))
temp = 0

comp1.sort()
comp2.sort()
comp2.reverse()


for i in range(b):
    if comp1[i] < comp2[i]:
        comp1[i] = comp2[i]

for i in range(a):
    temp += comp1[i]

print(temp)