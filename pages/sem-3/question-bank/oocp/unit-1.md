# Unit 1

## 1) Differentiate O.O.P and P.O.P

Here is a side-by-side comparison of Object-Oriented Programming (OOP) and Procedural-Oriented Programming (POP):

| Object-Oriented Programming (OOP)                                                  | Procedural-Oriented Programming (POP)                                           |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Focuses on creating objects that contain both data and methods                     | Focuses on breaking down a program into a collection of procedures or functions |
| Follows the principle of abstraction, encapsulation, inheritance, and polymorphism | Follows a top-down approach with a linear flow of control                       |
| Emphasizes data hiding and information hiding                                      | Emphasizes on the logic of the program rather than the data                     |
| Provides code reusability through inheritance                                      | Provides code reusability through functions                                     |
| Examples: C++, Java, Python, Ruby                                                  | Examples: C, Pascal, FORTRAN                                                    |
| Objects interact with each other through methods                                   | Functions call other functions to perform tasks                                 |
| Follows bottom-up approach                                                         | Follows top-down approach                                                       |
| Provides better data security                                                      | Provides less data security                                                     |
| Suitable for large and complex programs                                            | Suitable for small and simple programs                                          |

## 2) List out features of object oriented Language. Explain any one.

Here are the key features of Object-Oriented Programming (OOP):

1. **Encapsulation**: Combining data and methods that operate on that data within a single unit.
2. **Abstraction**: Showing only essential features of an object to the outside world.
3. **Inheritance**: Creating a new class based on an existing class.
4. **Polymorphism**: Having multiple forms of a method or operator.
5. **Composition**: Creating objects from other objects.
6. **Interface**: Defining a set of methods that must be implemented by a class.

Let's take a closer look at **Encapsulation**:

**Encapsulation** is a fundamental concept in Object-Oriented Programming (OOP). It involves bundling data and methods that operate on that data within a single unit, called a class or object. This approach helps to:

- **Hide Internal Details**: Encapsulation ensures that the internal implementation details of an object are not directly accessible from outside. This helps to prevent accidental changes or misuse of the object's internal state.
- **Control Access**: By encapsulating data and methods, you can control how and when the data is accessed or modified. This helps to maintain data integrity and prevent unauthorized changes.
- **Improve Code Organization**: Encapsulation helps to organize code in a more structured and modular way, making it easier to understand and maintain.

For example, consider a `BankAccount` class that encapsulates the account balance and methods to deposit and withdraw funds:

```cpp
class BankAccount {
private:
    double balance;

public:
    BankAccount(double initialBalance) : balance(initialBalance) {}

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            std::cout << "Insufficient funds!" << std::endl;
        }
    }

    double getBalance() {
        return balance;
    }
};

```

In this example, the `BankAccount` class encapsulates the `balance` data and provides methods to deposit, withdraw, and retrieve the balance. The internal implementation details of the class are hidden from the outside world, ensuring that the balance is not accidentally modified or accessed directly.

## 3) Name following operators and explain it. 1. `<<` 2. `>>`

The operators `<<` and `>>` are bitwise shift operators in C++.

### 1. `<<` (Left Shift Operator)

The left shift operator (`<<`) shifts the bits of the number to the left and fills 0 on voids left as a result. It is used to multiply the number by a power of 2.

### 2. `>>` (Right Shift Operator)

The right shift operator (`>>`) shifts the bits of the number to the right and fills the voids left with the sign bit (0 if the number is positive and 1 if the number is negative). It is used to divide the number by a power of 2.

Here is an example of how these operators work:

```cpp
#include <iostream>

int main() {
    int num = 8;  // Binary: 1000
    int leftShift = num << 1;  // Binary: 10000
    int rightShift = num >> 1;  // Binary: 0010

    std::cout << "Original Number: " << num << std::endl;
    std::cout << "Left Shift: " << leftShift << std::endl;
    std::cout << "Right Shift: " << rightShift << std::endl;

    return 0;
}

```

In this example, the number 8 is shifted left by one bit, resulting in 16. The number 8 is shifted right by one bit, resulting in 4.

## 4) Explain basic structure of c++.

The basic structure of a C++ program consists of the following elements:

