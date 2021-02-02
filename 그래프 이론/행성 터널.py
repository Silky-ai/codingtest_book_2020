import sys


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




n=int(input())

edges=[]
X=[]
Y=[]
Z=[]
root=[0]*(n)
for i in range(n):
    root[i]=i

for i in range(n):
    temp=list(map(int,sys.stdin.readline().strip().split()))
    X.append((temp[0],i))
    Y.append((temp[1],i))
    Z.append((temp[2],i))
X.sort()
Y.sort()
Z.sort()

for i in range(n-1):
    x=X[i+1][0]-X[i][0]
    y=Y[i+1][0]-Y[i][0]
    z=Z[i+1][0]-Z[i][0]
    edges.append((x,X[i][1],X[i+1][1]))
    edges.append((y,Y[i][1],Y[i+1][1]))
    edges.append((z,Z[i][1],Z[i+1][1]))

ans=0
edges.sort()
for e in edges:
    c,a,b=e
    if(find_root(root,a)!=find_root(root,b)):
        ans+=c
        union(root,a,b)


print(ans)
