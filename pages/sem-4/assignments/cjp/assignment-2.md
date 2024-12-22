# Assignment : 2

## 1) Write down different between interface and abstract class with proper syntax.

Here's a side-by-side comparison of interfaces and abstract classes in Java, along with their syntax:

| Feature                  | Interface                                                 | Abstract Class                                                |
| ------------------------ | --------------------------------------------------------- | ------------------------------------------------------------- |
| **Definition**           | Interface defines a contract for what a class can do.     | Abstract class is a partially implemented class.              |
| **Multiple Inheritance** | Interfaces support multiple inheritance.                  | Abstract classes do not support multiple inheritance.         |
| **Constructor**          | Interfaces cannot have constructors.                      | Abstract classes can have constructors.                       |
| **Fields**               | Interfaces cannot have instance fields.                   | Abstract classes can have instance fields.                    |
| **Implementation**       | All methods in an interface are implicitly abstract.      | Abstract classes can have both abstract and concrete methods. |
| **Default Methods**      | Interfaces can have default methods with implementations. | Abstract classes cannot have default methods.                 |
| **Access Modifiers**     | Interface methods are implicitly public.                  | Abstract class methods can have any access modifier.          |
| **Extending**            | Interfaces are extended using the `extends` keyword.      | Abstract classes are extended using the `extends` keyword.    |
| **Purpose**              | Interfaces are used for defining contracts.               | Abstract classes are used to provide a base for subclasses.   |
| **Example Syntax**       | `public interface Animal {                                |

void eat();
void sleep();` | public abstract class Shape {
abstract void draw();
void display() {
System.out.println("Displaying shape");
}
} |

## 2) What is dynamic method dispatch? Write a program to implement of dynamic method dispatch.

Dynamic method dispatch is a mechanism in Java where the method to be invoked is determined at runtime rather than at compile time. It allows a subclass to provide a specific implementation of a method that is already provided by its superclass.

Here's a simple program that demonstrates dynamic method dispatch:

```java
// Superclass
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}

// Subclass
class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Dog(); // Dog object
        Animal animal2 = new Cat(); // Cat object

        animal1.makeSound(); // Calls Dog's makeSound method
        animal2.makeSound(); // Calls Cat's makeSound method
    }
}

```

In this program, `Animal` is the superclass with a method `makeSound`, and `Dog` and `Cat` are subclasses that override the `makeSound` method. At runtime, the `makeSound` method of the actual object type (either `Dog` or `Cat`) is invoked, demonstrating dynamic method dispatch.

## 3) What is package? Explain different types of access specified in java programming.

A package in Java is a way to organize related classes and interfaces into a single namespace. It helps in avoiding naming conflicts and provides a modular structure to the Java program. Packages can contain sub-packages, which further organize the code.

Java provides four types of access specifiers to control the visibility and accessibility of classes, variables, methods, and constructors:

1. **Default (no specifier)**:
   - When no access specifier is used, it is considered as default.
   - Members are accessible within the same package but not outside the package.
   - Example: `class A` in package `com.example` is accessible to other classes in the `com.example` package but not to classes outside this package.
2. **Private**:
   - Members are accessible only within the same class.
   - Example: `private int x;` can only be accessed within the class where it is declared.
3. **Protected**:
   - Members are accessible within the same package and by subclasses (even if the subclass is in a different package).
   - Example: `protected void foo();` can be accessed by any subclass of the class where `foo()` is declared.
4. **Public**:
   - Members are accessible from any other class.
   - Example: `public void bar();` can be accessed from any class.

Access specifiers are used to implement encapsulation and control the visibility of members, ensuring better code maintainability and security.

## 4) Write a program to find square root of given array using static import.

To find the square root of each element in an array using static import, you can use the `sqrt` method from the `java.lang.Math` class. Here's a program that demonstrates this:

```java
import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        double[] array = {25, 36, 49, 64, 81};

        System.out.println("Square roots of the elements:");
        for (double num : array) {
            System.out.println(sqrt(num));
        }
    }
}

```

In this program, we import the `sqrt` method using static import (`import static java.lang.Math.sqrt;`). This allows us to directly use the `sqrt` method without prefixing it with the `Math` class name. We then iterate over each element in the array and print its square root using the `sqrt` method.

## 5) What is Exception? explain different types of built in exception in detail.

An exception in Java is an event that disrupts the normal flow of the program's instructions during execution. When an exceptional condition occurs, an object representing that exception is created and thrown in the method that caused the exception. The Java runtime system then looks for a handler for that exception. If a handler is found, the program control is transferred to the handler. If no appropriate handler is found, the program terminates abnormally.

Java provides a rich set of built-in exceptions that cover various types of exceptional conditions. These exceptions are categorized into two main types: checked exceptions and unchecked exceptions.

1. **Checked Exceptions**:
   - Checked exceptions are exceptions that are checked at compile time by the compiler. This means that the compiler will enforce the programmer to either handle the exception or declare it in the method signature using the `throws` keyword.
   - Examples of checked exceptions:
     - `IOException`: Signals that an I/O exception of some sort has occurred.
     - `ClassNotFoundException`: Thrown when an application tries to load a class through its string name but no definition for the class with the specified name could be found.
     - `SQLException`: An exception that provides information on a database access error or other errors.
2. **Unchecked Exceptions** (Runtime Exceptions):
   - Unchecked exceptions are exceptions that are not checked at compile time. This means that the compiler does not force the programmer to handle or declare these exceptions.
   - Examples of unchecked exceptions:
     - `NullPointerException`: Thrown when an application attempts to use null in a case where an object is required.
     - `ArrayIndexOutOfBoundsException`: Thrown to indicate that an array has been accessed with an illegal index.
     - `ArithmeticException`: Thrown when an exceptional arithmetic condition has occurred (e.g., division by zero).

Java also provides a top-level class `Exception` from which all other built-in exceptions inherit. This class is used to handle general exceptions that do not fall into any specific category.

Handling exceptions properly in your code can help make your programs more robust and reliable, as it allows you to gracefully handle unexpected situations and prevent the program from crashing.
