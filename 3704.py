import sys
sys.setrecursionlimit(1000000) 

n=int(input())
cnt=0

def f(total) :
    global cnt

    if n==0: 
        return 0

    if n-total>=1: 
        f(total+1)
    if n-total>=2:
        f(total+2)
    if n-total>=3:
        f(total+3)
    
    elif total==n:
        cnt+= 1

f(0)

print(cnt%1000)
