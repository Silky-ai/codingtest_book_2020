#include<iostream>
#include <functional>
#include <queue>
using namespace std;

class node{
    private:
        int m;
        int n;
        int cost;
        friend bool operator<(const node& node1,const node &node2);
        friend bool operator>( const node &node1, const node& node2);
    public:
        node(int _m,int _n,int _c):m(_m),n(_n),cost(_c){
    
        }
        int get_m(){
            return m;
        }
        int get_n(){
            return n;
        }
        int get_cost(){

            return cost;
        }
        
};
int INF=1e9;
bool operator<( const node &node1,const node &node2){
            return node1.cost<node2.cost;
        }
bool operator>( const node &node1, const node& node2){
            return node1.cost>node2.cost; 
        }
int main(){

    int t,n;
    int mov_x[4]={0,0,-1,1};
    int mov_y[4]={1,-1,0,0};
    cin>>t;
    int ans[t];
    for(int i=0;i<t;i++){
        cin>>n;
        int mat[n][n];
        priority_queue<node, vector<node>, greater<vector<node>::value_type>> pq;
        int temp[n];
        int dist[n][n];
        for(int j=0;j<n;j++)
        for(int k=0;k<n;k++)
        dist[j][k]=INF;

        for(int m=0;m<n;m++){
        for(int j=0;j<n;j++)
            cin>>temp[j];
        
        for(int l=0;l<n;l++){
            mat[m][l]=temp[l];
        }        
        }
     
        pq.push(node(0,0,mat[0][0]));
        node current(0,0,0);
        while(!pq.empty()){
            current=pq.top();
            int current_cost=current.get_cost();
            int current_x=current.get_m();
            int current_y=current.get_n();
            if(current_cost>dist[current_x][current_y])
            continue;

            dist[current_x][current_y]=current_cost;
            for(int s=0;s<4;s++){
                if((current_x+mov_x[s])>=0 &&(current_y+mov_y[s]>=0)&&(current_x+mov_x[s]<n)&&(current_y+mov_y[s]<n)){
            
                    pq.push(node(current_x+mov_x[s],current_y+mov_y[s],current.get_cost()+mat[current_x+mov_x[s]][current_y+mov_y[s]]));
                }
            }
        
        }
        ans[i]=dist[n-1][n-1];
       
    }
    for(int i=0;i<t;i++)
    cout<<ans[i]<<endl;

    return 0;
}