#include<stdio.h>
int main()
{
	char a[21];
	int b;
	char c[2];
	double d;
	
	scanf("%s",a);
	scanf("%d",&b);
	scanf("%s",c);
	scanf("%lf",&d);
	
	printf("%s\n",a);
	printf("%d\n",b);
	printf("%s\n",c);
	printf("%g\n",d);
	
	return 0;
}
