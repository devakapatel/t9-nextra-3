#include <stdio.h>
#include <string.h>
 
int binsearch(int ar[], int j, int left, int right) {
    if (left <= right) {
        int mid = (left + right) / 2;
        
        if (ar[mid] == j) {
            return mid; // Element found
        }
        if (ar[mid] > j) {
            return binsearch(ar, j, left, mid - 1); // Search in the left half
        }
        return binsearch(ar, j, mid + 1, right); // Search in the right half
    }
    return -1; // Element not found
}
 
int main() {
    int ar[10], i, j, search;
 
    printf("Enter 10 sorted elements in the array:\n");
    for (i = 0; i < 10; i++) {
        scanf("%d", &ar[i]);
    }
 
    printf("Entered elements in the array: ");
    for (i = 0; i < 10; i++) {
        printf("%d ", ar[i]);
    }
    printf("\n");
 
    printf("Enter the element you want to find in the array: ");
    scanf("%d", &j);
 
    search = binsearch(ar, j, 0, 9);
    if (search == -1) {
        printf("Element not found.\n");
    } else {
        printf("Element found at position: %d\n", search + 1);
    }
 
    return 0;
}