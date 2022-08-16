x,y=map(int,input().split())
z=0
for i in range(x,y+1):
    k=str(i)
    l=len(k)
    t=[0 for i in range(10)]
    r=0
    for j in range(l):
        t[int(k[j])]+=1
    for j in range(10):
        if t[j]==l-1:
            z+=1
print(z)
