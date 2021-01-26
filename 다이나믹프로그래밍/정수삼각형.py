
n=int(input())
arr=[]
for i in range(n):
  temp=list(map(int,input().split()))
  arr.append(temp)
 
ans=[]
ans.append([arr[0][0]])
for i in range(1,n):
  save=[]
  for j in range(i+1):
    if(j==0):
      temp=ans[i-1][j]+arr[i][j]
    elif(j==i):
      temp=ans[i-1][j-1]+arr[i][j]
    else:
      temp=max(ans[i-1][j-1]+arr[i][j],ans[i-1][j]+arr[i][j])
    save.append(temp)
  ans.append(save)

print(max(ans[n-1]))
print(ans)

