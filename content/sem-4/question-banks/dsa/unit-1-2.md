# Unit 1 & 2

## 1) Define primitive and non-primitive data types with example.

In the context of data structures, data types can be categorized into two main categories: primitive and non-primitive data types.

### Primitive Data Types

Primitive data types are the fundamental data types that are supported by a programming language. These data types are built-in and are used to store simple data such as numbers, characters, and booleans. Examples of primitive data types include:

- **Integers**: Whole numbers, such as 1, 2, 3, etc.
- **Floats**: Decimal numbers, such as 3.14 or -0.5.
- **Characters**: Single characters, such as 'a', 'b', 'c', etc.
- **Booleans**: Logical values, such as true or false.

### Non-Primitive Data Types

Non-primitive data types are those data structures that are created using primitive data types. These data structures can be further classified into two categories: linear and non-linear data structures.

- **Linear Data Structures**: These data structures store elements in a linear or sequential order. Examples include arrays, linked lists, stacks, and queues.
- **Non-Linear Data Structures**: These data structures do not store elements in a linear order. Examples include trees and graphs.

For example, an array is a non-primitive data type because it is created using primitive data types like integers. An array can store multiple integers, which are stored in consecutive memory locations. On the other hand, a linked list is also a non-primitive data type because it is created using primitive data types like integers and characters. A linked list stores elements in a linear order, but each element is stored in a separate block of memory, which is linked to the next element through a pointer.

In summary, primitive data types are the fundamental data types supported by a programming language, while non-primitive data types are created using these primitive data types and can be further categorized into linear and non-linear data structures.

## 2) Define Data Structure and differentiate between linear and nonlinear data structures.

A data structure is a way of organizing and storing data in a computer's memory so that it can be accessed and modified efficiently. It defines the relationship between data elements and determines how information is stored, retrieved, and modified.

Data structures can be classified into two main categories: linear and non-linear data structures.

### Linear Data Structures

Linear data structures maintain a linear relationship among their elements. The data is arranged in a sequential or linear fashion, although the arrangement may not be sequential in memory. Examples of linear data structures include:

- Arrays
- Linked lists
- Stacks
- Queues

In linear data structures, the elements are stored in a specific order, and the insertion and deletion of elements can be done at the beginning, end, or middle of the structure.

### Non-Linear Data Structures

Non-linear data structures do not maintain a linear relationship among their elements. Instead, they have a hierarchical or tree-like structure. The elements are not arranged in a sequential order, and the insertion and deletion of elements cannot be done in a linear fashion. Examples of non-linear data structures include:

- Trees
- Graphs

In non-linear data structures, the elements are organized in a more complex way, and the relationships between elements are not limited to a linear order. This allows for more efficient storage and retrieval of data in certain applications.

In summary, the main difference between linear and non-linear data structures is the way the elements are organized and the relationships between them. Linear data structures maintain a sequential order, while non-linear data structures have a more complex, hierarchical structure.

## 3) Write recursive algorithm to compute factorial of a given number. Which data structure can be used to implement this algorithm?

Here is a recursive algorithm to compute the factorial of a given number:

```
factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

```

The algorithm works as follows:

1. If the input number `n` is 0, return 1 (by definition, 0! = 1).
2. Otherwise, return the product of `n` and the factorial of `n-1` (using recursion).

For example, to compute `factorial(5)`:

```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 5 * 4 * 3 * 2 * 1 * 1
= 120

```

To implement this recursive algorithm, we can use a stack data structure. A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It is well-suited for implementing recursive algorithms because it allows us to keep track of the function calls and their return values.

Here's how we can use a stack to implement the factorial algorithm:

1. Push the initial value of `n` onto the stack.
2. While the top of the stack is not 0:
   - Pop the top value from the stack and multiply it with the result so far.
   - Decrement the popped value by 1 and push it back onto the stack.
3. Return the final result.

For example, to compute `factorial(5)` using a stack:

1. Push 5 onto the stack.
2. Pop 5, multiply with result (initially 1), and push 4 onto the stack.
3. Pop 4, multiply with result (5), and push 3 onto the stack.
4. Pop 3, multiply with result (20), and push 2 onto the stack.
5. Pop 2, multiply with result (60), and push 1 onto the stack.
6. Pop 1, multiply with result (120), and push 0 onto the stack.
7. Pop 0, return the result (120).

By using a stack data structure, we can efficiently implement the recursive factorial algorithm without the need for explicit recursion. The stack keeps track of the function calls and their return values, allowing us to compute the factorial iteratively.

## 4) What is Recursion? Write a pseudocode in ‘C’ language to find the multiplication of two natural numbers.

Recursion is a programming technique where a function calls itself to solve a problem. The function continues to call itself with a smaller version of the problem until it reaches a base case, at which point the function starts returning the results back up the call stack.

Here's a pseudocode in 'C' language to find the multiplication of two natural numbers using recursion:

```
int multiply(int a, int b) {
    // Base case
    if (b == 0) {
        return 0;
    }

    // Recursive case
    return a + multiply(a, b - 1);
}

int main() {
    int num1 = 5;
    int num2 = 3;
    int result = multiply(num1, num2);

    printf("The multiplication of %d and %d is %d", num1, num2, result);

    return 0;
}

```

Explanation:

1. The `multiply` function takes two integer parameters, `a` and `b`, representing the two numbers to be multiplied.
2. The base case is when `b` is 0, in which case the function returns 0, as anything multiplied by 0 is 0.
3. In the recursive case, the function calls itself with `a` and `b - 1` as the arguments. This effectively reduces the second number by 1 in each recursive call.
4. The function adds `a` to the result of the recursive call, which accumulates the product of the two numbers.
5. In the `main` function, we call the `multiply` function with the numbers 5 and 3, and store the result in the `result` variable.
6. Finally, we print the result.

The logic behind this recursive approach is that multiplying `a` by `b` is the same as adding `a` to itself `b` times. By recursively subtracting 1 from `b` and adding `a` to the result, we can compute the multiplication of `a` and `b`.

## 5) Describe: (1) Recursion (2) Priority Queue (3) Tower of Hanoi

1. Recursion:
   - Recursion is a programming technique where a function calls itself to solve a problem.
   - The function continues to call itself with a smaller version of the problem until it reaches a base case, at which point the function starts returning the results back up the call stack.
   - Recursive algorithms are often used to solve problems that can be broken down into smaller, similar subproblems.
2. Priority Queue:
   - A priority queue is a special type of queue where each element has a priority associated with it.
   - Elements are dequeued based on their priority, with the highest priority element being dequeued first, regardless of the order in which they were enqueued.
   - Priority queues are useful in scenarios where certain tasks or jobs need to be processed based on their importance or urgency, such as job scheduling, event handling, and graph algorithms like Dijkstra's shortest path algorithm.
3. Tower of Hanoi:
   - The Tower of Hanoi is a classic mathematical puzzle that involves moving a stack of disks from one peg to another, following a set of rules.
   - The rules are:
     1. Only one disk can be moved at a time.
     2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or an empty peg.
     3. No disk may be placed on top of a smaller disk.
   - The puzzle can be solved using a recursive algorithm, where the main problem is divided into smaller subproblems of moving a stack of disks from one peg to another.
   - The divide and conquer approach used in the Tower of Hanoi problem is an example of the advantages of the recursive technique mentioned in the provided sources.

## 6) Write algorithms for PUSH and POP stack operations.

Here are the algorithms for the PUSH and POP stack operations based on the information provided in the sources:

### Algorithm for PUSH Operation:

```
PUSH(STACK, TOP, MAX_SIZE, ITEM)
Begin
    if TOP = MAX_SIZE - 1 then
        Print "Stack Overflow"
    else
        TOP = TOP + 1
        STACK[TOP] = ITEM
        Print "Item pushed onto the stack"
    Endif
End

```

### Algorithm for POP Operation:

```
POP(STACK, TOP)
Begin
    if TOP = -1 then
        Print "Stack Underflow"
    else
        ITEM = STACK[TOP]
        TOP = TOP - 1
        Print "Item popped from the stack: ", ITEM
    Endif
End

```

