

t=int(input())
ans=[]
def ranking():
    n=int(input())
    graph=[[]for _ in range(n+1)]
    inline=[0]*(n+1)
    last_rank=list(map(int,input().split()))
    m=int(input())
    for i in range(len(last_rank)-1):
        for j in range(i+1,len(last_rank)):
            graph[last_rank[i]].append(last_rank[j])
            inline[last_rank[j]]+=1
    
    for i in range(m):
        a,b=list(map(int,input().split()))
        if(b in graph[a]):
            graph[a].remove(b)
            graph[b].append(a)
            inline[b]-=1
            inline[a]+=1
        elif( a in graph[b]):
            graph[b].remove(a)
            graph[a].append(b)
            inline[a]-=1
            inline[b]+=1
    q=[]
    for i in last_rank:
        if(inline[i]==0):
            q.append(i)
    
    cycle=False
    certain=True
    result=[]
    while q!=[]:
        if(len(q)>=2):
            certain=False
        current=q.pop(0)
        result.append(current)
        for n in graph[current]:
            inline[n]-=1
            if(inline[n]==0):
                q.append(n)
    if(len(result)!=len(last_rank)):
        cycle=True
    
    if(cycle==True):
        ans.append(-1)
    elif(certain==False):
        ans.append(0)
    else:
        ans.append(result)
    
for _ in range(t):
    ranking()
for i in ans:
    if(i==-1):
        print("IMPOSSIBLE")
    elif(i==0):
        print("?")
    else:
        for k in i:
            print(k,end=" ")
        print()