# Unit 3

## 1) Define: Principle of Optimality.

The **Principle of Optimality** is a foundational concept in dynamic programming and optimal control theory. It states that an optimal solution to any instance of an optimization problem is composed of optimal solutions to its subproblems. In other words, if you have a problem that can be broken down into smaller, overlapping subproblems, the best way to solve the overall problem is to solve each of the subproblems optimally.

### Key Points of the Principle of Optimality:

1. **Optimal Substructure**: The principle implies that the problem exhibits an optimal substructure, meaning that the solution to the problem can be constructed from solutions to its subproblems.

2. **Recursive Nature**: This principle often leads to recursive formulations where the solution to a larger problem depends on solutions to smaller instances of the same problem.

3. **Dynamic Programming**: The principle is crucial for dynamic programming algorithms, which store the results of subproblems to avoid redundant calculations and thus improve efficiency.

### Example

Consider a shortest path problem in a weighted graph. If you find the shortest path from vertex A to vertex C through vertex B, then both the path from A to B and from B to C must also be the shortest paths. If either of these paths is not optimal, then the overall path from A to C cannot be optimal either.

### Conclusion

The Principle of Optimality is essential for designing algorithms that solve complex problems efficiently by leveraging optimal solutions of their subproblems, forming the basis for many dynamic programming approaches.

## 2) Explain the terms: Optimal Substructure property

### Optimal Substructure Property

The **Optimal Substructure Property** is a key characteristic of certain optimization problems, particularly those that can be solved using dynamic programming or greedy algorithms. This property indicates that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

#### Key Characteristics

1. **Decomposability**:

   - The problem can be broken down into smaller, simpler subproblems. The optimal solution to the overall problem depends on the optimal solutions to these subproblems.

2. **Recursive Structure**:

   - The solution can often be expressed recursively. If you know the optimal solutions for smaller instances of the problem, you can combine them to find the optimal solution for the larger instance.

3. **Examples in Algorithms**:
   - Many classical algorithms exhibit this property, such as:
     - **Shortest Path Problems** (e.g., Dijkstra’s and Bellman-Ford algorithms): The shortest path from a source to a destination can be found by considering the shortest paths to intermediate vertices.
     - **Knapsack Problem**: In the 0/1 knapsack problem, the maximum profit for a given weight capacity can be determined by considering whether to include each item and then solving for the remaining capacity.
     - **Dynamic Programming Problems**: Problems like Fibonacci sequence calculation, matrix chain multiplication, and others leverage this property to build solutions incrementally.

#### Example

Consider the **Fibonacci sequence** defined as follows:

$$
F(n) = F(n-1) + F(n-2)
$$

- The optimal substructure here is evident because calculating $$ F(n) $$ requires knowing $$ F(n-1) $$ and $$ F(n-2) $$. If we know the optimal solutions for $$ F(n-1) $$ and $$ F(n-2) $$, we can derive the optimal solution for $$ F(n) $$.

### Conclusion

The Optimal Substructure Property is fundamental in algorithm design, particularly in dynamic programming and greedy algorithms. It allows complex problems to be solved efficiently by breaking them down into simpler subproblems whose solutions can be reused, thus ensuring that we do not compute the same results multiple times. This property is essential for achieving optimality in various computational problems.

## 3) Explain common characteristics of dynamic programming.

Dynamic programming is a powerful algorithmic technique used to solve optimization problems by breaking them down into simpler subproblems. Here are some common characteristics of dynamic programming:

### 1. **Optimal Substructure**

Dynamic programming problems exhibit the optimal substructure property, meaning that an optimal solution to the problem can be constructed from optimal solutions to its subproblems. This allows the problem to be solved recursively.

### 2. **Overlapping Subproblems**

Dynamic programming is particularly effective for problems that have overlapping subproblems, where the same subproblems are solved multiple times. Instead of solving these subproblems repeatedly, dynamic programming stores their results (memoization) to avoid redundant calculations.