1. **Include Directives**: These directives include necessary header files that provide access to predefined functions, classes, and variables. For example, `#include <iostream>` is used to access input/output functions like `std::cout` and `std::cin`.
2. **Namespace**: C++ uses namespaces to organize code and prevent naming conflicts. The `std` namespace is commonly used for standard library functions and objects. For example, `std::cout` and `std::endl` are part of the `std` namespace.
3. **Main Function**: Every C++ program must have a `main()` function, which is the entry point of the program. The `main()` function returns an integer value, typically 0 for successful execution or a non-zero value for an error.
4. **Variables and Data Types**: Variables are used to store data in memory. C++ supports various data types such as `int`, `float`, `double`, `char`, `bool`, and user-defined data types like classes and structs.
5. **Operators**: C++ provides a wide range of operators for performing various operations on data, such as arithmetic, relational, logical, and bitwise operators.
6. **Control Structures**: C++ provides control structures like `if-else`, `switch`, `for`, `while`, and `do-while` to control the flow of execution based on certain conditions.
7. **Functions**: Functions are named blocks of code that perform specific tasks. They can take parameters and return values. C++ supports function overloading, allowing multiple functions with the same name but different parameters.
8. **Classes and Objects**: C++ is an object-oriented programming language. Classes are user-defined data types that encapsulate data and functions. Objects are instances of classes.
9. **Preprocessor Directives**: Preprocessor directives are instructions processed by the preprocessor before compilation. They start with the `#` symbol, such as `#include`, `#define`, and `#ifdef`.

Here's a simple example of a C++ program that prints "Hello, World!" to the console:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

```

In this example, `#include <iostream>` includes the necessary header file for input/output operations. The `main()` function is the entry point of the program. `std::cout` is used to output the string "Hello, World!" to the console, and `std::endl` is used to insert a newline character. Finally, the program returns 0 to indicate successful execution.

## 5) List out c++ tokens and explain any one.

In C++, tokens are the basic building blocks of the language. The following are the different types of tokens in C++:

1. **Keywords**: Reserved words with predefined meanings, such as `if`, `else`, `for`, `while`, `int`, `char`, `class`, etc.
2. **Identifiers**: Names given to variables, functions, classes, etc. They must follow certain rules, such as starting with a letter or underscore and containing only letters, digits, and underscores.
3. **Literals**: Fixed values that can be assigned to variables, such as integer literals (e.g., `42`), floating-point literals (e.g., `3.14`), character literals (e.g., `'A'`), string literals (e.g., `"Hello, World!"`), and boolean literals (`true` and `false`).
4. **Operators**: Symbols that perform operations on operands, such as arithmetic operators (`+`, `, `, `/`, `%`), relational operators (`<`, `>`, `<=`, `>=`, `==`, `!=`), logical operators (`&&`, `||`, `!`), and bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`).
5. **Punctuators**: Special symbols used for various purposes, such as semicolons (`;`), commas (`,`), parentheses (`(`, `)`), brackets (`[`, `]`), braces (`{`, `}`), and the scope resolution operator (`::`).

Let's explain one of these tokens in more detail: **Identifiers**.

Identifiers are names given to variables, functions, classes, and other entities in C++. They are used to uniquely identify these elements within a program. Identifiers must follow these rules:

- They must start with a letter (uppercase or lowercase) or an underscore (`_`).
- After the first character, identifiers can contain letters, digits, and underscores.
- Identifiers are case-sensitive, meaning `myVariable` and `myvariable` are considered different identifiers.
- Identifiers cannot be the same as reserved keywords (e.g., `int`, `if`, `else`, etc.).
- Identifiers have a maximum length, which is implementation-defined (usually 255 characters or more).

Here are some examples of valid and invalid identifiers:

```cpp
// Valid identifiers
myVariable
_underscoreStart
variable123
camelCaseIdentifier
snake_case_identifier

// Invalid identifiers
1_invalidStart  // Starts with a digit
my variable    // Contains a space
my-variable    // Contains a hyphen
int            // Same as a keyword

```

Identifiers are crucial in C++ as they allow you to give meaningful names to variables, functions, and other entities, making your code more readable and maintainable.

## 6) Explain reference variable with example.

In C++, a **reference variable** is an alias for an existing variable. It allows you to use the same name for multiple variables, which can be useful for simplifying code and improving readability.

### Declaration of a Reference Variable

A reference variable is declared using the `&` symbol after the variable name. For example:

```cpp
int x = 10;
int &y = x;  // y is a reference to x

```

### Usage of a Reference Variable

Once a reference variable is declared, you can use it as if it were the original variable. This includes assigning values, performing operations, and accessing members.

Here is an example of using a reference variable:

```cpp
#include <iostream>

