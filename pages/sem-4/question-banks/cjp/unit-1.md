# Unit 1

## 1) Explain features of java with Example.

Java is a high-level programming language with several key features:

- **Platform Independent:** Once compiled, Java code can be run on any platform that has the Java Virtual Machine (JVM), without the need for recompilation. For example, a program written on Windows can run on Mac or Linux, as long as they have JVM installed.
- **Object-Oriented:** Java uses object-oriented programming (OOP) principles which include classes, objects, inheritance, encapsulation, polymorphism, and abstraction. For example, in a Java program modeling a car, "Car" could be a class, and each individual car would be an object of that class.
- **Robust:** Java has a strong memory management system, exception handling, and type checking mechanism, making it less prone to errors and security issues. For example, Java's garbage collection feature automatically deletes objects that are no longer in use, preventing memory leaks.
- **Multi-threaded:** Java supports multithreading, allowing multiple operations to run concurrently, improving the efficiency of programs. For example, a Java application could handle multiple user inputs simultaneously by assigning a separate thread to each user.
- **Secure:** Java is designed with security as a priority. Its platform independence and lack of explicit pointer use make it more secure against viral attacks and hacker threats. For example, Java’s security manager and bytecode verifier work together to ensure that class files adhere to Java’s safety rules.

## 2) Explain JVM, JDK and JRE.

1. **Java Virtual Machine (JVM):**
   - **Definition:** JVM is a crucial part of the Java platform that provides an execution environment for Java bytecode. It interprets the bytecode and translates it into machine-specific code, enabling Java programs to run on any device with a JVM installed.
   - **Functionality:** JVM ensures platform independence by executing Java programs in a consistent manner across different systems. It handles memory management, garbage collection, and provides security features to prevent unauthorized access to system resources.
   - **Key Role:** JVM acts as an intermediary between the Java code and the underlying hardware, abstracting the complexities of the hardware architecture and enabling Java's "write once, run anywhere" capability.
2. **Java Development Kit (JDK):**
   - **Definition:** JDK is a comprehensive software development kit that includes tools necessary for developing Java applications. It contains the JRE, compiler, debugger, and other development tools.
   - **Components:** JDK comprises the Java compiler (javac) for converting Java source code into bytecode, various development tools for debugging and monitoring, and libraries to support application development.
   - **Usage:** Developers use the JDK to write, compile, and debug Java programs. It provides a complete set of tools and resources needed for Java application development.
3. **Java Runtime Environment (JRE):**
   - **Definition:** JRE is an environment that provides the minimum requirements for executing Java applications. It includes the JVM, class libraries, and other necessary files to run Java programs.
   - **Functionality:** JRE does not contain development tools like the JDK; instead, it focuses on executing Java applications. It ensures that Java programs can run smoothly by providing the necessary runtime environment.
   - **Deployment:** End-users who want to run Java applications need to install the JRE on their systems. It allows them to execute Java programs without the need for development tools.

## 3) What is variable? Give one example program for defining variables in java. Also list rules for valid variable names.

A variable is a name given to a memory location in Java. It's a way to store data for later use. Each variable in Java has a specific data type, which determines the size and layout of the variable's memory, the range of values that can be stored within that memory, and the set of operations that can be applied to the variable.

Here's an example of how to define variables in Java:

```java
public class Main {
    public static void main(String[] args) {
        int myNumber = 5; // variable of type int
        String myString = "Hello"; // variable of type String
        double myDouble = 3.14; // variable of type double
    }
}

```

The rules for naming variables in Java are:

- Variable names are case-sensitive.
- A variable name must begin with a letter, underscore (\_), or dollar sign ($). It cannot begin with a number.
- After the first character, variable names can contain any combination of letters, numbers, underscores, or dollar signs.
- Reserved words (like `int`, `double`, `if`, etc.) cannot be used as variable names.

## 4) Explain this keyword with Example.

In Java, `this` is a reference variable that refers to the current object. It can be used to refer to the instance variables of the current class, to invoke the instance methods, or to return the current class instance.

Here's an example showing how to use `this` keyword to refer to the instance variable:

```java
public class Car {
    String color;

    // Constructor
    Car(String color) {
        this.color = color; // 'this' refers to the instance variable
    }

    void printColor() {
        System.out.println("Car color is: " + color);
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("Red");
        myCar.printColor(); // It prints: Car color is: Red
    }
}

```

In this example, `this.color` refers to the `color` instance variable of the `Car` class. It is used to distinguish between the instance variable `color` and the parameter `color` in the `Car` constructor.

## 5) Explain static keyword with Example.