### 3. **Bottom-Up Approach**

Dynamic programming often employs a bottom-up approach, where solutions to smaller subproblems are computed first and used to build up solutions to larger problems. This is typically implemented using iterative methods and tabulation.

### 4. **Top-Down Approach**

Alternatively, dynamic programming can also be implemented using a top-down approach with recursion and memoization. In this method, the algorithm starts solving the problem from the top level and breaks it down into smaller subproblems, storing their results for future reference.

### 5. **State Representation**

In dynamic programming, the state of the problem is defined by parameters that capture the current situation of the problem (e.g., indices in an array). The choice of state representation is crucial for efficiently solving the problem.

### 6. **Transition Function**

Dynamic programming involves defining a transition function that describes how to move from one state to another. This function typically expresses how the solution to a larger problem can be derived from solutions to smaller subproblems.

### 7. **Space and Time Complexity**

Dynamic programming algorithms often trade space for time efficiency. While they may require additional memory to store intermediate results (especially in memoization), they significantly reduce the time complexity compared to naive recursive approaches.

### Conclusion

Dynamic programming is a versatile technique applicable to various problems, including those in optimization, combinatorial problems, and decision-making processes. Its characteristics make it an essential tool in algorithm design and analysis, enabling efficient solutions to complex problems by leveraging optimal substructures and overlapping subproblems.

## 4) What is the Principle of Optimality? Explain its use in Dynamic Programming Method.

### Principle of Optimality

The **Principle of Optimality** is a fundamental concept in dynamic programming and optimization theory. It states that an optimal solution to any instance of an optimization problem is composed of optimal solutions to its subproblems. In essence, if you have a problem that can be broken down into smaller subproblems, the best way to solve the overall problem is to solve each of the subproblems optimally.

### Explanation of the Principle

1. **Optimal Substructure**: The principle implies that the problem exhibits an optimal substructure, meaning that the solution to the problem can be constructed from solutions to its subproblems.

2. **Recursive Nature**: This principle often leads to recursive formulations where the solution to a larger problem depends on solutions to smaller instances of the same problem.

3. **Example**: Consider a shortest path problem in a weighted graph. If you find the shortest path from vertex A to vertex C through vertex B, then both the path from A to B and from B to C must also be the shortest paths. If either of these paths is not optimal, then the overall path from A to C cannot be optimal either.

### Use in Dynamic Programming

In dynamic programming, the Principle of Optimality is employed in several ways:

1. **Problem Decomposition**: Dynamic programming problems are typically decomposed into smaller subproblems, which can be solved independently. The results of these subproblems are stored and reused, which avoids redundant computations.

2. **Recursive Formulation**: The principle allows for a recursive formulation of problems. By defining a recursive relation that expresses the solution in terms of its subproblems, dynamic programming algorithms can efficiently compute optimal solutions.

3. **Memoization and Tabulation**:

   - **Memoization**: In a top-down approach, dynamic programming uses memoization to store results of previously computed subproblems so that they do not need to be recomputed.
   - **Tabulation**: In a bottom-up approach, dynamic programming builds a table (or array) that stores solutions to all subproblems, allowing for efficient computation of larger problems based on previously computed values.

4. **Examples in Algorithms**: Many classical algorithms utilize the Principle of Optimality:
   - **Fibonacci Sequence**: The optimal solution for $$ F(n) $$ can be derived from $$ F(n-1) $$ and $$ F(n-2) $$.
   - **Knapsack Problem**: The maximum profit for a given weight capacity can be determined by considering whether to include each item and then solving for the remaining capacity.
   - **Shortest Path Algorithms** (e.g., Bellman-Ford): The shortest path from a source vertex can be computed by combining optimal paths through intermediate vertices.

### Conclusion

The Principle of Optimality is crucial for dynamic programming as it underpins the methodology used to solve complex optimization problems efficiently. By ensuring that optimal solutions are built from optimal subsolutions, dynamic programming provides a systematic approach to tackling problems that would otherwise require exponential time if solved using naive recursive methods.

