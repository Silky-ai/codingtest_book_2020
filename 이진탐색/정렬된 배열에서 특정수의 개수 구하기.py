n,x=map(int,input().split())

arr=list(map(int,input().split()))

cnt=0

start=0
end=n-1
def count_num(inx):
  cnt=0
  while(arr[inx]==x and inx>0):
    inx-=1
  if(inx!=0):
    inx+=1
  while(arr[inx]==x):
    cnt+=1
    inx+=1
  return cnt

while(start<=end):
  mid=(start+end)//2
  if(arr[mid]>x):
    end=mid-1
  elif(arr[mid]<x):
    start=mid+1
  else:
    cnt=count_num(mid)
    break

if(cnt==0):
  cnt=-1

print(cnt)    