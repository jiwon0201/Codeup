s,n=map(int,input().split())
a=[0 for i in range(n)]
l=0
for i in range(n):
    z=input()
    if z=='Ballad':
        a[i]=1
    if i+1<=n:
        l+=a[i]
max=0

for i in range(n-s):
    if max<l:
        max=l
        k=i
    l=l-a[i]+a[i+s]

if max<l:
    max=l
    k=n-s

print(k+1)
