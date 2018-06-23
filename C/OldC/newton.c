#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

/*
This program is designed to find a root of a function using Newton's Method, defined in the below function definition. 

Remember, reader, that -lm handle is required to use the math library. 
*/
double func(double x)
{
	return 2.0*pow(x,2.0) - 6*x + 2;
	//return 2.0*x - 6.0;
}

double deriv(double x)
{
	return 2.0*pow(x,1.0) - 6;
	//return 2.0;
}

void main()
{
	//printf("%f \n", func(7.4));
	//printf("%f \n", deriv(7.4));
	
	double domstart = 0.0;
	double domend = 7.0;
	double disc = 0.1;
	int num = floor( (domend - domstart) / disc );

	double xvals[num];
	xvals[0] = domstart;
	xvals[num] = domend;
	
	double fvals[num];
	
	double derivvals[num];
	
	double rootseq[num];
	rootseq[0] = 0.3;   // Initial guess
	
	double rootknown1 = 0.354;  // Known roots
	double rootknown2 = 5.6457;  // Known roots
	
	for(int i = 1; i < num; i++)
	{
		xvals[i] = xvals[0] + disc*i;
		fvals[i] = func(xvals[i]);
		derivvals[i] = deriv(xvals[i]);
		rootseq[i] = rootseq[i-1] - ( fvals[i-1] / derivvals[i-1] );
		
		
		printf("%f\n", xvals[i]);
		printf("%f\n", fvals[i]);
		printf("%f\n", derivvals[i]);
		printf("%f\n", rootseq[i]);
	}
	
	
	/*
	for(double i = domstart; i == domend; i = i + 0.1)
	{
		
	}
	
	array[x]
	array[root]
	
	array[fx]
	array[f'x]
	*/
}

