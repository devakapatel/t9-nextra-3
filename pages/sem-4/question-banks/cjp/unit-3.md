# Unit 3

## 1) Explain File constructors, any two methods of class File and method seek.

### File Constructors

The File class in Java provides several constructors to create File objects. Here are two commonly used constructors:

1. `File(String pathname)`:
   - This constructor creates a new File instance by converting the given pathname string into an abstract pathname.
   - Example: `File file = new File("/path/to/file.txt");`
2. `File(String parent, String child)`:
   - This constructor creates a new File instance from a parent pathname string and a child pathname string.
   - Example: `File file = new File("/path/to", "file.txt");`

### Methods of the File Class

1. `exists()`:
   - This method returns `true` if the file denoted by this abstract pathname exists; `false` otherwise.
   - Example: `if (file.exists()) { /* File exists */ }`
2. `delete()`:
   - This method deletes the file or directory denoted by this abstract pathname.
   - Example: `if (file.delete()) { /* File deleted successfully */ }`

### The `seek()` Method

The `seek()` method is not a method of the File class. It is a method of the `RandomAccessFile` class in Java.

The `RandomAccessFile` class provides random access to files. It allows you to read from and write to a file at any position.

The `seek()` method is used to set the file-pointer offset, measured from the beginning of this file, at which the next read or write occurs.

Example:

```java
RandomAccessFile raf = new RandomAccessFile("file.txt", "rw");
raf.seek(10); // Set the file pointer to position 10

```

In this example, the `seek()` method sets the file pointer to position 10, so the next read or write operation will start from that position.

## 2) Explain use of Array List collection class with example.

The ArrayList class in Java is a part of the Java Collections Framework and provides dynamic arrays that can grow as needed. Here's an explanation of how to use the ArrayList collection class with an example:

### Using ArrayList in Java

1.  **Import the ArrayList class**:
    You need to import the ArrayList class from the `java.util` package before using it in your code:
        ```java
        import java.util.ArrayList;

        ```
2.  **Create an ArrayList**:
    You can create an ArrayList of a specific type by specifying the type within angle brackets (`<>`). For example, to create an ArrayList of Strings:
        ```java
        ArrayList<String> names = new ArrayList<>();

        ```
3.  **Adding Elements**:
    You can add elements to the ArrayList using the `add()` method:
        ```java
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        ```
4.  **Accessing Elements**:
    You can access elements by their index using the `get()` method:
        ```java
        String firstElement = names.get(0); // Retrieves "Alice"

        ```
5.  **Iterating Over ArrayList**:
    You can iterate over the ArrayList using a loop, such as a for loop or an enhanced for loop:
        ```java
        for (String name : names) {
            System.out.println(name);
        }

        ```
6.  **Removing Elements**:
    You can remove elements by index or by object using the `remove()` method:
        ```java
        names.remove(1); // Removes the element at index 1

        ```
7.  **Size of ArrayList**:
    You can get the size of the ArrayList using the `size()` method:
        ```java
        int size = names.size(); // Returns the number of elements in the ArrayList

        ```

### Example of Using ArrayList

Here's a simple example demonstrating the use of ArrayList in Java:

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        System.out.println("Fruits in the list:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }

        fruits.remove("Banana");

        System.out.println("After removing Banana:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}

```

In this example, we create an ArrayList of Strings, add fruits to the list, print the fruits, remove "Banana" from the list, and then print the updated list.

## 3) Explain use of Linked List collection class with example.

The LinkedList class in Java is a part of the Java Collections Framework and provides a linked-list data structure. Here's an explanation of how to use the LinkedList collection class with an example:

### Using LinkedList in Java

1.  **Import the LinkedList class**:
    You need to import the LinkedList class from the `java.util` package before using it in your code:
        ```java
        import java.util.LinkedList;

        ```
2.  **Create a LinkedList**:
    You can create a LinkedList of a specific type by specifying the type within angle brackets (`<>`). For example, to create a LinkedList of Integers:
        ```java
        LinkedList<Integer> numbers = new LinkedList<>();

        ```
3.  **Adding Elements**:
    You can add elements to the LinkedList using the `add()` method:
        ```java
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);

        ```
4.  **Accessing Elements**:
    You can access elements by their index using the `get()` method:
        ```java
        int firstElement = numbers.get(0); // Retrieves the element at index 0

        ```
5.  **Iterating Over LinkedList**:
    You can iterate over the LinkedList using a loop, such as a for loop or an enhanced for loop:
        ```java
        for (Integer number : numbers) {
            System.out.println(number);
        }

        ```
6.  **Removing Elements**:
    You can remove elements by index or by object using the `remove()` method:
        ```java
        numbers.remove(1); // Removes the element at index 1

        ```
7.  **Size of LinkedList**:
    You can get the size of the LinkedList using the `size()` method:
        ```java
        int size = numbers.size(); // Returns the number of elements in the LinkedList

        ```

### Example of Using LinkedList

Here's a simple example demonstrating the use of LinkedList in Java:

```java
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> colors = new LinkedList<>();

        colors.add("Red");
        colors.add("Green");
        colors.add("Blue");

        System.out.println("Colors in the list:");
        for (String color : colors) {
            System.out.println(color);
        }

        colors.remove("Green");

        System.out.println("After removing Green:");
        for (String color : colors) {
            System.out.println(color);
        }
    }
}

