r,g,b=(input().split())
r=int(r)
g=int(g)
b=int(b)
s=0
for i in range(0,r):
    for j in range(0,g):
        for k in range(0,b):
            print(i, j ,k)
            s+=1
print(s)
