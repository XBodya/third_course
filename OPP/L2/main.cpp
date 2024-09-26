/*
Написать программу с использованием технологии OpenMP, которая
решает поставленную задачу. При этом вычислить максимальное, минимальное
и среднее время выполнения программы. Провести анализ для различной
размерности. Отчет должен содержать постановку задачи, краткое описание
решения, последовательную версию программы и параллельную (наиболее
производительную) и таблицу с результатами, выводы

1. Параллельное транспонирование матрицы
Используйте #pragma omp parallel для транспонирования матрицы размером M×N.
Распределите работу по транспонированию элементов между потоками.
*/

#include <iostream>
#include <omp.h>
#include <vector>
#include <fstream>
#include <ctime>
#include <string>

#define PRINT_TIME_MESSAGE(MESSAGE, TIME) cout << (MESSAGE) << " runtime: " << TIME << '\n'


using namespace std;

typedef vector<vector<int> > int_matrix;

int_matrix transpose(int_matrix &MTR){
    int M = MTR.size(), N = MTR[0].size();
    int_matrix tmp(N, vector<int> (M, 0));
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < M; ++j){
            tmp[i][j] = MTR[j][i];
        }
    }
    return tmp;
}

void print(int_matrix &MTR){
    for(auto it: MTR){
        for(auto el: it){
            cout << el << ' ';
        }
        cout << '\n';
    }
}

int_matrix make_test(int M, int N){
    int_matrix MTR(M, vector<int> (N, 0));
    for(auto &row: MTR){
        for(auto &el: row){
            el = rand() % 100 + 1;
        }
    }
    return MTR;
}

int_matrix mfile_read(string filename){
    int M, N;
    fstream fin(filename);
    fin >> M >> N;
    int_matrix MTR(M, vector<int> (N, 0));
    for(auto &row: MTR){
        for(auto &el: row){
            fin >> el;
        }
    }
    fin.close();
    return MTR;
}

int_matrix omp_transpose(int_matrix &MTR){
    int cnt_threads = omp_get_max_threads();
    int M = MTR.size(), N = MTR[0].size();
    int_matrix tmp(N, vector<int> (M, 0));
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        for(int i = 0; i < N; ++i){
            for(int j = id; j < M; j+= cnt_threads){
                tmp[i][j] = MTR[j][i];
            }
        }
    }
    return tmp;
}

int_matrix omp_transpose_for(int_matrix &MTR){
    int cnt_threads = omp_get_max_threads();
    int M = MTR.size(), N = MTR[0].size();
    int_matrix tmp(N, vector<int> (M, 0));
    #pragma omp parallel
    {
        
        for(int i = 0; i < N; ++i){
            #pragma omp for nowait schedule(auto)
            for(int j = 0; j < M; ++j){
                tmp[i][j] = MTR[j][i];
            }
        }
    }
    return tmp;
}

int main(){
    // random seed
    srand(time(0));
    fstream fin("in.in");
    int M, N;
    fin >> M >> N;
    fin.close();
    int_matrix MTR = make_test( M, N);
    double start_time, run_time;

    start_time = omp_get_wtime();
    transpose(MTR);
    run_time = omp_get_wtime() - start_time;
    PRINT_TIME_MESSAGE("NO OMP", run_time);

    start_time = omp_get_wtime();
    omp_transpose(MTR);
    run_time = omp_get_wtime() - start_time;
    PRINT_TIME_MESSAGE("WITH OMP", run_time);

    start_time = omp_get_wtime();
    omp_transpose_for(MTR);
    run_time = omp_get_wtime() - start_time;
    PRINT_TIME_MESSAGE("WITH OMP_FOR", run_time);
    //print(MTR);
    //cout << '\n';
    //print(TMTR);
    //cout << '\n';
    return 0;
}