These algorithms demonstrate the basic operations of a stack - PUSH and POP. The PUSH operation adds an item onto the top of the stack, while the POP operation removes and returns the top item from the stack. These operations are fundamental in managing a stack data structure, whether implemented using an array or a linked list, as described in the provided sources.

## 7) Write a pseudocode for PUSH and POP operations of stack.

Here is the pseudocode for the PUSH and POP operations on a stack:

### PUSH Operation

```
PUSH(STACK, TOP, MAX_SIZE, ITEM)
Begin
    if TOP = MAX_SIZE - 1 then
        Print "Stack Overflow"
    else
        TOP = TOP + 1
        STACK[TOP] = ITEM
        Print "Item pushed onto the stack"
    Endif
End

```

The steps for the PUSH operation are:

1. Check if the stack is full by comparing `TOP` with `MAX_SIZE - 1`. If `TOP` is equal to `MAX_SIZE - 1`, it means the stack is full, and we print "Stack Overflow".
2. If the stack is not full, increment `TOP` by 1 to point to the next available position in the stack.
3. Store the item to be pushed at the position pointed by `TOP` in the `STACK` array.
4. Print "Item pushed onto the stack" to indicate that the push operation was successful.

### POP Operation

```
POP(STACK, TOP)
Begin
    if TOP = -1 then
        Print "Stack Underflow"
    else
        ITEM = STACK[TOP]
        TOP = TOP - 1
        Print "Item popped from the stack: ", ITEM
    Endif
End

```

The steps for the POP operation are:

1. Check if the stack is empty by checking if `TOP` is equal to -1. If `TOP` is -1, it means the stack is empty, and we print "Stack Underflow".
2. If the stack is not empty, store the item at the position pointed by `TOP` in the `STACK` array into the variable `ITEM`.
3. Decrement `TOP` by 1 to point to the next available position in the stack.
4. Print "Item popped from the stack: " followed by the value of `ITEM` to indicate that the pop operation was successful.

These pseudocodes demonstrate the basic operations of pushing an item onto the stack and popping an item from the stack. The PUSH operation adds an item to the top of the stack, while the POP operation removes and returns the top item from the stack[1].

## 8) Evaluate the following postfix expression using stack. Show each step.

5 3 + 6 2 / _ 3 5 _ +

To evaluate the given postfix expression "5 3 + 6 2 / _ 3 5 _ +" using a stack, we can follow these steps:

Step 1: Initialize an empty stack.

Step 2: Scan the postfix expression from left to right.

Step 3: For each element in the expression:

- If the element is a number, push it onto the stack.
- If the element is an operator (+, -, \*, /), pop the top two elements from the stack, perform the operation, and push the result back onto the stack.

Let's go through the expression step-by-step:

1. Scan "5": Push 5 onto the stack.
   Stack:
2. Scan "3": Push 3 onto the stack.
   Stack:
3. Scan "+": Pop the top two elements (3 and 5), perform the addition (3 + 5 = 8), and push the result (8) onto the stack.
   Stack:
4. Scan "6": Push 6 onto the stack.
   Stack:
5. Scan "2": Push 2 onto the stack.
   Stack:
6. Scan "/": Pop the top two elements (2 and 6), perform the division (6 / 2 = 3), and push the result (3) onto the stack.
   Stack:
7. Scan "_": Pop the top two elements (3 and 8), perform the multiplication (8 _ 3 = 24), and push the result (24) onto the stack.
   Stack:
8. Scan "3": Push 3 onto the stack.
   Stack:
9. Scan "5": Push 5 onto the stack.
   Stack:
10. Scan "_": Pop the top two elements (5 and 3), perform the multiplication (3 _ 5 = 15), and push the result (15) onto the stack.
    Stack:
11. Scan "+": Pop the top two elements (15 and 24), perform the addition (24 + 15 = 39), and push the result (39) onto the stack.
    Stack:

The final result of the postfix expression evaluation is 39, which is the only element left on the stack.

## 9) Consider the stack S of characters, where S is allocated 8 memory cells. S: A,C,D, F, K, _, _, \_ Describe the stack as the following operations take place. Pop(), Pop() ,Push(L), Push(P), Pop(), Push(R), Push (S), Pop()

Let's describe the stack S after each operation:

1. Initially, the stack S is allocated 8 memory cells and contains the following characters:
   S: A, C, D, F, K, _, _, \_
2. Pop(): Removes the top element from the stack. The stack now becomes:
   S: A, C, D, F, _, _, _, _
3. Pop(): Removes the top element from the stack. The stack now becomes:
   S: A, C, D, _, _, _, _, \_
4. Push(L): Adds the character 'L' to the top of the stack. The stack now becomes:
   S: A, C, D, L, _, _, _, _
5. Push(P): Adds the character 'P' to the top of the stack. The stack now becomes:
   S: A, C, D, L, P, _, _, \_
6. Pop(): Removes the top element from the stack. The stack now becomes:
   S: A, C, D, L, _, _, _, _
7. Push(R): Adds the character 'R' to the top of the stack. The stack now becomes:
   S: A, C, D, L, R, _, _, \_
8. Push(S): Adds the character 'S' to the top of the stack. The stack now becomes:
   S: A, C, D, L, R, S, _, _
9. Pop(): Removes the top element from the stack. The stack now becomes:
   S: A, C, D, L, R, _, _, \_

After all the operations, the final state of the stack S is:
S: A, C, D, L, R, _, _, \_

## 10) Evaluate the Postfix Expression 6 2 3 + - 3 8 2 / + \* 2 - 3 + using Stack.

To evaluate the given postfix expression "6 2 3 + - 3 8 2 / + \* 2 - 3 +" using a stack, we can follow these steps:

1. Initialize an empty stack.
2. Scan the postfix expression from left to right.
3. For each element in the expression:
   - If the element is a number, push it onto the stack.
   - If the element is an operator, pop the top two elements from the stack, perform the operation, and push the result back onto the stack.

Let's go through the expression step-by-step:

1. Scan "6": Push 6 onto the stack.
   Stack: 6
2. Scan "2": Push 2 onto the stack.
   Stack: 6, 2
3. Scan "3": Push 3 onto the stack.
   Stack: 6, 2, 3
4. Scan "+": Pop 3 and 2, perform addition (2 + 3 = 5), push 5 onto the stack.
   Stack: 6, 5
5. Scan "-": Pop 5 and 6, perform subtraction (6 - 5 = 1), push 1 onto the stack.
   Stack: 1
6. Scan "3": Push 3 onto the stack.
   Stack: 1, 3
7. Scan "8": Push 8 onto the stack.
   Stack: 1, 3, 8
8. Scan "2": Push 2 onto the stack.
   Stack: 1, 3, 8, 2
9. Scan "/": Pop 2 and 8, perform division (8 / 2 = 4), push 4 onto the stack.
   Stack: 1, 3, 4
10. Scan "+": Pop 4 and 3, perform addition (3 + 4 = 7), push 7 onto the stack.
    Stack: 1, 7
11. Scan "_": Pop 7 and 1, perform multiplication (1 _ 7 = 7), push 7 onto the stack.
    Stack: 7
12. Scan "2": Push 2 onto the stack.
    Stack: 7, 2
13. Scan "-": Pop 2 and 7, perform subtraction (7 - 2 = 5), push 5 onto the stack.
    Stack: 5
14. Scan "3": Push 3 onto the stack.
    Stack: 5, 3
15. Scan "+": Pop 3 and 5, perform addition (5 + 3 = 8), push 8 onto the stack.
    Stack: 8

After evaluating the entire postfix expression, the final result is 8, which is the only element left on the stack.

## 11) Convert Infix Expression A ^ B \* C - D + E / F / (G + H) into Postfix expression using stack

To convert the given infix expression "A ^ B \* C - D + E / F / (G + H)" into a postfix expression using a stack, we can follow these steps:

1. Initialize an empty stack.
2. Scan the infix expression from left to right.
3. For each character in the expression:
   - If the character is an operand (A, B, C, D, E, F, G, H), append it to the postfix expression.
   - If the character is an opening parenthesis '(', push it onto the stack.
   - If the character is an operator (^, \*, -, /, +):
     - While the stack is not empty and the top of the stack has a higher or equal precedence than the current operator, pop the operator from the stack and append it to the postfix expression.
     - Push the current operator onto the stack.
   - If the character is a closing parenthesis ')', pop operators from the stack and append them to the postfix expression until an opening parenthesis '(' is encountered. Discard the opening parenthesis.
