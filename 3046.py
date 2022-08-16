n=int(input())
k=list(map(int,input().split()))
s,t=map(int,input().split())
s,t=min(s,t)-1,max(s,t)-1
l=sum(k)
l1=0

for i in range(s,t):
    l1+=k[i]

print(min(l1,l-l1))
