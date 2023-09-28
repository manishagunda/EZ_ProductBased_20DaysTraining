#include<stdio.h>
int factorial(int);
main()
{
	int n;
	printf("enter n");
	scanf("%d",&n);
	printf("\nfactorial of n=%d",factorial(n));
}
int factorial(int n)
{
	if(n==1)
	return 1;
	else
	return(n*factorial(n-1));
}
