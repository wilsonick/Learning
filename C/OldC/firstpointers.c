#include <stdio.h>
#include <math.h>

void main()
{
  
  // Pointers for friends addresses
  int larry = 176;
  int *addlarry = &larry;
  int *addsergey = &larry;

  printf("%i\n",*addlarry);
  printf("%i\n",*addsergey);
  
  //Larry's GPS position
  float gpslarry[2];
  
  gpslarry[0] = -27.563664;
  gpslarry[1] = 152.867745;
  
  printf("%f\n",gpslarry[0]);
  printf("%f\n",gpslarry[1]);
  
  //Sergey's GPS position. Where is Sergey? Is he unspecified?
  
  float *gpssergey[2];    //Good friends
  
  gpssergey[0] = &gpslarry[0];
  gpssergey[1] = &gpslarry[1];
  
  printf("%f\n",*gpssergey[0]);
  printf("%f\n",*gpssergey[1]);
  
  
  
  //Giving Sergey movement won't work because he doesn't know where he is
  /*float gpssergeymov[2];
  gpssergeymov[0] = -50;
  gpssergeymov[1] = gpssergey[1]; //Error! DNC!
  printf("%f\n",*gpssergeymov[0]);
  */
  
  //Moving Sergey 'directly' won't work because he doesn't know where he is
  //gpssergey[0] = -28;
  //printf("%f\n",*gpssergey[0]);
  
  
  
  //Moving Larry will work and Sergey will follow
  //gpslarry[0] = -27.6;
  //printf("%f\n",*gpssergey[0]);
  
  
  
  
  //Moving sergey with both ways won't seperate them
  /*
  float *gpslarryp[2];
  
  gpslarryp[0] = *gpssergey[0];
  gpslarryp[1] = *gpssergey[1];
  */
  
  
}