In Java, the `static` keyword is used to create fields and methods that belong to the class, rather than to an instance of the class. This means that you can access the static field or call the static method without creating an instance of the class.

Here's an example showing how to use the `static` keyword:

```java
public class Counter {
    static int count = 0; // static variable

    // static method
    static void incrementCount() {
        count++;
    }

    // method to display the current count
    static void displayCount() {
        System.out.println("Count is: " + count);
    }
}

public class Main {
    public static void main(String[] args) {
        Counter.incrementCount(); // calling the static method
        Counter.incrementCount();
        Counter.displayCount(); // It prints: Count is: 2
    }
}

```

In this example, `count` is a static variable that is shared by all instances of the `Counter` class. The `incrementCount()` and `displayCount()` are static methods that can be called without creating an instance of the `Counter` class.

## 6) Explain finalize() and garbage collection with Example.

In Java, garbage collection is an automatic memory management system that frees up memory that is no longer needed. When an object is no longer reachable or referenced by any part of the program, it is considered eligible for garbage collection. The garbage collector, a part of the JVM, deallocates memory for these objects, preventing memory leaks and optimizing the use of system resources.

The `finalize()` method in Java is a special method that is invoked by the garbage collector just before an object is being collected. This method is part of the `java.lang.Object` class and can be overridden in your class to define cleanup operations before the object is garbage collected. It's important to note that the invocation of `finalize()` is not guaranteed and should not be relied upon for critical resource management tasks.

Here's an example of how `finalize()` could be used:

```java
public class MyClass {

    @Override
    protected void finalize() throws Throwable {
        try {
            // release resources, perform cleanup ;
        } finally {
            super.finalize();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj = null; // obj is now eligible for garbage collection
        System.gc(); // request to run the garbage collector
    }
}

```

In this example, we override the `finalize()` method in our `MyClass` class to perform some cleanup operation. We then create an instance of `MyClass` in our `main` method, set the instance `obj` to `null` to make it eligible for garbage collection, and call `System.gc()` to request the JVM to run the garbage collector.

## 7) Explain Ragged Array With Examples.

A ragged array, also known as a jagged array, is a multi-dimensional array in which the length of each array element can be different. This is in contrast to a rectangular multi-dimensional array where every row must have the same number of columns. In other words, a ragged array is an array of arrays of potentially different sizes.

Here's an example of a ragged array in Java:

```java
public class Main {
    public static void main(String[] args) {
        // Declare and initialize a ragged array
        int[][] raggedArray = {
            {1, 2, 3},
            {4, 5},
            {6, 7, 8, 9}
        };

        // Print the ragged array
        for (int i = 0; i < raggedArray.length; i++) {
            for (int j = 0; j < raggedArray[i].length; j++) {
                System.out.print(raggedArray[i][j] + " ");
            }
            System.out.println();
        }
    }
}

```

In this example, `raggedArray` is a 2-dimensional ragged array. The first row has 3 elements, the second row has 2 elements, and the third row has 4 elements. This is a valid ragged array because each row can have a different number of columns.

## 8) Write a java program that creates and initialises a four integer element array. Calculate and display the average of its values.

Here is the Java program:

```java
public class Main {
    public static void main(String[] args) {
        // Create and initialize an array
        int[] numbers = {10, 20, 30, 40};

        // Calculate the sum
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }

        // Calculate and display the average
        double average = (double) sum / numbers.length;
        System.out.println("The average is: " + average);
    }
}

```

In this program, we first create and initialize an array of four integer elements. We then calculate the sum of the array elements using a for-each loop. Finally, we calculate the average by dividing the sum by the length of the array and display the result.

## 9) Declare a class called employee having employee_id and employee_name as members. Extend class employees to have a subclass called salary having designation and monthly_salary as members.

Define following:

- Required constructors
- A method to find and display all details of employees drawing salaries more than Rs. 20000/-.
- Method main for creating an array for storing these details given as command line
  arguments and showing usage of above methods.

```java
public class Employee {
    int employee_id;
    String employee_name;

    // Constructor
    Employee(int id, String name) {
        employee_id = id;
        employee_name = name;
    }
}

public class Salary extends Employee {
    String designation;
    double monthly_salary;

    // Constructor
    Salary(int id, String name, String desig, double salary) {
        super(id, name); // calling Employee class constructor
        designation = desig;
        monthly_salary = salary;
    }

    // Method to display details of employees with salary more than Rs. 20000/-
    void displayDetails() {
        if (monthly_salary > 20000) {
            System.out.println("Employee ID: " + employee_id);
            System.out.println("Employee Name: " + employee_name);
            System.out.println("Designation: " + designation);
            System.out.println("Monthly Salary: " + monthly_salary);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an array of Salary objects
        Salary[] employees = new Salary[3];
        employees[0] = new Salary(1, "John", "Engineer", 30000);
        employees[1] = new Salary(2, "Jane", "Manager", 50000);
        employees[2] = new Salary(3, "Jim", "Assistant", 15000);

        // Display details of employees with salary more than Rs. 20000/-
        for (Salary employee : employees) {
            employee.displayDetails();
        }
    }
}

```

