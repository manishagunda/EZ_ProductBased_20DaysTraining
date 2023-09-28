#include<stdio.h>
int main()
{
	int a[100],i,m,l,h;
	printf("enter num of elements");
	scanf("%d",&m);
	printf("enter range");
	scanf("%d",&l);
	scanf("%d",&h);
	printf("enter array elements");
	for(i=0;i<m;i++)
	{
		scanf("%d",&a[i]);
    }
    printf("\n array is\n");
    for(i=0;i<m;i++)
	{
		if(a[i]>=l && a[i]<=h)
		{
		printf("\n%d",a[i]);
	    }	
    }
    printf("\neven numbers\n");
    for(i=0;i<m;i++)
	{
		if(a[i]%2==0)
		{
			printf("\n%d",a[i]);
		}
	}
	int 2power(int number)
{
    while(number!=1)
    {
        if(number%2!=0)
            return 0;
        number=number/2;
    }
    return 1;
}
	printf("\n2 power numbers");
	for(i=0;i<m;i++)
	{
		if(2power(a[i]))
		{
		printf("\n%d",a[i]);
    	}
    }
}
