#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main()
{
	
	srand(time(NULL));   // Seed
	int size = 10;
	int randarray[size];

	// Random printing of numbers
	for(int i = 0; i < size; i++)
	{
		randarray[i] = rand();
		printf("%i,",randarray[i]);
	}
	
	int desired;
	
	// Ask what integer to find a value close to
	printf("\nWhat would you like to find in your quest? \n");
	scanf("%d", &desired);
	printf("I got it, you said you want to find something like %i! \n",desired);
	
	int done = 0;
	
	// Find a number closest to a certain number in a random array by looking directly
	for(int i = 0; i < size; i++)
	{
		if (randarray[i] == desired)
		{
			printf("This number was found at place %i in the array. ", i+1);
			done = 1;
		}
	}
	
	if (done == 0)
	{
		// Find the closest number to the number specified in the random array
		int randarraydiff[size];
		
		// Find the difference between each value and desired 
		for(int i = 0; i < size; i++)
		{
			randarraydiff[i] = abs(randarray[i] - desired);
			//printf("%i ", randarraydiff[i]);
		}
		
		int minim = randarraydiff[0];
		int pos = 0;
		int val;
		
		// Find the minimum difference in all the differences
		for(int i = 0; i < size; i++)
		{
			if (randarraydiff[i] < minim)
			{
				minim = randarraydiff[i]; 
				pos = i+1;
				val = randarray[i];
			}
			if ( (randarraydiff[i] == minim) && ( (randarraydiff[i+1] - randarraydiff[i]) == 0) ) // This is a rare, inbetween case
			{
				printf("Inbetween! Note that either of the positions and values are valid! \n");
			}
			
		}
		printf("The number you chose is %i away from %i and this number is in the position %i. ", minim, val, pos);
	}
	
	
}

