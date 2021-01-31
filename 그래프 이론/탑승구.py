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


g=int(input())
p=int(input())
root=[0]*(g+1)
for i in range(1,g+1):
    root[i]=i
cnt=0
for i in range(p):
    k=int(input())
    if(find_root(root,k)!=0):
        union(root,k,k-1)
        cnt+=1
    else:
        continue
print(cnt)
