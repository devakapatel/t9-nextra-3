# Unit 3

## <mark> 1) What is intermediate code? write benefits of intermediate code generation. </mark>

**Intermediate code**

In the analysis phase, the source program is translated into an intermediate representation. Many forms of intermediate code are possible. These form should be easy to produce and easy to translate into the target program.

**Benefits of intermediate code generation**

1.  Ease of Optimization: Intermediate code can be optimized to improve performance before the final machine code is generated. This optimization is machine-independent, making the compiler more flexible.
2.  Machine Independence: Since the intermediate code is not specific to any particular machine architecture, the front-end of the compiler (which generates the intermediate code) can be separated from the back-end (which generates the machine code). This allows for easier retargeting of the compiler to different platforms.
3.  Modularity: Using an intermediate representation enhances the modularity of a compiler. Different front-ends for various source languages can generate the same intermediate code, and different back-ends can translate the intermediate code into machine code for different target machines.
4.  Abstraction: Intermediate representations often provide a level of abstraction that hides the details of the target machine from the front-end of the compiler.

## <mark> 2) Explain different forms of intermediate code generation. <br> 1. Abstract syntax tree <br> 2. Polish notation <br> 3. Three address code </mark>

Intermediate code serves as a representation of the source program that lies between the high-level source code and the low-level machine code. It offers benefits like machine independence, facilitates optimization, and enhances modularity in the compilation process. Here are some common forms:

1.  **Abstract Syntax Tree (AST)**

    - An AST is a tree representation of the abstract syntactic structure of the source code.
    - Each node in the tree denotes a construct occurring in the source code.
    - The leaves of the tree represent the operands.
    - Example: The expression `a + b * c` would have an AST with "+" at the root, "a" as the left child, and "\*" as the right child. The "\*" node would have "b" and "c" as its children.
    - ASTs are used extensively in compilers because they represent the hierarchical structure of the program in a clear and unambiguous way.

2.  **Polish Notation (Prefix and Postfix)**

    - Polish notation is a notation for writing expressions without using parentheses.
    - **Prefix Notation (Polish Notation):** Operators precede their operands. Example: `+ a * b c`
    - **Postfix Notation (Reverse Polish Notation):** Operators follow their operands. Example: `a b c * +`
    - Postfix notation is particularly useful in compilers for expression evaluation because it can be easily evaluated using a stack-based algorithm.

3.  **Three-Address Code**

    - Three-address code is a sequence of statements of the form `A := B op C`, where A, B, and C are either variable names, constants, or temporary variables.
    - `op` represents any operator.
    - Each statement involves at most one operator.
    - Temporary variables are used to hold intermediate values computed during the evaluation.
    - Example: The expression `a + b * c` can be translated into the following three-address code:
      ```
      T1 := b * c
      T2 := a + T1
      ```
    - Three-address code is a common intermediate representation because it is simple, and it makes it easier to perform optimizations.

## <mark> 3) Explain Quadruple, triple, and indirect triple with a suitable example. <br> OR <br> Write about implementation of 3 address code

**Three-Address Code Implementation**

Three-address code is an intermediate representation where each instruction typically has at most three operands. These operands can be variables, constants, or temporary variables. To implement three-address code, we need data structures to store and manipulate these instructions. Quadruples, triples, and indirect triples are different ways to represent these three-address instructions.

**1. Quadruples**

- A quadruple is a record structure with four fields: `op`, `arg1`, `arg2`, and `result`.
  - `op`: Holds an operator.
  - `arg1` and `arg2`: Hold the two operands.
  - `result`: Holds the result of the operation.
- Example: The three-address code `a = b + c` would be represented by the quadruple `(+, b, c, a)`.
- Quadruples are easy to understand and implement.

**2. Triples**

- A triple is a record structure with three fields: `op`, `arg1`, and `arg2`.
  - `op`: Holds an operator.
  - `arg1` and `arg2`: Hold the two operands.
- The results of the operations are referred to by their position.
- Example: The three-address code:
  ```
  T1 = b + c
  a = T1
  ```
  would be represented by the triples:
  ```
  (+, b, c)
  (=, a, (0))
  ```
  - `(0)` refers to the result of the first triple.
- Triples conserve storage compared to quadruples because the temporary names are not explicitly stored.

**3. Indirect Triples**

