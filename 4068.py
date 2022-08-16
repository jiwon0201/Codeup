n=int(input(""))
k=2
i=2
t=1
check=0
z=[]
while t<=n:
    while k<i:
        if i%k==0:
            check+=1
            break
        k+=1
    if check==0:
        t+=1
        z.append(i)
    check=0
    k=2
    i+=1

print(z[n-1])
