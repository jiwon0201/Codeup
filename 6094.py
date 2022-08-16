n = int(input())    
a = input().split()

for i in range(0,n) :
  a[i]=int(a[i])
k=a[0]

for j in range(0,n):
    if (k>a[j]):
        k=a[j]

print(k)
