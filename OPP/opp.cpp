#include <iostream>
#include <omp.h>
#include <vector>
#include <numeric> // для std::accumulate
#include <chrono>  // для измерения времени

using namespace std;

double calc_avg(vector<int> arr) {
    float sum = 0;
    double start_time;
    start_time = omp_get_wtime();
    #pragma omp parallel for
        for (int i = 0; i < arr.size(); i++) {
            sum += arr[i];
        }
    cout << "TIME_EXEC " << omp_get_wtime() - start_time << '\n';
    return sum / arr.size();
}



int main() {
    vector<int> a = {1, 1, 1, 1, 2};
    cout << calc_avg(a);
    return 0;
}
