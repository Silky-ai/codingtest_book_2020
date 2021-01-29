import sys
input = sys.stdin.readline
def find_parent(parent,x):
    if(parent[x]!=x):
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

edges=[]
n,m=map(int,input().split())
for _ in range(m):
    a,b,c=list(map(int,input().strip().split()))
    edges.append((c,a,b))
parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i
edges.sort()
result=0
last=0
for e in edges:
    if(find_parent(parent,e[1])!=find_parent(parent,e[2])):
        union(parent,e[1],e[2])
        result+=e[0]
        last=e[0]
           
print(result-last)
