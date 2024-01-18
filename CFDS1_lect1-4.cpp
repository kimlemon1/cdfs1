#include <iostream>
#include <string>
#include <sstream>


void swap(int* a, int* b){
    std::cout << "swap by pointer\n";
    int temp = *a;
    *a = *b;
    *b = temp;
}

void swap(int &a, int &b){
    std::cout << "swap by reference\n";
    int temp = a;
    a = b;
    b = temp;
}

template <class T>
T sum(T &a, T &b){
	T ans{};
	ans = a + b;
	return ans;
}

template <typename T, int N>
T new_sum(T &a, T &b){
	T ans{};
	ans = a + b;
    ans = ans * N;
	return ans;
}


int main(){

    // std::string sentence{"1234"};
    // int myInt{};
    // //std::cin >> sentence;
    // std::stringstream(sentence) >> myInt;
    // std::cout << myInt << "\n";

    // int a(5);
    // int b(10);
    // std::cout << a << " " << b << "\n";
    // swap(&a, &b);
    // std::cout << a << " " << b << "\n";

    // swap(a, b);
    // std::cout << a << " " << b << "\n";

	int i_a(3);
	int i_b(5);
	double d_a(3.1);
	double d_b(6.7);

    int ans_i = sum<int>(i_a, i_b);
    double ans_d = sum<double>(d_a, d_b);
    std::cout << ans_i << " " << ans_d << std::endl;

    int ans_f = new_sum<int, 4>(i_a, i_b);
    std::cout << ans_f << std::endl;




    return 0;
}