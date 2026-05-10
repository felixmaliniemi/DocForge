#include <iostream>

/** Detta är ett exempel på addition */
int add(int a, int b) { return a + b; }

/** Detta är ett exempel på subtraktion */
int subtract(int a, int b) { return a - b; }

/** Detta är ett exempel på multiplikation */
int multiply(int a, int b) { return a * b; }

/** Detta är ett exempel på division */
double divide(double a, double b) { return b != 0 ? a / b : 0; }

/** Kör alla matematiska operationer med exempelvärden */
int main() {
    std::cout << "Addition: " << add(3,2) << std::endl;
    std::cout << "Subtraction: " << subtract(5,3) << std::endl;
    std::cout << "Multiplication: " << multiply(4,2) << std::endl;
    std::cout << "Division: " << divide(10,2) << std::endl;
    return 0;
}
