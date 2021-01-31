

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


n,m=map(int,input().split())
root=[0]*(n+1)
for i in range(1,n+1):
    root[i]=i
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in range(0,n):
        if(temp[j]==1):
            union(root,i,j+1)
travel=list(map(int,input().split()))
ans=True
flag=find_root(root,travel[0])
for t in travel:
    if(find_root(root,t)!=flag):
        ans=False
if(ans==True):
    print("YES")
else:
    print("NO")

print(root)
