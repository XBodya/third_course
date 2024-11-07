#include <iostream>
#include <omp.h>
#include <vector>
#include <fstream>
#include <ctime>
#include <string>
#include <cmath>

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
            
        }
        else if(axis == 'y' or axis == 'Y'){

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
    
};

int main(){
    double3 q(5, 4, 3), n(q);
    q.get_swaped_axes_forward().print();
    q.get_swaped_axes_backward().print();
    q.get_swaped_axes_backward().get_swaped_axes_forward().print();
    q.get_swaped_axes_forward().get_swaped_axes_backward().print();
    q.get_swaped_axes_forward().get_swaped_axes_forward().print();
    q.get_swaped_axes_backward().get_swaped_axes_backward().print();
    return 0;
}

