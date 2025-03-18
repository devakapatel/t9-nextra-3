#include <stdio.h>
 
int count(int S[], int m, int n) {
    // Base case: If n is 0, there is one solution (do not include any coin)
    if (n == 0)
        return 1;
 
    // If n is less than 0, no solution exists
    if (n < 0)
        return 0;
 
    // If there are no coins left and n is greater than 0, no solution exists
    if (m <= 0 && n >= 1)
        return 0;
 
    // Count the solutions including the last coin and excluding the last coin
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);
}
 
int main() {
    int arr[] = {2, 5, 8}; // Denominations
    int m = sizeof(arr) / sizeof(arr[0]); // Number of denominations
 
    printf("%d\n", count(arr, m, 10)); // Count ways to make change for 10
    return 0;
}