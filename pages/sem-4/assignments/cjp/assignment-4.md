# Assignment : 4

## 1) Explain socket, server socket classes in detail.

In Java, the `Socket` class and `ServerSocket` class are used for network communication between two applications over TCP/IP. Here's a detailed explanation of each class:

1. **Socket Class**:

   - The `Socket` class represents a client-side socket that connects to a server-side socket.
   - It provides methods for connecting to a server, sending and receiving data, and closing the connection.
   - To create a socket, you need to specify the IP address and port number of the server to connect to.

   Important methods of the `Socket` class include:

   - `Socket(String host, int port)`: Constructor to create a new socket and connect it to the specified host and port.
   - `InputStream getInputStream()`: Returns an input stream for this socket, which can be used to read data from the socket.
   - `OutputStream getOutputStream()`: Returns an output stream for this socket, which can be used to write data to the socket.
   - `void close()`: Closes the socket and releases any resources associated with it.

2. **ServerSocket Class**:

   - The `ServerSocket` class represents a server-side socket that listens for incoming connections from client sockets.
   - It provides methods for accepting incoming connections, sending and receiving data, and closing the server socket.
   - To create a `ServerSocket`, you need to specify the port number on which the server will listen for incoming connections.

   Important methods of the `ServerSocket` class include:

   - `ServerSocket(int port)`: Constructor to create a new server socket that listens on the specified port.
   - `Socket accept()`: Listens for a connection to be made to this socket and accepts it. The method blocks until a connection is made.
   - `InputStream getInputStream()`: Returns an input stream for this server socket, which can be used to read data from the accepted socket.
   - `OutputStream getOutputStream()`: Returns an output stream for this server socket, which can be used to write data to the accepted socket.
   - `void close()`: Closes the server socket and releases any resources associated with it.

Example of using `ServerSocket` and `Socket` classes in Java:

```java
// Server side
ServerSocket serverSocket = new ServerSocket(12345);
Socket clientSocket = serverSocket.accept();
InputStream inputStream = clientSocket.getInputStream();
OutputStream outputStream = clientSocket.getOutputStream();

// Client side
Socket socket = new Socket("localhost", 12345);
InputStream inputStream = socket.getInputStream();
OutputStream outputStream = socket.getOutputStream();

```

In this example, the server creates a `ServerSocket` listening on port `12345` and waits for a client connection. The client then creates a `Socket` and connects to the server's IP address and port number. Once the connection is established, both the server and client can use the input and output streams to send and receive data.

## 2) Write an application that reads a file and counts the number of occurrences of a character ‘a’. Supply the file name as a command line argument.

Here's a Java application that reads a file and counts the number of occurrences of the character 'a'. The file name is supplied as a command line argument:

```java
import java.io.FileReader;
import java.io.IOException;

public class CharacterCounter {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java CharacterCounter <filename>");
            return;
        }

        String fileName = args[0];
        int count = countCharacter(fileName, 'a');

        System.out.println("Number of occurrences of 'a': " + count);
    }

    public static int countCharacter(String fileName, char character) {
        int count = 0;
        try (FileReader reader = new FileReader(fileName)) {
            int c;
            while ((c = reader.read()) != -1) {
                if (Character.toLowerCase((char) c) == Character.toLowerCase(character)) {
                    count++;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return count;
    }
}

```

You can compile this code using `javac CharacterCounter.java` and run it using `java CharacterCounter <filename>`, where `<filename>` is the name of the file you want to analyze.

## 3) Explain basic terminology related to Network Programming:

a. Socket 2) Port 3)Protocol 4)IP Address 5)URL

Here's an explanation of the basic terminology related to network programming:

1. **Socket**: A socket is an endpoint for communication between two machines over a network. It is identified by an IP address and a port number. Sockets can be used to establish connections, send and receive data, and close connections.
2. **Port**: A port is a logical endpoint on a machine that is used to uniquely identify a specific process or service. Ports are numbered from 0 to 65535, and certain port numbers are reserved for specific purposes (e.g., port 80 for HTTP, port 443 for HTTPS).
3. **Protocol**: A protocol is a set of rules and conventions that govern the communication between devices on a network. Common network protocols include TCP (Transmission Control Protocol), UDP (User Datagram Protocol), HTTP (Hypertext Transfer Protocol), and FTP (File Transfer Protocol).
4. **IPAddress**: An IP address is a unique numerical label assigned to each device connected to a network that uses the Internet Protocol for communication. IP addresses are used to identify and locate devices on a network.
5. **URL (Uniform Resource Locator)**: A URL is a reference to a web resource that specifies the protocol used to access the resource (e.g., HTTP, HTTPS), the domain name or IP address of the server, and the path to the resource on the server. Example: `https://www.example.com/index.html`.

