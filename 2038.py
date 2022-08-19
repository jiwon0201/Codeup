hpx=list(map(int,input().split()))
hp=sum(hpx)
kal=int(input())
po=input()
k=2
if po[0]=='1':
    po=list(po.split())
    l=len(po)
    if l==4:
        if po[1]=='*':
            k=1
        else:
            k=0
        t1=int(po[2])
        t2=int(po[3])
    elif l==3:
        if po[1][0]=='*':
            k=1
        else:
            k=0
        t1=int(po[1][1:])
        t2=int(po[2])

x,y=map(int,input().split())

while hp>0 and y>0:
    if k==1 and t2>0:
        y=y-(t1*kal)
    elif k==0 and t2>0:
        y=y-(t1+kal)
    else:
        y-=kal
    
    hp-=x

if hp>0 and y<=0:
    print(1)
elif y>0 and hp<=0:
    print(0)
elif y<=0 and hp<=0:
    print(1)