## 5) Compare Dynamic Programming Technique with Greedy Algorithms.

### Comparison of Dynamic Programming Technique with Greedy Algorithms

Dynamic programming and greedy algorithms are both algorithmic techniques used for solving optimization problems, but they differ significantly in their approach and applicability. Here’s a comparison of the two:

| Feature                       | Dynamic Programming                                                                                                                         | Greedy Algorithms                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach**                  | Solves problems by breaking them down into smaller subproblems and solving each one optimally. It considers all possible solutions.         | Makes a series of choices, each of which looks best at the moment (locally optimal), without considering the global consequences.       |
| **Optimality**                | Guarantees an optimal solution by considering all possible configurations and storing results of subproblems (optimal substructure).        | Does not guarantee an optimal solution for all problems; works well for specific problems where local choices lead to a global optimum. |
| **Problem Structure**         | Suitable for problems with overlapping subproblems and optimal substructure (e.g., Fibonacci sequence, knapsack problem).                   | Suitable for problems where local optimal choices lead to a global optimum (e.g., activity selection, Huffman coding).                  |
| **Efficiency**                | Generally more computationally intensive due to the need to explore all subproblems; may require more memory to store intermediate results. | Typically faster due to fewer computations; often runs in linear or logarithmic time.                                                   |
| **Implementation Complexity** | More complex to implement due to the need for recursion or iterative solutions and maintaining state information.                           | Simpler and easier to implement due to straightforward decision-making process.                                                         |
| **Use Cases**                 | Used in problems like shortest path (Bellman-Ford), matrix chain multiplication, and 0/1 knapsack.                                          | Used in problems like minimum spanning tree (Kruskal’s and Prim’s), job scheduling, and coin change (greedy version).                   |

### Summary

In summary, dynamic programming is a more comprehensive approach that guarantees optimal solutions by considering all possible configurations, while greedy algorithms focus on making local optimal choices with the hope that they will lead to a global optimum. The choice between using dynamic programming or greedy algorithms depends on the specific problem being addressed and its characteristics.

## 6) Explain the difference between divide and conquer method and dynamic programming.

### Difference Between Divide and Conquer Method and Dynamic Programming

Both **Divide and Conquer** and **Dynamic Programming** are algorithmic techniques used to solve complex problems by breaking them down into simpler subproblems. However, they differ significantly in their approach, structure, and application.

| Feature                       | Divide and Conquer                                                                                                                              | Dynamic Programming                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Approach**                  | Divides the problem into smaller subproblems, solves each subproblem independently, and combines their solutions to solve the original problem. | Breaks the problem into overlapping subproblems, solves each one optimally, and stores results to avoid redundant computations. |
| **Problem Structure**         | Suitable for problems that can be divided into independent subproblems (e.g., merge sort, quicksort, binary search).                            | Suitable for problems with overlapping subproblems and optimal substructure (e.g., Fibonacci sequence, knapsack problem).       |
| **Subproblem Independence**   | The subproblems are independent of each other; solving one does not affect the others.                                                          | The subproblems may overlap; the solution to one subproblem may depend on solutions to other subproblems.                       |
| **Efficiency**                | Generally efficient for problems with a logarithmic depth of recursion; may not always guarantee optimal solutions.                             | More computationally intensive due to storing results of subproblems but guarantees optimal solutions when applicable.          |
| **Implementation Complexity** | Often simpler to implement due to straightforward recursive structure.                                                                          | More complex due to the need for memoization or tabulation to store intermediate results.                                       |
| **Examples**                  | Merge Sort, Quick Sort, Binary Search, Strassen’s Matrix Multiplication.                                                                        | Fibonacci Sequence (using memoization), 0/1 Knapsack Problem, Longest Common Subsequence.                                       |

### Summary

