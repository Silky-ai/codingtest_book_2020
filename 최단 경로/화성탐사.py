import heapq

t=int(input())
INF=int(1e9)
ans=[]
mov_x=[0,0,-1,1]
mov_y=[1,-1,0,0]
for _ in range(t):
    mat=[]
    n=int(input())
    dist=[[INF]*n for _ in range(n)]
    for i in range(n):
        temp=list(map(int,input().split()))
        mat.append(temp)
    pq=[]
    heapq.heappush(pq,[0,0,mat[0][0]])
    while(pq!=[]):
        current=heapq.heappop(pq)
        cost=current[2]
        x=current[0]
        y=current[1]
        if(cost>dist[x][y]):
            continue
        dist[x][y]=cost
        for j in range(4):
          x_n=x+mov_x[j]
          y_n=y+mov_y[j]
          if(0<=x_n<n and 0<=y_n<n):
              heapq.heappush(pq,[x_n,y_n,dist[x][y]+mat[x_n][y_n]])
        
    ans.append(dist[n-1][n-1])
print(ans)