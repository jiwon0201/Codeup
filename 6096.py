d=[[0 for j in range(20)]for i in range(20)]

for i in range(19):
    d[i]=input().split()

n=int(input())

for i in range(n):
    x,y=map(int,input().split())
    for j in range(19):
        if int(d[j][y-1])==0:
            d[j][y-1]=1
        else:
            d[j][y-1]=0
        
        if int(d[x-1][j])==0:
            d[x-1][j]=1
        else:
            d[x-1][j]=0

for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
    print()