In summary, while both techniques involve breaking down problems into smaller parts, **Divide and Conquer** focuses on independent subproblems and combines their results, whereas **Dynamic Programming** emphasizes solving overlapping subproblems optimally and storing their results for reuse. The choice between the two methods depends on the nature of the problem being solved.

## 7)What are the advantages of dynamic programming method over divide and conquer method?

Dynamic programming (DP) and divide and conquer (D&C) are both powerful algorithmic techniques, but dynamic programming has several advantages over divide and conquer in specific contexts. Here are the key advantages of dynamic programming:

### 1. **Optimal Solutions for Overlapping Subproblems**

Dynamic programming is particularly effective for problems with overlapping subproblems. In cases where the same subproblems are solved multiple times, DP stores the results of these computations (memoization) to avoid redundant calculations. This leads to significant time savings compared to divide and conquer, which may recompute the same subproblems multiple times.

### 2. **Guaranteed Optimality**

Dynamic programming guarantees an optimal solution for problems that exhibit optimal substructure and overlapping subproblems. This means that if a problem can be broken down into smaller problems whose optimal solutions contribute to the optimal solution of the larger problem, DP will find that optimal solution.

### 3. **Efficiency in Time Complexity**

For many problems, dynamic programming can reduce the time complexity significantly compared to divide and conquer. While D&C may lead to exponential time complexity due to repeated calculations, DP often achieves polynomial time complexity by storing intermediate results.

### 4. **Structured Approach**

Dynamic programming often provides a more structured approach to solving complex problems, as it systematically builds solutions from smaller subproblems. This structure can make it easier to understand and implement than some divide and conquer algorithms that may require more intricate merging of results.

### 5. **Applicability to a Wider Range of Problems**

Dynamic programming is applicable to a broader range of problems, especially those in optimization contexts, such as resource allocation, shortest paths in graphs, and sequence alignment in bioinformatics. While divide and conquer is effective for sorting and searching algorithms, its applicability is more limited.

### Conclusion

In summary, dynamic programming offers advantages in terms of efficiency, guaranteed optimality, and applicability to a wider range of problems compared to divide and conquer. It is particularly beneficial when dealing with overlapping subproblems where storing intermediate results can lead to significant performance improvements.

## 8) How to solve knapsack problem using dynamic programming?

To solve the **Knapsack Problem** using **dynamic programming**, we typically focus on the **0/1 Knapsack Problem**, where each item can either be included in the knapsack or excluded (not fractional). Here’s a step-by-step guide on how to approach it:

### Problem Definition

- You are given a set of items, each with a weight and a value.
- You have a knapsack with a maximum weight capacity.
- The goal is to maximize the total value of items in the knapsack without exceeding its weight capacity.

### Dynamic Programming Approach

1. **Define the Problem**:
   Let:

   - $$ n $$ = number of items
   - $$ W $$ = maximum weight capacity of the knapsack
   - $$ w[i] $$ = weight of item $$ i $$
   - $$ v[i] $$ = value of item $$ i $$

2. **Create a DP Table**:
   Create a 2D array (table) `dp` where:

   - `dp[i][j]` represents the maximum value that can be attained with the first $$ i $$ items and a maximum weight limit of $$ j $$.

3. **Initialize the Table**:

   - Set `dp[j] = 0` for all $$ j $$ (0 items means 0 value).
   - Set `dp[i] = 0` for all $$ i $$ (0 capacity means 0 value).

4. **Fill the DP Table**:
   Use nested loops to fill in the table based on the following logic:

   - If the weight of the current item $$ w[i-1] $$ is less than or equal to $$ j $$:
     - Include the item: `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])`
     - Exclude the item: `dp[i][j] = dp[i-1][j]`
   - If the weight of the current item is greater than $$ j $$:
     - Exclude it: `dp[i][j] = dp[i-1][j]`

5. **Extract the Result**:
   The maximum value that can be attained with all items and full capacity will be found in `dp[n][W]`.

