#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <myfirstlibrary.h>

//Four first few functions






/* float root (float num)
{
	for(int )
	1/2*()
} */





void main()
{
	int optest = 0;
	int optest2 = 5;
	
	static int unchange = 4;
	
	char charizard = 'h';
	
	float floattest = 3.4547656;
	float floattest2 = 5.345349495;
	
	float mass = 3e30;
	
	//printf("%f\n",mass);
	//optest *= optest2;
	
	//optest++;
	
	//printf("%i\n",optest);
	//printf("%i\n",optest2);
	//printf("%f\n",floattest / floattest2);
	
	//printf("%f\n",asin(0.5));
	
	//unchange++;
	
	printf("%i\n",absval(-132)); 
	
	
	//srand(time(NULL));
	//printf("%d\n",rand());
	
	
  /* //Basic while
  while(optest != 20)
  {
	 printf("Conditional experiments!");
	 optest++;
  }
  */
  
  /*   //Basic if
  if(optest)
  {
	  printf("First if");
	  printf("Second if");
  }
  else 
  {	
	printf("%i\n",optest);
	printf("%i\n",optest2);
  }
  */
  
  /* //While and case
  while(optest <= 3)
  {
	switch(optest)
	{
	 case 3:
	 {
		printf("1");
		optest++;
		break;
	 }
	 case 1:
	 {
		printf("2"); 
		optest++;
		break; 
	 }
	 case 2:
	 {
		printf("3");
		optest++;
		break;
	 }
	 //default:
		//printf("Default");
	 
	}
  }
  */
  
  /*
  int luma = 12;
  while (luma < 6)
  {
	printf("No sex with Luma when %i, only talk. \n",luma);
	luma++;
  }


  luma = 12;
  do
  {
	printf("No sex with Luma when %i, only talk. \n",luma);
	luma++;
  }
  while (luma < 6);
  */
 
 
 
 struct model
 {
	 int weight;
	 int height;
	 int followers;
	 int waistsize;
	 int cokeexp;
	 int sexpartners;
 }; 
  
 struct model luma = {62,168,200000,8,1,6};
 
 printf("Luma's weight is %i kg. \n",luma.weight);
 printf("Luma's height is %i centimetres. \n",luma.height);
 printf("Luma's followers are %i people strong!\n",luma.followers);
 printf("Luma's waist size is %i centimetres. \n",luma.waistsize);
 printf("Luma's has done coke %i times. \n",luma.cokeexp);
 printf("Luma's has fucked %i people. \n",luma.sexpartners);
 
 struct model cara = {85,210,1000000,200,3000,100};
 
 printf("Cara's weight is %i kg. \n",cara.weight);
 printf("Cara's height is %i centimetres. \n",cara.height);
 printf("Cara's followers are %i people strong!\n",cara.followers);
 printf("Cara's waist size is %i centimetres. \n",cara.waistsize);
 printf("Cara's has done coke %i times. \n",cara.cokeexp);
 printf("Cara's has fucked %i people. \n",cara.sexpartners);
 
 
 
  enum friend
 {
	height,
	weight,
	lovelevel,
 };
 
	 
	 
 //Luma's for loop
 for(int lumag = 1; lumag < 10; lumag += 3)
 {
	printf("Luma is irrelevant and is %i years old!\n",lumag);
	//lumag = 4;
	
 }
 
 
  //Luma's second and final for loop
 for(int lumagr = 0; lumagr < 10; lumagr++)
 {
	 printf("This for loop is as empty as Luma! She has %i substance. \n",lumagr);
	 lumagr++, lumagr++;
	 
 }
 
 
	// Counting up and down
	int x, y;
	for (x = 1, y = 10; x <= 10 && y >= 1; x+=2, y--)
	printf ("%d %d\n", x, y);



	//This shit don't do shit. 
	;;;;;;;
	
	
 
}

/*
+=
-=
*=
/=
&=
>>=
<<=

++
--

==
!=
>
<
<=
>=


!
&&
||

~
|
&
*/