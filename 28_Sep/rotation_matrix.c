#include<stdio.h>
int main()
{
	int a[100][100],i,j,n,m,temp,r1,r2;
	scanf("%d",&m);
	scanf("%d",&n);
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);	
		}
    }
    printf("\n matrix is");
    for(i=0;i<m;i++)
	{
		printf("\n");
		for(j=0;j<n;j++)
		{
			printf("%d",a[i][j]);	
		}
    }
    printf("\n transpose matrix is");
    for(i=0;i<m;i++)
	{
		printf("\n");
		for(j=0;j<n;j++)
		{
			printf("%d",a[j][i]);	
		}
    }
    printf("\nEnter two row numbers that will be");
    scanf("%d %d", &r1, &r2);
  

    printf("\n matrix is");
    for(i=r1-1;i<m;i++)
	{
		printf("\n");
		for(j=r1-1;j>n;j--)
		{
			printf("%d",a[i][j]);	
		}
    }
    
    
}
