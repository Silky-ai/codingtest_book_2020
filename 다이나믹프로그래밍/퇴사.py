n=int(input())
arr=[]
for i in range(1,n+1):
  t,p=list(map(int,input().split()))
  if(i+t-1>n):
    continue
  temp=[i,i+t-1,p]
  arr.append(temp)

def quit():
  dp=[0]*(len(arr))
  for i in range(len(arr)):
    dp[i]=arr[i][2]


  for i in range(1,len(arr)):
    for j in range(0,i):
      if(arr[j][1]<arr[i][0]):
        dp[i]=max(dp[i],dp[j]+arr[i][2])  
  print(max(dp))
if(arr==[]):
  print(0)
else:
  quit()
