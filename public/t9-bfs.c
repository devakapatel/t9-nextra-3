#include <stdio.h>
 
int a[20][20], q[20], visited[20], n, i, j, f = 0, r = -1;
 
// Function to perform BFS
void bfs(int v) {
    for (i = 1; i <= n; i++) {
        if (a[v][i] && !visited[i]) {
            q[++r] = i; // Add to queue
        }
    }
    if (f <= r) {
        visited[q[f]] = 1; // Mark as visited
        bfs(q[f++]); // Recursive call for the next vertex
    }
}
 
int main() {
    int v;
    printf("\nEnter the number of vertices: ");
    scanf("%d", &n);
 
    // Initialize queue and visited arrays
    for (i = 1; i <= n; i++) {
        q[i] = 0;
        visited[i] = 0;
    }
 
    printf("\nEnter graph data in matrix form:\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &a[i][j]); // Input adjacency matrix
        }
    }
 
    printf("\nEnter the starting vertex: ");
    scanf("%d", &v);
    
    // Start BFS from the specified vertex
    bfs(v);
 
    printf("\nThe nodes which are reachable are:\n");
    for (i = 1; i <= n; i++) {
        if (visited[i]) {
            printf("%d\t", i);
        } else {
            printf("\nBFS is not possible. Not all nodes are reachable.");
            break; // Exit loop if not all nodes are reachable
        }
    }
 
    return 0;
}