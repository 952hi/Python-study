'''
https://www.acmicpc.net/problem/1010
다리놓기

좌측 다리 건설 포인트 수와 우측 다리 건설 포인트 수를 입력받아
건설가능한 경우의 수를 출력하시오

입력예시
3
2 2
1 5
13 29

출력예시
1
5
67863915

느낀점
첫번째 시도에서 순열함수를 사용하지않고 팩토리얼을 따로 생성해서 사용했는데
순열을 사용했을때와 차이가 없을까 하고 시도해보니 조합함수를 사용하면 시간이 많이걸려 문제를 틀리게됩니다.

'''
import itertools
import sys
input = sys.stdin.readline
# from itertools import combinations

def factorial(n):
    if n<=0:
        return 1;
    else:
        return n*factorial(n-1);

result =0
for i in range(int(input())):
    left,right = map(int,input().split())
    # 조합 함수 사용시 시간초과
    # print(len(list(itertools.combinations(range(1,right+1),left))))
    result = int(factorial(right)/(factorial(right-left)*factorial(left)))
    print(result)