int main() {
    int x = 10;
    int &y = x;  // y is a reference to x

    std::cout << "Value of x: " << x << std::endl;
    std::cout << "Value of y: " << y << std::endl;

    y = 20;  // Modifying y also modifies x
    std::cout << "Value of x after modifying y: " << x << std::endl;

    return 0;
}

```

### Output

```
Value of x: 10
Value of y: 10
Value of x after modifying y: 20

```

In this example, `y` is a reference to `x`. When `y` is assigned a new value, `x` is also updated because `y` is an alias for `x`.

## 7) Explain scope resolution operator without using class.

The **scope resolution operator** (`::`) is used in C++ to specify the scope of a variable or function. It is used to distinguish between variables or functions with the same name but different scopes.

### Example Without Classes

Here is an example of using the scope resolution operator without classes:

```cpp
#include <iostream>

int globalVariable = 10;

int main() {
    int localVariable = 20;

    std::cout << "Global Variable: " << globalVariable << std::endl;
    std::cout << "Local Variable: " << localVariable << std::endl;

    return 0;
}

```

In this example, `globalVariable` and `localVariable` are two separate variables with different scopes. The `globalVariable` is accessible from anywhere in the program, while `localVariable` is only accessible within the `main()` function.

### Using the Scope Resolution Operator

To access `globalVariable` within `main()`, you would use the scope resolution operator:

```cpp
#include <iostream>

int globalVariable = 10;

int main() {
    int localVariable = 20;

    std::cout << "Global Variable: " << globalVariable << std::endl;
    std::cout << "Local Variable: " << localVariable << std::endl;

    return 0;
}

```

### Output

```
Global Variable: 10
Local Variable: 20

```

In this example, the scope resolution operator (`::`) is used to access `globalVariable` within `main()`, ensuring that the correct variable is accessed.

## 8) Explain memory management operators.

In C++, memory management operators are used to dynamically allocate and deallocate memory for variables and objects. Here are the key memory management operators:

### 1. `new` Operator

The `new` operator is used to dynamically allocate memory for a variable or object. It returns a pointer to the allocated memory.

```cpp
int* p = new int;  // Dynamically allocate memory for an integer

```

### 2. `delete` Operator

The `delete` operator is used to deallocate memory that was previously allocated using `new`. It takes a pointer to the memory to be deallocated as an argument.

```cpp
delete p;  // Deallocate the memory allocated for p

```

### 3. `new[]` Operator

The `new[]` operator is used to dynamically allocate memory for an array of variables or objects. It returns a pointer to the first element of the array.

```cpp
int* arr = new int[5];  // Dynamically allocate memory for an array of 5 integers

```

### 4. `delete[]` Operator

The `delete[]` operator is used to deallocate memory that was previously allocated using `new[]`. It takes a pointer to the first element of the array as an argument.

```cpp
delete[] arr;  // Deallocate the memory allocated for arr

```

### Example

Here is an example of using these operators:

```cpp
#include <iostream>

int main() {
    // Dynamically allocate memory for an integer
    int* p = new int;
    *p = 10;

    std::cout << "Value of p: " << *p << std::endl;

    // Deallocate the memory
    delete p;

    // Dynamically allocate memory for an array of 5 integers
    int* arr = new int[5];
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 2;
    }

    std::cout << "Values of arr: ";
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // Deallocate the memory
    delete[] arr;

    return 0;
}

```

### Output

```
Value of p: 10
Values of arr: 0 2 4 6 8

```

In this example, `new` and `delete` are used to dynamically allocate and deallocate memory for a single integer, while `new[]` and `delete[]` are used to dynamically allocate and deallocate memory for an array of integers.

## 9) Explain manipulators.

In C++, manipulators are special functions that are used to modify the behavior of input/output streams. They are typically used with `std::cout` and `std::cin` to format the output or input.

Here are some commonly used manipulators:

1. **`endl`**: Inserts a newline character and flushes the output buffer.

```cpp
std::cout << "Hello, World!" << std::endl;

```

1. **`setw`**: Sets the field width for the next value to be inserted.

```cpp
std::cout << std::setw(10) << "Value" << std::endl;

```

1. **`setfill`**: Sets the fill character for the field width.

```cpp
std::cout << std::setw(10) << std::setfill('0') << 42 << std::endl;

