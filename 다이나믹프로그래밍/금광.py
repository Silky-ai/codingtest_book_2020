T=int(input())
tests=[]
for _ in range(T):
  m,n=list(map(int,input().split()))
  temp=list(map(int,input().split()))
  real=[]
  for i in range(1,m+1):
    row=temp[(i-1)*n:(i)*n]
    real.append(row)
  tests.append(real)
def gold_mining(mat):
  m=len(mat)
  n=len(mat[0])
  ans=[[0]*n for _ in range(m)]
  for i in range(m):
    ans[i][0]=mat[i][0]
  for j in range(1,n):
    for i in range(m):
      if(i==0):
        ans[i][j]=max(ans[i][j-1]+mat[i][j],ans[i+1][j-1]+mat[i][j])
      elif(i==(m-1)):
        ans[i][j]=max(ans[i][j-1]+mat[i][j],ans[i-1][j-1]+mat[i][j])
      else:
        ans[i][j]=max(ans[i][j-1]+mat[i][j],ans[i-1][j-1]+mat[i][j],ans[i+1][j-1]+mat[i][j])
  maxx=0
  for i in range(m):
    if(maxx<ans[i][n-1]):
      maxx=ans[i][n-1]
  print(maxx)
  print(ans)


for mat in tests:
  gold_mining(mat)