In this code, we have an `Employee` class with `employee_id` and `employee_name` as members. The `Salary` class extends `Employee` and adds `designation` and `monthly_salary` as members. The `Salary` class also has a `displayDetails` method that displays the details of employees with a salary more than Rs. 20000/-. Finally, in the `main` method, we create an array of `Salary` objects and call the `displayDetails` method on each of them.

## 10) Differentiate String class and StringBuffer class with explanation of its methods.

| Aspect        | `String`                                                                                                                              | `StringBuffer`                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Immutability  | `String` is immutable. Once a `String` object is created, its value cannot be changed.                                                | `StringBuffer` is mutable. You can modify the value of a `StringBuffer` object.                                        |
| Performance   | Concatenation operations with `String` create a new object, which can be less efficient when performing a large number of operations. | `StringBuffer` allows modifications to the same object, making it more efficient for operations like concatenation.    |
| Thread Safety | `String` is thread-safe because it is immutable. It doesn't need synchronization due to its immutability.                             | `StringBuffer` is thread-safe. It is safe to use in a multi-threaded environment because its methods are synchronized. |

**Commonly used methods:**

| `String` methods                          | Explanation                                                  | `StringBuffer` methods         | Explanation                                              |
| ----------------------------------------- | ------------------------------------------------------------ | ------------------------------ | -------------------------------------------------------- |
| `charAt(int index)`                       | Returns the character at the specified index.                | `append(String str)`           | Appends the specified string to this character sequence. |
| `concat(String str)`                      | Concatenates the specified string to the end of this string. | `insert(int offset, String s)` | Inserts the string into this character sequence.         |
| `length()`                                | Returns the length of this string.                           | `length()`                     | Returns the length (character count) of this sequence.   |
| `substring(int beginIndex, int endIndex)` | Returns a new string that is a substring of this string.     | `delete(int start, int end)`   | Removes the characters in a substring of this sequence.  |

In summary, both `String` and `StringBuffer` classes have their own uses in Java programming. `String` is ideal for string literals and fixed strings, while `StringBuffer` is more suited for dynamic strings where modification operations are frequently performed.

## 11) Differentiate StringBuilder class and StringBuffer class with explanation of its methods.

| Aspect        | StringBuilder                                                                                     | StringBuffer                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Mutability    | StringBuilder is mutable. You can modify the value of a StringBuilder object.                     | StringBuffer is also mutable. You can modify the value of a StringBuffer object.                                     |
| Performance   | StringBuilder is more efficient in terms of performance because its methods are not synchronized. | StringBuffer is less efficient because its methods are synchronized to allow thread-safety.                          |
| Thread Safety | StringBuilder is not thread-safe. It is not safe to use in a multi-threaded environment.          | StringBuffer is thread-safe. It is safe to use in a multi-threaded environment because its methods are synchronized. |

**Commonly used methods:**

| StringBuilder methods        | Explanation                                              | StringBuffer methods         | Explanation                                              |
| ---------------------------- | -------------------------------------------------------- | ---------------------------- | -------------------------------------------------------- |
| append(String str)           | Appends the specified string to this character sequence. | append(String str)           | Appends the specified string to this character sequence. |
| insert(int offset, String s) | Inserts the string into this character sequence.         | insert(int offset, String s) | Inserts the string into this character sequence.         |
| length()                     | Returns the length (character count) of this sequence.   | length()                     | Returns the length (character count) of this sequence.   |
| delete(int start, int end)   | Removes the characters in a substring of this sequence.  | delete(int start, int end)   | Removes the characters in a substring of this sequence.  |

In summary, both `StringBuilder` and `StringBuffer` classes are used for creating mutable strings. However, `StringBuilder` is generally preferred over `StringBuffer` for single-threaded applications, as it is faster due to the lack of synchronization.

## 12) What is a Wrapper class in Java? Explain with examples.

A wrapper class in Java is a class that encapsulates (or "wraps") primitive data types so that they can be used as objects. Java provides a wrapper class for each of the eight primitive data types. These are Integer, Character, Double, Float, Byte, Short, Long, and Boolean.

