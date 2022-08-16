n=int(input())
a=[[0]*103 for i in range(103)]
for i in range(n):
    x,y=map(int,input().split())
    for j in range(x,x+11):
        for k in range(y,y+11):
            a[j][k]=1

cnt=0
for i in range(102):
    for j in range(102):
        z=a[i][j-1]+a[i][j+1]+a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
        if a[i][j]==1 and z!=8:
            cnt+=1
print(cnt)
