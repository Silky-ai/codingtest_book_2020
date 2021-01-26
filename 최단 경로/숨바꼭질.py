n,m=list(map(int,input().split()))

INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    temp=list(map(int,input().split()))
    graph[temp[0]][temp[1]]=1
    graph[temp[1]][temp[0]]=1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
ans=[]
maxx=max(graph[1][1:])
for i in range(1,n+1):
    if(graph[1][i]==maxx):
        ans.append(i)
ans.sort()
print(ans[0])
print(graph[1][ans[0]])
print(len(ans))
