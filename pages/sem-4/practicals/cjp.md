# Core Java Programming

## Lab 01

### 1) Write a program to display “Welcome To Java World”.

```java
public class WelcomeToJava {
    public static void main(String[] args) {
        System.out.println("Welcome To Java World");
    }
}
```

### 2) Write a program to find whether the number is prime or not.

```java
import java.util.Scanner;

public class PrimeNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();
        boolean isPrime = true;
        if (number <= 1) {
            isPrime = false;
        } else {
            for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }
        if (isPrime) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }
    }
}
```

### 3) Write a program to find a greater number among given three numbers using a) ternary operator b) nested if.

a) Using ternary operator:

```java
import java.util.Scanner;

public class GreaterNumberTernary {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter three numbers: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int num3 = scanner.nextInt();
        scanner.close();

        int max = (num1 > num2) ? ((num1 > num3) ? num1 : num3) : ((num2 > num3) ? num2 : num3);
        System.out.println("The greater number is: " + max);
    }
}
```

b) Using nested if:

```java
import java.util.Scanner;

public class GreaterNumberNestedIf {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter three numbers: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int num3 = scanner.nextInt();
        scanner.close();

        int max;
        if (num1 >= num2) {
            if (num1 >= num3) {
                max = num1;
            } else {
                max = num3;
            }
        } else {
            if (num2 >= num3) {
                max = num2;
            } else {
                max = num3;
            }
        }
        System.out.println("The greater number is: " + max);
    }
}
```

### 4) Write a program to print the Fibonacci series.

```java
import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of terms in Fibonacci series: ");
        int n = scanner.nextInt();
        scanner.close();

        int firstTerm = 0, secondTerm = 1;
        System.out.println("Fibonacci Series:");
        for (int i = 1; i <= n; ++i) {
            System.out.print(firstTerm + " ");
            int nextTerm = firstTerm + secondTerm;
            firstTerm = secondTerm;
            secondTerm = nextTerm;
        }
    }
}
```

## Lab 02

### 1) Write a program to find the average of n numbers stored in an Array.

```java
import java.util.Scanner;

public class AverageOfNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();

        double[] numbers = new double[n];
        double sum = 0;

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextDouble();
            sum += numbers[i];
        }
        scanner.close();

        double average = sum / n;
        System.out.println("Average of the numbers: " + average);
    }
}
```

## Lab 03

### 1) WAP to replace substring with other substring in the given string.

```java
import java.util.Scanner;

public class ReplaceSubstring {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String str = scanner.nextLine();
        System.out.print("Enter the substring to replace: ");
        String substring = scanner.nextLine();
        System.out.print("Enter the new substring: ");
        String newSubstring = scanner.nextLine();
        scanner.close();

        String replacedString = str.replace(substring, newSubstring);
        System.out.println("Original String: " + str);
        System.out.println("Replaced String: " + replacedString);
    }
}
```

### 2) WAP that to sort given strings into alphabetical order.

```java
import java.util.Arrays;
import java.util.Scanner;

public class SortStringsAlphabetically {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of strings: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        String[] strings = new String[n];
        System.out.println("Enter the strings:");
        for (int i = 0; i < n; i++) {
            strings[i] = scanner.nextLine();
        }
        scanner.close();

        Arrays.sort(strings);

        System.out.println("Strings in alphabetical order:");
        for (String s : strings) {
            System.out.println(s);
        }
    }
}
```

### 3) Create a String Buffer with some default string. Append any string to i th position of original string and display the modified string. Also display the reverse of modified string.

```java
public class StringBufferExample {
    public static void main(String[] args) {
        String defaultString = "Hello, World!";
        StringBuffer stringBuffer = new StringBuffer(defaultString);

        int i = 6; // position to insert
        String insertString = "Java ";

        // Append string at i-th position
        stringBuffer.insert(i, insertString);
        System.out.println("Modified String: " + stringBuffer);

        // Reverse the modified string
        stringBuffer.reverse();
        System.out.println("Reversed Modified String: " + stringBuffer);
    }
}
```

## Lab 04

### 1a) WAP that declares a class named Person. It should have instance variables to record name, age and salary. Use new operator to create a Person object. Set and display its instance variables.