```

In this example, we create a LinkedList of Strings, add colors to the list, print the colors, remove "Green" from the list, and then print the updated list.

## 4) Explain use of Vector collection class with example.

The Vector class in Java is a part of the Java Collections Framework and provides a dynamic array that can grow or shrink as needed. Here's an explanation of how to use the Vector collection class with an example:

### Using Vector in Java

1.  **Import the Vector class**:
    You need to import the Vector class from the `java.util` package before using it in your code:
        ```java
        import java.util.Vector;

        ```
2.  **Create a Vector**:
    You can create a Vector of a specific type by specifying the type within angle brackets (`<>`). For example, to create a Vector of Doubles:
        ```java
        Vector<Double> prices = new Vector<>();

        ```
3.  **Adding Elements**:
    You can add elements to the Vector using the `add()` method:
        ```java
        prices.add(10.5);
        prices.add(20.0);
        prices.add(15.75);

        ```
4.  **Accessing Elements**:
    You can access elements by their index using the `get()` method:
        ```java
        double firstPrice = prices.get(0); // Retrieves the element at index 0

        ```
5.  **Iterating Over Vector**:
    You can iterate over the Vector using a loop, such as a for loop or an enhanced for loop:
        ```java
        for (Double price : prices) {
            System.out.println(price);
        }

        ```
6.  **Removing Elements**:
    You can remove elements by index or by object using the `remove()` method:
        ```java
        prices.remove(1); // Removes the element at index 1

        ```
7.  **Size of Vector**:
    You can get the size of the Vector using the `size()` method:
        ```java
        int size = prices.size(); // Returns the number of elements in the Vector

        ```

### Example of Using Vector

Here's a simple example demonstrating the use of Vector in Java:

```java
import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
        Vector<String> names = new Vector<>();

        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        System.out.println("Names in the vector:");
        for (String name : names) {
            System.out.println(name);
        }

        names.remove("Bob");

        System.out.println("After removing Bob:");
        for (String name : names) {
            System.out.println(name);
        }
    }
}

```

In this example, we create a Vector of Strings, add names to the vector, print the names, remove "Bob" from the vector, and then print the updated vector.

## 5) Explain use of Enumeration with examples.

Enumeration is an interface in Java that provides a way to iterate over the elements of a collection. It is a legacy interface and has been superseded by the Iterator interface, which provides more functionality and flexibility.

Here's how to use Enumeration with examples:

### Using Enumeration in Java

1.  **Import the Enumeration interface**:
    You need to import the Enumeration interface from the `java.util` package before using it in your code:
        ```java
        import java.util.Enumeration;

        ```
2.  **Create a Vector or Hashtable**:
    Enumeration is commonly used with legacy collections like Vector and Hashtable. Here's an example of creating a Vector:
        ```java
        Vector<String> names = new Vector<>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        ```
3.  **Get an Enumeration**:
    You can obtain an Enumeration from the Vector or Hashtable using the `elements()` method:
        ```java
        Enumeration<String> enumeration = names.elements();

        ```
4.  **Iterate Over Elements**:
    You can use the `hasMoreElements()` and `nextElement()` methods to iterate over the elements of the Enumeration:
        ```java
        while (enumeration.hasMoreElements()) {
            String name = enumeration.nextElement();
            System.out.println(name);
        }

        ```

### Example of Using Enumeration

Here's a complete example demonstrating the use of Enumeration with a Vector:

```java
import java.util.Enumeration;
import java.util.Vector;

public class EnumerationExample {
    public static void main(String[] args) {
        Vector<String> names = new Vector<>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        System.out.println("Names in the vector:");

        Enumeration<String> enumeration = names.elements();
        while (enumeration.hasMoreElements()) {
            String name = enumeration.nextElement();
            System.out.println(name);
        }
    }
}

```

Output:

```
Names in the vector:
Alice
Bob
Charlie

```

In this example, we create a Vector of Strings, obtain an Enumeration from the Vector using the `elements()` method, and then iterate over the elements using the `hasMoreElements()` and `nextElement()` methods.

It's important to note that Enumeration is a legacy interface, and it's generally recommended to use the more modern Iterator interface instead, as it provides additional functionality and flexibility.

## 6)Explain Client-Server Communication in java networking with proper diagrams only [No Code].

### Client-Server Communication Diagram

```
                   +---------------+
                   |   Client      |
                   |               |
                   |   +--------+  |
                   |   | Socket |  |
                   |   +--------+  |
                   |               |
                   +---------------+
                           |
                           |
                           |
                   +---------------+
                   |   Server      |
                   |               |
                   |   +--------+  |
                   |   | Socket |  |
                   |   +--------+  |
                   |               |
                   +---------------+

