#include "cgcustommath.hpp"
#include <iostream>

/**
 * This executable aims to verify cgcustommath program
 * This executable should 
 * - Take 2 command line parameters. 
 * - Pass them to the matrix function as a and b. 
 * - Print the resulting matrix on screen. 
 */

int main(int argc, char ** argv) {
    int a, b;
    std::cout << "Enter first number a:";
    std::cin >> a;
    std::cout << "Enter first number b:";
    std::cin >> b;

    std::cout << "Result of matrix(a,b) is:" << std::endl;
    std::cout << matrix(a,b) << std::endl;
    return 0;
}
