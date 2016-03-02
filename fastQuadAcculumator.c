#include <stdio.h>
// Fast Faux Quad Precision accumulator

int main(void)
{

// Lower precision result goes into L, Higher precision goes into H
// The "quad" precision answer is the (conceptual) sum of L and H.
double L=0.0,H=0.0;
double f = 1.0;

// Sum up series 1 + 1/2 + 1/4 + ...
for (f=1.0;f>1e-30;f*=0.5)
{
  double oldL = L;
  L += f;
  H += (oldL - L) + f;
  printf("%1.16e: %1.16e, %1.16e\n",f,L,H);
}

return 0;
}