```

In this diagram, we have a Client and a Server communicating with each other using Sockets. The Client initiates the communication by creating a Socket and connecting to the Server's IP address and port number. The Server also creates a Socket and listens for incoming connections on a specific port.

### Client-Server Communication Sequence Diagram

```
                   +---------------+                   +---------------+
                   |   Client      |                   |   Server      |
                   +---------------+                   +---------------+
                         |                                     |
                         |  1. Create Socket                   |
                         |------------------------>            |
                         |                                     |
                         |  2. Connect to Server               |
                         |------------------------>            |
                         |                                     |
                         |                        3. Accept Connection
                         |                        <---------------
                         |                                     |
                         |                        4. Create Socket
                         |                        <---------------
                         |                                     |
                         |                        5. Listen for Data
                         |                        <---------------
                         |                                     |
                         |  6. Send Data                       |
                         |------------------------>            |
                         |                                     |
                         |                        7. Receive Data
                         |                        <---------------
                         |                                     |
                         |  8. Receive Response                |
                         |<-----------------------             |
                         |                                     |
                         |                        9. Send Response
                         |                        <---------------
                         |                                     |
                         |                                     |

```

This sequence diagram illustrates the step-by-step communication between the Client and the Server:

1. The Client creates a Socket.
2. The Client connects to the Server's IP address and port number using the `connect()` method.
3. The Server accepts the incoming connection using the `accept()` method.
4. The Server creates a Socket to handle the communication with the Client.
5. The Server listens for incoming data from the Client.
6. The Client sends data to the Server using the `write()` or `send()` method.
7. The Server receives the data from the Client using the `read()` or `receive()` method.
8. The Server processes the received data and sends a response back to the Client.
9. The Client receives the response from the Server.

This communication process can be repeated multiple times during a single session, with the Client and Server exchanging data as needed.

## 7) Write a client-server program using TCP sockets to echo the message sent by the client.

Sure, here's a simple client-server program using TCP sockets in Java to echo the message sent by the client:

### Server Code

```java
import java.io.*;
import java.net.*;

public class EchoServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8080);
            System.out.println("Server started. Listening on port 8080...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            String message = in.readLine();
            System.out.println("Received message: " + message);

            out.println("Echo: " + message);

            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

### Client Code

```java
import java.io.*;
import java.net.*;

public class EchoClient {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 8080);
            System.out.println("Connected to server.");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter a message: ");
            String message = userInput.readLine();

            out.println(message);
            System.out.println("Message sent: " + message);

            String response = in.readLine();
            System.out.println("Server response: " + response);

            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

## How it works

1. The server creates a `ServerSocket` and listens for incoming connections on port 8080.
2. The client creates a `Socket` and connects to the server's IP address (in this case, "localhost") and port 8080.
3. Once the connection is established, the client sends a message to the server using `PrintWriter`.
4. The server receives the message using `BufferedReader`, prints it, and then echoes the message back to the client using `PrintWriter`.
5. The client receives the echoed message using `BufferedReader` and prints it.
6. Both the client and server close their respective sockets.

To run the program:

1. Start the server by running the `EchoServer` class.
2. Run the `EchoClient` class, which will prompt you to enter a message.
3. The client will send the message to the server, and the server will echo it back to the client.
4. The client will display the server's response.

This example demonstrates the basic client-server communication using TCP sockets in Java, where the server echoes the message sent by the client.

## 8) Write the use of InetAddress class. List and explain the methods of it.

### Use of InetAddress Class

The `InetAddress` class in Java represents an Internet Protocol (IP) address. It provides methods to manipulate and retrieve information about IP addresses. Here are some common use cases of the `InetAddress` class:

1. Resolving hostnames to IP addresses
2. Retrieving the local host's IP address
3. Checking if an IP address is reachable
4. Retrieving the hostname associated with an IP address
5. Comparing IP addresses

### Methods of InetAddress Class

1. `getByName(String host)`:
   - This method returns an `InetAddress` object for the specified hostname or IP address.
   - Example: `InetAddress.getByName("www.example.com")`
2. `getLocalHost()`:
   - This method returns the `InetAddress` object representing the local host.
   - Example: `InetAddress.getLocalHost()`
3. `isReachable(int timeout)`:
   - This method tests whether the host is reachable.
   - It returns `true` if the host is reachable within the specified timeout, `false` otherwise.
   - Example: `address.isReachable(5000)` (5-second timeout)
4. `getHostName()`:
   - This method returns the hostname associated with the IP address.
   - Example: `address.getHostName()`
5. `getHostAddress()`:
   - This method returns the IP address string in textual format.
   - Example: `address.getHostAddress()`
6. `equals(Object obj)`:
   - This method compares this IP address to the specified object.
   - It returns `true` if the object is an `InetAddress` and it has the same IP address as this object.
   - Example: `address1.equals(address2)`
7. `hashCode()`:
   - This method returns the hash code value for the IP address.
   - Example: `address.hashCode()`

Here's an example demonstrating the usage of some `InetAddress` methods:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {
    public static void main(String[] args) {
        try {
            InetAddress localAddress = InetAddress.getLocalHost();
            System.out.println("Local Address: " + localAddress.getHostAddress());

            InetAddress googleAddress = InetAddress.getByName("www.google.com");
            System.out.println("Google Address: " + googleAddress.getHostAddress());

            boolean isReachable = googleAddress.isReachable(5000);
            System.out.println("Google is reachable: " + isReachable);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

In this example, we retrieve the local host's IP address, resolve the IP address for "[www.google.com](http://www.google.com/)", and check if Google is reachable within a 5-second timeout.

## 9) Explain java.util package with examples.

The `java.util` package, also known as the Java utilities package, is part of the Java Standard Edition (Java SE) and provides several classes and interfaces for handling common operations such as date and time manipulation, data structure management, random number generation, string parsing and scanning, and system property access, among others.

Here are a few key classes provided by the `java.util` package:

1. **Collections Framework Classes**: These classes provide robust data structures for storing and manipulating data. They include `ArrayList`, `LinkedList`, `HashSet`, `HashMap`, `TreeSet`, `TreeMap`, `Stack`, `Queue`, etc.

Example:

```java
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");

```

1. **Date and Time Classes**: Classes like `Date`, `Calendar`, `TimeZone`, and `Locale` help in representing and manipulating date, time and locale specific data.

Example:

```java
import java.util.Date;
Date currentDate = new Date();

```

1. **Random Class**: The `Random` class allows the generation of random numbers.

Example:

```java
import java.util.Random;
Random rand = new Random();
int randomNum = rand.nextInt(100);

```

1. **Scanner Class**: The `Scanner` class is used for parsing text for strings and primitive types using regular expressions.

Example:

```java
import java.util.Scanner;
Scanner scanner = new Scanner(System.in);
String input = scanner.nextLine();

```

1. **Enumeration, Iterator and ListIterator Interfaces**: These interfaces provide ways to iterate over various types of collections.

Example:

```java
import java.util.ArrayList;
import java.util.Iterator;
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}

