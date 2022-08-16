n=int(input())
s=input().split()

for i in range(n):
    s[i]=int(s[i])
m,k=map(int,input().split())

t=0
for i in range(m+k):
    x,a,b=map(int,input().split())
    if x==0:
        s[a-1]=b
    else:
        for j in range(a-1,b):
            t+=int(s[j])
        print(t)
        t=0
