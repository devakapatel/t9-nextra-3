#include <stdio.h>
 
long int multiplyNumbers(int n);
 
int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
 
    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d = %ld\n", n, multiplyNumbers(n));
    }
    
    return 0;
}
 
long int multiplyNumbers(int n) {
    if (n >= 1) {
        return n * multiplyNumbers(n - 1);
    } else {
        return 1; // Base case: factorial of 0 is 1
    }
}