- Indirect triples use a listing of pointers to triples.
- An additional table stores the list of pointers to the triples.
- Example:
  - Instead of storing the triples directly, we store pointers to them.
  - This allows for more efficient code optimization.
- Indirect triples allow for more flexibility and can lead to better optimization.

## <mark> 4) Write a short note on symbol table management. </mark>

Here is a short note on symbol table management:

A symbol table is a crucial data structure used by a compiler to store information about the various entities in a program, such as variables, functions, classes, and interfaces. It is used in all phases of compilation.

The purpose of symbol table management is to organize and maintain these identifiers and their associated attributes.

Key operations in symbol table management include:

- **Insertion:** Adding new symbols and their attributes to the table. This occurs during lexical analysis and parsing when identifiers are encountered.
- **Lookup:** Searching for a symbol in the table to retrieve its attributes. This is essential during semantic analysis and code generation to verify the correct usage of identifiers.
- **Deletion:** Removing symbols from the table, typically when they go out of scope.

Attributes stored in the symbol table might include:

- **Name:** The identifier itself.
- **Type:** The data type of a variable or the return type of a function.
- **Scope:** Information about where the identifier is valid and accessible.
- **Address:** The memory location assigned to a variable.
- **Other information:** Such as size, storage class, and parameters (for functions).

Efficient symbol table management is vital for the performance and correctness of a compiler.

## <mark> 5) Explain how type checking & error reporting is performed in the compiler. </mark>

Type checking is a crucial phase in the compilation process that ensures the program adheres to the type rules of the programming language. It verifies that operations are performed on compatible data types and that data is used consistently throughout the program. Error reporting is closely tied to type checking, as the compiler must provide informative messages to the programmer when type errors are detected.

Here’s how type checking and error reporting are generally performed in a compiler:

**Type Checking**

1.  **Symbol Table:** The symbol table, constructed during lexical and syntax analysis, plays a vital role. It stores information about the type of each identifier (variable, function, etc.) in the program.

2.  **Type Rules:** Every programming language has a set of type rules that define how types can be combined and manipulated. For example, an addition operation might require both operands to be numeric types.

3.  **Traversal of the Abstract Syntax Tree (AST):** The type checker traverses the AST, which represents the program's structure. At each node of the AST, the type checker applies the type rules of the language.

4.  **Type Inference:** In some cases, the compiler can infer the type of an expression without explicit type declarations (e.g., in languages with type inference features). It uses the context in which an expression appears to deduce its type.

5.  **Type Checking of Expressions:**

    - For operators (e.g., +, -, \*, /), the type checker verifies that the operands have the expected types. If not, a type error is reported.
    - For function calls, the type checker checks that the number of arguments matches the function's definition and that the argument types are compatible with the parameter types.
    - For assignments, the type checker ensures that the type of the right-hand side expression is compatible with the type of the variable on the left-hand side.

6.  **Type Checking of Control Flow:** The type checker also examines control flow statements (e.g., if, while) to ensure that the conditions are of a suitable type (e.g., boolean).

**Error Reporting**

1.  **Detection of Type Errors:** When the type checker encounters a violation of the type rules, it detects a type error.

2.  **Error Message Generation:** The compiler generates an error message that informs the programmer about the type error. The error message typically includes:

    - The location of the error in the source code (e.g., line number, column number).
    - A description of the error (e.g., "type mismatch," "invalid operand type").
    - Information about the expected and actual types.

3.  **Error Reporting Mechanisms:**

    - The compiler may report errors as soon as they are detected during the traversal of the AST.
    - Some compilers collect all the errors and report them at the end of the type-checking phase.

4.  **Error Recovery:** After reporting an error, the compiler may attempt to recover and continue type checking. This allows the compiler to detect multiple errors in a single compilation. Error recovery strategies might involve:
    - Substituting a default type for the erroneous expression.
    - Skipping the rest of the current statement or block.

**Example**

Consider the following code snippet:

```
int x;
float y;
x = y + "hello";
```

- The type checker would access the symbol table to determine that `x` is of type `int` and `y` is of type `float`.
- When checking the assignment statement, it would encounter the expression `y + "hello"`.
- The type checker would determine that the `+` operator is being applied to a `float` (`y`) and a `string` (`"hello"`), which is a type mismatch according to the language's type rules.
- The compiler would generate an error message similar to: "Error: Type mismatch. Cannot add float and string."
- The error message would include the line number where the error occurred.

