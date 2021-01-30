
n=int(input())
graph=[[] for _ in range(n+1)]
inline=[0]*(n+1)
cost=[0]*(n+1)
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    cost[i]=temp[0]
    if(len(temp)>2):
        for k in range(1,len(temp)-1):
            graph[temp[k]].append(i)
            inline[i]+=1
def sort():
    ans=[0]*(n+1)
    q=[]
    for i in range(1,n+1):
        if(inline[i]==0):
            q.append(i)
    while q!=[]:
        
        x=q.pop(0)
        ans[x]+=cost[x]
        n_list=graph[x]
        
        for nd in n_list:
            ans[nd]+=ans[x]
            inline[nd]-=1
            if(inline[nd]==0):
                q.append(nd)
       
    return ans
ans=sort()
print(ans)
