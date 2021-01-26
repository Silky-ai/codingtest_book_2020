n,m=list(map(int,input().split()))
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  graph[i][i]=0

for _ in range(m):
  temp=tuple(map(int,input().split()))
  graph[temp[0]][temp[1]]=1
  graph[temp[1]][temp[0]]=1

x,k=list(map(int,(input().split())))

def get_min_idx(distance,visited):
  minn=INF
  idx=0
  for i in range(1,n+1):
    if(distance[i]<minn and not visited[i]):
      minn=distance[i]
      idx=i
  return idx
def dijkstra(start,end):
  visited=[False]*(n+1)
  distance=[INF]*(n+1)
  distance[start]=0
  for i in range(1,n+1):
    
    new=get_min_idx(distance,visited)
    visited[new]=True
    for j in range(1,n+1):
      cost=distance[new]+graph[new][j]
      if(cost<distance[j]):
        distance[j]=cost
    
  return distance[end]

one_to_k=dijkstra(1,k)
k_to_x=dijkstra(k,x)
print(one_to_k,k_to_x)
print(one_to_k+k_to_x)