## <mark> 6) List out various syntax directed translation Mechanisms. Explain any two with an example. </mark>

Here's a breakdown of syntax-directed translation mechanisms, along with explanations of two key methods:

**Syntax-Directed Translation**

Syntax-directed translation is a compiler construction technique where the semantic analysis phase is driven by the syntax of the programming language. It involves attaching rules or actions to the grammar productions of a language's context-free grammar. These rules specify how to compute attributes or perform actions based on the syntactic structure of the program.

**Various Syntax-Directed Translation Mechanisms**

1.  **Syntax-Directed Definitions (SDDs):**
    - SDDs associate attributes with grammar symbols and semantic rules with grammar productions.
    - Attributes can be of any type (e.g., strings, numbers, data structures).
    - Semantic rules specify how to compute the values of attributes.
    - SDDs do not specify the order in which the attributes are computed.
2.  **Translation Schemes:**
    - Translation schemes are similar to SDDs, but they provide explicit information about the order in which semantic actions are to be performed.
    - Semantic actions (code fragments) are embedded within the grammar productions.
    - Translation schemes are often used in parser generators.
3.  **Attribute Grammars:**
    - Attribute grammars are a formal framework for defining SDDs.
    - They provide a more structured and rigorous way to specify attribute computations.
    - Attribute grammars distinguish between synthesized attributes (computed from children nodes) and inherited attributes (computed from parent and/or sibling nodes).

**Explanation of Two Mechanisms**

1.  **Syntax-Directed Definitions (SDDs)**

    - An SDD associates attributes with each grammar symbol and semantic rules with each production.
    - Attributes can be synthesized or inherited.

      - **Synthesized attributes:** Their values are computed from the values of the attributes of their children in the parse tree.
      - **Inherited attributes:** Their values are computed from the values of the attributes of the parent and/or siblings in the parse tree.

    - Example: Consider the following grammar for simple arithmetic expressions:

      ```
      E -> E + T
      E -> T
      T -> T * F
      T -> F
      F -> ( E )
      F -> id
      ```

    - We can define an SDD to compute the value of each expression. Let's use a synthesized attribute `val` for each non-terminal.

    - SDD:

      | Production   | Semantic Rule           |
      | :----------- | :---------------------- |
      | E -> E1 + T  | E.val = E1.val + T.val  |
      | E -> T       | E.val = T.val           |
      | T -> T1 \* F | T.val = T1.val \* F.val |
      | T -> F       | T.val = F.val           |
      | F -> ( E )   | F.val = E.val           |
      | F -> id      | F.val = id.lexval       |

      - `id.lexval` is the value of the token id (obtained from the lexical analyzer).

    - In this example, the `val` attribute for each expression is computed based on the values of its sub-expressions.

2.  **Translation Schemes**

    - Translation schemes are a procedural way of specifying syntax-directed translation. Semantic actions are embedded within the grammar productions.

    - Example: Using the same grammar as above, we can write a translation scheme to perform the same computations:

      ```
      E -> E + T { E.val = E.val + T.val }
      E -> T { E.val = T.val }
      T -> T * F { T.val = T.val * F.val }
      T -> F { E.val = F.val }
      F -> ( E ) { F.val = E.val }
      F -> id { F.val = id.lexval }
      ```

    - The actions within the curly braces `{}` are performed in the order they appear during parsing.

    - For instance, in the production `E -> E + T { E.val = E.val + T.val }`, the addition is performed after the values of `E.val` and `T.val` have been computed (presumably through recursive calls).

Key Differences Summarized

- SDDs are declarative: They specify _what_ computations need to be done, without specifying the order.
- Translation Schemes are procedural: They specify _how_ the computations are to be done, including the order of evaluation.

## <mark> 7) Explain Activation record and Activation tree in brief. </mark>

Here are explanations for "Quadruple, triple, and indirect triple" and "3 address code implementation:"

### Quadruple, Triple, and Indirect Triple

These are various notations used in intermediate code representation, particularly in the context of compilers. They are methods to represent the operations and operands in a program in a structured format before the final machine code generation.

1.  **Quadruple:** This notation represents each operation in a program as a record with four fields. These fields typically include:
    - Op: To store the operation to be performed.
    - Arg1: To store the first operand.
    - Arg2: To store the second operand.
    - Result: To store the result of the operation.
