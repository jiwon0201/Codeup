d=[]
for i in range(11):
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(10):
    a=input().split()
    for j in range(10):
        d[i][j]=int(a[j])
    
m1=1
m2=1
while True:
    d[m1][m2]=9
    if d[m1][m2+1]==1 and d[m1+1][m2]==1:
        d[m1][m2]=9
        break
    elif d[m1][m2+1]==2:
        d[m1][m2+1]=9
        m2+=1
        break
    elif d[m1+1][m2]==2 and d[m1][m2+1]==1:
        m1+=1
        d[m1][m2]=9
        break
    elif d[m1][m2+1]==0:
        m2+=1
        d[m1][m2]=9
    elif d[m1][m2+1]==1 and d[m1+1][m2]==0:
        m1+=1
        d[m1][m2]=1

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()