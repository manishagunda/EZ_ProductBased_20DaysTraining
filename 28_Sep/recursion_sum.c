int add(int n)
{
	if (n<=0)
	{
		return 0;
	}
	return n+add(n-1);
}
int main()
{
	printf("%d",add(5));
}
