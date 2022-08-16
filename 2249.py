k,a=map(int,input().split())
i=0
while True:
    s=k**i
    s=str(s)
    l=len(str(a))
    if str(a)==s[0:l]:
        print(i)
        break
    i+=1

    if i>=3000000:
        print(-1)
        break
