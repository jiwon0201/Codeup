n=int(input())
a=[]
id=[]
for i in range(n):
    c,no,name=input().strip().split()
    k=0
    if c=="I":
        if int(no) not in id:
            id.append(int(no))
            a.append([int(no),name])
        elif int(no) in id:
            for j in range(len(a)):
                if id[j]==int(no):
                    id.insert(j,int(no))
                    a.insert(j,[int(no),name])
    elif c=="D":
        if int(no) in id:
            id.remove(int(no))
            for j in range(len(a)):
                if a[j][0]==int(no) and (k==0 or a[j][1]==y):
                    y=a[j][1]
                    k+=1
                    del a[j]
                    break
    
z1,z2,z3,z4,z5=map(int,input().split())
p=[z1,z2,z3,z4,z5]
a.sort(key=lambda x:x[0])

for i in range(len(p)):
    print(a[p[i]-1][0],a[p[i]-1][1])
