'''
병사배치하기 https://www.acmicpc.net/problem/18353
교재 380 page

병사의 수와 병사의 전투력 리스트를 입력 받아
전투력을 내림차순 했을때 최대길이가 되도록 제외해야하는 병사의 수를 구하기

ex)
7
15 11 4 8 5 2 4 -> 3번째 4  6번째 2 제외 시키면 5의 최대길이 가능

뒤집어서 생각하면 

4 2 5 8 4 11 15
1 1 2 3 2 4  5

#느낀점
내림차순으로 할때보다 뒤집어서 오름차순으로 할때 생각하기가 편했다
 
'''
n = int(input())
batch = list(map(int, input().split()))
dp = [1]*n
batch.reverse()

for i in range(1,n):
    for j in range(0,i):
        if batch[i]> batch[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))