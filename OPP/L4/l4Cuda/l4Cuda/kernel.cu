#include <iostream>

#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include "time.h"

#define ifStatusIsFail if(cudaStatus != cudaSuccess) 
#define check cudaStatus =
#define INIT_TIMER time_t start; double __time_in_sec;
#define START_TIMER start = time(0)
#define STOP_TIMER __time_in_sec = difftime(time(0), start);
#define PRINT_TIME(message) std::cout << message << " @Time execution: " << __time_in_sec << '\n';


__global__ void transposeKernel(float* out, const float* in, int width, int height) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;
    
    if (i < height && j < width) {
        out[j * height + i] = in[i * width + j];
    }
}

void transpose(float* arr, float* out_arr, int width, int height) {
    cudaEvent_t start, stop;
    float time;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0);

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            out_arr[j * height + i] = arr[i * width + j];
        }
    }

    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&time, start, stop);
    printf("Time to exec by cpu:  %3.1f ms \n", time);
}

void initMatrix(float* matrix, int width, int height, int c=1) {
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            matrix[i * width + j] = (i * width + j)*c;
        }
    }
}

void print(const float* matrix, int width, int height) {
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            std::cout << matrix[i * width + j] << " ";
        }
        std::cout << std::endl;
    }
}

cudaError_t cudaTranspose(float *host_in, float *host_out, int width, int height) {
    size_t size = width * height * sizeof(float);
    cudaError_t cudaStatus = cudaSuccess;
    float* device_in;
    float* device_out;

    float time;
    cudaEvent_t start, stop;

    check cudaMalloc(&device_in, size);
    ifStatusIsFail{
        std::cout << "device_in malloc fail\n";
        return cudaStatus;
    }
    check cudaMalloc(&device_out, size);
    ifStatusIsFail{
        std::cout << "device_out malloc fail\n";
        return cudaStatus;
    }

    check cudaMemcpy(device_in, host_in, size, cudaMemcpyHostToDevice);
    ifStatusIsFail{
        std::cout << "device_in copy fail\n";
        return cudaStatus;
    }
    dim3 threadsPerBlock(2, 2);
    dim3 numBlocks((width + threadsPerBlock.x - 1) / threadsPerBlock.x,
        (width + threadsPerBlock.y - 1) / threadsPerBlock.y);
    //START_TIMER;

    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0);

    transposeKernel << <numBlocks, threadsPerBlock >> > (device_out, device_in, width, height);
    //STOP_TIMER;
    //PRINT_TIME("Kernel time exec: ");

    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&time, start, stop);

    printf("Time to exec cuda gpu kernel:  %3.1f ms \n", time);

    cudaStatus = cudaGetLastError();
    ifStatusIsFail{
        std::cout << "transpose fail\n";
        return cudaStatus;
    }

    check cudaMemcpy(host_out, device_out, size, cudaMemcpyDeviceToHost);
    ifStatusIsFail{
        std::cout << "copy device2host fail\n";
        return cudaStatus;
    }

    cudaFree(device_in);
    cudaFree(device_out);
    cudaEventDestroy(start);
    cudaEventDestroy(stop);
    return cudaStatus;
}

int main() {
    INIT_TIMER;
    int w = 60000, h = 20000;
    size_t size = w * h * sizeof(float);
    float* h_in = (float*)malloc(size);
    float* host_out = (float*)malloc(size);
    initMatrix(h_in, w, h);
    START_TIMER;
    cudaTranspose(h_in, host_out, w, h);
    //print(h_in, w, h);
    //std::cout << '\n';
    //print(host_out, h, w);
    STOP_TIMER;
    //PRINT_TIME("Cuda trans.");
    START_TIMER;
    initMatrix(h_in, w, h, 2);
    transpose(h_in, host_out, w, h);
    //print(h_in, w, h);
    //print(host_out, h, w);
    STOP_TIMER;
    //PRINT_TIME("CPU trans.");
    free(h_in);
    free(host_out);
    return 0;
}