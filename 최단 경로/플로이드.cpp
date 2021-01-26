#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n,m;
  cin>>n;
  cin>>m;
  int INF=1e8;

  int graph[n+1][n+1];
  for(int i=0;i<n+1;i++)
    for(int j=0;j<n+1;j++){
      if(i==j)
      graph[i][j]=0;
      else
      graph[i][j]=INF;}
  

  int arr[3];
  for(int i=0;i<m;i++){
    cin>>arr[0]>>arr[1]>>arr[2];
    if(arr[2]<graph[arr[0]][arr[1]])
    graph[arr[0]][arr[1]]=arr[2];
  } 

  for(int k=1;k<n+1;k++){
  for(int a=1;a<n+1;a++){
  for(int b=1;b<n+1;b++){
  graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]);}}}

  for(int i=1;i<n+1;i++){
    for(int j=1;j<n+1;j++){
    if(graph[i][j]==INF){
    cout<<0<<" ";
    }
    else{
    cout<<graph[i][j]<<" ";}
    }
    cout<<endl;
  }
  return 0;
}
