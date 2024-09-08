#include <omp.h>
#include <iostream>

static long num_steps = 100000000;
double step;
double start_time, run_time;
int i;
double x, pi, sum = 0.;

void print_res(){
    std::cout << "\n Pi with " << num_steps << " steps is " << pi << " in " << run_time << "sec. \n";
}

void calc_pi_no_omp(){
    step = 1.0 / (double) num_steps;
    start_time = omp_get_wtime();
    for(i = 1; i <= num_steps; ++i){
        x = (i - 0.5) * step;
        sum += 4.0 / (1.0  + x * x);
    }
    pi = sum * step;
    run_time = omp_get_wtime() - start_time;
    print_res();
}

void calc_pi_with_omp(){

}

int main(){
    calc_pi_no_omp();
    return 0;
}