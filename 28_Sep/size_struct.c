#include<stdio.h>
struct a
{
	char y;
	double z;
	int	x;
	

};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
/*type 1 double double char  --> place char at any where =24
int int char          -->place char at any where=12*/
/*type 2 int double char --> 16
char int double          --> 16*/
/*type 3 double int char -->
double char int          -->   */
/*type 4 char double int -->24*/


