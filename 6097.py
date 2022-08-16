d=[[0 for j in range(1,102)]for i in range(1,102)]

h,w=map(int,input().split())
n=int(input())

for i in range(n):
    l,d1,x,y=map(int,(input().split()))
    for j in range(l):
        if d1==0:
            d[x][y+j]=1
        else:
            d[x+j][y]=1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(d[i][j],end=' ')
    print()