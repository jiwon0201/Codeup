n = int(input())    
a = input().split()

for i in range(0,n) :
  a[i]=int(a[i])

for j in range(0,n):
    print(a[n-j-1], end=' ')
