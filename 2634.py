n=int(input())
k=int(input())
s=input().split()

for i in range(k):
    s[i]=int(s[i])

l=0
for i in range(k):
    if n==0:
        break
    else:
        l+=n//s[k-i-1]
        n-=(n//s[k-i-1])*s[k-i-1]

print(l)