4. After scanning the entire infix expression, pop any remaining operators from the stack and append them to the postfix expression.

Applying these steps to the given infix expression, we get the following postfix expression:

A B ^ C \* D - E F / G H + / +

Here's the step-by-step process:

1. Scan "A": Append "A" to the postfix expression.
2. Scan "^": Push "^" onto the stack.
3. Scan "B": Append "B" to the postfix expression.
4. Scan "_": Pop "^" from the stack and append it to the postfix expression. Then, push "_" onto the stack.
5. Scan "C": Append "C" to the postfix expression.
6. Scan "-": Pop "\*" from the stack and append it to the postfix expression. Then, push "-" onto the stack.
7. Scan "D": Append "D" to the postfix expression.
8. Scan "+": Pop "-" from the stack and append it to the postfix expression. Then, push "+" onto the stack.
9. Scan "E": Append "E" to the postfix expression.
10. Scan "/": Pop "+" from the stack and append it to the postfix expression. Then, push "/" onto the stack.
11. Scan "F": Append "F" to the postfix expression.
12. Scan "/": Pop "/" from the stack and append it to the postfix expression. Then, push "/" onto the stack.
13. Scan "(": Push "(" onto the stack.
14. Scan "G": Append "G" to the postfix expression.
15. Scan "+": Append "+" to the postfix expression.
16. Scan "H": Append "H" to the postfix expression.
17. Scan ")": Pop operators from the stack and append them to the postfix expression until an opening parenthesis "(" is encountered. Discard the opening parenthesis.
18. After scanning the entire expression, pop any remaining operators from the stack and append them to the postfix expression.

The final postfix expression is: A B ^ C \* D - E F / G H + / +

## 12) Convert (A + B) _ C – D ^ E ^ (F _ G) infix expression into prefix format showing stack status after every step in tabular form.

To convert the given infix expression into prefix format, we will use the Shunting Yard Algorithm. The algorithm involves two stacks: an output stack for the prefix expression and an operator stack for operators. Here's a step-by-step breakdown:

| Infix Expression                  | Operator Stack | Output Stack                 |
| --------------------------------- | -------------- | ---------------------------- |
| ( A + B ) _ C - D ^ E ^ ( F _ G ) |                |                              |
| ( A + B ) _ C - D ^ E ^ F _ G )   | (              | (                            |
| A + B ) _ C - D ^ E ^ F _ G )     | \* (           | \* ( A                       |
| A + B ) _ C - D ^ E ^ F _ G )     | +              | \* + A B                     |
| A + B ) _ C - D ^ E ^ F _ G )     | )              | \* + A B                     |
| A + B _ C - D ^ E ^ F _ G )       | \*             | _ + A B _                    |
| A + B _ C - D ^ E ^ F _ G )       | -              | - _ + A B _ C                |
| A + B _ C D ^ E ^ F _ G )         | ^              | - _ + A B _ C ^ D            |
| A + B _ C D E ^ F _ G )           | ^              | - _ + A B _ C ^ D ^ E        |
| A + B _ C D E F _ G )             | \*             | - _ + A B _ C ^ D ^ E \* F   |
| A + B \* C D E F G )              | )              | - _ + A B _ C ^ D ^ E \* F G |

The final prefix expression is: - _ + A B _ C ^ D ^ E \* F G

Here's a breakdown of the algorithm:

1. Scan the infix expression from left to right.
2. If the current token is an operand, push it onto the output stack.
3. If the current token is a left parenthesis, push it onto the operator stack.
4. If the current token is a right parenthesis, pop operators from the operator stack and push them onto the output stack until the corresponding left parenthesis is encountered.
5. If the current token is an operator, compare its precedence with the top operator on the operator stack.
   a. If the current operator has higher precedence, push it onto the operator stack.
   b. If the current operator has lower precedence or equal precedence and is left-associative, pop operators from the operator stack and push them onto the output stack until an operator with higher precedence is encountered. Then push the current operator onto the operator stack.
   c. If the current operator has lower precedence or equal precedence and is right-associative, pop the top operator from the operator stack and push it onto the output stack. Then repeat step 5.
6. Repeat steps 2-5 until the infix expression is fully scanned.
7. Pop all remaining operators from the operator stack and push them onto the output stack.
8. The output stack now contains the prefix expression.

## 13) Write an algorithm to convert an infix expression to postfix expression. Show the working of the algorithm for the following expression. A + B _ C / D $ E - ( F _ G )

To convert an infix expression to a postfix expression, we can use the Shunting Yard Algorithm. Here's the algorithm:

1. Create an empty output stack and an empty operator stack.
2. Scan the infix expression from left to right.
3. If the current token is an operand, add it to the output stack.
4. If the current token is a left parenthesis, push it onto the operator stack.
5. If the current token is a right parenthesis, pop operators from the operator stack and add them to the output stack until the corresponding left parenthesis is encountered. Discard the left parenthesis.
6. If the current token is an operator, compare its precedence with the top operator on the operator stack.
   a. If the operator stack is empty or the current operator has higher precedence, push the current operator onto the operator stack.
   b. If the current operator has lower precedence or equal precedence and is left-associative, pop operators from the operator stack and add them to the output stack until an operator with higher precedence is encountered. Then push the current operator onto the operator stack.
   c. If the current operator has lower precedence or equal precedence and is right-associative, pop the top operator from the operator stack and add it to the output stack. Then repeat step 6.
7. Repeat steps 3-6 until the infix expression is fully scanned.
8. Pop all remaining operators from the operator stack and add them to the output stack.
9. The output stack now contains the postfix expression.

Here's the working of the algorithm for the given expression A + B \* C / D $ E - ( F \* G ):

| Infix Expression                | Operator Stack | Output Stack |
| ------------------------------- | -------------- | ------------ |
| A + B \* C / D $ E - ( F \* G ) |                |              |
| A + B \* C / D $ E - F \* G )   | (              |              |
| A + B \* C / D $ E - F \* G )   | \* (           |              |
| A + B \* C / D $ E - F G )      | )              |              |
| A + B \* C / D $ E - F G        | \*             |              |
| A + B \* C / D $ E - F G        | /              | \*           |
| A + B \* C D $ E - F G          | \$             | \* /         |
| A + B \* C D E - F G            | -              | \* / \$      |
| A + B \* C D E F G              | +              | \* / \$ -    |

The final postfix expression is: AB \* CD / \$ E - FG \* +

Here's a breakdown of the algorithm:

1. Scan the infix expression from left to right.
2. If the current token is an operand, add it to the output stack.
3. If the current token is a left parenthesis, push it onto the operator stack.
4. If the current token is a right parenthesis, pop operators from the operator stack and add them to the output stack until the corresponding left parenthesis is encountered. Discard the left parenthesis.
5. If the current token is an operator, compare its precedence with the top operator on the operator stack.
   a. If the operator stack is empty or the current operator has higher precedence, push the current operator onto the operator stack.
   b. If the current operator has lower precedence or equal precedence and is left-associative, pop operators from the operator stack and add them to the output stack until an operator with higher precedence is encountered. Then push the current operator onto the operator stack.
   c. If the current operator has lower precedence or equal precedence and is right-associative, pop the top operator from the operator stack and add it to the output stack. Then repeat step 5.
6. Repeat steps 2-5 until the infix expression is fully scanned.
7. Pop all remaining operators from the operator stack and add them to the output stack.
8. The output stack now contains the postfix expression.

## 14) Write a C functions for insertion and deletion operation in simple queue.

Here are the C functions for the insertion (enqueue) and deletion (dequeue) operations in a simple queue:

1. Enqueue (Insertion) Operation:

```c
void enqueue(int queue[], int *front, int *rear, int max, int item) {
    if (*rear == max - 1) {
        printf("Queue Overflow\\n");
    } else {
        if (*front == -1 && *rear == -1) {
            *front = *rear = 0;
        } else {
            *rear = *rear + 1;
        }
        queue[*rear] = item;
        printf("Inserted %d into the queue\\n", item);
    }
}

```

