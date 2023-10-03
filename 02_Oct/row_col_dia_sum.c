#include<stdio.h>
main()
{
	int n=3;
	int even[10],odd[10],a[10][10];
	int i,j,ke=0,ko=0;
	for(i=1;i<=n*n;i++)
	{
		if(i%2==0)
		{
			even[ke]=i;
			ke++;
		}
		else
		{
			odd[ko]=i;
			ko++;
		}
	}
	int e=0,o=4;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(i==2 && j==2)
			{
				a[i][j]=5;	
			}
			else if((i+j)%2==0)
			{
				a[i][j]=even[e];
				e++;
			}
			else
			{
				a[i][j]=odd[o];
				o--;
			}
		}
	}
	for(i=1;i<=n;i++)
	{
		printf("\n");
		for(j=1;j<=n;j++)
		{
			printf("%d\t",a[i][j]);
		}
	}
}
	