```

1. **Observer and Observable**: These classes are used to implement the observer design pattern which is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes.
2. **Properties Class**: The `Properties` class is a subclass of `Hashtable` that is used to maintain lists of values in which the key is a String and the value is also a String.

Example:

```java
import java.util.Properties;
Properties properties = new Properties();
properties.setProperty("username", "admin");
String username = properties.getProperty("username");

```

These are just a few examples of the classes provided by the `java.util` package. This package provides many more classes that provide utility functions to the programmer.

## 10) Differentiate Byte Streams and Character Streams in java with suitable example programs for both.

### Byte Streams vs. Character Streams in Java

| **Byte Streams**                           | **Character Streams**                            |
| ------------------------------------------ | ------------------------------------------------ |
| Used for raw binary data                   | Used for text data                               |
| Operate on bytes (8-bit values)            | Operate on characters (16-bit Unicode values)    |
| Suitable for non-text data (images, audio) | Suitable for text data (reading/writing strings) |
| Examples: `InputStream`, `OutputStream`    | Examples: `Reader`, `Writer`                     |

### Example Programs

### Byte Stream Example: Copying a File

```java
import java.io.*;

public class ByteStreamExample {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("input.txt");
            FileOutputStream fos = new FileOutputStream("output.txt");

            byte[] buffer = new byte[1024];
            int bytesRead;