Explanation:

- The function takes the following parameters:
  - `queue[]`: The array representing the queue
  - `front`: Pointer to the front index of the queue
  - `rear`: Pointer to the rear index of the queue
  - `max`: The maximum size of the queue
  - `item`: The element to be inserted into the queue
- It first checks if the queue is full (i.e., `rear` is at the maximum index `max - 1`). If so, it prints "Queue Overflow" and returns.
- If the queue is empty (i.e., both `front` and `rear` are -1), it sets both `front` and `rear` to 0.
- Otherwise, it increments the `rear` index and inserts the `item` at the new `rear` position.
- Finally, it prints a message indicating that the element has been inserted.

1. Dequeue (Deletion) Operation:

```c
int dequeue(int queue[], int *front, int *rear) {
    int item;
    if (*front == -1 && *rear == -1) {
        printf("Queue Underflow\\n");
        return -1;
    } else {
        item = queue[*front];
        if (*front == *rear) {
            *front = *rear = -1;
        } else {
            *front = *front + 1;
        }
        printf("Deleted %d from the queue\\n", item);
        return item;
    }
}

```

Explanation:

- The function takes the following parameters:
  - `queue[]`: The array representing the queue
  - `front`: Pointer to the front index of the queue
  - `rear`: Pointer to the rear index of the queue
- It first checks if the queue is empty (i.e., both `front` and `rear` are -1). If so, it prints "Queue Underflow" and returns -1.
- Otherwise, it stores the element at the `front` index in the `item` variable.
- If `front` and `rear` are the same (i.e., the queue has only one element), it sets both `front` and `rear` to -1 to indicate an empty queue.
- Otherwise, it increments the `front` index to remove the element from the front of the queue.
- Finally, it prints a message indicating that the element has been deleted and returns the deleted element.

These functions can be used in a menu-driven program or integrated into a larger application to implement a simple queue data structure using an array.

## 15) What is a Queue? Write down drawback of simple queue. Also write an algorithm for deleting an element from circular queue

### What is a Queue?

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It is a collection of elements where the element that is inserted first is the first one to be removed. The elements in a queue are added at one end called the rear and removed from the other end called the front[1].

### Drawbacks of Simple Queue

1. **Memory Waste**: In a simple queue, if the front and rear pointers reach the end of the array, the remaining space in the array is wasted. This is because the front pointer cannot move back to the beginning of the array once it reaches the end[1].
2. **Overflow and Underflow**: Simple queues can overflow if the queue is full and a new element is tried to be inserted. Similarly, they can underflow if the queue is empty and an element is tried to be dequeued[1].

### Algorithm for Deleting an Element from Circular Queue

Here is the algorithm for deleting an element from a circular queue:

```c
void dequeue(int queue[], int *front, int *rear, int max) {
    int val;
    if (*front == -1 && *rear == -1) {
        printf("Queue Underflow\\n");
    } else {
        val = queue[*front];
        if (*front == *rear) {
            *front = *rear = -1;
        } else {
            *front = (*front + 1) % max;
        }
        printf("Deleted %d from the queue\\n", val);
    }
}

```

This algorithm checks if the queue is empty. If it is, it prints "Queue Underflow". Otherwise, it stores the element at the front of the queue in the `val` variable. If the queue has only one element left, it resets both `front` and `rear` to -1. Otherwise, it increments `front` by 1 and takes the new value modulo `max` to ensure it wraps around to the beginning of the array if necessary. Finally, it prints a message indicating that the element has been deleted and returns the deleted element[1].

## 16) Write an algorithm to delete an element from circular queue. Show the steps of insertion and deletion operation in sample circular queue.

Here is the algorithm to delete an element from a circular queue:

Algorithm to Delete an Element from Circular Queue:

1. Check if the queue is empty. If it is, print "Queue Underflow" and return.
2. If the front and rear pointers are equal, it means there is only one element in the queue. Set both front and rear to -1 to indicate an empty queue.
3. Otherwise, remove the element at the front of the queue by incrementing the front pointer. If the front pointer becomes equal to the maximum size of the queue, wrap it around to 0.
4. Print the deleted element.

Here's an example of the step-by-step insertion and deletion operations in a circular queue:

Let's assume we have a circular queue of size 5.

Initial State:
Front = -1
Rear = -1
Queue = [_, _, _, _, _]

Step 1: Insert 10 into the queue.
Rear = (Rear + 1) % 5 = 0
Queue = [10, _, _, _, _]
Front = 0
Rear = 0

Step 2: Insert 20 into the queue.
Rear = (Rear + 1) % 5 = 1
Queue = [10, 20, _, _, _]
Front = 0
Rear = 1

Step 3: Insert 30 into the queue.
Rear = (Rear + 1) % 5 = 2
Queue = [10, 20, 30, _, _]
Front = 0
Rear = 2

Step 4: Insert 40 into the queue.
Rear = (Rear + 1) % 5 = 3
Queue = [10, 20, 30, 40, _]
Front = 0
Rear = 3

Step 5: Insert 50 into the queue.
Rear = (Rear + 1) % 5 = 4
Queue =
Front = 0
Rear = 4

Step 6: Delete an element from the queue.
Front = (Front + 1) % 5 = 1
Queue = [_, 20, 30, 40, 50]
Front = 1
Rear = 4

Step 7: Delete another element from the queue.
Front = (Front + 1) % 5 = 2
Queue = [_, _, 30, 40, 50]
Front = 2
Rear = 4

The key points to note are:

- The front and rear pointers are used to keep track of the front and rear elements in the circular queue.
- The modulo operation is used to wrap around the pointers when they reach the end of the array.
- Deletion is performed by incrementing the front pointer, and insertion is performed by incrementing the rear pointer.

This way, the circular queue can efficiently utilize the available memory space and perform both insertion and deletion operations effectively.

## 17) Illustrate the working of priority queue with suitable example.

Here is an illustration of how a priority queue works with a suitable example:

A priority queue is a special type of queue where each element has a priority associated with it. Elements are dequeued based on their priority, with the highest priority element being dequeued first, regardless of the order in which they were enqueued[1].

Let's consider an example of a hospital emergency room where patients are treated based on the severity of their condition. We can use a priority queue to manage the patients.

Suppose we have the following patients in the emergency room:

1. Patient A with a broken leg (priority 3)
2. Patient B with chest pain (priority 5)
3. Patient C with a minor cut (priority 1)
4. Patient D with severe bleeding (priority 6)

We can represent these patients in a priority queue as follows:

```
Priority Queue:
Front -> Patient D (priority 6)
         Patient B (priority 5)
         Patient A (priority 3)
Rear  -> Patient C (priority 1)

```

Now, let's see how the priority queue works as patients are treated:

1. Initially, the priority queue contains all the patients in the order shown above, with Patient D having the highest priority and Patient C having the lowest priority.
2. The doctor treats the patient at the front of the queue, which is Patient D with severe bleeding. After treatment, Patient D is removed from the queue.
3. The priority queue now looks like this:

   ```
   Priority Queue:
   Front -> Patient B (priority 5)
            Patient A (priority 3)
   Rear  -> Patient C (priority 1)

   ```

4. The doctor treats the next patient at the front of the queue, which is Patient B with chest pain. After treatment, Patient B is removed from the queue.
5. The priority queue now looks like this:

   ```
   Priority Queue:
   Front -> Patient A (priority 3)
   Rear  -> Patient C (priority 1)

   ```

6. The doctor treats the remaining patients in the order of their priority until the queue is empty.

In this example, the priority queue ensures that patients with higher priority (more severe conditions) are treated first, even if they arrived later than patients with lower priority. This is the key advantage of using a priority queue in scenarios where urgency or importance is a factor[1].

The implementation of a priority queue can be done using various data structures like arrays, linked lists, or heaps. The choice of data structure depends on the specific requirements of the application and the desired performance characteristics[1].

## 18) How does priority queue work?

A priority queue is a special type of queue where each element has a priority associated with it. Elements are dequeued based on their priority, with the highest priority element being dequeued first, regardless of the order in which they were enqueued[1].

Here is how a priority queue works:

