N=int(input())
dp=[0 for i in range(N+1)]

dp[1]=1
if(N>1):
  dp[2]=3

for i in range(3,N+1):
  a=dp[i-1]
  b=0
  if(i-2>=1):
    b=dp[i-2]*2
  dp[i]=a+b

print(dp)
print(dp[-1]%796796)