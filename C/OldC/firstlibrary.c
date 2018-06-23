#include <stdio.h>
#include <gsl/specfunc/gsl_sf_bessel.h>

void main()
{
  double x = 5.0;
  double y = gsl_sf_bessel_J0 (x);
  printf ("J0(%g) = %.18e\n", x, y);
}
