n,k=map(int,input().split())
b=[]
l=1
for i in range(1,n+1):
    b.append(i)

for i in range((n-1)//2):
    b.remove(b[l-1])
    l=(l+k)%6
    b.remove(b[l-2])
    l=(l+k)%6

if n%2==0:
    b.remove(b[l-1])
print(b[0])
