#include <stdio.h>
#include <math.h>

void main()
{
  // Generate odd numbers
  // Generate fractions

  double total = 0;
  //float total = 0;

  for(int i = 0; i < 100000; i++)
  {
    total = total + ( pow(-1,i) / (2*i + 1) );
    //total = total + ( pow(-1,i) );
    printf("%f\n", total);
  }

  double piap = total*4;
  //float piap = total*4;
  printf("%f\n", piap);
  
}
