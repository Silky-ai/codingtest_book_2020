N,M=list(map(int,input().split()))
mon=list(map(int,input().split()))
arr=[[0]*(M+1)for _ in range(N)]

for i in range(1,M+1):
  if(mon[0]>i):
    arr[0][i]=0
  if(i%mon[0]==0):
    arr[0][i]=i//mon[0]
for i in range(1,N):
  for j in range(1,M+1):
    if(mon[i]>j):
      arr[i][j]=arr[i-1][j]
    else:
      ch1=arr[i][j-mon[i]]+1
      if(ch1==1): # 현재 화폐를 통해 못만듦
        arr[i][j]=arr[i-1][j]
      if(j==mon[i]):
        arr[i][j]=1
      elif(arr[i-1][j]!=0): # 과거에도 만들기 가능
        arr[i][j]=min(arr[i-1][j],ch1)
      elif(arr[i-1][j]==0): #과거에도 못만듦
        if(ch1!=1): #현재 화폐로는 만들기 가능
          arr[i][j]=ch1
        else: #현재도 불가능
          arr[i][j]=0
print(arr)

if(arr[N-1][M]==0):
  print(-1)
else:
  print(arr[N-1][M])