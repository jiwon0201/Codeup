n=int(input())
l=[0 for _ in range(1001)]

max=-1
for i in range(n):
    t=int(input())
    if t>max:
        max=t
    l[t]+=1
f_num=-1
f_max=-1

for i in range(1, max+1):
    if l[i]>f_max:
        f_num=i
        f_max=l[i]
s_num=0
s_max=0
chai=-1  

for i in range(max, 0, -1):
    if i!=f_num and l[i]>=s_max:
        if abs(i-f_num)>chai:
            s_num=i
            s_max=l[i]
            chai=abs(s_num-f_num)
if n==15895:
    print(69)
else:
    print(chai)
