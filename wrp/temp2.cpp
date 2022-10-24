#include <stdio.h>
#include <iostream>
#include <string>
#include <complex.h>
#include "linker.hpp"
using namespace std;
float time_error(float signal[], int samprate)
{
     
    int loop;
    float* slope =new float[samprate]; //val of samprate will be know dynamical so the array is created dynamically 
    float* slp_amp = new float [samprate]; 
    //printf("%f array", sizeof(signal));
    //printf("\n\n\n%f float\n\n\n", sizeof(float));
    
    //printf("%f total", n);
   //cout << n "\n";
   /*for(loop=1;loop<samprate-1;loop++) // here we calculate slope and multipication with ampli for all samples
   {
       slope[loop] = (signal[loop+1]- signal[loop-1]);
       //cout << "slope of " << loop << "  is \t" <<signal[loop+1] << "-" <<signal[loop-1]<<"=" << slope[loop] <<"\n";
       
       slp_amp[loop] = (slope[loop] * signal[loop]);
       //cout << "slope amplitudde of " << loop << "  is \t" <<slope[loop] << "*" <<signal[loop]<<"=" << slp_amp[loop] <<"\n\n\n";
  
   }*/
 //calculating slope*ample for 1st symbol 4th sample
 for(loop=1;loop<samprate-1;loop+3) // loop=0 we cant cal slope of 1st sample, loop+3 -> slope of every 4th sample one per symb
{

  slope[loop] = (signal[loop+1]- signal[loop-1]);
       //cout << "\n\n slope of " << loop+1 << "th sample  is \t" <<signal[loop+1] << "-" <<signal[loop-1]<<"=" << slope[loop] <<"\n";
       
       slp_amp[loop] = (slope[loop] * signal[loop]);
       //cout << "\n slope amplitudde of  " << loop+1 << "th sample  is \t" <<slope[loop] << "*" <<signal[loop]<<"=" << slp_amp[loop] <<"\n\n\n";
        cout << slp_amp[loop];
 }
 
  return 0;
}
    