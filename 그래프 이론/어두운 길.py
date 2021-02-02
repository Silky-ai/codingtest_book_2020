def find_root(root,x):
    if(root[x]!=x):
        root[x]=find_root(root,root[x])
    return root[x]

def union(root,a,b):
    a=find_root(root,a)
    b=find_root(root,b)
    if(a<b):
        root[b]=a
    else:
        root[a]=b



n,m=list(map(int,input().split()))

edges=[]

root=[0]*(n)
for i in range(n):
    root[i]=i

total_cost=0
for i in range(m):
    temp=list(map(int,input().split()))
    edges.append((temp[2],temp[0],temp[1]))
    total_cost+=temp[2]

edges.sort()

min_cost=0
for edge in edges:
    c,a,b=edge
    if(find_root(root,a)!=find_root(root,b)):
        min_cost+=c
        union(root,a,b)
print(total_cost-min_cost)