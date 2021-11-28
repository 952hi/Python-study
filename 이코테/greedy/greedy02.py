# 실전문제 3-2
# 큰 수의 법칙
# n개의 숫자가 주어졌을때 
# 같은인덱스의 수를 연속 K번까지 사용할수있을때
# m번 더하기를 수행했을때 최댓값을 출력하는 문제
# 입력예시
# 5 8 3
# 2 4 5 4 6
 
n,m,k = map(int,input().split())

temp = list(map(int,input().split()))

temp.sort()
check = 0
hap = 0

for i in range(m):
    if check == k:
        hap += temp[-2]
        check = 0
    else:
        hap += temp[-1]
        check += 1

print(hap)
        