            while ((bytesRead = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }

            fis.close();
            fos.close();

            System.out.println("File copied successfully.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

### Character Stream Example: Reading User Input

```java
import java.io.*;

public class CharacterStreamExample {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter your name: ");

        try {
            String name = reader.readLine();
            System.out.println("Hello, " + name + "!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

In the byte stream example, we copy the contents of a file using `FileInputStream` and `FileOutputStream`, while in the character stream example, we read user input from the console using `InputStreamReader` and `BufferedReader`.

The choice between byte streams and character streams depends on the type of data being handled and the specific requirements of the application.

## 11) Explain FileOutputStream in java with an example program.

### Explanation of FileOutputStream in Java

In Java, `FileOutputStream` is a class used for writing raw bytes to a file. It is part of the `java.io` package and is commonly used to write data to files in a byte-oriented manner. When you create an instance of `FileOutputStream`, you can write bytes to the specified file.

### Example Program Using FileOutputStream

Here is an example program that demonstrates how to use `FileOutputStream` to write data to a file:

```java
import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamExample {
    public static void main(String[] args) {
        String data = "Hello, FileOutputStream!";

        try (FileOutputStream fos = new FileOutputStream("output.txt")) {
            byte[] bytes = data.getBytes();
            fos.write(bytes);

            System.out.println("Data has been written to the file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

In this example:

1. We create a `String` variable `data` with the content we want to write to the file.
2. We create an instance of `FileOutputStream` and specify the file name "output.txt" to write to.
3. We convert the string `data` to bytes using `getBytes()` method.
4. We write the bytes to the file using the `write()` method of `FileOutputStream`.
5. We handle any potential `IOException` that may occur during the file writing process.

### Key Points:

- `FileOutputStream` is used to write raw bytes to a file.
- It is important to close the `FileOutputStream` after writing data to ensure that all resources are properly released.
- The `write()` method writes bytes to the file, and the `close()` method should be called to release system resources.

By using `FileOutputStream`, you can write data to files byte by byte or in chunks, making it a versatile class for handling file output operations in Java.

## 12) Explain FileInputStream in java with an example program.

### Explanation of FileInputStream in Java

In Java, `FileInputStream` is a class used for reading raw bytes from a file. It is part of the `java.io` package and is commonly used to read data from files in a byte-oriented manner. When you create an instance of `FileInputStream`, you can read bytes from the specified file.

### Example Program Using FileInputStream

Here is an example program that demonstrates how to use `FileInputStream` to read data from a file:

```java
import java.io.FileInputStream;
import java.io.IOException;

public class FileInputStreamExample {
    public static void main(String[] args) {
        try (FileInputStream fis = new FileInputStream("input.txt")) {
            byte[] buffer = new byte[1024];
            int bytesRead;

            while ((bytesRead = fis.read(buffer)) != -1) {
                String data = new String(buffer, 0, bytesRead);
                System.out.println(data);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

In this example:

1. We create an instance of `FileInputStream` and specify the file name "input.txt" to read from.
2. We create a byte array `buffer` to store the read bytes.
3. We use a `while` loop to continuously read bytes from the file using the `read()` method of `FileInputStream`.
4. The `read()` method reads bytes into the `buffer` array and returns the number of bytes read. It returns -1 when the end of the file is reached.
5. We convert the read bytes to a string using the `String` constructor and print the data.
6. We handle any potential `IOException` that may occur during the file reading process.

### Key Points:

- `FileInputStream` is used to read raw bytes from a file.
- It is important to close the `FileInputStream` after reading data to ensure that all resources are properly released.
- The `read()` method reads bytes from the file and returns the number of bytes read. It returns -1 when the end of the file is reached.

By using `FileInputStream`, you can read data from files byte by byte or in chunks, making it a versatile class for handling file input operations in Java.

## 13) Explain the following terms with respect to exception handling.

i) try ii) catch ii) throw iv) throws v) finally

### Explanation of Exception Handling Terms

### i) `try`:

- The `try` block is used to enclose the code that may throw an exception.
- It is followed by one or more `catch` blocks or a `finally` block.
- If an exception occurs within the `try` block, the control is transferred to the corresponding `catch` block.

### ii) `catch`:

- The `catch` block is used to handle exceptions that are thrown within the `try` block.
- It specifies the type of exception it can catch and the code to be executed when that exception occurs.
- Multiple `catch` blocks can be used to handle different types of exceptions.

### iii) `throw`:

- The `throw` keyword is used to explicitly throw an exception within a method.
- It is followed by an instance of an exception class or a new exception object.
- This allows you to create and throw custom exceptions based on specific conditions.

### iv) `throws`:

- The `throws` keyword is used in the method signature to declare that the method may throw certain types of exceptions.
- It specifies the exceptions that the method can throw but does not handle them within the method.
- The calling method or the JVM must handle these exceptions.

### v) `finally`:

- The `finally` block is used to execute code that should always run, regardless of whether an exception is thrown or not.
- It is typically used for cleanup tasks like closing resources (e.g., files, database connections).
- The `finally` block is executed even if an exception is thrown and not caught.

### Example Demonstrating Exception Handling Terms

```java
public class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero");
        } finally {
            System.out.println("Cleanup code here");
        }
    }

    public static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
}

```

In this example:

- The `try` block contains the code that may throw an exception.
- The `catch` block handles the `ArithmeticException` that occurs when dividing by zero.
- The `throw` statement is used to throw an `ArithmeticException` in the `divide` method.
- The `finally` block contains cleanup code that will always run, regardless of whether an exception is thrown or not.

## 14) Explain Built in Exception.

### Explanation of Built-in Exceptions in Java

In Java, built-in exceptions are predefined exception classes provided by the Java language to handle common error conditions that may occur during program execution. These exceptions are part of the Java API and are organized in a hierarchy under the `java.lang` package. Here are some key points about built-in exceptions:

1. **Hierarchy**: Built-in exceptions are organized in a class hierarchy, with the root class being `Throwable`. This hierarchy includes `Error` (for serious errors) and `Exception` (for exceptional conditions) classes.
2. **Types**: Built-in exceptions cover a wide range of error conditions, such as arithmetic errors (`ArithmeticException`), null pointer access (`NullPointerException`), input/output errors (`IOException`), and more.
3. **Handling**: Java provides mechanisms like `try-catch` blocks, `throws` clause, and `finally` block to handle and manage exceptions gracefully.
4. **Checked vs. Unchecked**: Built-in exceptions are categorized as checked exceptions (must be caught or declared) and unchecked exceptions (do not need to be caught or declared).

### Example of Built-in Exception: `ArithmeticException`

The `ArithmeticException` is a built-in exception that occurs when an arithmetic operation encounters an exceptional condition, such as division by zero.

```java
public class ArithmeticExceptionExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // Division by zero
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero");
        }
    }
}

```

In this example:

- The `try` block attempts to perform a division operation that results in an `ArithmeticException` due to division by zero.
- The `catch` block catches the `ArithmeticException` and handles the error condition by printing an error message.
- By handling the `ArithmeticException`, the program can gracefully recover from the error and continue execution.

Built-in exceptions in Java provide a standardized way to handle errors and exceptional conditions, making it easier to write robust and reliable Java programs.

## 15) Explain Custom Exception.

### Explanation of Custom Exceptions in Java

In addition to built-in exceptions, Java allows you to create your own custom exceptions, also known as user-defined exceptions. Custom exceptions are useful when you want to handle specific error conditions that are not covered by the built-in exceptions provided by the Java API.

To create a custom exception, you need to define a new exception class that extends either the `Exception` class (for checked exceptions) or the `RuntimeException` class (for unchecked exceptions).

Here's an example of creating a custom exception:

```java
public class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

```

In this example, we define a custom exception called `InvalidAgeException` that extends the `Exception` class. This makes it a checked exception, meaning it must be caught or declared in the method signature.

Now, let's see how to use this custom exception in a program:

```java
public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            validateAge(-5);
            System.out.println("Age is valid.");
        } catch (InvalidAgeException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 0) {
            throw new InvalidAgeException("Age cannot be negative.");
        }
        // Rest of the validation logic
    }
}