```java
public class Person {
    String name;
    int age;
    double salary;

    public static void main(String[] args) {
        Person person = new Person(); // Creating a Person object

        // Setting instance variables
        person.name = "John Doe";
        person.age = 30;
        person.salary = 50000.0;

        // Displaying instance variables
        System.out.println("Name: " + person.name);
        System.out.println("Age: " + person.age);
        System.out.println("Salary: " + person.salary);
    }
}
```

### 1b) Add a constructor to the Person class developed above.

```java
public class Person {
    String name;
    int age;
    double salary;

    // Constructor
    public Person(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public static void main(String[] args) {
        // Creating a Person object using the constructor
        Person person = new Person("John Doe", 30, 50000.0);

        // Displaying instance variables
        System.out.println("Name: " + person.name);
        System.out.println("Age: " + person.age);
        System.out.println("Salary: " + person.salary);
    }
}
```

### 2) The employee list for a company contains employee code, name, designation and basic pay. The employee is given HRA of 10% of the basic and DA of 45% of the basic pay. The total pay of the employee is calculated as Basic pay+HRA+ DA. Write a class to define the details of the employee. Write a constructor to assign the required initial values. Add a method to calculate HRA, DA and Total pay and print them out. Write another class with a main method. Create objects for three different employees and calculate the HRA, DA and total pay.

```java
class Employee {
    int empCode;
    String name;
    String designation;
    double basicPay;

    // Constructor to assign initial values
    public Employee(int empCode, String name, String designation, double basicPay) {
        this.empCode = empCode;
        this.name = name;
        this.designation = designation;
        this.basicPay = basicPay;
    }

    // Method to calculate HRA
    public double calculateHRA() {
        return 0.10 * basicPay;
    }

    // Method to calculate DA
    public double calculateDA() {
        return 0.45 * basicPay;
    }

    // Method to calculate Total Pay
    public double calculateTotalPay() {
        return basicPay + calculateHRA() + calculateDA();
    }

    // Method to display employee details
    public void displayDetails() {
        System.out.println("Employee Code: " + empCode);
        System.out.println("Name: " + name);
        System.out.println("Designation: " + designation);
        System.out.println("Basic Pay: " + basicPay);
        System.out.println("HRA: " + calculateHRA());
        System.out.println("DA: " + calculateDA());
        System.out.println("Total Pay: " + calculateTotalPay());
    }
}

public class EmployeeDetails {
    public static void main(String[] args) {
        // Creating objects for three different employees
        Employee employee1 = new Employee(101, "John Doe", "Manager", 50000.0);
        Employee employee2 = new Employee(102, "Jane Smith", "Developer", 40000.0);
        Employee employee3 = new Employee(103, "Alice Johnson", "HR", 30000.0);

        // Displaying details for each employee
        System.out.println("Details of Employee 1:");
        employee1.displayDetails();

        System.out.println("\\nDetails of Employee 2:");
        employee2.displayDetails();

        System.out.println("\\nDetails of Employee 3:");
        employee3.displayDetails();
    }
}
```

## Lab 05

### 1) Write a program which defines base class Employee having three data members, namely name[30], emp*numb and gender and two methods namely input_data() and show_data(). Derive a class SalariedEmployee from Employee and adds a new data member, namely salary. It also adds two member methods, namely allowance (if gender is female HRA=0.1 \_salary else 0.09* salary. DA= 0.05*salary) and increment (salary= salary+0.1*salary). Display the gross salary in main class. (Tip: Use super to call base class’s constructor0).

```java
class Employee {
    String name;
    int emp_numb;
    char gender;

    Employee(String n, int numb, char g) {
        name = n;
        emp_numb = numb;
        gender = g;
    }

    void input_data() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name: ");
        name = sc.nextLine();
        System.out.println("Enter employee number: ");
        emp_numb = sc.nextInt();
        System.out.println("Enter gender (M/F): ");
        gender = sc.next().charAt(0);
    }

    void show_data() {
        System.out.println("Name: " + name);
        System.out.println("Employee number: " + emp_numb);
        System.out.println("Gender: " + gender);
    }
}

class SalariedEmployee extends Employee {
    double salary;

    SalariedEmployee(String n, int numb, char g, double s) {
        super(n, numb, g);
        salary = s;
    }

    void allowance() {
        if (gender == 'F')
            salary = salary + salary * 0.1 + salary * 0.05;
        else
            salary = salary + salary * 0.09 + salary * 0.05;
    }

    void increment() {
        salary = salary + salary * 0.1;
    }

    void show_salary() {
        System.out.println("Gross salary: " + salary);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SalariedEmployee se = new SalariedEmployee("", 0, 'M', 0);
        se.input_data();
        se.allowance();
        se.increment();
        se.show_data();
        se.show_salary();
    }
}
```

