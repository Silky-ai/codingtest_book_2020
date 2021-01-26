n,c=map(int,input().split())
arr=[]
points=[]
for _ in range(n):
  arr.append(int(input()))

arr.sort()
start=1
end=arr[-1]-arr[0]
ans_gap=-1
while(start<=end):
  mid=(start+end)//2 #gap
  val=arr[0]
  count=1
  for i in range(1,n):
    if(arr[i]-val>=mid):
      count+=1
      val=arr[i]
  
  if(count>=c):
    ans_gap=mid
    start=mid+1

  else:
    end=mid-1

print(ans_gap)