One of the main reasons to use wrapper classes is that they provide a way to use primitive data types in situations that require objects, such as in Java collections or with generics. Wrapper classes also provide a number of utility methods for converting, comparing, and performing operations on the underlying primitive values.

Here's an example of using a wrapper class in Java:

```java
Integer myInt = Integer.valueOf(10); // creating an Integer object

int primitiveInt = myInt.intValue(); // converting the Integer object back to an int

System.out.println("Primitive int value: " + primitiveInt); // prints "Primitive int value: 10"

```

In this example, we first create an `Integer` object from an `int` value using the `Integer.valueOf()` method. We then convert the `Integer` object back to an `int` value using the `Integer.intValue()` method.

## 13) There is no destructor in Java. Justify.

In Java, the concept of destructors, as known in languages such as C++ and others, does not exist. This is primarily because Java has an in-built garbage collector which handles the task of memory management.

In languages such as C++, the destructor is a special function for a class that is called whenever an object of that class goes out of scope or is explicitly deleted. A destructor is used to de-allocate memory that was previously allocated to the object by the constructor.

In contrast, Java operates on a different principle. Instead of destructors, Java provides a system of automated garbage collection. The garbage collector operates in the background, efficiently managing memory by automatically freeing up memory resources that are no longer needed by the program, i.e., objects that are no longer accessible in the program.

The garbage collector works by tracking object references. If an object is not referenced anywhere in the program, it is considered not needed and is made eligible for garbage collection. The garbage collector then reclaims the heap memory that was allocated to the object, freeing up the memory for future use.

Java does provide a mechanism that resembles destructors - the `finalize()` method. This method is called by the garbage collector on an object when garbage collection determines that there are no more references to the object. However, it's important to note that `finalize()` is not a destructor and should not be used as such. The `finalize()` method is meant to give an object the last chance to perform any cleanup before it is collected. The behavior of `finalize()` is not predictable and it's generally not recommended to rely on this method for critical tasks. It's also worth noting that the use of `finalize()` is deprecated since Java 9.

In conclusion, Java's automated garbage collection and the lack of explicit pointer manipulation eliminates the need for destructors in the language. This design choice simplifies memory management and helps avoid common errors such as memory leaks and dangling pointers that are often encountered in languages where developers have to manually manage memory.

## 14) Differentiate POP and OOP.

| Aspect               | Procedure Oriented Programming (POP)                                                   | Object Oriented Programming (OOP)                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Focus                | The focus is on the procedures or functions, and data is not given as much importance. | The focus is on the data rather than procedures. Procedures revolve around the data, securing it from easy access by external functions or programs. |
| Division             | The program is divided into small parts called procedures.                             | The program is divided into small parts called objects.                                                                                              |
| Data Movement        | Data can move freely from function to function in the system.                          | Data cannot move freely from function to function; it can be accessed only within a single class.                                                    |
| Programming Paradigm | It follows a top-down programming paradigm.                                            | It follows a bottom-up programming paradigm.                                                                                                         |
| Data Security        | In POP, data is exposed to the whole program, which can lead to unauthorized access.   | In OOP, data hiding is possible, making it more secure.                                                                                              |
| Examples             | Examples of POP languages include C, FORTRAN, and COBOL.                               | Examples of OOP languages include Java, C++, and Python.                                                                                             |

## 15) State whether any error exists in the following code. If so, correct the error and give output.

class Test {
public static void main(String args[]) {
A a = new A();
a.print();
}
}
class A {
String s;
A(String s) {
this.s=s;
}
public void print() {
System.out.println(s);
}
}

Yes, there is an error in the code. The class `A` has a constructor that takes a `String` parameter, but when creating a new object `a` of class `A` in the `main` method, no arguments are being passed to the constructor. This will result in a compilation error.

The corrected code should look like this:

```java
class Test {
    public static void main(String args[]) {
        A a = new A("Hello, World!"); // Pass a String to the constructor
        a.print();
    }
}

class A {
    String s;
    A(String s) {
        this.s = s;
    }
    public void print() {
        System.out.println(s);
    }
}

```

When you run this corrected code, it will print:

```
Hello, World!

```

## 16) Write a java program to do the sum of command line arguments passed two Double numbers.

```java
public class Main {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Please provide two double numbers as arguments.");
            return;
        }

        try {
            double num1 = Double.parseDouble(args[0]);
            double num2 = Double.parseDouble(args[1]);

            double sum = num1 + num2;

            System.out.println("Sum of " + num1 + " and " + num2 + " is " + sum);
        } catch (NumberFormatException e) {
            System.out.println("Please ensure the arguments passed are valid double numbers.");
        }
    }
}

```