```

In this example:

- The `validateAge` method checks if the given age is negative.
- If the age is negative, the method throws an `InvalidAgeException` with a custom error message.
- In the `main` method, we call the `validateAge` method inside a `try` block.
- If an `InvalidAgeException` is thrown, it is caught by the corresponding `catch` block, and the error message is printed.

By creating custom exceptions, you can provide more meaningful and specific error messages, making it easier to identify and handle exceptional conditions in your application.

Custom exceptions are particularly useful when:

- You want to provide more specific error messages than those provided by built-in exceptions.
- You need to handle exceptional conditions that are specific to your application's domain.
- You want to create a hierarchy of exceptions to organize and manage different types of errors.

Using custom exceptions can improve the maintainability and readability of your code by making it clearer where and why exceptions are being thrown.

## 16) Explain Throwable Class.

### Explanation of Throwable Class in Java

In Java, the `Throwable` class is the superclass of all exceptions and errors. It is at the top of the exception hierarchy in Java and serves as the base class for all types of exceptions that can be thrown during the execution of a Java program.

### Key Points about the Throwable Class:

1. **Hierarchy**: The `Throwable` class is at the root of the exception hierarchy in Java. It has two direct subclasses: `Exception` (for exceptional conditions that a well-written application should anticipate and recover from) and `Error` (for serious errors that are typically beyond the control of the application).
2. **Methods**:
   - `getMessage()`: Returns a detailed message about the exception.
   - `toString()`: Returns a string representation of the exception.
   - `printStackTrace()`: Prints the stack trace of the exception to the standard error stream.
3. **Common Subclasses**:
   - `Exception`: Represents exceptional conditions that a program should catch and handle.
   - `RuntimeException`: Represents exceptions that can be thrown during the normal operation of the Java Virtual Machine.
   - `Error`: Represents serious errors that are typically beyond the control of the application.

### Example of Using Throwable Class:

```java
public class ThrowableExample {
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (Throwable t) {
            System.out.println("An error occurred: " + t.getMessage());
            t.printStackTrace();
        }
    }

    public static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
}