### 2) WAP that illustrates method overriding. Class A3 is extended by Class B3. Each of these classes defines a hello(string s) method that outputs the string “A3: Hello From” or “B3: Hello From” respectively. Use the concept DynamicMethod Dispatch and keyword super.

```java
class A3 {
    public void hello(String s) {
        System.out.println("A3: Hello From " + s);
    }
}

class B3 extends A3 {
    @Override
    public void hello(String s) {
        System.out.println("B3: Hello From " + s);
    }
}

public class Main {
    public static void main(String[] args) {
        A3 objA = new A3();
        B3 objB = new B3();

        A3 ref;

        ref = objA;
        ref.hello("Object A"); // Output: A3: Hello From Object A

        ref = objB;
        ref.hello("Object B"); // Output: B3: Hello From Object B
    }
}
```

## Lab 06

### 1) Write an abstract class shape, which defines abstract method area. Derive class circle from shape. It has data member radius and implementation for area function. Derive class Triangle from shape. It has data members height, base and implementation for area function. Derive class Square from shape. It has data member side and implementation for area function. In main class, use dynamic method dispatch in order to call correct version of method.

```java
abstract class Shape {
    public abstract double area();
}

class Circle extends Shape {
    private double radius;

    public Circle(double r) {
        radius = r;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

class Triangle extends Shape {
    private double height;
    private double base;

    public Triangle(double h, double b) {
        height = h;
        base = b;
    }

    @Override
    public double area() {
        return 0.5 * base * height;
    }
}

class Square extends Shape {
    private double side;

    public Square(double s) {
        side = s;
    }

    @Override
    public double area() {
        return side * side;
    }
}

public class Main {
    public static void main(String[] args) {
        Shape circle = new Circle(5);
        Shape triangle = new Triangle(4, 3);
        Shape square = new Square(6);

        System.out.println("Area of Circle: " + circle.area());
        System.out.println("Area of Triangle: " + triangle.area());
        System.out.println("Area of Square: " + square.area());
    }
}
```

### 2) Create an interface Shape2D which declares a getArea() method.. The abstract class Shape declares abstract display () method .Circle class is extended from shape class and implemented from shape2D interface. Write appropriate method required in class circle and Create instance of circle object and display area of circle

```java
interface Shape2D {
    double getArea();
}

abstract class Shape {
    public abstract void display();
}

class Circle extends Shape implements Shape2D {
    private double radius;

    public Circle(double r) {
        radius = r;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public void display() {
        System.out.println("Area of Circle: " + getArea());
    }
}

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle(5);
        circle.display();
    }
}
```

## Lab 07

### 1) Create a package “employee” and define a Class Employee having three data members, name, emp_num, and gender and two methods- input_data and show_data. Inherit class SalariedEmployee from this class and keep it in package “employee”. Add new variable salary and methods allowance (if female hra=0.1* salary else 0.09* salary. DA= 0.05*salary) and increment (salary= salary+0.01 * salary). Calculate gross salary in main class defined in the same package.

To create a package "employee" and define the classes as described, you would follow these steps:

1. Create a directory named `employee`.
2. Inside the `employee` directory, create a file `Employee.java` for the base class `Employee`.
3. Inside the `employee` directory, create a file `SalariedEmployee.java` for the subclass `SalariedEmployee`.
4. Put both files in the package `employee` by adding the line `package employee;` at the top of each file.

Here's the implementation:

1. `Employee.java`:

```java
package employee;

import java.util.Scanner;

public class Employee {
    String name;
    int empNum;
    char gender;

    public void input_data() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = scanner.nextLine();
        System.out.print("Enter employee number: ");
        empNum = scanner.nextInt();
        System.out.print("Enter gender (M/F): ");
        gender = scanner.next().charAt(0);
    }

    public void show_data() {
        System.out.println("Name: " + name);
        System.out.println("Employee Number: " + empNum);
        System.out.println("Gender: " + gender);
    }
}

```

