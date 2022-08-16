a,b=map(int,input().split())
from math import *
d1=[]
d2=[]
l=0
for i in range(a,b-1):
    k1=i
    k2=i+2
    x=0
    y=0
    for j in range(2,int(sqrt(k1))+1):
        if k1%j==0:
            x+=1
    for j in range(2,int(sqrt(k2))+1):
        if k2%j==0:
            y+=1
    if x==0 and y==0:
        d1.append(k1)
        d2.append(k2)
        l+=1
for i in range(l):
    print(d1[i], d2[i])
