#include <stdio.h>

/** Detta är ett exempel på addition */
int add(int a, int b) { return a + b; }

/** Detta är ett exempel på subtraktion */
int subtract(int a, int b) { return a - b; }

/** Detta är ett exempel på multiplikation */
int multiply(int a, int b) { return a * b; }

/** Detta är ett exempel på division */
double divide(double a, double b) { return b != 0 ? a / b : 0; }

/** Kör alla operationer */
int main() {
    printf("Addition: %d\n", add(3,2));
    printf("Subtraction: %d\n", subtract(5,3));
    printf("Multiplication: %d\n", multiply(4,2));
    printf("Division: %.2f\n", divide(10,2));
    return 0;
}
