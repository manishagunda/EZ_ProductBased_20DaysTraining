#include<stdio.h>
/*#def ke=0 not change*/
int fun(int n)
{
	int even[n+1],odd[n+1];
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
	return even[n+1],odd[n+1];	
}
main()
{
	int a[10][10],i,j,n=3,ke=0,ko=4;
	int even[10],odd[10];
	even[n+1],odd[n+1]=fun(n);
	for(i=0;i<=n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i==2 && j==2)
			{
				a[i-1][j-1]=5;	
			}
			else if((i+j)%2==0)
			{
				a[i-1][j-1]=even[ke];
				ke++;
			}
			else
			{
				a[i-1][j-1]=odd[ko];
				ko--;
			}
		}
	}
	for(i=1;i<=n;i++)
	{
		printf("\n");
		for(j=1;j<=n;j++)
		{
			printf("\n%d",a[i][j]);
		}
	}
	 
}
