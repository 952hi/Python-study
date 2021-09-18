x = int(input())
dp= [0,1,1,1]+(pow(10,6)-3)*[0]
for i in range(4,x+1):
    dp[i]= dp[i-1]+1     
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)    
print(dp[x])