```

1. **`setprecision`**: Sets the precision for floating-point numbers.

```cpp
std::cout << std::setprecision(2) << 3.14159 << std::endl;

```

1. **`setbase`**: Sets the base for integer output (2 for binary, 8 for octal, 10 for decimal, or 16 for hexadecimal).

```cpp
std::cout << std::setbase(16) << 255 << std::endl;

```

1. **`setiosflags`** and **`resetiosflags`**: Set and reset format flags for the stream.

```cpp
std::cout << std::setiosflags(std::ios::fixed | std::ios::showpos) << 3.14 << std::endl;

```

1. **`left`, `right`, and `internal`**: Specify the alignment of the output within the field width.

```cpp
std::cout << std::left << std::setw(10) << "Left" << std::endl;

```

Here's an example that demonstrates the usage of some manipulators:

```cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << "Integer: " << 42 << std::endl;
    std::cout << "Float: " << 3.14159 << std::endl;

    std::cout << std::setw(10) << std::setfill('0') << 42 << std::endl;
    std::cout << std::setw(10) << std::setfill('0') << std::left << 42 << std::endl;

    std::cout << std::setprecision(2) << 3.14159 << std::endl;

    std::cout << std::hex << 255 << std::endl;
    std::cout << std::oct << 255 << std::endl;

    return 0;
}

```

Output:

```
Integer: 42
Float: 3.14159
0000000042
42000000
3.14
ff
377

```

Manipulators provide a convenient way to format input/output in C++ and make the code more readable and maintainable.

## 10) Explain inline function .

In C++, an inline function is a function that is expanded in-line when it is called. The compiler replaces the function call with the actual code of the function body.

### Declaring an Inline Function

To declare a function as inline, you need to use the `inline` keyword before the function return type. Here's an example:

```cpp
inline int add(int a, int b) {
    return a + b;
}

```

### Benefits of Inline Functions

1. **Improved Performance**: Inline functions can improve performance by eliminating the overhead of function calls, such as pushing arguments onto the stack and returning from the function.
2. **Reduced Compilation Time**: When a function is declared as inline, the compiler can optimize the function call by replacing it with the actual code of the function body, which can lead to faster compilation times.
3. **Better Code Readability**: Inline functions can make the code more readable by providing a concise way to perform simple operations without the need for a separate function call.

### Limitations of Inline Functions

1. **Compiler Discretion**: The compiler is not obligated to inline a function even if it is declared as inline. The compiler may choose not to inline a function based on various factors, such as the size of the function body or the number of function calls.
2. **Increased Code Size**: Inlining functions can lead to an increase in the size of the compiled code, as the function body is duplicated at each call site.
3. **Recursive Functions**: Inline functions cannot be recursive, as the compiler cannot inline a function that calls itself.
4. **Variadic Functions**: Inline functions cannot be variadic (functions that take a variable number of arguments), as the compiler cannot inline such functions.

Here's an example that demonstrates the usage of an inline function:

```cpp
#include <iostream>

inline int square(int x) {
    return x * x;
}