Understanding these basic terms is essential for working with network programming, as they form the foundation for communication between devices on a network.

## 4) Explain use of Linked List collection class with example.

In Java, the `LinkedList` class is a part of the `java.util` package and implements the `List` interface. It provides a linked-list data structure, which is a collection of elements where each element has a reference to the next element in the list.

Here's an example of how you can use the `LinkedList` class:

```java
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        // Creating a LinkedList
        LinkedList<String> linkedList = new LinkedList<>();

        // Adding elements to the LinkedList
        linkedList.add("Alice");
        linkedList.add("Bob");
        linkedList.add("Charlie");

        // Adding an element at the beginning of the LinkedList
        linkedList.addFirst("David");

        // Adding an element at the end of the LinkedList
        linkedList.addLast("Eve");

        // Removing an element from the LinkedList
        linkedList.remove("Bob");

        // Iterating over the LinkedList
        System.out.println("LinkedList elements:");
        for (String element : linkedList) {
            System.out.println(element);
        }

        // Getting the size of the LinkedList
        System.out.println("Size of the LinkedList: " + linkedList.size());

        // Checking if an element is present in the LinkedList
        System.out.println("Is 'Charlie' present? " + linkedList.contains("Charlie"));

        // Getting the first and last elements of the LinkedList
        System.out.println("First element: " + linkedList.getFirst());
        System.out.println("Last element: " + linkedList.getLast());

        // Removing the first and last elements of the LinkedList
        linkedList.removeFirst();
        linkedList.removeLast();

        // Clearing the LinkedList
        linkedList.clear();

        // Checking if the LinkedList is empty
        System.out.println("Is the LinkedList empty? " + linkedList.isEmpty());
    }
}

```

In this example, we create a `LinkedList` called `linkedList` and add several elements to it. We then demonstrate various operations such as adding elements at the beginning and end of the list, removing elements, iterating over the list, getting the size of the list, checking for the presence of an element, and clearing the list.

`LinkedList` is useful when you need to frequently add or remove elements from the beginning, middle, or end of the list, as it provides efficient operations for these operations compared to an array-based list.

## 5) Compare byte streams and character streams? Explain any two-character stream class in detail.

Byte streams and character streams in Java are used for reading and writing data. Here's a comparison between the two:

1. **Byte Streams**:
   - Byte streams are used for reading and writing raw bytes of data.
   - They are suitable for handling binary data, such as images, audio, video, etc.
   - Byte streams are represented by classes like `InputStream` and `OutputStream`.
   - Example classes: `FileInputStream`, `FileOutputStream`.
2. **Character Streams**:
   - Character streams are used for reading and writing text data as characters.
   - They are suitable for handling text files, where characters are represented using a character encoding (e.g., UTF-8).
   - Character streams are represented by classes like `Reader` and `Writer`.
   - Example classes: `FileReader`, `FileWriter`.

Character streams are preferred over byte streams when working with text data because they handle character encoding automatically, ensuring that characters are correctly converted to and from bytes according to the specified character encoding. This helps in avoiding encoding issues that can occur when using byte streams directly.

Here's a detailed explanation of two character stream classes, `FileReader` and `FileWriter`:

1. **FileReader**:
   - `FileReader` is used for reading text files.
   - It reads data from a file as a stream of characters.
   - Example usage:
     ```java
     try (FileReader reader = new FileReader("example.txt")) {
         int character;
         while ((character = reader.read()) != -1) {
             System.out.print((char) character);
         }
     } catch (IOException e) {
         e.printStackTrace();
     }

     ```
2. **FileWriter**:
   - `FileWriter` is used for writing text files.
   - It writes data to a file as a stream of characters.
   - Example usage:
     ```java
     try (FileWriter writer = new FileWriter("output.txt")) {
         writer.write("Hello, World!");
     } catch (IOException e) {
         e.printStackTrace();
     }

     ```

Both `FileReader` and `FileWriter` are used for reading and writing text files, respectively. They are capable of handling character encoding automatically, making them suitable for working with text data in Java.
