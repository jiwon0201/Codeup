#include <stdio.h>
long long int n;
 
int sqrt(long long int n)
{
    double a,b;
 
    a=0.5*(1+(n/1));
 
    while(1)
    {
        b=a;
        a=0.5*(a+(n/a));
 
        if(b-a<0.00001 || b-a<-0.00001)
        {
            break;
        }
 
    }
    a=(long long int)a;
    return a;
}
 
int main()
{
  scanf("%lld", &n);
  printf("%d\n", sqrt(n));
  return 0;
}
