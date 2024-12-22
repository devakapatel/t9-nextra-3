# Assignment : 3

## 1) Explain following keyword

a. try
b. catch
c. throw
d. throws
e. finally

a. `try`: This keyword is used to start a block of code that will be tested for exceptions. The `try` block is followed by one or more `catch` blocks or a `finally` block.

b. `catch`: This keyword is used to catch an exception that is thrown within a `try` block. It is followed by a block of code that handles the exception.

c. `throw`: This keyword is used to explicitly throw an exception. It is followed by an instance of the `Throwable` class (or a subclass of `Throwable`) that represents the exception being thrown.

d. `throws`: This keyword is used in the method signature to indicate that the method may throw certain types of exceptions. It is followed by a list of the exceptions that the method may throw.

e. `finally`: This keyword is used to define a block of code that will be executed after a `try` block, regardless of whether an exception is thrown or not. The `finally` block is often used to perform cleanup tasks, such as closing resources.

These keywords are essential for handling exceptions in Java, allowing you to write robust and fault-tolerant code.

## 2) What are use of multithreading in java programming? Explain Thread class

with important method of thread class.

Multithreading in Java allows you to write programs that can perform multiple tasks concurrently, improving the efficiency and responsiveness of your applications. Here are some common uses of multithreading in Java programming:

1. **Improved performance**: Multithreading allows you to take advantage of multiple CPU cores, enabling your program to perform tasks in parallel and potentially speeding up the execution time.
2. **Concurrency**: Multithreading allows your program to handle multiple tasks simultaneously, making it easier to write programs that can respond to multiple inputs or events at the same time.
3. **Asynchronous programming**: Multithreading enables you to perform tasks asynchronously, which is useful for handling tasks that may take a long time to complete without blocking the main thread of execution.
4. **Responsive user interfaces**: Multithreading allows you to keep your application's user interface responsive while performing long-running tasks in the background.
5. **Resource sharing**: Multithreading allows multiple threads to share resources, such as memory, enabling efficient resource utilization.

Now, let's explain the `Thread` class and its important methods:

The `Thread` class in Java is the main class used for creating and managing threads. Here are some important methods of the `Thread` class:

1. `start()`: This method is used to start the execution of a thread. When the `start()` method is called, the JVM calls the `run()` method of the thread.
2. `run()`: This method contains the code that is executed by the thread. You should override this method in your subclass to define the behavior of the thread.
3. `sleep(long millis)`: This method causes the current thread to sleep for the specified number of milliseconds. It is used to introduce a delay in the execution of a thread.
4. `join()`: This method waits for the thread on which it is called to die. It is used to ensure that a thread has completed its execution before continuing with the rest of the program.
5. `interrupt()`: This method interrupts the execution of a thread. It is typically used to gracefully stop a thread by setting a flag that the thread checks periodically.
6. `isAlive()`: This method returns `true` if the thread is still alive (i.e., has been started and has not yet died), otherwise it returns `false`.

These are some of the important methods of the `Thread` class in Java. By using these methods, you can create and manage threads in your Java programs to achieve concurrency and improved performance.

## 3) What is thread synchronization? Explain it with proper class.

Thread synchronization is a mechanism in Java that ensures that only one thread can access a shared resource (such as a variable or a piece of code) at a time. This is important in multithreaded environments to prevent race conditions and ensure the consistency of shared data.

Here's an example class that demonstrates thread synchronization using the `synchronized` keyword in Java:

```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized void decrement() {
        count--;
    }

    public synchronized int getCount() {
        return count;
    }
}

```

In this `Counter` class, the `increment()` and `decrement()` methods are declared as `synchronized`, which means that only one thread can execute these methods on a particular instance of `Counter` at a time. This prevents multiple threads from concurrently modifying the `count` variable and ensures that the operations are performed atomically.

Here's an example of how you might use the `Counter` class with multiple threads:

```java
public class Main {
    public static void main(String[] args) {
        Counter counter = new Counter();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.decrement();
            }
        });

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Final count: " + counter.getCount());
    }
}

```

In this example, two threads (`t1` and `t2`) are created to increment and decrement the counter, respectively. The `synchronized` methods in the `Counter` class ensure that the operations are performed safely, and the final count is printed without any race conditions.

## 4) What is deadlock? Explain to deadlock handling mechanism.

A deadlock in multithreading occurs when two or more threads are blocked forever, waiting for each other to release the resources they need to proceed. In other words, each thread is waiting for a resource that is held by another thread, creating a cyclic dependency that cannot be resolved.

Here's a simple example to illustrate a deadlock situation:

```java
public class DeadlockExample {
    private static final Object resource1 = new Object();
    private static final Object resource2 = new Object();

    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            synchronized (resource1) {
                System.out.println("Thread 1: Holding resource 1");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 1: Waiting for resource 2");
                synchronized (resource2) {
                    System.out.println("Thread 1: Holding resource 1 and resource 2");
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            synchronized (resource2) {
                System.out.println("Thread 2: Holding resource 2");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 2: Waiting for resource 1");
                synchronized (resource1) {
                    System.out.println("Thread 2: Holding resource 2 and resource 1");
                }
            }
        });

        thread1.start();
        thread2.start();
    }
}

```

In this example, `thread1` locks `resource1` and then tries to lock `resource2`, while `thread2` locks `resource2` and then tries to lock `resource1`. Since each thread is holding one resource and waiting for the other, both threads will be blocked forever, leading to a deadlock.

To prevent deadlocks, you can follow some best practices:

1. **Avoid nested locks**: Try to avoid acquiring multiple locks in a nested manner. If you must, ensure that all locks are acquired in the same order across all threads.
2. **Use a timeout**: When acquiring locks, use `tryLock()` instead of `synchronized` blocks and specify a timeout. If a lock cannot be acquired within the timeout, release all locks and retry later.
3. **Avoid long-running operations inside synchronized blocks**: Long-running operations inside synchronized blocks increase the likelihood of deadlocks. Try to keep synchronized blocks short and simple.
4. **Avoid waiting for resources while holding a lock**: If a thread needs to wait for a resource, it should release any locks it holds to avoid potential deadlocks.
5. **Use higher-level concurrency utilities**: Instead of using low-level synchronization primitives like `synchronized` blocks, consider using higher-level concurrency utilities provided by Java, such as `java.util.concurrent` classes. These classes often provide built-in mechanisms to avoid deadlocks.

## 5) Explain generic class with the help of example.

A generic class in Java is a class that can work with any data type. It allows you to create classes, interfaces, and methods that operate on parameters, which are specified at compile time. Generics provide compile-time type safety, allowing you to catch errors at compile time rather than at runtime.

Here's an example of a generic class in Java:

```java
public class Box<T> {
    private T value;

    public void setValue(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public static void main(String[] args) {
        // Creating a Box for Integer
        Box<Integer> integerBox = new Box<>();
        integerBox.setValue(10);
        System.out.println("Integer value: " + integerBox.getValue());

        // Creating a Box for String
        Box<String> stringBox = new Box<>();
        stringBox.setValue("Hello, World!");
        System.out.println("String value: " + stringBox.getValue());
    }
}

```

In this example, the `Box` class is a generic class with a type parameter `T`. This `T` can be any type, and it is specified when creating an instance of the `Box` class.

In the `main` method, we create two instances of the `Box` class: one for `Integer` and one for `String`. We can set and get values of any type using the `Box` class, and the compiler ensures type safety at compile time.
