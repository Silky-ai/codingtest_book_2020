N=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
food=[0 for i in range(N+1)]
food[1]=arr[1]
for i in range(2,N+1):
  MAX=food[i-1]
  food[i]=max(MAX,food[i-2]+arr[i])

print(food)
print(food[-1])