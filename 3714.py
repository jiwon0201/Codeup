import sys
sys.setrecursionlimit(100000)

memo={1:1, 2:5, 3:11}
def f(n):
    if n in memo:
        return memo[n]
    memo[n]=(f(n-1)+4*f(n-2)+2*f(n-3))%100007
    return memo[n]
n=int(input())
print(f(n))
