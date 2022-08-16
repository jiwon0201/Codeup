import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
c=int(sys.stdin.readline())
d=list(map(int,sys.stdin.readline().split()))
for i in d:
  if i in b:
    k=b.index(i)+1
    print(k,end=" ")
  else:
    print("-1",end=" ")
