X=int(input())
dp=[0 for i in range(X+1)]

for i in range(2,X+1):
  minn=dp[i]=dp[i-1]+1
  
  if(i%5==0):
    minn=min(minn,dp[i//5]+1)
  if(i%3==0):
    minn=min(minn,dp[i//3]+1)
  if(i%2==0):
    minn=min(minn,dp[i//2]+1)
  dp[i]=minn
    

print(dp[X])
print(dp)