1. `SalariedEmployee.java`:

```java
package employee;

public class SalariedEmployee extends Employee {
    double salary;

    public void input_data() {
        super.input_data();
        System.out.print("Enter salary: ");
        salary = scanner.nextDouble();
    }

    public double allowance() {
        double hra = (gender == 'F') ? 0.10 * salary : 0.09 * salary;
        double da = 0.05 * salary;
        return hra + da;
    }

    public void increment() {
        salary += 0.1 * salary;
    }

    public void displayGrossSalary() {
        System.out.println("Gross Salary: " + (salary + allowance()));
    }
}

```

1. `Main.java` (inside the `employee` package):

```java
package employee;

public class Main {
    public static void main(String[] args) {
        SalariedEmployee salariedEmployee = new SalariedEmployee();
        salariedEmployee.input_data();
        salariedEmployee.show_data();
        salariedEmployee.increment();
        salariedEmployee.displayGrossSalary();
    }
}

```

## Lab 08

### 1) WAP using try catch block. User should enter two command line arguments. If only one argument is entered then exception should be caught. In case of two command line arguments, if first is divided by second and if second command line argument is 0 then catch the appropriate exception.

```java
public class Main {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Please enter exactly two command line arguments.");
            System.exit(1);
        }

        try {
            double result = Double.parseDouble(args[0]) / Double.parseDouble(args[1]);
            System.out.println("The result is: " + result);
        } catch (NumberFormatException e) {
            System.out.println("One or both of the command line arguments are not valid numbers.");
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed.");
        }
    }
}
```

### 2) Define an exception called “NoMatchException” that is thrown when a string is not equal to “India”. Write a program that uses this exception.

**NoMatchException.java**

```java
public class NoMatchException extends Exception {
    public NoMatchException(String message) {
        super(message);
    }
}

```

**Main.java**

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String input = sc.nextLine();

        try {
            if (!input.equals("India")) {
                throw new NoMatchException("String does not match 'India'");
            } else {
                System.out.println("String matches 'India'");
            }
        } catch (NoMatchException e) {
            System.out.println("Custom Exception: " + e.getMessage());
        }
    }
}

```

## Lab 09

### 1) The program to creates and run the following three threads. The first thread prints the letter ‘a’ 100 times.

The second thread prints the letter ‘b’ 100 times.
The third thread prints the integer 1 to 100.

```java
public class Main {
    public static void main(String[] args) {
        Thread threadA = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++) {
                    System.out.print("a");
                }
            }
        });

        Thread threadB = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++) {
                    System.out.print("b");
                }
            }
        });

        Thread thread123 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 100; i++) {
                    System.out.print(" " + i);
                }
            }
        });

        threadA.start();
        threadB.start();
        thread123.start();
    }
}
```

### 2) Write the thread program using Runnable interface.

```java
public class Main {
    public static void main(String[] args) {
        Runnable runnableA = new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++) {
                    System.out.print("a");
                }
            }
        };

        Runnable runnableB = new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++) {
                    System.out.print("b");
                }
            }
        };

        Runnable runnable123 = new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 100; i++) {
                    System.out.print(" " + i);
                }
            }
        };

        Thread threadA = new Thread(runnableA);
        Thread threadB = new Thread(runnableB);
        Thread thread123 = new Thread(runnable123);

        threadA.start();
        threadB.start();
        thread123.start();
    }
}
```

## Lab 10

### 1) Write a program that takes two files names (source and destination) as command line argument .Copy source file’s content to destination file. Use character stream class. Also do same using byte stream and buffer stream.

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Please provide two file names as command line arguments.");
            System.exit(1);
        }

        String sourceFileName = args[0];
        String destinationFileName = args[1];

        // Copy using character streams
        try (FileReader fileReader = new FileReader(sourceFileName);
             FileWriter fileWriter = new FileWriter(destinationFileName)) {

            int c;
            while ((c = fileReader.read()) != -1) {
                fileWriter.write(c);
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error: Source file not found.");
        } catch (IOException e) {
            System.out.println("Error: Unable to copy file.");
        }

        // Copy using byte streams
        try (FileInputStream fileInputStream = new FileInputStream(sourceFileName);
             FileOutputStream fileOutputStream = new FileOutputStream(destinationFileName)) {

            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fileInputStream.read(buffer)) != -1) {
                fileOutputStream.write(buffer, 0, bytesRead);
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error: Source file not found.");
        } catch (IOException e) {
            System.out.println("Error: Unable to copy file.");
        }

        // Copy using buffer streams
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(sourceFileName));
             BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(destinationFileName))) {

            String line;
            while ((line = bufferedReader.readLine()) != null) {
                bufferedWriter.write(line);
                bufferedWriter.newLine();
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error: Source file not found.");
        } catch (IOException e) {
            System.out.println("Error: Unable to copy file.");
        }
    }
}
```