2.  **Triple:** Triple notation is similar to quadruple, but it reduces the number of fields by not storing the result. Instead, the result of an operation is referred to by its position (triple number). So, a triple has three fields:
    - Op: Operation.
    - Arg1: First operand.
    - Arg2: Second operand.
3.  **Indirect Triple:** This is an enhancement over triple notation. Instead of rearranging the triples themselves during optimization, a list of pointers to the triples is maintained. This allows for reordering of operations by just reordering the pointers, without modifying the triples. [cite: 634, 635, 636, 637, 638, 639]

### Implementation of 3-Address Code

3-address code is a form of intermediate code where each instruction involves at most three operands. It is a common representation used by compilers due to its simplicity and ease of optimization.

**Implementation Aspects:**

- **Data Structures:**
  - For efficient code generation and manipulation, 3-address code can be implemented using data structures like arrays, linked lists, or hash tables.
  - Arrays provide a simple way to store instructions but may require reallocation if the number of instructions grows.
  - Linked lists allow for dynamic growth but may have overhead in terms of memory and traversal.
- **Code Generation:**
  - The process of generating 3-address code involves traversing the abstract syntax tree (AST) of the source code and generating corresponding 3-address instructions for each operation.
  - Temporary variables are often introduced to hold intermediate values.
- **Optimization:**
  - 3-address code is designed to facilitate various optimizations. Techniques like constant folding, dead code elimination, and loop optimization can be applied more easily on 3-address code.
- **Example:**
  - Consider a simple expression: `a = b + c * d`. The 3-address code for this might look like:
    ```
    T1 = c * d
    T2 = b + T1
    a = T2
    ```
    Here, T1 and T2 are temporary variables. [cite: 237, 238, 239, 580, 634, 635, 636, 637, 638, 639]

## <mark> 8) Explain Stack allocation and Activation record organization in brief. </mark>

Here are brief explanations of stack allocation and activation record organization, drawing from the provided compiler design resources:

**Stack Allocation**

Stack allocation is a memory management technique used to allocate and deallocate memory for function calls and local variables during the execution of a program. It operates on a Last-In, First-Out (LIFO) principle.

- When a function is called, a block of memory called an activation record (or stack frame) is pushed onto the stack.
- This activation record contains space for the function's parameters, local variables, return address, and other necessary information.
- When the function completes its execution, its activation record is popped off the stack, freeing the memory.
- Stack allocation is efficient for managing function calls and local variables because the allocation and deallocation operations are simple and fast.

**Activation Record Organization**

An activation record is a data structure that stores all the information needed for a single execution of a procedure. The contents of an activation record vary depending on the programming language and the compiler implementation, but it typically includes the following:

- **Temporary variables:** Space for storing temporary values computed during the execution of the procedure.
- **Local variables:** Space for storing the local variables of the procedure.
- **Saved machine registers:** Space to save the values of machine registers before the procedure call, so they can be restored after the procedure returns.
- **Control link (Dynamic link):** A pointer to the activation record of the caller procedure. This is used to restore the caller's environment when the called procedure returns.
- **Access link (Static link):** In languages that support nested procedures, a pointer to the activation record of the statically enclosing procedure. This is used to access non-local variables.
- **Actual parameters:** Space to store the actual parameters passed to the procedure.
- **Return value:** Space to store the return value of the procedure.
- **Return address:** The address of the instruction to which execution should return after the procedure call.

## <mark> 9) List out and explain various storage allocation strategies. </mark>

Here's a list of storage allocation strategies:

1.  **Static Allocation:**
    - Memory is allocated to variables and data structures at compile time.
    - The size and location of the allocated memory are fixed throughout the program's execution.
    - Examples: Global variables, static variables.
2.  **Stack Allocation:**
    - Memory is allocated and deallocated in a Last-In, First-Out (LIFO) manner.
    - Used for managing function calls and local variables.
    - Activation records (or stack frames) are pushed onto the stack when a function is called and popped off when the function returns.
3.  **Heap Allocation:**
    - Memory is allocated and deallocated dynamically at run time.
    - Used for data structures whose size is not known at compile time or that need to persist beyond the lifetime of a function call.
    - Memory is allocated from a pool of available memory (the heap) using functions like `malloc()` (in C/C++) or `new` (in C++, Java, etc.).

## <mark> 10) Write in brief about storage organization in compiler. </mark>

