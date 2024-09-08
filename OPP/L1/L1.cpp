#include <omp.h>
#include <iostream>

static long num_steps = 100000000;
double step;
double start_time, run_time;
int i;
double x, pi = 0, sum = 0.;

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
    //std::cout << omp_get_max_threads();
    int MAX_THREADS = omp_get_max_threads();
    omp_set_num_threads(MAX_THREADS);
    double sum[32];
    for(int j = 0; j < MAX_THREADS; ++j)
        sum[j] = 0.0;
    step = 1.0 / (double) num_steps;
    start_time = omp_get_wtime();
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int start = 1 + id * (num_steps) / MAX_THREADS,
            end = (id + 1) * (num_steps) / MAX_THREADS;
        //std::cout << 's' << start << " f" << end << '\n'; 
        for(i = start; i <= end; ++i){
            x = (x - 0.5) * step;
            sum[id] += 4.0 / (1.0 + x * x);
        }
    }
    for(int j = 0; j < MAX_THREADS; ++j) pi += sum[j] * step;
    run_time = omp_get_wtime() - start_time;
    print_res();
}

int main(){
    //calc_pi_no_omp();
    calc_pi_with_omp();
    return 0;
}