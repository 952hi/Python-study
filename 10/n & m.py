'''
https://www.acmicpc.net/problem/15651
N과 M (3)
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

입력예시
n 4 m 2

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

느낀점
재귀문제를 만날때마다 쉬운난이도지만 어렵게 느껴지는거같다
날 잡고 연습해야 할 것 같다 

'''
n,m=map(int,input().split())

# 입력받을 리스트
result=[0 for _ in range(m)]


def backtracking(index,n,m):
    # 인덱스와 m이 같으면
    if index==m:
        for i in result:
            print(i,end=" ")
        print()
        return
    
    # 1부터 n까지 반복해서 수행
    for i in range(1,n+1):
        
        result[index]=i
        
        # result 통에 m개씩 넣기위해 index를 늘려줌
        backtracking(index+1,n,m)

      
backtracking(0,n,m)