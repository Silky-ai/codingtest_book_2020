import heapq

n,m=list(map(int,input().split()))

INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    temp=list(map(int,input().split()))
    graph[temp[0]][temp[1]]=1
    graph[temp[1]][temp[0]]=1

distance=[INF]*(n+1)
q=[]
start=1
heapq.heappush(q,(0,start))
while (q!=[]):
    dist,current=heapq.heappop(q)
    if(dist>distance[current]):
        continue
    for i in range(1,n+1):
        cost=dist+graph[current][i]
        if(cost<distance[i]):
            distance[i]=cost
            heapq.heappush(q,(cost,i))

ans=[]

maxx=max(distance[1:])
for i in range(1,n+1):
    if(distance[i]==maxx):
        ans.append(i)
ans.sort()
print(ans[0])
print(maxx)
print(len(ans))