1. **Insertion**: When an element is inserted into the priority queue, it is assigned a priority based on its importance or urgency. The priority can be determined by various factors such as the severity of a medical condition, the priority of a task, or the urgency of a request.
2. **Deletion**: When an element is dequeued from the priority queue, the element with the highest priority is removed first. This ensures that the most critical or urgent elements are handled first.
3. **Priority Comparison**: When multiple elements have the same priority, they are dequeued based on their order of insertion. This ensures that the elements are dequeued in the order they were inserted, even if they have the same priority.
4. **Priority Update**: If an element's priority changes, it can be updated in the priority queue. This ensures that the element is dequeued based on its new priority.

Here is an example of how a priority queue works:

Suppose we have a hospital emergency room where patients are treated based on the severity of their condition. We can use a priority queue to manage the patients.

Initially, the priority queue contains the following patients:

- Patient A with a broken leg (priority 3)
- Patient B with chest pain (priority 5)
- Patient C with a minor cut (priority 1)
- Patient D with severe bleeding (priority 6)

When a patient is treated, the patient with the highest priority is dequeued first. In this case, Patient D with severe bleeding is dequeued first.

After Patient D is treated, the priority queue contains the following patients:

- Patient A with a broken leg (priority 3)
- Patient B with chest pain (priority 5)
- Patient C with a minor cut (priority 1)

When the next patient is treated, the patient with the highest priority is dequeued first. In this case, Patient B with chest pain is dequeued first.

After Patient B is treated, the priority queue contains the following patients:

- Patient A with a broken leg (priority 3)
- Patient C with a minor cut (priority 1)

When the next patient is treated, the patient with the highest priority is dequeued first. In this case, Patient A with a broken leg is dequeued first.

After Patient A is treated, the priority queue contains the following patient:

- Patient C with a minor cut (priority 1)

When the next patient is treated, the patient with the highest priority is dequeued first. In this case, Patient C with a minor cut is dequeued first.

This example illustrates how a priority queue works by ensuring that the most critical or urgent elements are handled first, regardless of the order in which they were inserted[1].

## 19) Describe the advantages of linked list over array.

Advantages of Linked List over Array:

1. **Dynamic Size**: One of the key advantages of linked lists over arrays is that linked lists can dynamically grow or shrink in size. In a linked list, memory is allocated as needed, allowing for efficient memory utilization and flexibility in managing data structures of varying sizes.
2. **Insertion and Deletion**: Linked lists excel at insertion and deletion operations. In a linked list, inserting or deleting an element at any position is efficient, as it involves adjusting pointers to rearrange the links between nodes. This contrasts with arrays, where inserting or deleting elements may require shifting elements, resulting in slower performance for large arrays.
3. **Memory Utilization**: Linked lists do not require contiguous memory allocation like arrays. Each node in a linked list can be located anywhere in memory, linked together by pointers. This flexibility in memory allocation allows for efficient use of memory space, especially when dealing with fragmented memory or when the size of the data structure is not known in advance.
4. **Ease of Implementation**: Linked lists are relatively easy to implement and manipulate. The structure of a linked list is straightforward, consisting of nodes with data and pointers. Operations like insertion, deletion, and traversal are simpler to implement in a linked list compared to arrays, where resizing and shifting elements can be more complex.
5. **Efficient for Insertions and Deletions**: Linked lists are efficient for insertions and deletions, especially in scenarios where elements need to be added or removed frequently. Inserting or deleting elements in the middle of a linked list involves adjusting pointers, making these operations faster compared to arrays, where shifting elements can be time-consuming.
6. **No Wastage of Memory**: Linked lists do not suffer from memory wastage due to fixed-size allocations like arrays. In a linked list, memory is allocated dynamically as nodes are added, reducing the risk of unused memory or memory fragmentation that can occur in arrays.
7. **Versatility**: Linked lists offer different types such as singly linked lists, doubly linked lists, and circular linked lists, providing versatility in implementing various data structures and algorithms based on specific requirements.

Linked lists offer several advantages over arrays, making them a preferred choice in scenarios where dynamic size, efficient insertions and deletions, and flexible memory utilization are essential considerations in data structure design and implementation.

## 20) Write an algorithm to insert a node at last position in doubly linked list.

Here is an algorithm to insert a node at the last position in a doubly linked list:

```c
void insertAtLast(struct Node **head, int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        newNode->prev = NULL;
    } else {
        struct Node *lastNode = *head;
        while (lastNode->next != NULL) {
            lastNode = lastNode->next;
        }
        lastNode->next = newNode;
        newNode->prev = lastNode;
    }
}

```

This algorithm works by first creating a new node with the given data. If the list is empty, it sets the new node as the head of the list. Otherwise, it traverses the list to find the last node and inserts the new node after it. The new node's `next` pointer is set to `NULL` and its `prev` pointer is set to the last node in the list.

## 21) Write a ‘C’ program to implement stack using linked list.

Here's a C program to implement a stack using a linked list:

```c
#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the linked list
struct Node {
    int data;
    struct Node* next;
};

// Global variable to keep track of the top of the stack
struct Node* top = NULL;

// Function to push an element onto the stack
void push(int value) {
    // Create a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = top;
    top = newNode;
    printf("Pushed %d onto the stack\\n", value);
}

// Function to pop an element from the stack
int pop() {
    if (top == NULL) {
        printf("Stack Underflow\\n");
        return -1;
    }
    int value = top->data;
    struct Node* temp = top;
    top = top->next;
    free(temp);
    printf("Popped %d from the stack\\n", value);
    return value;
}

// Function to display the elements in the stack
void display() {
    if (top == NULL) {
        printf("Stack is empty\\n");
        return;
    }
    printf("Stack elements: ");
    struct Node* temp = top;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\\n");
}

int main() {
    int choice, value;
    while (1) {
        printf("\\nStack Operations:\\n");
        printf("1. Push\\n");
        printf("2. Pop\\n");
        printf("3. Display\\n");
        printf("4. Exit\\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter the value to push: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Exiting...\\n");
                return 0;
            default:
                printf("Invalid choice\\n");
        }
    }
    return 0;
}

```

This program implements a stack using a linked list. The main functions are:

1. `push(int value)`: Adds a new node with the given value to the top of the stack.
2. `pop()`: Removes and returns the top element from the stack. If the stack is empty, it returns -1 and prints "Stack Underflow".
3. `display()`: Prints all the elements in the stack.

The program also includes a menu-driven interface that allows the user to perform the stack operations.

The key points to note in this implementation are:

1. The `top` pointer keeps track of the top element in the stack.
2. The `push` operation creates a new node and updates the `top` pointer to point to the new node.
3. The `pop` operation removes the node at the top of the stack and updates the `top` pointer to point to the next node.
4. The `display` operation traverses the linked list and prints the elements in the stack.

This linked list-based implementation of a stack provides the same time complexity as the array-based implementation for the basic operations (push, pop, and display), but it has the advantage of dynamic memory allocation and no fixed size limitation.

## 22) Write an algorithm to print the singly linked list in reverse order using stack.

To print a singly linked list in reverse order using a stack, we can follow this algorithm:

Algorithm to Print Singly Linked List in Reverse Order using Stack:

1. Create an empty stack.
2. Traverse the singly linked list and push each node's data onto the stack.
3. Pop the elements from the stack and print them. This will print the elements in reverse order.

Here are the detailed steps:

```
REVERSE_PRINT(HEAD)
    1. Create an empty stack S
    2. SET current = HEAD
    3. WHILE current != NULL
        PUSH current->data onto stack S
        SET current = current->next
    4. WHILE stack S is not empty
        POP an element from stack S and print it
    5. EXIT

```

Explanation:

1. We start by creating an empty stack `S`.
2. We initialize a `current` pointer to the head of the singly linked list.
3. We traverse the linked list using a `WHILE` loop. In each iteration, we push the data of the current node onto the stack `S`, and then move the `current` pointer to the next node.
4. After the entire linked list has been pushed onto the stack, we pop the elements from the stack one by one and print them. This will print the elements in reverse order.
5. Finally, we exit the algorithm.

