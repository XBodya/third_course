#include <iostream>
#include <omp.h>
#include <vector>
#include <fstream>
#include <ctime>
#include <string>
#include <cmath>

#define INIT_TIMER double start_time, run_time
#define START_TIMER start_time = omp_get_wtime()
#define STOP_TIMER run_time = omp_get_wtime() - start_time
#define PRINT_TIME_MESSAGE(MESSAGE, TIME) cout << (MESSAGE) << " runtime: " << TIME << '\n'


using namespace std;

double to_grad(double rad){
    return rad * 180 / M_PI;
}

double to_rad(double grad){
    return grad * M_PI / 180;
}

struct double3{
    // X <-> x <-> r 
    // Y <-> y <-> theta
    // Z <-> z <-> phi
    // systems D - Decart, P - Polar
    double X;
    double Y;
    double Z;
    char stype;

    double3(): X(0), Y(0), Z(0), stype('D') {};
    double3(double _X, double _Y, double _Z): X(_X), Y(_Y), Z(_Z), stype('D') {};
    double3(double _X, double _Y, double _Z, char _stype): X(_X), Y(_Y), Z(_Z), stype(_stype) {};
    double3(const double3 &obj): X(obj.X), Y(obj.Y), Z(obj.Z), stype(obj.stype) {};

    double3& operator=(const double3& obj){
        if(&obj != this){
            this->X = obj.X;
            this->Y = obj.Y;
            this->Z = obj.Z;
            this->stype = obj.stype;
        }
        return *this;
    }

    friend double3 operator+(const double3& a, const double3& b){
        return double3(a.X + b.X, a.Y + b.Y, a.Z + b.Z);
    }

    friend double3 operator-(const double3& a, const double3& b){
        return double3(a.X - b.X, a.Y - b.Y, a.Z - b.Z);
    }

    void print(){
        if(stype == 'D')
            cout << "\ndouble3{X=" << X << ", Y=" << Y << ", Z=" << Z <<", system_coords_type=" << stype << "}\n";
        if(stype == 'P')
            cout << "\ndouble3{X=" << X << ", Y=" << min(to_grad(Y), 180 - to_grad(Y)) << ", Z=" << to_grad(Z) <<", system_coords_type=" << stype << "}\n";
    }

    double3 get_polar_coords(){
        double3 polar(*this);
        if(stype != 'P'){
            polar.stype = 'P';
            polar.X = sqrt(X * X + Y * Y + Z * Z);
            polar.Y = atan(sqrt(X * X + Y * Y) / Z);
            polar.Z = atan(Y / X);
        }
        return polar;
    }

    double3 get_decart_coords(){
        double3 decart(*this);
        if(stype != 'D'){
            decart.stype = 'D';
            decart.X = X * sin(Y) * cos(Z);
            decart.Y = X * sin(Y) * sin(Z);
            decart.Z = X * cos(Y);
        }
        return decart;
    }

    void to_polar(){
        double tmp[3] = {0, 0, 0};
        if(stype != 'P' and stype == 'D'){
            this->stype = 'P';
            tmp[0] = sqrt(X * X + Y * Y + Z * Z);
            tmp[1] = atan(sqrt(X * X + Y * Y) / Z);
            tmp[2] = atan(Y / X);
            X = tmp[0];
            Y = tmp[1];
            Z = tmp[2];
        }
    }

    void to_decart(){
        double tmp[3] = {0, 0, 0};
        if(stype != 'D' and stype == 'P'){
            this->stype = 'D';
            tmp[0] = X * sin(Y) * cos(Z);
            tmp[1] = X * sin(Y) * sin(Z);
            tmp[2] = X * cos(Y);
            X = tmp[0];
            Y = tmp[1];
            Z = tmp[2];
        }
    }

    void rotate_by_rad(char axis, double phi){
        if(axis == 'z' or axis == 'Z'){
            to_polar();
            Z += phi;
            to_decart();    
        }
        else if(axis == 'x' or axis == 'X'){
            swap_axes_forward();
            rotate_by_rad('z', phi);
            swap_axes_backward();
        }
        else if(axis == 'y' or axis == 'Y'){
            swap_axes_backward();
            rotate_by_rad('z', phi);
            swap_axes_forward();
        }

    }

    void rotate_by_grad(char axis, double phi){
        rotate_by_rad(axis, to_rad(phi));
    }

    void swap_axes_forward(){
        swap(this->X, this->Z);
        swap(this->X, this->Y);
    }

