# Assignment : 1

## 1) JVM is platform dependent. Justify.

Yes, the Java Virtual Machine (JVM) is platform dependent. Here's why:

1. **Bytecode Interpretation**: Java source code is compiled into bytecode, which is platform-independent. However, the JVM interprets this bytecode into machine code, which is specific to the underlying hardware and operating system. This interpretation process makes the JVM platform dependent.
2. **Native Libraries**: JVM implementations often rely on native libraries and system calls to perform certain tasks. These native libraries are specific to the underlying platform, contributing to the platform dependency of the JVM.
3. **Memory Management**: The JVM manages memory allocation and garbage collection, which can vary depending on the platform's memory management mechanisms and constraints. This platform-specific memory management adds to the JVM's platform dependency.
4. **Hardware Interaction**: The JVM interacts with hardware components such as the CPU, memory, and I/O devices. Since different platforms have different hardware architectures and specifications, the JVM needs to be implemented differently for each platform.

Due to these reasons, the JVM is considered platform dependent, requiring specific implementations for different operating systems and hardware platforms.

## 2) Write down different between String and StringBuffer class.

Here are the main differences between the `String` and `StringBuffer` classes in Java:

1. **Mutability**:
   - `String`: Immutable. Once a `String` object is created, its value cannot be changed. Any operation that appears to modify a `String` actually creates a new `String` object.
   - `StringBuffer`: Mutable. A `StringBuffer` object can be modified after it is created using various methods without creating a new object.
2. **Performance**:
   - `String`: Less efficient for concatenation or frequent modifications because it involves creating new `String` objects.
   - `StringBuffer`: More efficient for concatenation or frequent modifications due to its mutable nature. It uses a dynamically expandable buffer to store characters, reducing the need for creating new objects.
3. **Thread Safety**:
   - `String`: Immutable and therefore thread-safe. Multiple threads can safely access a `String` object without synchronization issues.
   - `StringBuffer`: Mutable and therefore not thread-safe by default. To ensure thread safety, `StringBuffer` provides synchronized methods, but this can impact performance.
4. **Usability**:
   - `String`: Suitable for situations where the value of the string is not expected to change frequently.
   - `StringBuffer`: Suitable for situations where frequent modifications to the string are required, such as in loops or when building a string dynamically.

In summary, the choice between `String` and `StringBuffer` depends on the specific requirements of your program. Use `String` when immutability and thread safety are desired, and use `StringBuffer` when you need mutability and efficient string modifications.

## OR

| Feature           | String                               | StringBuffer                                      |
| ----------------- | ------------------------------------ | ------------------------------------------------- |
| **Mutability**    | Immutable                            | Mutable                                           |
| **Performance**   | Less efficient for concatenation     | More efficient for concatenation                  |
| **Memory Usage**  | Creates a new object for each change | Modifies the existing object without creating new |
| **Thread Safety** | Thread-safe (immutable)              | Not thread-safe (mutable)                         |
| **Usage**         | Suitable for immutable strings       | Suitable for modifiable strings                   |

## 3) Explain command line argument with proper program.

Command-line arguments are values provided to a program when it is executed from the command line or terminal. These arguments are passed to the `main` method of the program as an array of strings. Here's a simple Java program that demonstrates how to use command-line arguments:

```java
public class CommandLineArguments {
    public static void main(String[] args) {
        // Check if any arguments were provided
        if (args.length == 0) {
            System.out.println("No arguments provided.");
        } else {
            // Print the number of arguments
            System.out.println("Number of arguments: " + args.length);

            // Print all arguments
            System.out.println("Arguments:");
            for (int i = 0; i < args.length; i++) {
                System.out.println("Argument " + (i + 1) + ": " + args[i]);
            }
        }
    }
}

```

To run this program with command-line arguments, follow these steps:

1. Save the code above into a file named `CommandLineArguments.java`.
2. Compile the program using the command `javac CommandLineArguments.java`.
3. Run the program with some arguments, for example: `java CommandLineArguments arg1 arg2 arg3`.

In this example, if you run the program with the command `java CommandLineArguments arg1 arg2 arg3`, the output will be:

```
Number of arguments: 3
Arguments:
Argument 1: arg1
Argument 2: arg2
Argument 3: arg3

```

The program prints the number of arguments provided and then prints each argument along with its position in the array.

## 4) What is use of wrapper class? Explain important methods of wrapper class.

Wrapper classes in Java are used to represent primitive data types as objects. They provide a way to use primitive data types in situations that require objects, such as collections (like `ArrayList` and `HashMap`) and generics. Wrapper classes also provide utility methods for converting primitive types to and from strings, as well as other useful functionalities.

Here are some important methods of wrapper classes:

1. **valueOf()**: This static method is used to create a wrapper object from a primitive value or a string. For example, `Integer.valueOf(10)` creates an `Integer` object with the value 10.
2. **parseXxx()**: These static methods are used to parse a string into a primitive type. For example, `Integer.parseInt("10")` returns the integer 10.
3. **toString()**: This method returns the string representation of the object. For example, `Integer.toString(10)` returns the string "10".
4. **intValue(), doubleValue(), floatValue(), etc.**: These methods return the primitive value of the object. For example, `Integer.valueOf(10).intValue()` returns the integer 10.
5. **equals()**: This method compares two wrapper objects for equality, returning true if they are equal and false otherwise.
6. **compareTo()**: This method compares two wrapper objects numerically, returning a negative value if the first object is less than the second, zero if they are equal, and a positive value if the first object is greater than the second.

Wrapper classes are also used in Java's autoboxing and unboxing feature, which automatically converts between primitive types and their corresponding wrapper classes when needed.

## 5) Explain following keyword

- final
- static
- this
- super

Here's a brief explanation of each of these keywords in Java:

1. **Final**:
   - When applied to a variable, `final` indicates that the variable's value cannot be changed once initialized.
   - When applied to a method, `final` prevents the method from being overridden by subclasses.
   - When applied to a class, `final` prevents the class from being subclassed.
2. **Static**:
   - When applied to a variable, `static` indicates that the variable belongs to the class itself, rather than to instances of the class. There will be only one copy of the variable shared among all instances of the class.
   - When applied to a method, `static` indicates that the method belongs to the class, not to instances of the class. Static methods can be called directly on the class without creating an instance.
   - When applied to a block of code, `static` indicates a static initializer block, which is executed when the class is loaded into memory.
3. **this**:
   - `this` is a reference to the current object within an instance method or constructor.
   - It is used to access instance variables and methods of the current object, to differentiate between instance variables and local variables with the same name, and to pass the current object as a parameter to other methods.
4. **super**:
   - `super` is a reference to the superclass of the current object.
   - It is used to call superclass constructors, to access superclass methods and variables that are hidden by subclass methods or variables, and to pass the current object as a parameter to other methods in the superclass.

These keywords are fundamental in Java and are used extensively in class definitions to control behavior, manage data, and facilitate inheritance.
