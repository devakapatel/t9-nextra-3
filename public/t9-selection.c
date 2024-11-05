#include <stdio.h>
 
int main() {
    int a[10], i, j, temp, num;
 
    printf("Enter the number of elements (max 10): ");
    scanf("%d", &num);
 
    if (num > 10) {
        printf("Please enter a number less than or equal to 10.\n");
        return 1;
    }
 
    for (i = 0; i < num; i++) {
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }
 
    // Selection Sort
    for (i = 0; i < num - 1; i++) {
        for (j = i + 1; j < num; j++) {
            if (a[i] > a[j]) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
 
    printf("Sorted array:\n");
    for (i = 0; i < num; i++) {
        printf("a[%d] = %d\n", i, a[i]);
    }
 
    return 0;
}