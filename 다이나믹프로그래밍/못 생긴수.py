n=int(input())

arr=[0]*n
arr[0]=1

idx1=idx3=idx5=0
num1,num3,num5=2,3,5

for idx in range(1,n):
  temp=min(num1,num3,num5)
  arr[idx]=temp
  if(temp==num1):
    idx1+=1
    num1=arr[idx1]*2
  if(temp==num3):
    idx3+=1
    num3=arr[idx3]*3
  if(temp==num5):
    idx5+=1
    num5=arr[idx5]*5


print(arr)