
def check(tteok,H):
  summ=0
  for i in tteok:
    if(i>=H):
      summ+=(i-H)
  return summ
N,M=map(int,input().split())

tteok=list(map(int,input().split()))

LIMIT=max(tteok)

end=LIMIT
start=0
mid=(start+end)//2

while(start<=end):
  mid=(start+end)//2
  c=check(tteok,mid)
  if(c<M):
    if(start==end):
      mid=lm
      break
    end=mid-1
  elif(c>M):
    start=mid+1
    lm=mid
  elif(c==M):
    break
  


print(mid)
