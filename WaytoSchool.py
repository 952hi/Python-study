'''
등굣길 https://programmers.co.kr/learn/courses/30/lessons/42898
계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 
집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

느낀점
ncs 수리문제에서 매번 보는 문제라 익숙해서 편하게 코딩할 수 있었습니다.
두가지 방법으로 풀 수 있을거 같은데 다른 방법도 해보면 좋을것 같습니다.

'''
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0] *(m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1: continue
            if [i,j] in puddles:
                dp[i][j] == 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]%1000000007

print(solution(4, 3, [[2,2]]))     