int main() {
    int result = square(5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}

```

Output:

```
Result: 25

```

In this example, the `square` function is declared as inline. When the `square(5)` function call is encountered in the `main` function, the compiler replaces it with the actual code of the `square` function body, which calculates the square of the argument.

It's important to note that the `inline` keyword is only a suggestion to the compiler, and the compiler may choose to ignore it based on various factors.

## 11) What is default argument?

In C++, a default argument is a value that is automatically assigned to a function parameter if no argument is provided when the function is called. This allows for more flexibility in function calls and can reduce the number of overloaded functions needed.

### Declaring Default Arguments

To declare a default argument, you specify the default value for the parameter in the function declaration, separated by an equal sign (`=`). Here's an example:

```cpp
int add(int a, int b, int c = 0) {
    return a + b + c;
}

```

In this example, `c` is a default argument with a default value of `0`.

### Using Default Arguments

When calling a function with default arguments, you can either provide all the arguments or omit the arguments with default values. If an argument is omitted, the default value is used.

```cpp
int result1 = add(1, 2);      // result1 = 3 (c is 0 by default)
int result2 = add(1, 2, 3);   // result2 = 6 (c is explicitly provided)

```

### Rules for Default Arguments

1. Default arguments must be placed at the end of the parameter list.
2. Once a default argument is encountered, all subsequent parameters must also have default arguments.
3. Default arguments can be constants, global variables, or functions that return constants.
4. Default arguments are resolved at compile-time, not at runtime.

Here's an example that demonstrates the usage of default arguments:

```cpp
#include <iostream>

int volume(int length, int width = 1, int height = 1) {
    return length * width * height;
}

int main() {
    std::cout << "Volume: " << volume(5) << std::endl;      // Volume: 5
    std::cout << "Volume: " << volume(5, 2) << std::endl;   // Volume: 10
    std::cout << "Volume: " << volume(5, 2, 3) << std::endl;// Volume: 30
    return 0;
}

```

In this example, the `volume` function has three parameters: `length`, `width`, and `height`. `width` and `height` have default values of `1`. When the function is called with only one argument (`volume(5)`), the default values are used for `width` and `height`, resulting in a volume of `5`. When called with two arguments (`volume(5, 2)`), the default value is used for `height`, resulting in a volume of `10`. When called with all three arguments (`volume(5, 2, 3)`), the provided values are used, resulting in a volume of `30`.

Default arguments provide a convenient way to make function calls more flexible and reduce the need for overloaded functions.

## 12) Write a c.p.p program to……using friend function.

Here is a C++ program that demonstrates the use of a friend function to add two complex numbers:

```cpp
#include <iostream>

class Complex {
private:
    double real;
    double imag;

public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    void display() {
        std::cout << real << " + " << imag << "i" << std::endl;
    }

    friend Complex add(Complex c1, Complex c2);
};

Complex add(Complex c1, Complex c2) {
    Complex temp;
    temp.real = c1.real + c2.real;
    temp.imag = c1.imag + c2.imag;
    return temp;
}

int main() {
    Complex c1(3.0, 4.0);
    Complex c2(2.0, 5.0);

    std::cout << "Complex Number 1: ";
    c1.display();

    std::cout << "Complex Number 2: ";
    c2.display();

    Complex c3 = add(c1, c2);

    std::cout << "Sum of Complex Numbers: ";
    c3.display();

    return 0;
}

```

Output:

```
Complex Number 1: 3 + 4i
Complex Number 2: 2 + 5i
Sum of Complex Numbers: 5 + 9i

```

In this program, the `Complex` class represents complex numbers with real and imaginary parts. The `add` function is a friend function that takes two `Complex` objects as arguments and returns their sum. The `main` function demonstrates the usage of the `add` function to add two complex numbers.

The `add` function is declared as a friend function inside the `Complex` class, which allows it to access the private members of the class. This is necessary because the `add` function needs to access the real and imaginary parts of the complex numbers to perform the addition.

The `main` function creates two `Complex` objects, `c1` and `c2`, and then calls the `add` function to add them. The result is stored in `c3`, which is then displayed using the `display` method.

This program demonstrates how friend functions can be used to extend the functionality of a class without modifying its internal implementation.

## 13) What are the limitations of structures in 'C'?

In C, structures have several limitations:

1. **No Inheritance**: Structures in C do not support inheritance, which means that a structure cannot inherit properties or methods from another structure.
2. **No Polymorphism**: Structures in C do not support polymorphism, which means that a structure cannot be treated as a different type based on its contents.
3. **No Encapsulation**: Structures in C do not support encapsulation, which means that the data members of a structure are accessible directly and can be modified from outside the structure.
4. **No Abstraction**: Structures in C do not support abstraction, which means that the internal implementation details of a structure are accessible directly and cannot be hidden from the outside world.
5. **No Operator Overloading**: Structures in C do not support operator overloading, which means that you cannot define custom behavior for operators like `+`, `, `, `/`, etc.
6. **No Exception Handling**: Structures in C do not support exception handling, which means that you cannot handle runtime errors or exceptions in a structured way.
7. **No Template Metaprogramming**: Structures in C do not support template metaprogramming, which means that you cannot write code that is executed at compile-time based on the properties of a structure.
8. **No Lambda Functions**: Structures in C do not support lambda functions, which means that you cannot define small, anonymous functions that can be used as arguments to higher-order functions.
9. **No Type Safety**: Structures in C do not provide type safety, which means that you can assign a value of one type to a variable of another type without any errors.
10. **No Garbage Collection**: Structures in C do not provide garbage collection, which means that you need to manually manage memory and avoid memory leaks.

These limitations are due to the fact that C is a low-level, procedural programming language that is designed for efficiency and portability. While structures are a powerful tool for organizing data, they are not as powerful as the data structures and abstractions provided by modern programming languages like C++ or Java.