This algorithm has a time complexity of O(n), where n is the number of nodes in the singly linked list, as we need to traverse the entire list once to push the elements onto the stack, and then pop and print the elements from the stack.

The space complexity is also O(n), as we are using a stack to store all the elements of the linked list.

## 23) Write a program to implement a circularly linked list.

Here is a simple C program to implement a circularly linked list:

```c
#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a new node at the end of the list
void insertNode(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        newNode->next = newNode;
    } else {
        struct Node* lastNode = *head;
        while (lastNode->next != *head) {
            lastNode = lastNode->next;
        }
        lastNode->next = newNode;
        newNode->next = *head;
    }
}

// Function to print the linked list
void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\\n");
}

int main() {
    struct Node* head = NULL;

    // Insert nodes into the list
    insertNode(&head, 1);
    insertNode(&head, 2);
    insertNode(&head, 3);
    insertNode(&head, 4);
    insertNode(&head, 5);

    // Print the linked list
    printf("Linked List: ");
    printList(head);

    return 0;
}

```

This program defines a linked list where each node contains an integer value and a pointer to the next node. The `createNode` function is used to create a new node with a given value. The `insertNode` function inserts a new node at the end of the list. The `printList` function prints the values in the linked list.

In the `main` function, we create a new linked list and insert five nodes into it. Finally, we print the linked list to verify that it is correctly implemented.

This program demonstrates the basic operations of a circularly linked list, including insertion and printing.

## 24) Write an algorithm for binary searching.

Here is the algorithm for binary search:

```c
BINARY_SEARCH(A, lower_bound, upper_bound, VAL)
    1. [INITIALIZE] SET BEG = lower_bound
    2. [INITIALIZE] SET END = upper_bound
    3. [INITIALIZE] SET POS = -1

    4. REPEAT Steps 5 and 6 while BEG <= END
    5. SET MID = (BEG + END)/2
    6. IF A[MID] = VAL
        SET POS = MID
        PRINT POS
        GO TO Step 7
    ELSE IF A[MID] > VAL
        SET END = MID - 1
    ELSE
        SET BEG = MID + 1

    7. [END OF IF]
    8. IF POS = -1
        PRINT “VALUE IS NOT PRESENT IN THE ARRAY”
    9. [END OF IF]
    10. EXIT

```

This algorithm is used to find an element in a sorted array. It works by repeatedly dividing the search interval in half and searching for the element in one of the two halves until the element is found or the search interval is empty.

## 25) Apply bubble sort on following data and show all steps.

123, 34, 65, 105, 27, 79, 12, 10, 125, 156

Here are the steps to apply bubble sort on the given data:

```
Initial Array: 123, 34, 65, 105, 27, 79, 12, 10, 125, 156

Pass 1:
Compare 123 and 34, swap: 34, 123, 65, 105, 27, 79, 12, 10, 125, 156
Compare 123 and 65, no swap: 34, 65, 123, 105, 27, 79, 12, 10, 125, 156
Compare 123 and 105, no swap: 34, 65, 105, 123, 27, 79, 12, 10, 125, 156
Compare 123 and 27, swap: 34, 65, 105, 27, 123, 79, 12, 10, 125, 156
Compare 123 and 79, swap: 34, 65, 105, 27, 79, 123, 12, 10, 125, 156
Compare 123 and 12, swap: 34, 65, 105, 27, 79, 12, 123, 10, 125, 156
Compare 123 and 10, swap: 34, 65, 105, 27, 79, 12, 10, 123, 125, 156
Compare 123 and 125, no swap: 34, 65, 105, 27, 79, 12, 10, 123, 125, 156
Compare 123 and 156, no swap: 34, 65, 105, 27, 79, 12, 10, 123, 125, 156

After Pass 1, the largest element 156 is at its correct position.

Pass 2:
Compare 34 and 65, no swap: 34, 65, 105, 27, 79, 12, 10, 123, 125, 156
Compare 65 and 105, no swap: 34, 65, 105, 27, 79, 12, 10, 123, 125, 156
Compare 105 and 27, swap: 34, 65, 27, 105, 79, 12, 10, 123, 125, 156
Compare 105 and 79, swap: 34, 65, 27, 79, 105, 12, 10, 123, 125, 156
Compare 105 and 12, swap: 34, 65, 27, 79, 12, 105, 10, 123, 125, 156
Compare 105 and 10, swap: 34, 65, 27, 79, 12, 10, 105, 123, 125, 156

After Pass 2, the two largest elements 156 and 125 are at their correct positions.

Pass 3:
Compare 34 and 65, no swap: 34, 65, 27, 79, 12, 10, 105, 123, 125, 156
Compare 65 and 27, swap: 34, 27, 65, 79, 12, 10, 105, 123, 125, 156
Compare 65 and 79, no swap: 34, 27, 65, 79, 12, 10, 105, 123, 125, 156
Compare 79 and 12, swap: 34, 27, 65, 12, 79, 10, 105, 123, 125, 156
Compare 79 and 10, swap: 34, 27, 65, 12, 10, 79, 105, 123, 125, 156

After Pass 3, the three largest elements 156, 125 and 123 are at their correct positions.

Pass 4:
Compare 34 and 27, swap: 27, 34, 65, 12, 10, 79, 105, 123, 125, 156
Compare 34 and 65, no swap: 27, 34, 65, 12, 10, 79, 105, 123, 125, 156
Compare 65 and 12, swap: 27, 34, 12, 65, 10, 79, 105, 123, 125, 156
Compare 65 and 10, swap: 27, 34, 12, 10, 65, 79, 105, 123, 125, 156

After Pass 4, the four largest elements are at their correct positions.

Pass 5:
Compare 27 and 34, no swap: 27, 34, 12, 10, 65, 79, 105, 123, 125, 156
Compare 34 and 12, swap: 27, 12, 34, 10, 65, 79, 105, 123, 125, 156
Compare 34 and 10, swap: 27, 12, 10, 34, 65, 79, 105, 123, 125, 156

After Pass 5, the five largest elements are at their correct positions.

Pass 6:
Compare 27 and 12, swap: 12, 27, 10, 34, 65, 79, 105, 123, 125, 156
Compare 27 and 10, swap: 12, 10, 27, 34, 65, 79, 105, 123, 125, 156

After Pass 6, the six largest elements are at their correct positions.

Pass 7:
Compare 12 and 10, swap: 10, 12, 27, 34, 65, 79, 105, 123, 125, 156

After Pass 7, the entire array is sorted.

Final Sorted Array: 10, 12, 27, 34, 65, 79, 105, 123, 125, 156

```

The time complexity of bubble sort is O(n^2), where n is the number of elements in the array. In the worst case, when the array is in reverse order, the algorithm will perform n(n-1)/2 comparisons and n(n-1)/2 swaps, resulting in a time complexity of O(n^2)[1].

## 26) Write an algorithm for linear searching.

Here is the algorithm for linear searching:

```c
LINEAR_SEARCH(A, N, VAL)
    1. [INITIALIZE] SET POS = -1
    2. [INITIALIZE] SET I = 1
    3. REPEAT Step 4 while I <= N
    4. IF A[I] = VAL
        SET POS = I
        PRINT POS
        GO TO Step 6
    ELSE
        SET I = I + 1
    [END OF LOOP]
    5. IF POS = -1
        PRINT "VALUE IS NOT PRESENT IN THE ARRAY"
    [END OF IF]
    6. EXIT

```

This algorithm works by comparing the value to be searched with every element of the array one by one in a sequence until a match is found. If the value is found, the position of the element is printed. If the value is not found, it prints "VALUE IS NOT PRESENT IN THE ARRAY"[1].

## 27) Sort the following numbers in ascending order by applying quick sort.

29 15 11 82 22 17 53 57 4 8

Here is the step-by-step process of applying the Quick Sort algorithm to sort the given numbers in ascending order:

Initial Array: 29, 15, 11, 82, 22, 17, 53, 57, 4, 8

Step 1: Choose a pivot element. Let's choose 8 as the pivot.

Step 2: Partition the array around the pivot 8:
Left subarray: 4, 7, 11, 15, 22, 17, 29, 82, 53, 57
Right subarray: 29, 82, 53, 57

Step 3: Recursively apply Quick Sort to the left and right subarrays.

