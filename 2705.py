n=int(input())

l,T=map(int,input().split())
s=input().split()
for i in range(l):
    s.append(0)
d=0
c=0
t=0
r=0
for i in range(n):
    s[i]=int(s[i])
    
for i in range(n):
    if s[i]<d:
        continue
    else:
        r+=1
        t=s[i]
        for j in range(l):
            if s[i+j]==t:
                c+=1
        if c==l:
            d=T+t
        t=0

print(r*10000)
