import heapq

INF=int(1e9)
n,m,c=list(map(int,input().split()))

graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  temp=tuple(map(int,input().split()))
  graph[temp[0]][temp[1]]=temp[2]

def dijkstra(start):
  q=[]
  
  distance=[INF]*(n+1)
  heapq.heappush(q,(0,start))
  
  while(q!=[]):
    current=heapq.heappop(q)

    if(current[0]>distance[current[1]]):
      continue
    
    distance[current[1]]=current[0]
    for i in range(1,n+1):
      cost=distance[current[1]]+graph[current[1]][i]
      if(cost<distance[i]):
        
        distance[i]=cost
        heapq.heappush(q,(distance[i],i))
    
  return distance

distance=dijkstra(c)
print(distance)
max=-1
cnt=0
for i in distance[1:]:
    if(i!=INF):
      cnt+=1
      if(i>max):
        max=i
print(cnt-1,max) #시작노드도 잡히기 때문에 -1을 해주어야함