Left Subarray:
Pivot: 15
Partitioned array: 4, 7, 11, 15, 22, 17, 29, 82, 53, 57

Right Subarray:
Pivot: 57
Partitioned array: 29, 82, 53, 57

Step 4: Recursively apply Quick Sort to the left and right subarrays of the left and right subarrays.

Left Subarray of Left Subarray:
Pivot: 11
Partitioned array: 4, 7, 11, 15, 22, 17, 29, 82, 53, 57

Right Subarray of Left Subarray:
Pivot: 22
Partitioned array: 4, 7, 11, 15, 17, 22, 29, 82, 53, 57

Right Subarray of Right Subarray:
Pivot: 82
Partitioned array: 29, 53, 57, 82

Step 5: Merge the sorted subarrays.

Final Sorted Array: 4, 7, 11, 15, 17, 22, 29, 53, 57, 82

The numbers 29, 15, 11, 82, 22, 17, 53, 57, 4, 8 are now sorted in ascending order using the Quick Sort algorithm.

## 28) Apply merge sort algorithm for the following data and show the steps. 66,

33, 40, 22, 55, 88, 11, 80, 20, 50, 44, 77, 30

Here are the steps to apply merge sort algorithm to the given data:

1. Divide the array into two halves:
   Original array: [66, 33, 40, 22, 55, 88, 11, 80, 20, 50, 44, 77, 30]
   First half: [66, 33, 40, 22, 55]
   Second half: [88, 11, 80, 20, 50, 44, 77, 30]
2. Recursively divide each half until we have subarrays of size 1:

   a. First half:

   [66]
   [33]
   [40]
   [22]
   [55]

   b. Second half:

   [88]
   [11]
   [80]
   [20]
   [50]
   [44]
   [77]
   [30]

3. Merge the subarrays of size 1 back together, comparing and combining them in sorted order:

   a. First half:

   Merge [66] and [33] -> [33, 66]
   Merge [40] and [22] -> [22, 40]
   Merge [55] and empty subarray (since [22, 40] was merged first) -> [55]
   Merge [33, 66] and [22, 40] -> [22, 33, 40, 66]
   Merge [55] and [22, 33, 40, 66] -> [22, 33, 40, 55, 66]

   b. Second half:

   Merge [88] and [11] -> [11, 88]
   Merge [80] and [20] -> [20, 80]
   Merge [50] and [44] -> [44, 50]
   Merge [77] and [30] -> [30, 77]
   Merge [11, 88] and [20, 80] -> [11, 20, 80, 88]
   Merge [44, 50] and [30, 77] -> [30, 44, 50, 77]
   Merge [11, 20, 80, 88] and [30, 44, 50, 77] -> [11, 20, 30, 44, 50, 77, 80, 88]

4. Merge the two sorted halves together:

   Merge [22, 33, 40, 55, 66] and [11, 20, 30, 44, 50, 77, 80, 88] -> [11, 20, 22, 30, 33, 40, 44, 50, 55, 66, 77, 80, 88]

So the sorted array is [11, 20, 22, 30, 33, 40, 44, 50, 55, 66, 77, 80, 88].

## 29) Evaluate the following postfix expression in tabular form showing stack after every step.

7 6 + 4 \* 4 10 + - 5 +

Here is the step-by-step evaluation of the given postfix expression using a stack:

| Step | Expression | Stack   | Operation                                                                                  |
| ---- | ---------- | ------- | ------------------------------------------------------------------------------------------ |
| 1    | 7          | 7       | Push 7 onto the stack                                                                      |
| 2    | 7 6 +      | 7 6     | Push 6 onto the stack                                                                      |
| 3    | 7 +        | 13      | Pop 7 and 6 from the stack, add them, and push the result (13) onto the stack              |
| 4    | 13 4 \*    | 13 4    | Push 4 onto the stack                                                                      |
| 5    | 13 \*      | 52      | Pop 13 and 4 from the stack, multiply them, and push the result (52) onto the stack        |
| 6    | 52 4       | 52 4    | Push 4 onto the stack                                                                      |
| 7    | 52 4 10 +  | 52 4 10 | Push 10 onto the stack                                                                     |
| 8    | 52 14      | 52 14   | Pop 4 and 10 from the stack, add them, and push the result (14) onto the stack             |
| 9    | 52 14 -    | 52 14   | No operation, since the next token is an operator                                          |
| 10   | 52 -       | 38      | Pop 52 and 14 from the stack, subtract 14 from 52, and push the result (38) onto the stack |
| 11   | 38 5 +     | 38 5    | Push 5 onto the stack                                                                      |
| 12   | 38 +       | 43      | Pop 38 and 5 from the stack, add them, and push the result (43) onto the stack             |

The final result of the postfix expression evaluation is 43.

## 30) Apply quick sort on following data: 42 23 74 11 65 58 94 36 99 87

Here are the steps to apply quicksort algorithm on the given data:

1. Choose a pivot element, say the last element of the array, which is 87 in this case.
2. Partition the array into three parts: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.

   Original array: [42, 23, 74, 11, 65, 58, 94, 36, 99, 87]
   Pivot: 87

   Partitioned array: [11, 23, 36, 42, 58, 65, 74, 94, | 87 |, 99]

3. Recursively apply quicksort to the subarrays of elements less than and greater than the pivot:

   a. Subarray of elements less than the pivot:

   [11, 23, 36, 42, 58, 65]

   Choose a pivot element, say the last element of the subarray, which is 65.
   Partition the subarray:

   [11, 23, 36, 42, | 58 |, 65]

   Recursively apply quicksort to the subarrays of elements less than and greater than the pivot:

   ```
     i. Subarray of elements less than the pivot:

        [11, 23, 36, 42]

        Choose a pivot element, say the middle element of the subarray, which is 36.
        Partition the subarray:

        [11, 23, | 36 |, 42]

        Recursively apply quicksort to the subarrays of elements less than and greater than the pivot:

           a. Subarray of elements less than the pivot:

              [11, 23]

              Choose a pivot element, say the first element of the subarray, which is 11.
              Partition the subarray:

              [| 11 |, 23]

              No further partitioning needed, since the subarray has only two elements.

           b. Subarray of elements greater than the pivot:

              [42]

              No further partitioning needed, since the subarray has only one element.

        Merge the subarrays and the pivot:

        [11, 23, 36, 42]

     ii. Subarray of elements greater than the pivot:

        [58]

        No further partitioning needed, since the subarray has only one element.

   ```

   Merge the subarrays and the pivot:

   [11, 23, 36, 42, 58, 65]

   b. Subarray of elements greater than the pivot:

   [94, 99]

   Choose a pivot element, say the first element of the subarray, which is 94.
   Partition the subarray:

   [94, | 99 |]

   No further partitioning needed, since the subarray has only two elements.

   Merge the subarrays and the pivot:

   [11, 23, 36, 42, 58, 65, 74, 87, 94, 99]

The final sorted array is [11, 23, 36, 42, 58, 65, 74, 87, 94, 99].

## 31) Explain the trace of selection sort on following data.

42,23,74,11,65,58,94,36,99,87

Here is the step-by-step trace of the Selection Sort algorithm applied to the given data: 42, 23, 74, 11, 65, 58, 94, 36, 99, 87.

Pass 1:

- Find the smallest element in the unsorted part of the array, which is 11.
- Swap the element at index 0 (42) with the smallest element (11).
- The array now looks like: 11, 23, 74, 42, 65, 58, 94, 36, 99, 87.

Pass 2:

- Find the smallest element in the unsorted part of the array, which is 23.
- Swap the element at index 1 (23) with the smallest element (23).
- The array now looks like: 11, 23, 74, 42, 65, 58, 94, 36, 99, 87.

Pass 3:

- Find the smallest element in the unsorted part of the array, which is 36.
- Swap the element at index 2 (74) with the smallest element (36).
- The array now looks like: 11, 23, 36, 42, 65, 58, 94, 74, 99, 87.

Pass 4:

- Find the smallest element in the unsorted part of the array, which is 42.
- Swap the element at index 3 (42) with the smallest element (42).
- The array now looks like: 11, 23, 36, 42, 65, 58, 94, 74, 99, 87.

