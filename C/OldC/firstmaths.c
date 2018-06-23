#include <stdio.h>
#include <math.h>

// C:\Nics Stuff\WebDev\CompilersInterpreters\MinGW\bin

#define markiscool 12

double fibonacci(int term)
{
	double seq[term];
	seq[0] = 1.0;
	seq[1] = 1.0;
	int current;
	for(current = 2 ;  current <= term ; current++)
	{
		seq[current] = seq[current-1] + seq[current-2];
		//printf("%Lf\n",seq[current]);
	}
	return seq[term-1];
} 

double factorial(int term)
{
	double seq[term];
	seq[0] = 1;
	seq[1] = 2;
	int current;
	for(current = 1 ; current <= term ; current++)
	{
		seq[current] = seq[current-1] * current;
		//printf("%Lf\n",seq[current]);
	}
	return seq[term];
}

void main()
{
  printf("%Lf\n",fibonacci(10));
  printf("%Lf\n",factorial(10));	
}
