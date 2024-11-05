#include <stdio.h>
#include <string.h>
 
int main() {
    int arr[10], i, j;
 
    printf("Enter 10 numbers for the array:\n");
    for (j = 0; j < 10; j++) {
        scanf("%d", &arr[j]);
    }
 
    printf("Enter the number you want to search for in the array: ");
    scanf("%d", &i);
 
    int found = 0; // To check if the number was found
    for (j = 0; j < 10; j++) {
        if (arr[j] == i) {
            printf("Number %d found at position: %d\n", arr[j], j + 1);
            found = 1; // Mark as found
        }
    }
 
    if (!found) {
        printf("Number %d not found in the array.\n", i);
    }
 
    return 0;
}