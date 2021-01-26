n=int(input())
arr=list(map(int,input().split()))


end=n-1
start=0

while(start<=end):
  mid=(start+end)//2
  if(arr[mid]==mid):
    break
  elif(arr[mid]>mid):
    end=mid-1
  else:
    start=mid+1
  
if(arr[mid]==mid):
  print(arr[mid])
else:
  print(-1)