### Pseudocode

```plaintext
function knapsack(w, v, W):
    n = length(w)
    dp = array[n+1][W+1]

    // Initialize DP table
    for i from 0 to n:
        for j from 0 to W:
            if i == 0 or j == 0:
                dp[i][j] = 0

    // Fill DP table
    for i from 1 to n:
        for j from 1 to W:
            if w[i-1] <= j: // If current item can be included
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
            else: // If current item cannot be included
                dp[i][j] = dp[i-1][j]

    return dp[n][W]
```

### Example

Consider an example with weights and values:

- Weights: $$ w = [4, 5, 6, 3] $$
- Values: $$ v = [10, 15, 12, 8] $$
- Maximum Capacity: $$ W = 10 $$

Using the above method, you would fill out your DP table and find that the maximum profit attainable without exceeding the weight capacity is at `dp[n][W]`.

### Time Complexity

The time complexity of this dynamic programming solution is:

$$
O(nW)
$$

Where $$ n $$ is the number of items and $$ W $$ is the maximum weight capacity. The space complexity is also $$ O(nW) $$, but it can be optimized to $$ O(W) $$ by using a single-dimensional array.

### Conclusion

Dynamic programming provides an efficient way to solve the Knapsack Problem by systematically exploring possible combinations of items while storing intermediate results to avoid redundant calculations. This method guarantees finding an optimal solution for the 0/1 Knapsack Problem.

## 9) Explain Chained Matrix Multiplication with example.

### Chained Matrix Multiplication

**Chained Matrix Multiplication** is a problem in computer science that involves determining the most efficient way to multiply a sequence of matrices. The goal is to minimize the total number of scalar multiplications needed to compute the product of the matrices.

### Problem Definition

Given a chain of matrices $$ A*1, A_2, \ldots, A_n $$, where matrix $$ A_i $$ has dimensions $$ p*{i-1} \times p_i $$, the objective is to find the optimal order of multiplication that minimizes the computational cost.

### Matrix Dimensions

If we have matrices $$ A_1, A_2, \ldots, A_n $$ with dimensions:

- $$ A_1: p_0 \times p_1 $$
- $$ A_2: p_1 \times p_2 $$
- $$ A_3: p_2 \times p_3 $$
- ...
- $$ A*n: p*{n-1} \times p_n $$

The cost of multiplying two matrices $$ A*i (p*{i-1} \times p*i) $$ and $$ A_j (p*{j-1} \times p_j) $$ is given by:

$$
\text{Cost}(A_i, A_j) = p_{i-1} \times p_i \times p_j
$$

### Dynamic Programming Approach

To solve the Chained Matrix Multiplication problem using dynamic programming, we follow these steps:

1. **Define the Cost Table**:
   Create a 2D array `m` where `m[i][j]` represents the minimum number of scalar multiplications needed to compute the product of matrices from $$ A_i $$ to $$ A_j $$.

2. **Initialization**:
   Set `m[i][i] = 0` for all $$ i $$ (the cost of multiplying one matrix is zero).

3. **Compute Costs**:
   For chains of increasing length, compute the minimum cost for multiplying matrices from $$ i $$ to $$ j $$:

   - For each possible split point $$ k $$:
     - Calculate the cost as:
       $$
       m[i][j] = \min(m[i][k] + m[k+1][j] + p_{i-1} \times p_k \times p_j)
       $$

4. **Result**:
   The minimum cost for multiplying all matrices will be found in `m[1][n]`.

### Example

Consider three matrices with dimensions:

- $$ A_1: 10 \times 30 $$
- $$ A_2: 30 \times 5 $$
- $$ A_3: 5 \times 60 $$

The dimensions array will be:
$$ p = [10, 30, 5, 60] $$

#### Step-by-Step Calculation

1. **Matrix Dimensions**:

   - $$ A_1: 10 \times 30$$
   - $$ A_2: 30 \times 5$$
   - $$ A_3: 5 \times 60$$

