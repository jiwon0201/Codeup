def factorial(n):
    a=1

    for i in range(1, n+1):
        a=a*i
    return a


def combination(n, r):
    n=int(n)
    r=int(r)
    s=(factorial(n)//(factorial(r)*factorial(n-r)))
    print(int(s)%1999)
    
n, r=input("").split()
combination(n,r)
