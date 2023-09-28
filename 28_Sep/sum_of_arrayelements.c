#include<stdio.h>
int sum1(int a[],int n)
 {
 	int i,sum=0;
 
    for(i=0; i<n; i++)
    {
         sum+=a[i];
         
    }
 	return sum;
 }
int main()
{
	int a[100],i,m,l,h,sum=0;
	printf("enter num of elements");
	scanf("%d",&m);
	printf("enter array elements");
	for(i=0;i<m;i++)
	{
		scanf("%d",&a[i]);
    }
    sum=sum1(a,m);
    printf("sum of array is :%d",sum);
}
    