2. **Cost Table Initialization**:

   - `m[1][1] = 0`
   - `m[2][2] = 0`
   - `m = 0`

3. **Compute Costs**:

   For chains of length 2:

   - For $$ m[1][2] = m[1][1] + m[2][2] + (10 _ 30 _ 5) = 0 + 0 + 1500 = 1500$$
   - For $$ m[2] = m[2][2] + m + (30 _ 5 _ 60) = 0 + 0 + 9000 = 9000$$

   For chain length 3:

   - For $$ m[1] = min(m[1][1] + m[2] + (10 _ 30 _ 60), m[1][2] + m + (10 _ 5 _ 60))$$
     - First split at k=1:
       - Cost = $$ m[1][1] + m[2] + (10 _ 30 _ 60) = 0 + 9000 + 18000 = 27000$$
     - Second split at k=2:
       - Cost = $$ m[1][2] + m + (10 _ 5 _ 60) = 1500 + 0 +3000 =4500$$

The minimum cost for multiplying all three matrices is:

$$
m[1] = min(27000,4500) = **4500**
$$

### Conclusion

The Chained Matrix Multiplication problem can be efficiently solved using dynamic programming by systematically calculating and storing intermediate results. This approach minimizes the total number of scalar multiplications required to compute the product of a chain of matrices.

## 10) Give optimal substructure for make change problem. Consider an instance of such a problem with coins 1, 4 and 6 units. Illustrate its solutions using a dynamic programming approach involving a payment of 8 units or less.

### Optimal Substructure for the Make Change Problem

The **Make Change Problem** involves determining the minimum number of coins needed to make a certain amount of money using a given set of coin denominations. The problem has an optimal substructure, meaning that the optimal solution to the problem can be constructed from optimal solutions to its subproblems.

#### Optimal Substructure Explanation

For a given amount $$ n $$ and a set of coin denominations $$ C = \{c_1, c_2, \ldots, c_k\} $$:

1. If we want to make change for an amount $$ n $$, we can consider using one of the coins $$ c_i $$ (where $$ c_i $$ is one of the denominations).
2. If we use coin $$ c_i $$, the remaining amount to make change for is $$ n - c_i $$.
3. Thus, the problem can be broken down into subproblems:
   - The optimal solution for making change for $$ n $$ is equal to 1 (for using coin $$ c_i $$) plus the optimal solution for making change for $$ n - c_i $$.

This leads to the recurrence relation:

$$
\text{minCoins}(n) = 1 + \min(\text{minCoins}(n - c_1), \text{minCoins}(n - c_2), \ldots, \text{minCoins}(n - c_k))
$$

where $$ n - c_i \geq 0 $$.

### Example: Coin Denominations {1, 4, 6} and Amounts Up to 8

Let’s illustrate this with coin denominations of 1, 4, and 6 units and find the minimum number of coins needed for amounts from 0 to 8.

#### Step-by-Step Dynamic Programming Approach

1. **Define the DP Array**:
   Create an array `minCoins` where `minCoins[i]` represents the minimum number of coins needed to make change for amount $$ i $$.

2. **Initialize the Array**:
   Set `minCoins = 0` (zero coins are needed to make zero amount) and initialize all other entries to infinity (or a large number).

3. **Fill the DP Array**:
   For each amount from 1 to 8, calculate the minimum coins required using the available denominations.

#### Dynamic Programming Table Calculation

- **Coin Denominations**: {1, 4, 6}
- **Target Amounts**: From 0 to 8

