
#include<stdio.h>
int main() {
	
	volatile int a = 5;
	a= a+1;

	printf("The Value of a is = %0d\n", a);
	return 0;
}
