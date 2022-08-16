t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    l=(n-k)/2
    if n==0:
        print(k)
        continue
    if l==int(l):
        print(0)
    else:
        print(abs(int(2*l)))