| Amount | minCoins Value | Calculation                                            |
| ------ | -------------- | ------------------------------------------------------ |
| 0      | 0              | (Base case)                                            |
| 1      | 1              | minCoins(1-1) + 1 = minCoins(0) + 1 = **1**            |
| 2      | 2              | minCoins(2-1) + 1 = minCoins(1) + 1 = **2**            |
| 3      | 3              | minCoins(3-1) + 1 = minCoins(2) + 1 = **3**            |
| 4      | 1              | minCoins(4-4) + 1 = minCoins(0) + 1 = **1**            |
| 5      | 2              | minCoins(5-4) + 1 = minCoins(1) + 1 = **2**            |
| 6      | 1              | minCoins(6-6) + 1 = minCoins(0) + 1 = **1**            |
| 7      | 2              | minCoins(7-6) + 1 = minCoins(1) + 1 = **2**            |
| 8      | 2              | min(minCoins(8-6)+1, minCoins(8-4)+1, minCoins(8-1)+1) |

### Final Results

After filling out the table:

- For each amount from **0 to 8**, we have calculated the minimum number of coins required:
  - Amount **0**: **0 coins**
  - Amount **1**: **1 coin**
  - Amount **2**: **2 coins**
  - Amount **3**: **3 coins**
  - Amount **4**: **1 coin**
  - Amount **5**: **2 coins**
  - Amount **6**: **1 coin**
  - Amount **7**: **2 coins**
  - Amount **8**: **2 coins**

### Conclusion

The dynamic programming approach effectively utilizes the optimal substructure property of the Make Change Problem. By systematically calculating and storing results for each subproblem (amount), we can efficiently determine the minimum number of coins needed for any target amount up to a specified limit. This method ensures that we do not recompute values unnecessarily and guarantees an optimal solution.

## 11) Solve Making Change problem using Dynamic Programming. (Denominations: d1=1, d2=4, d3=6). Give your answer for making change of Rs. 9.

To solve the **Making Change Problem** using **Dynamic Programming** with the given denominations $$ d_1 = 1 $$, $$ d_2 = 4 $$, and $$ d_3 = 6 $$, we will determine the minimum number of coins needed to make change for Rs. 9.

### Problem Definition

- **Denominations**: {1, 4, 6}
- **Target Amount**: 9

### Dynamic Programming Approach

1. **Define the DP Array**:
   Create an array `minCoins` where `minCoins[i]` represents the minimum number of coins needed to make change for amount $$ i $$.

2. **Initialize the Array**:

   - Set `minCoins = 0` (zero coins are needed to make zero amount).
   - Initialize all other entries to infinity (or a large number) since initially, we don't know how to make those amounts.

3. **Fill the DP Array**:
   For each amount from 1 to 9, calculate the minimum coins required using the available denominations.

### Step-by-Step Calculation

#### Initialize the DP Array

```plaintext
Target Amount: 9
Denominations: 1, 4, 6

minCoins = [0, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]
```

#### Fill the DP Array

We will iterate through each amount and update the `minCoins` array based on the available denominations.

1. For each amount $$ i $$ from 1 to 9:
   - For each denomination $$ d $$:
     - If $$ d $$ is less than or equal to $$ i $$:
       - Update `minCoins[i]` as follows:
         $$
         minCoins[i] = \min(minCoins[i], minCoins[i - d] + 1)
         $$

#### Iteration Details

