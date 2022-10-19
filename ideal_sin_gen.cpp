#include <stdio.h>
#include <iostream>
#include <string>
#include <complex.h>
using namespace std;
int main()
{
    float signal[]={1.0, 0.5, 0.0,  0.5, 1.0,  0.5, 0.0,  0.5}; 
    int n,loop;n = (sizeof(signal) /  sizeof(float)); 
    float slope[n],slp_amp[n]; 

   for(loop=1;loop<n-1;loop++)
   {
       slope[loop] = (signal[loop+1]- signal[loop-1]);
       cout << "slope of " << loop << "  is \t" <<signal[loop+1] << "-" <<signal[loop-1]<<"=" << slope[loop] <<"\n";
       
       slp_amp[loop] = (slope[loop] * signal[loop]);
       cout << "slope amplitudde of " << loop << "  is \t" <<slope[loop] << "*" <<signal[loop]<<"=" << slp_amp[loop] <<"\n\n\n";
  
   }
 
  return 0;
}
    