n = int(input())
l=map(int, input().strip().split())

s=[0]*100001

for i in l:
    s[i]+=1

for i in range(len(s)):
    while s[i]>0:
        print(str(i), end=" ")
        s[i]-=1