| Amount (i) | Denomination (d) | Calculation                               | minCoins[i] |
| ---------- | ---------------- | ----------------------------------------- | ----------- |
| 1          | 1                | minCoins[1] = min(∞, minCoins + 1) = 1    | 1           |
| 2          | 1                | minCoins[2] = min(∞, minCoins[1] + 1) = 2 | 2           |
|            | 4                | Not applicable                            |             |
|            | 6                | Not applicable                            |             |
| 3          | 1                | minCoins = min(∞, minCoins[2] + 1) = 3    | 3           |
|            | 4                | Not applicable                            |             |
|            | 6                | Not applicable                            |             |
| 4          | 1                | minCoins = min(∞, minCoins + 1) = 4       | 4           |
|            | 4                | minCoins = min(4, minCoins + 1) = **1**   | **1**       |
|            | 6                | Not applicable                            |             |
| 5          | 1                | minCoins = min(∞, minCoins + 1) = **2**   | **2**       |
|            | 4                | Not applicable                            |             |
|            | 6                | Not applicable                            |             |
| 6          | 1                | minCoins = min(∞, minCoins + 1) = **3**   | **3**       |
|            | 4                | Not applicable                            |             |
|            | 6                | minCoins = min(3, minCoins + 1) = **1**   | **1**       |
| 7          | 1                | minCoins = min(∞, minCoins + 1) = **2**   | **2**       |
|            | 4                | Not applicable                            |             |
|            | 6                | Not applicable                            |             |
| 8          | 1                | minCoins = min(∞, minCoins + 1) = **3**   | **3**       |
|            | 4                | Not applicable                            |             |
|            | 6                | Not applicable                            |             |
| **9**      | **1**            | **minCoins = min(∞, minCoins+1)**= **4**  |             |
|            |                  |                                           |             |

### Final Results

After filling out the table up to amount Rs. $$9$$:

- The minimum number of coins needed to make change for Rs. $$9$$ is found in `minCoins`, which is:

$$
\text{minCoins} = \text{4}
$$

### Conclusion

Using dynamic programming for the Making Change Problem with denominations of {1, 4, and 6}, we find that a total of **4 coins** are needed to make change for Rs. **9**. The approach effectively utilizes previously computed results to build up solutions for larger amounts efficiently.

## 12) Given coins of denominations 1, 3 and 4 with the amount to be pay is 7. Find optimal no. Of coins and sequence of coins used to pay a given amount using a dynamic method.

To solve the coin change problem using dynamic programming, we need to determine the optimal number of coins needed to make a specific amount (in this case, 7) using coins of denominations 1, 3, and 4. We will also identify the sequence of coins used.

### Dynamic Programming Approach

#### Problem Definition

We are given:

- Coin denominations: $$ \{1, 3, 4\} $$
- Target amount: $$ 7 $$

#### Steps to Solve

1. **Initialization**:

   - Create an array `dp` where `dp[i]` will store the minimum number of coins needed to make the amount $$ i $$.
   - Initialize `dp = 0` (0 coins are needed to make the amount 0) and set all other entries to infinity (or a large number) initially.

2. **Filling the DP Table**:

   - For each coin in our denominations, iterate through all amounts from that coin value up to the target amount (7).
   - Update `dp[j]` as follows:
     $$
     dp[j] = \min(dp[j], dp[j - \text{coin}] + 1)
     $$
     This means we take the minimum between the current value of `dp[j]` and the value obtained by using one more coin of the current denomination.

3. **Backtracking to Find Coin Sequence**:
   - After filling the `dp` array, if `dp` is still infinity, it means that it is not possible to form that amount with the given coins.
   - Otherwise, backtrack through the `dp` array to find which coins were used.

#### Implementation

Here’s a Python implementation of this approach:

```python
def coin_change(coins, amount):
    # Initialize dp array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Fill dp array
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If no combination can form the amount
    if dp[amount] == float('inf'):
        return None, []

    # Backtrack to find the coins used
    result = []
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result.append(coin)
                amount -= coin
                break

    return dp[-1], result

# Example usage
coins = [1, 3, 4]
amount = 7
min_coins, sequence_of_coins = coin_change(coins, amount)
print(f"Minimum number of coins: {min_coins}")
print(f"Sequence of coins used: {sequence_of_coins}")
```

#### Output Explanation

When you run this code with the provided denominations and target amount:

- **Minimum number of coins**: The output will indicate how many coins are needed.
- **Sequence of coins used**: It will display which specific coins were used to achieve that total.

#### Conclusion

Using dynamic programming allows us to efficiently compute both the minimum number of coins required and the specific combination of those coins for any given target amount. In this example with an amount of 7 using denominations of 1, 3, and 4, you can find that the optimal solution uses two coins: one coin of denomination 3 and one coin of denomination 4.