Here's a brief explanation of stack allocation and activation record organization:

**Stack Allocation**

In computer science, stack allocation is a memory allocation technique where memory is allocated and deallocated in a last-in, first-out (LIFO) manner. [cite: 187, 569] It's like a stack of plates – the last plate placed on top is the first one removed. This method is efficient for managing memory in functions calls and local variables.

**Activation Record Organization**

An activation record, also known as a stack frame, is a data structure that stores information about a specific invocation of a procedure or function. [cite: 1088, 1121, 1122] It typically contains:

- Return address
- Call arguments
- Saved registers
- Local variables
- Temporary storage [cite: 1122, 1123, 122]

The activation record is pushed onto the stack when a function is called and popped off when the function completes its execution. [cite: 196, 536, 537, 538, 539, 540] This منظم organization helps in managing the execution of functions and their data in an organized way.

## <mark> 11) Compare and contrast between static , stack and heap allocation. </mark>

Here's a comparison of static, stack, and heap allocation:

- **Static Allocation:**
  - Memory is allocated to variables and data structures at compile time.
  - The size and location of the allocated memory are fixed throughout the program's execution.
  - Examples: Global variables, static variables.
- **Stack Allocation:**
  - Memory is allocated and deallocated in a Last-In, First-Out (LIFO) manner.
  - Used for managing function calls and local variables.
  - Activation records (or stack frames) are pushed onto the stack when a function is called and popped off when the function returns.
- **Heap Allocation:**
  - Memory is allocated and deallocated dynamically at run time.
  - Used for data structures whose size is not known at compile time or that need to persist beyond the lifetime of a function call.
  - Memory is allocated from a pool of available memory (the heap) using functions like malloc() (in C/C++) or new (in C++, Java, etc.).

## <mark> 12) What is the use of a symbol table? How are identifiers stored in the symbol table? </mark>

Here's what the documents say about the use of a symbol table and how identifiers are stored:

**Use of a Symbol Table**

The documents "Introduction to Automata Theory, Languages, and Computation (John Hopcroft, Rajeev Motwani, Jeffrey Ullman) (Z-Library).pdf" and "Compilers Principles and Practice (Parag H. Dave, Himanshu B. Dave) (Z-Library).pdf" explain that a symbol table is a crucial data structure used by a compiler. It stores information about various entities in a program, such as:

- Variables
- Functions
- Classes
- Interfaces

The symbol table is used throughout the compilation process for tasks like:

- **Type checking:** Verifying that variables are used consistently with their declared types.
- **Code generation:** Storing information needed to allocate memory and generate correct instructions.
- **Scope management:** Keeping track of the visibility and accessibility of identifiers in different parts of the program.

**How Identifiers Are Stored**

The documents explain that the symbol table stores various attributes associated with each identifier. These attributes can include:

- **Name:** The identifier itself.
- **Type:** The data type of a variable or the return type of a function.
- **Scope:** Information about where the identifier is valid and accessible.
- **Memory location:** The address assigned to a variable.
- **Other information:** Such as size, storage class, and parameters (for functions).

The way this information is stored can vary depending on the specific implementation of the symbol table. Common techniques include using:

- **Hash tables:** For efficient lookup of identifiers.
- **Linked lists:** To handle collisions in hash tables or to maintain the order of declarations.
- **Tree structures:** For more complex scope management.

## <mark> 13) Explain dynamic storage allocation techniques. </mark>

Here are some key points regarding storage organization in a compiler:

- **Compiler's Role:** The compiler plays a crucial role in organizing how memory is used during program execution. This involves allocating space for variables, data structures, and managing function calls.
- **Memory Management:** Efficient storage organization is essential for optimizing program performance and ensuring correct execution.
- **Key Storage Areas:**
  - **Static Allocation:** Memory is allocated at compile time, and the size is fixed throughout the program's execution.
  - **Stack Allocation:** Memory is allocated and deallocated in a LIFO manner, primarily used for function calls and local variables.
  - **Heap Allocation:** Memory is dynamically allocated and deallocated during program execution, providing flexibility for data structures with varying sizes.
- **Activation Records:** These are used to manage information related to function calls, including local variables, parameters, and return addresses.
- **Symbol Table:** The compiler uses a symbol table to store information about identifiers (variables, functions, etc.) and their attributes (type, scope, etc.).