```

In this example:

- We catch the `Throwable` superclass in the `catch` block to handle any type of exception or error that may occur.
- The `getMessage()` method is used to retrieve the exception message.
- The `printStackTrace()` method is used to print the stack trace of the exception, showing the sequence of method calls that led to the exception.

By using the `Throwable` class, you can catch and handle exceptions of different types in a more general way, providing a fallback mechanism to deal with unexpected errors in your Java programs.

## 17) Give the difference between throw and throws keywords with example.

### Difference Between `throw` and `throws` Keywords in Java

| **`throw` Keyword**                                                     | **`throws` Keyword**                                                                                |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Used to explicitly throw an exception within a method                   | Used to declare that a method may throw certain types of exceptions                                 |
| Followed by an instance of an exception class or a new exception object | Used in the method signature followed by the exception classes that the method can throw            |
| Used to throw custom exceptions based on specific conditions            | Used to specify the exceptions that the method can throw but does not handle them within the method |
| Used inside a method to raise an exception                              | Used in the method declaration to indicate the exceptions that the method might throw               |
| Example: `throw new ArithmeticException("Division by zero");`           | Example: `public void readFile() throws IOException { ... }`                                        |

### Example Demonstrating `throw` Keyword

```java
public class ThrowExample {
    public static void main(String[] args) {
        try {
            validateAge(-5);
        } catch (InvalidAgeException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 0) {
            throw new InvalidAgeException("Age cannot be negative.");
        }
    }
}