Pass 5:

- Find the smallest element in the unsorted part of the array, which is 58.
- Swap the element at index 4 (65) with the smallest element (58).
- The array now looks like: 11, 23, 36, 42, 58, 65, 94, 74, 99, 87.

Pass 6:

- Find the smallest element in the unsorted part of the array, which is 65.
- Swap the element at index 5 (65) with the smallest element (65).
- The array now looks like: 11, 23, 36, 42, 58, 65, 94, 74, 99, 87.

Pass 7:

- Find the smallest element in the unsorted part of the array, which is 74.
- Swap the element at index 6 (94) with the smallest element (74).
- The array now looks like: 11, 23, 36, 42, 58, 65, 74, 94, 99, 87.

Pass 8:

- Find the smallest element in the unsorted part of the array, which is 87.
- Swap the element at index 7 (94) with the smallest element (87).
- The array now looks like: 11, 23, 36, 42, 58, 65, 74, 87, 99, 94.

Pass 9:

- Find the smallest element in the unsorted part of the array, which is 94.
- Swap the element at index 8 (99) with the smallest element (94).
- The array now looks like: 11, 23, 36, 42, 58, 65, 74, 87, 94, 99.

The array is now sorted in ascending order: 11, 23, 36, 42, 58, 65, 74, 87, 94, 99.

The time complexity of Selection Sort is O(n^2), where n is the number of elements in the array. This is because the algorithm needs to perform n passes, and in each pass, it needs to find the smallest element in the unsorted part of the array, which takes O(n) time.

## 32) Explain the trace of bubble sort on following data.

42,23,74,11,65,58,94,36,99,87

Here is the step-by-step trace of the Bubble Sort algorithm applied to the given data: 42, 23, 74, 11, 65, 58, 94, 36, 99, 87.

Pass 1:

- Compare 42 and 23. Since 42 > 23, swapping is done.
- Compare 42 and 74. Since 42 < 74, no swapping is done.
- Compare 42 and 11. Since 42 > 11, swapping is done.
- Compare 42 and 65. Since 42 < 65, no swapping is done.
- Compare 42 and 58. Since 42 > 58, swapping is done.
- Compare 42 and 94. Since 42 < 94, no swapping is done.
- Compare 42 and 36. Since 42 > 36, swapping is done.
- Compare 42 and 99. Since 42 < 99, no swapping is done.
- Compare 42 and 87. Since 42 > 87, swapping is done.
- The array now looks like: 23, 11, 42, 65, 58, 94, 36, 99, 87, 74.

Pass 2:

- Compare 23 and 11. Since 23 > 11, swapping is done.
- Compare 23 and 42. Since 23 < 42, no swapping is done.
- Compare 23 and 65. Since 23 < 65, no swapping is done.
- Compare 23 and 58. Since 23 < 58, no swapping is done.
- Compare 23 and 94. Since 23 < 94, no swapping is done.
- Compare 23 and 36. Since 23 < 36, no swapping is done.
- Compare 23 and 99. Since 23 < 99, no swapping is done.
- Compare 23 and 87. Since 23 < 87, no swapping is done.
- The array now looks like: 11, 23, 42, 65, 58, 94, 36, 99, 87, 74.

Pass 3:

- Compare 11 and 23. Since 11 < 23, no swapping is done.
- Compare 11 and 42. Since 11 < 42, no swapping is done.
- Compare 11 and 65. Since 11 < 65, no swapping is done.
- Compare 11 and 58. Since 11 < 58, no swapping is done.
- Compare 11 and 94. Since 11 < 94, no swapping is done.
- Compare 11 and 36. Since 11 < 36, no swapping is done.
- Compare 11 and 99. Since 11 < 99, no swapping is done.
- Compare 11 and 87. Since 11 < 87, no swapping is done.
- The array now looks like: 11, 23, 42, 65, 58, 94, 36, 99, 87, 74.

Pass 4:

- Compare 23 and 42. Since 23 < 42, no swapping is done.
- Compare 23 and 65. Since 23 < 65, no swapping is done.
- Compare 23 and 58. Since 23 < 58, no swapping is done.
- Compare 23 and 94. Since 23 < 94, no swapping is done.
- Compare 23 and 36. Since 23 < 36, no swapping is done.
- Compare 23 and 99. Since 23 < 99, no swapping is done.
- Compare 23 and 87. Since 23 < 87, no swapping is done.
- The array now looks like: 11, 23, 42, 65, 58, 94, 36, 99, 87, 74.

Pass 5:

- Compare 42 and 65. Since 42 < 65, no swapping is done.
- Compare 42 and 58. Since 42 < 58, no swapping is done.
- Compare 42 and 94. Since 42 < 94, no swapping is done.
- Compare 42 and 36. Since 42 < 36, no swapping is done.
- Compare 42 and 99. Since 42 < 99, no swapping is done.
- Compare 42 and 87. Since 42 < 87, no swapping is done.
- The array now looks like: 11, 23, 42, 58, 65, 94, 36, 99, 87, 74.

Pass 6:

- Compare 58 and 65. Since 58 < 65, no swapping is done.
- Compare 58 and 94. Since 58 < 94, no swapping is done.
- Compare 58 and 36. Since 58 > 36, swapping is done.
- Compare 58 and 99. Since 58 < 99, no swapping is done.
- Compare 58 and 87. Since 58 < 87, no swapping is done.
- The array now looks like: 11, 23, 36, 42, 58, 65, 94, 99, 87, 74.

Pass 7:

- Compare 65 and 94. Since 65 < 94, no swapping is done.
- Compare 65 and 99. Since 65 < 99, no swapping is done.
- Compare 65 and 87. Since 65 < 87, no swapping is done.
- The array now looks like: 11, 23, 36, 42, 58, 65, 74, 87, 94, 99.

The array is now sorted in ascending order: 11, 23, 36, 42, 58, 65, 74, 87, 94, 99.

The time complexity of Bubble Sort is O(n2), where n is the number of elements in the array. This is because the algorithm needs to perform n passes, and in each pass, it needs to compare each element with every other element, resulting in a total of n2 comparisons.

## 33) List the advantages of a doubly linked list over singly linked list.

Here are the main advantages of a doubly linked list over a singly linked list:

1. **Traversal**: In a doubly linked list, we can traverse the list in both forward and backward directions, whereas in a singly linked list, we can only traverse in the forward direction[1].
2. **Deletion**: Deleting a node in a doubly linked list is easier compared to a singly linked list. In a singly linked list, to delete a node, we need to keep track of the previous node to update its link. However, in a doubly linked list, we can directly update the links of the previous and next nodes to delete the current node[1].
3. **Insertion**: Inserting a new node in a doubly linked list is easier compared to a singly linked list. In a singly linked list, to insert a new node, we need to update the link of the previous node. However, in a doubly linked list, we can directly update the links of the previous and next nodes to insert the new node[1].
4. **Searching**: Searching for a node in a doubly linked list is easier compared to a singly linked list. In a doubly linked list, we can start the search from both ends (front or rear) depending on the position of the node. This allows for more efficient searching, especially when the node is closer to one of the ends[1].
5. **Memory Utilization**: A doubly linked list requires more memory compared to a singly linked list because each node in a doubly linked list contains an additional pointer to the previous node[1].

In summary, a doubly linked list provides more flexibility in traversal, deletion, and insertion operations compared to a singly linked list, but at the cost of additional memory requirements.

## 34) Write an algorithm for insertion sort.

Here is the algorithm for insertion sort:

```
INSERTION_SORT(ARR, N)
    1. REPEAT Steps 2 to 5 for K = 1 to N - 1
    2. SET TEMP = ARR[K]
    3. SET J = K - 1
    4. REPEAT while TEMP <= ARR[J]
        SET ARR[J + 1] = ARR[J]
        SET J = J - 1
    [END OF INNER LOOP]
    5. SET ARR[J + 1] = TEMP
    [END OF LOOP]
    6. EXIT

```

This algorithm sorts the array `ARR` of size `N` using the insertion sort method. It iterates through the array, comparing each element with the elements before it and inserting it in its proper position. The time complexity of this algorithm is O(n2), where n is the size of the array[1].
