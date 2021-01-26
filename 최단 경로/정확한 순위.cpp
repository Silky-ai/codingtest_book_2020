#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int n,m;
  cin>>n>>m;
  
  int INF=1e9;
  int graph[n+1][n+1];
  for(int i=1;i<n+1;i++){
  for(int j=1;j<n+1;j++){
    if(i==j)
    graph[i][j]=0;
    else
    graph[i][j]=INF;
  }}
  int a,b;
  for(int i=0;i<m;i++){
    cin>>a>>b;
    graph[a][b]=1;
    
  }

  for(int k=1;k<n+1;k++)
  for(int a=1;a<n+1;a++)
  for(int b=1;b<n+1;b++)
  graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]);

  int higher[n+1];
  int lower[n+1];
  for(int a=1;a<n+1;a++){
    int cnt=0;
    for(int b=1;b<n+1;b++){
      if(graph[a][b]!=INF && a!=b)
      cnt++;
    }
    higher[a]=cnt;
  }
  for(int a=1;a<n+1;a++){
    int cnt=0;
    for(int b=1;b<n+1;b++){
      if(graph[b][a]!=INF && a!=b)
      cnt++;
    }
    lower[a]=cnt;
  }

  int ans=0;
  for(int i=1;i<n+1;i++){
    if(higher[i]+lower[i]==n-1)
    ans++;
  }
  cout<<ans<<endl;
  return 0;
}