This Java program takes two command line arguments, converts them to double values, sums them, and then prints the result. If less than two arguments are provided, or if the arguments cannot be converted to double values, an error message is printed.

## 17) Discuss public, private, protected and default access modifiers with examples. OR What is a visibility modifier? Explain all with examples.

In Java, access modifiers are keywords that set the access levels for classes, variables, methods, and constructors. They are used to restrict the scope of variables, methods, classes, and constructors. There are four types of access modifiers in Java:

1. **Public**: The public access modifier is accessible everywhere. It has the widest scope among all other modifiers.

```java
public class MyPublicClass {
    public String myPublicMethod() {
        return "Hello, world!";
    }
}

```

In this example, both the class `MyPublicClass` and the method `myPublicMethod` are declared as public, so they can be accessed from any other class.

1. **Private**: The private access modifier is accessible only within the class.

```java
public class MyPrivateClass {
    private String myPrivateMethod() {
        return "Hello, world!";
    }
}

```

In this example, the method `myPrivateMethod` is declared as private, so it can only be accessed within the `MyPrivateClass` class. If you try to access it from another class, it will result in a compile-time error.

1. **Protected**: The protected access modifier is accessible within the same package and also for subclasses in any package.

```java
protected class MyProtectedClass {
    protected String myProtectedMethod() {
        return "Hello, world!";
    }
}

```

In this example, both the class `MyProtectedClass` and the method `myProtectedMethod` are declared as protected, so they can be accessed from any class in the same package and from subclasses in any package.

1. **Default**: If no access modifier is specified, then it is default by nature and is accessible only within the same package.

```java
class MyDefaultClass {
    String myDefaultMethod() {
        return "Hello, world!";
    }
}

```

In this example, both the class `MyDefaultClass` and the method `myDefaultMethod` have no access modifier specified, so they are default by nature and can be accessed only from within the same package.

In conclusion, access modifiers are an important part of Java because they manage the visibility of class, interface, variables, methods, and constructors. By using them properly, we can ensure proper encapsulation in our code.

## 18) Explain recursion in java with example.

Recursion in Java is a process where a method calls itself continuously. A method in Java that calls itself is called a recursive method. It makes the code compact but complex to understand. The basic idea is to divide the problem into smaller sub-problems until it becomes simple enough to be solved directly.

Here is an example of a simple recursive method to calculate the factorial of a number:

```java
public class Main {
    static int factorial(int n) {
        if (n == 0)
            return 1;
        else
            return(n * factorial(n-1));
    }

    public static void main(String[] args) {
        int number = 5;
        int fact = factorial(number);
        System.out.println("Factorial of " + number + " is: " + fact);
    }
}

```

In this example, the `factorial` method calls itself to find the factorial of a number. The base case is when `n` is 0, in which case the method returns 1. For all other cases, the method calls itself with the argument `n-1` and multiplies the result by `n`. This process continues until the base case is reached. The result is the factorial of the original number.

Please note, it's crucial to have a base case in recursive methods to prevent them from calling themselves infinitely, which would result in a `StackOverflowError`.

## 19) Define Inner class. List and explain nested class with example.

An Inner class, or nested class, is a class defined within another class in Java. Nested classes are divided into two types: static and non-static. Non-static nested classes are also known as inner classes.

1. **Inner Class**: An inner class is a non-static nested class. It has access to all of the enclosing class's members, including its private members. Because an inner class is associated with an instance of the outer class, it cannot define any static methods or variables itself.

Here's an example of an inner class:

```java
public class OuterClass {
    private String msg = "Hello, World!";

    class InnerClass {
        void display() {
            System.out.println(msg);
        }
    }

    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.display(); // prints "Hello, World!"
    }
}

```

In this example, `InnerClass` is an inner class of `OuterClass`. It has access to `OuterClass`'s private member `msg` and displays it when its `display` method is called.

1. **Static Nested Class**: A static nested class is a static class defined at the member level. It can access the static members of the outer class, including private ones, but it cannot access non-static members.

Here's an example of a static nested class:

```java
public class OuterClass {
    static String msg = "Hello, World!";

    static class NestedStaticClass {
        void printMessage() {
            System.out.println(msg); // can access static member of outer class
        }
    }

    public static void main(String[] args) {
        OuterClass.NestedStaticClass printer = new OuterClass.NestedStaticClass();
        printer.printMessage(); // prints "Hello, World!"
    }
}

```

In this example, `NestedStaticClass` is a static nested class of `OuterClass`. It can access the static member `msg` of `OuterClass` and prints it when its `printMessage` method is called.
