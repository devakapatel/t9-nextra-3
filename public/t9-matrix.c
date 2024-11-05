#include <stdio.h>
#include <limits.h>
 
int MatrixChainMultiplication(int p[], int n) {
    int m[n][n];
    int i, j, k, L, q;
 
    // Initialize the diagonal of the matrix to 0
    for (i = 1; i < n; i++) {
        m[i][i] = 0;
    }
 
    // L is the chain length
    for (L = 2; L < n; L++) {
        for (i = 1; i < n - L + 1; i++) {
            j = i + L - 1;
            m[i][j] = INT_MAX; // Initialize to a large value
            for (k = i; k <= j - 1; k++) {
                // Calculate cost of multiplying
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (q < m[i][j]) {
                    m[i][j] = q; // Update minimum cost
                }
            }
        }
    }
    return m[1][n - 1]; // Return the minimum cost
}
 
int main() {
    int n, i;
    printf("Enter number of matrices: ");
    scanf("%d", &n);
    
    n++; // Increment to account for the number of dimensions
    int arr[n];
    
    printf("Enter dimensions:\n");
    for (i = 0; i < n; i++) {
        printf("Enter d%d: ", i);
        scanf("%d", &arr[i]);
    }
 
    printf("Minimum number of multiplications is: %d\n", MatrixChainMultiplication(arr, n));
    
    return 0;
}