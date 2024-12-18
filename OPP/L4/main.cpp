#include <omp.h>
#include <iostream>

#define N 200

using namespace std;



int main(){
    int tmp;
#pragma omp parallel for
   for(int i=0; i<N; i++)
  { 
   tmp++;
   }
   #pragma omp barrier
   cout << tmp;
}