### 2) Write a program which generates random integers and stores them in a file named “rand.dat”. The program then reads the integers from the file and displays on the screen.

```java
import java.io.*;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        // Write random integers to file
        try (Random random = new Random();
             DataOutputStream outputStream = new DataOutputStream(new FileOutputStream("rand.dat"))) {

            for (int i = 0; i < 100; i++) {
                int randomInt = random.nextInt(100);
                outputStream.writeInt(randomInt);
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found.");
        } catch (IOException e) {
            System.out.println("Error: Unable to write to file.");
        }

        // Read random integers from file and display on screen
        try (DataInputStream inputStream = new DataInputStream(new FileInputStream("rand.dat"))) {

            for (int i = 0; i < 100; i++) {
                int randomInt = inputStream.readInt();
                System.out.println(randomInt);
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found.");
        } catch (IOException e) {
            System.out.println("Error: Unable to read from file.");
        }
    }
}
```

## Lab 11

### 1) Write the program that demonstrate the use of Stack, Vector and ArrayList classes.

```java
import java.util.ArrayList;
import java.util.Stack;
import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        // Stack
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("Stack: " + stack);
        System.out.println("Stack top: " + stack.peek());
        System.out.println("Stack pop: " + stack.pop());
        System.out.println("Stack: " + stack);

        // Vector
        Vector<Integer> vector = new Vector<>();
        vector.add(1);
        vector.add(2);
        vector.add(3);
        System.out.println("Vector: " + vector);
        System.out.println("Vector get: " + vector.get(1));
        System.out.println("Vector remove: " + vector.remove(1));
        System.out.println("Vector: " + vector);

        // ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);
        System.out.println("ArrayList: " + arrayList);
        System.out.println("ArrayList get: " + arrayList.get(1));
        System.out.println("ArrayList remove: " + arrayList.remove(1));
        System.out.println("ArrayList: " + arrayList);
    }
}
```

## Lab 12

### 1) Write a Network program that client sends the data as redius of circle to server and server received that data and send the resultant area of circle to requested client.

**Server.java**

```java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server started on port 5000...");

        while (true) {
            Socket socket = serverSocket.accept();
            System.out.println("Client connected.");

            InputStream inputStream = socket.getInputStream();
            DataInputStream dataInputStream = new DataInputStream(inputStream);

            OutputStream outputStream = socket.getOutputStream();
            DataOutputStream dataOutputStream = new DataOutputStream(outputStream);

            double radius = dataInputStream.readDouble();
            double area = Math.PI * radius * radius;

            dataOutputStream.writeDouble(area);

            dataInputStream.close();
            dataOutputStream.close();
            socket.close();

            System.out.println("Area sent to client: " + area);
        }
    }
}
```

**Client.java**

```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5000);

        OutputStream outputStream = socket.getOutputStream();
        DataOutputStream dataOutputStream = new DataOutputStream(outputStream);

        InputStream inputStream = socket.getInputStream();
        DataInputStream dataInputStream = new DataInputStream(inputStream);

        double radius = 5.0;
        dataOutputStream.writeDouble(radius);

        double area = dataInputStream.readDouble();

        dataOutputStream.close();
        dataInputStream.close();
        socket.close();

        System.out.println("Area received from server: " + area);
    }
}
```

## Lab 13

