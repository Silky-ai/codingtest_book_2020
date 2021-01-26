#플로이드 워셜 방식으로 문제해결

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


for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


ans=graph[1][k]+graph[k][x]

if(ans>=INF):
  print(-1)
else:
  print(ans)