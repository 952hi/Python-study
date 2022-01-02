'''
page382 편집거리

입력받은 N 문자열을 -> 입력받은 M 문자열로 바꿀때 최소행동 수를 출력하는 문제

삽입 삭제 교체 사용가능

입력예시
saturday
sunday

출력예시
3

느낀점
LIS나 LCS 알고리즘일거라고 생각하고 접근해서 힘들었다
구글링해서 찾아보니 LD라는 알고리즘으로 해결할수있었다.

'''
str1 = "sunday"
str2 = "saturday"

n = len(str1)
m = len(str2)

dp = [[0] * (1+m) for _ in range(1+n)]

for i in range(1, n+1):
  dp[i][0] = i
  
for j in range(1, m+1):
  dp[0][j] = j
  
for i in range(1, n+1):
  for j in range(1, m+1):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
 
print(dp[n][m])