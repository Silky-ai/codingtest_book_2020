
def binary_search(arr,target):
  end=len(arr)-1
  start=0
  while(start<=end):
    mid=(start+end)//2
    if(arr[mid]==target):
      return True
    elif(arr[mid]>target):
      end=mid-1
    else:
      start=mid+1
  return False
N=int(input())
shop=list(map(int,input().split()))

M=int(input())
want=list(map(int,input().split()))

shop.sort()
for i in want:
  if(binary_search(shop,i)):
    print('yes')
  else:
    print('no')