```

In this example, the `throw` keyword is used to throw a custom `InvalidAgeException` when the age is negative.

### Example Demonstrating `throws` Keyword

```java
public class ThrowsExample {
    public static void main(String[] args) {
        try {
            readFile();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void readFile() throws IOException {
        // Code that may throw an IOException
    }
}

```

In this example, the `throws` keyword is used in the method signature of `readFile()` to declare that the method may throw an `IOException`. The actual handling of the exception is done in the calling method.

## 18) Write an application that generates custom exception if any value from its command line arguments Is negative.

Here is a Java application that generates a custom exception if any value from its command line arguments is negative:

```java
public class NegativeValueException extends Exception {
    public NegativeValueException(String message) {
        super(message);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            for (String arg : args) {
                int value = Integer.parseInt(arg);
                if (value < 0) {
                    throw new NegativeValueException("Negative value found: " + value);
                }
                System.out.println("Value: " + value);
            }
        } catch (NegativeValueException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format");
        }
    }
}

```

To run this application, you can use the following command:

```
java Main 1 2 -3 4 5

```

In this example, the application will throw a `NegativeValueException` when it encounters the value `-3` in the command line arguments. The exception message will be "Negative value found: -3".

Here's how the application works:

1. The `NegativeValueException` class is a custom exception class that extends the `Exception` class.
2. In the `main` method, we iterate over the command line arguments using a `for` loop.
3. For each argument, we parse it to an integer using `Integer.parseInt`.
4. If the parsed value is negative, we throw a `NegativeValueException` with a message indicating the negative value.
5. If the parsing fails (e.g., if the argument is not a valid integer), we catch the `NumberFormatException` and print an error message.
6. If a `NegativeValueException` is thrown, we catch it and print the error message.

Note that this application assumes that the command line arguments are integers. If you want to handle other types of values, you may need to modify the application accordingly.

## 19) Write the program to print the IP address of the local machine.

Here is a Java program that prints the IP address of the local machine:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class LocalIPAddress {
    public static void main(String[] args) {
        try {
            InetAddress localhost = InetAddress.getLocalHost();
            System.out.println("Local IP Address: " + localhost.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Error: Unable to determine the local IP address.");
            e.printStackTrace();
        }
    }
}

```

When you run this program, it will retrieve the IP address of the local machine and print it to the console. The `getHostAddress()` method of the `InetAddress` class is used to get the IP address in a string format.

Make sure to handle the `UnknownHostException` that may occur if the local host's IP address cannot be determined.

## 20) What is Server Socket? How does it work in java ? Explain it with an example.

### What is ServerSocket in Java?

In Java, `ServerSocket` is a class used for creating server-side sockets. It is part of the `java.net` package and is used to listen for incoming client connections on a specific port. When a client connects to the server, the `ServerSocket` creates a new `Socket` object to handle the communication between the client and the server.

### How ServerSocket Works

1. The server creates an instance of `ServerSocket` and specifies the port number on which it will listen for incoming connections.
2. The `ServerSocket` listens for incoming connection requests on the specified port.
3. When a client connects to the server, the `ServerSocket` accepts the connection and creates a new `Socket` object to handle the communication with the client.
4. The server can then read data from the client's socket and write data back to it.

### Example of Using ServerSocket

Here's an example of a simple server-side program using `ServerSocket`:

```java
import java.io.*;
import java.net.*;

public class SimpleServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8080);
            System.out.println("Server started. Listening on port 8080...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            String message = in.readLine();
            System.out.println("Received message: " + message);

            out.println("Hello, client!");

            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

In this example:

1. The server creates a `ServerSocket` and listens for incoming connections on port 8080.
2. When a client connects, the `accept()` method blocks until a connection is made.
3. Once a connection is established, the server creates a `Socket` object to handle the communication with the client.
4. The server uses `BufferedReader` and `PrintWriter` to read and write data to the client's socket.
5. The server reads a message from the client, prints it, and sends a response back to the client.
6. Finally, the server closes the client's socket and its own `ServerSocket`.

To run this example, you would need to create a client-side program that connects to the server and sends/receives data accordingly.

By using `ServerSocket`, you can create server-side applications in Java that can handle multiple clients concurrently and communicate with them using sockets.

## 21) Explain the following classes with their use.

- DatagramSocket
- DatagramPacket class

### 1. DatagramSocket

`DatagramSocket` is a class in Java that represents a socket for sending and receiving datagram packets. It is part of the `java.net` package and is used for connectionless, unreliable, point-to-point, or multicast datagram-based communication.

Key points about `DatagramSocket`:

- It is used for sending and receiving `DatagramPacket` objects.
- It can be used for both unicast (point-to-point) and multicast communication.
- It does not establish a connection between the client and the server.
- It is suitable for applications that require fast, low-overhead communication, such as real-time applications or games.

Example usage of `DatagramSocket`:

```java
DatagramSocket socket = new DatagramSocket();
socket.send(packet);
socket.receive(packet);
socket.close();

```

### 2. DatagramPacket class

`DatagramPacket` is a class in Java that represents a datagram packet. It is part of the `java.net` package and is used in conjunction with `DatagramSocket` for sending and receiving datagram packets.

Key points about `DatagramPacket`:

- It encapsulates the data being sent or received, along with the IP address and port number of the destination or source.
- It can be used to send and receive both unicast and multicast packets.
- It provides methods to set and retrieve the data, IP address, and port number.

Example usage of `DatagramPacket`:

```java
byte[] buffer = new byte[1024];
DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
packet.setAddress(InetAddress.getByName("example.com"));
packet.setPort(8080);
packet.setData(data);

```

Here's an example of a simple UDP server and client using `DatagramSocket` and `DatagramPacket`:

Server:

```java
DatagramSocket socket = new DatagramSocket(8080);
byte[] buffer = new byte[1024];
DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
socket.receive(packet);
String message = new String(packet.getData(), 0, packet.getLength());
System.out.println("Received message: " + message);
socket.close();

```

Client:

```java
DatagramSocket socket = new DatagramSocket();
byte[] data = "Hello, server!".getBytes();
DatagramPacket packet = new DatagramPacket(data, data.length, InetAddress.getByName("localhost"), 8080);
socket.send(packet);
socket.close();

```

In this example, the server creates a `DatagramSocket` and listens for incoming packets on port 8080. The client creates a `DatagramSocket`, constructs a `DatagramPacket` with the message and the server's address and port, and sends the packet using the `send()` method. The server receives the packet and prints the message.

`DatagramSocket` and `DatagramPacket` are useful for building UDP-based applications that require fast, lightweight communication between clients and servers.

## 22) List and write the use of classes available in java.net Package.

The `java.net` package in Java provides a wide range of classes for network programming. Here's a list of some of the most commonly used classes and their uses:

1. **URL (Uniform Resource Locator)**:
   - Used for representing a URL (e.g., `http://www.example.com`).
   - Provides methods to access and manipulate the components of a URL.
2. **URLConnection**:
   - Represents a communication link between an application and a URL.
   - Used for sending and receiving data over the internet.
3. **Socket**:
   - Represents a socket for network communication.
   - Used for establishing a connection between a client and a server.
4. **ServerSocket**:
   - Represents a server-side socket for listening and accepting incoming client connections.
   - Used for creating server-side applications.
5. **DatagramSocket**:
   - Represents a socket for sending and receiving datagram packets.
   - Used for connectionless, unreliable, point-to-point, or multicast communication.
6. **DatagramPacket**:
   - Represents a datagram packet.
   - Used in conjunction with `DatagramSocket` for sending and receiving datagram packets.
7. **InetAddress**:
   - Represents an Internet Protocol (IP) address.
   - Used for resolving hostnames to IP addresses and vice versa.
8. **HttpURLConnection**:
   - Represents a connection to a URL that uses the HTTP protocol.
   - Used for sending HTTP requests and receiving responses.
9. **CookieHandler**:
   - Represents a cookie handler for managing cookies in HTTP requests and responses.
   - Used for handling cookies in web applications.
10. **NetworkInterface**:
    - Represents a network interface.
    - Used for retrieving information about network interfaces and their addresses.

Here are some examples of using these classes:

```java
// Using URL and URLConnection
URL url = new URL("<http://www.example.com>");
URLConnection connection = url.openConnection();
InputStream inputStream = connection.getInputStream();

// Using Socket and ServerSocket
ServerSocket serverSocket = new ServerSocket(8080);
Socket clientSocket = serverSocket.accept();
InputStream inputStream = clientSocket.getInputStream();

// Using DatagramSocket and DatagramPacket
DatagramSocket socket = new DatagramSocket();
byte[] buffer = new byte[1024];
DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
socket.receive(packet);

```

These are just a few examples of the classes available in the `java.net` package. Each class provides specific functionality for network programming, allowing developers to create a wide range of network applications, from simple clients and servers to complex web applications and network utilities.
