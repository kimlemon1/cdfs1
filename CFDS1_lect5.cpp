#include <iostream>
#include <string>
#include <sstream>


class Triangle{
    private:
        double sideA;
        double sideB;
        double sideC;
    public:
        // 생성자 선언할때 넣어놔야한다
        Triangle(double a, double b, double c);

        double area();
        double perimeter();
};

Triangle::Triangle(double a, double b, double c){
    sideA = a;
    sideB = b;
    sideC = c;
}

double Triangle::area(){
    return 0.0;
}
double Triangle::perimeter(){
    return this->sideA + this->sideB + this->sideC;
}



// container 사용법

template<class T>
class mypair{
	T a;
	T b;
	public:
		mypair(T i, T j);
        T get_a();
        T get_b();
};


template<class T> 
mypair<T>::mypair(T i, T j):a(i), b(j){
    
}

template<class T>
T mypair<T>::get_a(){
    return a;
}

template<class T>
T mypair<T>::get_b(){
    return b;
}



int main(){

    // int *ptr = new int [5]; // 정수형 5칸 할당해준다!
    // delete[] ptr; // 받을 때 1칸 이상 받으면 [] 필수

    mypair<int> *ptr = new mypair<int>(3, 10);
    std::cout <<ptr->get_a() <<std::endl;

    return 0;
}