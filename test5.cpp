#include <iostream>

extern "C" int64_t check_of();

int main(){

    std::cout << check_of() ;
    return 0;
}