### 1) Write a program to count occurrence of character in a string

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String str = "Hello, World!";
        HashMap<Character, Integer> charCountMap = new HashMap<>();

        // Count occurrences of each character in the string
        for (char c : str.toCharArray()) {
            if (charCountMap.containsKey(c)) {
                charCountMap.put(c, charCountMap.get(c) + 1);
            } else {
                charCountMap.put(c, 1);
            }
        }

        // Display the character count
        System.out.println("Character Count in the String:");
        for (char c : charCountMap.keySet()) {
            System.out.println("'" + c + "': " + charCountMap.get(c));
        }
    }
}
```

## Lab 14 ~ _Out of syllabus_

### 1) Write a programs to create simple calculator using applet.

```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculatorApplet extends Applet implements ActionListener {
    TextField display;
    Button[] buttons;
    String[] buttonLabels = {"7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+"};
    String input = "";

    public void init() {
        display = new TextField(20);
        display.setEditable(false);
        add(display);

        buttons = new Button[buttonLabels.length];
        for (int i = 0; i < buttonLabels.length; i++) {
            buttons[i] = new Button(buttonLabels[i]);
            buttons[i].addActionListener(this);
            add(buttons[i]);
        }
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (command.equals("C")) {
            input = "";
        } else if (command.equals("=")) {
            try {
                input = String.valueOf(eval(input));
            } catch (ArithmeticException ex) {
                input = "Error";
            }
        } else {
            input += command;
        }

        display.setText(input);
    }

    private double eval(String expression) {
        return new Object() {
            int pos = -1, ch;

            void nextChar() {
                ch = (++pos < expression.length()) ? expression.charAt(pos) : -1;
            }

            boolean eat(int charToEat) {
                while (ch == ' ') nextChar();
                if (ch == charToEat) {
                    nextChar();
                    return true;
                }
                return false;
            }

            double parse() {
                nextChar();
                double x = parseExpression();
                if (pos < expression.length()) throw new RuntimeException("Unexpected: " + (char) ch);
                return x;
            }

            double parseExpression() {
                double x = parseTerm();
                for (; ; ) {
                    if (eat('+')) x += parseTerm();
                    else if (eat('-')) x -= parseTerm();
                    else return x;
                }
            }

            double parseTerm() {
                double x = parseFactor();
                for (; ; ) {
                    if (eat('*')) x *= parseFactor();
                    else if (eat('/')) x /= parseFactor();
                    else return x;
                }
            }

            double parseFactor() {
                if (eat('+')) return parseFactor();
                if (eat('-')) return -parseFactor();

                double x;
                int startPos = this.pos;
                if (eat('(')) {
                    x = parseExpression();
                    eat(')');
                } else if ((ch >= '0' && ch <= '9') || ch == '.') {
                    while ((ch >= '0' && ch <= '9') || ch == '.') nextChar();
                    x = Double.parseDouble(expression.substring(startPos, this.pos));
                } else {
                    throw new RuntimeException("Unexpected: " + (char) ch);
                }

                if (eat('^')) x = Math.pow(x, parseFactor());

                return x;
            }
        }.parse();
    }
}
```

## Lab 15 ~ _Out of syllabus_

### 1) Write programms to create student registration form in applet and store data in database.

```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class StudentRegistrationApplet extends Applet implements ActionListener {
    Label nameLabel, ageLabel, genderLabel, addressLabel;
    TextField nameField, ageField, addressField;
    Choice genderChoice;
    Button submitButton;

    public void init() {
        nameLabel = new Label("Name:");
        ageLabel = new Label("Age:");
        genderLabel = new Label("Gender:");
        addressLabel = new Label("Address:");

        nameField = new TextField(20);
        ageField = new TextField(3);
        addressField = new TextField(20);

        genderChoice = new Choice();
        genderChoice.add("Male");
        genderChoice.add("Female");

        submitButton = new Button("Submit");

        add(nameLabel);
        add(nameField);
        add(ageLabel);
        add(ageField);
        add(genderLabel);
        add(genderChoice);
        add(addressLabel);
        add(addressField);
        add(submitButton);

        submitButton.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            String name = nameField.getText();
            int age = Integer.parseInt(ageField.getText());
            String gender = genderChoice.getSelectedItem();
            String address = addressField.getText();

            try {
                Class.forName("com.mysql.jdbc.Driver");
                Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "username", "password");
                PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO students (name, age, gender, address) VALUES (?, ?, ?, ?)");
                preparedStatement.setString(1, name);
                preparedStatement.setInt(2, age);
                preparedStatement.setString(3, gender);
                preparedStatement.setString(4, address);
                preparedStatement.executeUpdate();
                connection.close();
                System.out.println("Data inserted successfully.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
}
```
