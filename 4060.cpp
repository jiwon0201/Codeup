#include<stdio.h>
 
int a[101][101],i,j,cnt,cnt1,p;
 
void dfs(int y,int x,int co)
{
    if(a[y][x]==co)
    {
        p++;
        a[y][x]=-1;
        dfs(y-1,x,co);
        dfs(y,x-1,co);
        dfs(y,x+1,co);
        dfs(y+1,x,co);
    }
}
  
int main()
{
    int n,m;
    scanf("%d %d", &n, &m);
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
            scanf("%d",&a[i][j]);
 
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
            if(a[i][j]==1)
            {
                p=0;
                dfs(i,j,a[i][j]);
                if(p>=3)cnt++;
            }
            else{
                p=0;
                dfs(i,j,a[i][j]);
                if(p>=3)cnt1++;
            }
    printf("%d %d",cnt,cnt1);
}
