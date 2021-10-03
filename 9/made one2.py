'''
page 217 1로만들기 문제

임의의 숫자 X를 받아 그수를 1로 만들때 최소 횟수를 출력하는 문제
1빼기 , 2,3,5로 나누기

느낀점
스터디 들어와서 첫번째 문제로 받아서 푼 문제인데 다시 풀어보면서
확실히 이해한 느낌이 들었습니다.
'''
import math

def madeonedigit():
    x = int(input())
    result= [0,1,1,1,2,1]
    
    for i in range(6,x+1):
        case = result[i-1]
        case1,case2,case3 = math.inf,math.inf,math.inf
        
        if i % 2 == 0:
            case1 = result[i//2]
        if i % 3 == 0:
            case2 = result[i//3]
        if i % 5 == 0:
            case3 = result[i//5]
            
        compare = 1+min(case,case1,case2,case3)
        
        result.append(compare)
    
    print(result[x])

madeonedigit()

# ----------------------------------------------------------------
# 백준 1로 만들기

x = int(input())
dp= [0,1,1,1]+(pow(10,6)-3)*[0]
for i in range(4,x+1):
    dp[i]= dp[i-1]+1     
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)    
print(dp[x])