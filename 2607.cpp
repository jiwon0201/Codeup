#include <stdio.h>
int ar[4000001];
int main()
{ 
	int a,b,i,j;
	scanf("%d %d",&a,&b);
	for(i=2; i<=b/2; i++)
	{
		for(j=2; i*j<=b; j++)
		{ 
			ar[i*j]=1; 
		} 
	}
	for(i=a; i<=b-2; i++) 
	{ 
		if(ar[i]!=1 && ar[i+2]!=1) 
		printf("%d %d\n",i,i+2);
	}
}