    void swap_axes_backward(){
        swap(this->X, this->Z);
        swap(this->Z, this->Y);
    }

    double3 get_swaped_axes_forward(){
        double3 tmp(*this);
        tmp.swap_axes_forward();
        return tmp;
    }

    double3 get_swaped_axes_backward(){
        double3 tmp(*this);
        tmp.swap_axes_backward();
        return tmp;
    }

    double3 get_rotate_by_rad(char axes, double phi){
        double3 tmp(*this);
        tmp.rotate_by_rad(axes, phi);
        return tmp;
    }

    double3 get_rotate_by_grad(char axes, double phi){
        double3 tmp(*this);
        tmp.rotate_by_grad(axes, phi);
        return tmp;
    }
    
};

class Obj3D{
public:
    vector<double3> obj;
    Obj3D();
    Obj3D(int n){
        obj.resize(n);
    }
    void random_fill(){
        for(auto &point: obj){
            point = double3 (rand() % 100 + 1, rand() % 100 + 1, rand() % 100 + 1);
        }
    }

    void print(){
        for(auto point: obj){
            point.print();
        }
    }

    void rotate_by_rad(char axes, double phi){
        for(auto &point: obj){
            point.rotate_by_rad(axes, phi);
        }
    }

    void rotate_by_grad(char axes, double phi){
        for(auto &point: obj){
            point.rotate_by_grad(axes, phi);
        }
    }

    void parallel_rotate_by_rad(char axes, double phi){
        #pragma omp parallel
        {
            #pragma omp for nowait schedule(auto)
            for(int i = 0; i < obj.size(); ++i){
                obj[i].rotate_by_rad(axes, phi);
            }
        }

        #pragma omp barrier
    }

    void parallel_rotate_by_grad(char axes, double phi){
        parallel_rotate_by_rad(axes, to_rad(phi));
    }
};

int main(){
    
    // q.get_swaped_axes_forward().print();
    // q.get_swaped_axes_backward().print();
    // q.get_swaped_axes_backward().get_swaped_axes_forward().print();
    // q.get_swaped_axes_forward().get_swaped_axes_backward().print();
    // q.get_swaped_axes_forward().get_swaped_axes_forward().print();
    // q.get_swaped_axes_backward().get_swaped_axes_backward().print();
    // double3 q(1, 1, 1), n(q);
    // double phi;
    // cin >> phi;
    // q.get_rotate_by_grad('x', phi).print();
    // q.get_rotate_by_grad('y', phi).print();
    // q.get_rotate_by_grad('z', phi).print();
    INIT_TIMER;
    int N[] = {10000, 20000, 100000, 500000};
    for(auto cnt: N){
        Obj3D test_case(cnt);
        test_case.random_fill();
        double test_phi = rand() % 361;
        cout << "N=" << cnt << '\n';
        START_TIMER;
        test_case.rotate_by_grad('x', test_phi);
        STOP_TIMER;
        PRINT_TIME_MESSAGE("NO OMP", run_time);
        
        START_TIMER;
        test_case.parallel_rotate_by_grad('x', test_phi);
        STOP_TIMER;
        // cout << "N=" << cnt << ' ';
        PRINT_TIME_MESSAGE("With OMP", run_time);
    }
    cout << '\n';
    // MAX MIN AVG TEST
    Obj3D cube(100000);
    
    cube.random_fill();
    //cube.print();

    // START_TIMER;
    // cube.rotate_by_grad('x', 90);
    // STOP_TIMER;
    // PRINT_TIME_MESSAGE("NO OMP", run_time);

    // START_TIMER;
    // cube.parallel_rotate_by_grad('x', 90);
    // STOP_TIMER;
    // PRINT_TIME_MESSAGE("WITH OMP", run_time);
    //cube.print();

    int cnt_tests = 1000;
    double max_time = 0, min_time=1e9 + 7, avg_time=0;
    for(int i = 0; i < cnt_tests; ++i){
        double phi = rand() % 361;
        START_TIMER;
        cube.parallel_rotate_by_grad('x', phi);
        STOP_TIMER;
        if(run_time > max_time) max_time = run_time;
        if(min_time > run_time) min_time = run_time;
        avg_time += (run_time / (double)cnt_tests);
    }
    PRINT_TIME_MESSAGE("MAX_TIME: ", max_time);
    PRINT_TIME_MESSAGE("MIN_TIME: ", min_time);
    PRINT_TIME_MESSAGE("AVG_TIME: ", avg_time);
    return 0;
}

