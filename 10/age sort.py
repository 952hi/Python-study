import sys

n = int(input())
name = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    name.append((int(a),b))

name.sort(key= lambda a : a[0])

for i in range(n):
    print(name[i][0],name[i][1])