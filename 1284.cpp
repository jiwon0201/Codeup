#include<stdio.h>
#include<math.h>
int main()
{
    int n, i, p=0, a[30], t, s=0;

    scanf("%d", &n);
    t=(int)sqrt((double)n);

    for(i=2; i<=t; i++)
    {
	    while(n%i==0)
        {
            n/=i;
            a[s]=i;
            s++;
        }
    }

    if (n!=1) 
	a[s]=n, s++;
    if (s==2) 
	printf("%d %d", a[0], a[1]);
    else 
	printf("wrong number");
}
