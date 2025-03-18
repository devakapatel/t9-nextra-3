#include <stdio.h>
#include <string.h>
 
int i, j, m, n, LCS_table[20][20];
char S1[20] = "ACADB", S2[20] = "CBDA", lcsStr[20];
 
void lcsAlgo() {
    m = strlen(S1);
    n = strlen(S2);
 
    // Filling 0's in the LCS table
    for (i = 0; i <= m; i++)
        LCS_table[i][0] = 0;
    for (j = 0; j <= n; j++)
        LCS_table[0][j] = 0;
 
    // Building the table in bottom-up way
    for (i = 1; i <= m; i++) {
        for (j = 1; j <= n; j++) {
            if (S1[i - 1] == S2[j - 1]) {
                LCS_table[i][j] = LCS_table[i - 1][j - 1] + 1;
            } else if (LCS_table[i - 1][j] >= LCS_table[i][j - 1]) {
                LCS_table[i][j] = LCS_table[i - 1][j];
            } else {
                LCS_table[i][j] = LCS_table[i][j - 1];
            }
        }
    }
 
    // Constructing the LCS string
    int index = LCS_table[m][n];
    lcsStr[index] = '\0'; // Null-terminate the LCS string
    i = m;
    j = n;
 
    while (i > 0 && j > 0) {
        if (S1[i - 1] == S2[j - 1]) {
            lcsStr[index - 1] = S1[i - 1];
            i--;
            j--;
            index--;
        } else if (LCS_table[i - 1][j] > LCS_table[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
 
    // Printing the subsequences
    printf("S1: %s\nS2: %s\n", S1, S2);
    printf("LCS: %s\n", lcsStr);
}
 
int main() {
    lcsAlgo();
    return 0;
}