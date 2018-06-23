#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main()
{

	srand(time(NULL));   //Seed
	int size = 20;
	int randarray[size];

	//Random printing of numbers
	for(int i = 0; i < size; i++)
	{
		randarray[i] = rand();
		printf("%i,",randarray[i]);
	}


	// Sorting of random numbers; Taming the chaos! 
	for(int i = 0; i < size; i++)
	{
		for(int j = 0; j < size; j++)
		{
			if( (i < j) && (randarray[i] > randarray[j]) )
			{
				int third = randarray[i];
				int fourth = randarray[j];
				randarray[j] = third;
				randarray[i] = fourth;
			}
		}
		printf("\n%i,", randarray[i]);
	}


}


