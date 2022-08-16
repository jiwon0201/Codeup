n=int(input())
import sys
s=input().split()
max=0
l=0
for i in range(n):
    s[i]=int(s[i])
    l+=s[i]
    if s[i]>max:
        max=s[i]
m=int(input())
new=m
k=m//n
t=0
for i in range(n):
    if s[i]<=k:
        m-=s[i]
        t+=1

if l<=new:
    print(max)
elif t==0:
    print(new//n)
else:
    print(m//t)
