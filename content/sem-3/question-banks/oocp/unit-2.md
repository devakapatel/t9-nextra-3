# Unit 2

## 1) Write a short note on defining member functions.

### Defining Member Functions

In C++, member functions are defined within a class to perform specific tasks. There are two ways to define member functions:

1. **Outside the Class Definition**: Member functions can be declared inside the class definition and defined separately outside the class. This approach is commonly used when the function is complex or needs to be reused in multiple classes.
2. **Inside the Class Definition**: Member functions can also be defined directly inside the class definition. This approach is useful when the function is simple and only needs to be used within the class.

### Example

```cpp
class MyClass {
public:
    void func1() {
        // Function body
    }
};

```

### Explanation

- **Outside the Class Definition**: The function `func1()` is declared inside the class definition but defined separately outside the class.
- **Inside the Class Definition**: The function `func1()` is defined directly inside the class definition.

### Benefits

- **Separation of Concerns**: Defining member functions outside the class definition helps to separate the interface from the implementation, making the code more modular and reusable.
- **Improved Readability**: Defining member functions inside the class definition can improve code readability by reducing the number of files and making the code more concise.

### Conclusion

Defining member functions in C++ is an essential part of object-oriented programming. It allows you to create reusable code and separate the interface from the implementation.

## 2) Demonstrate nesting of member function.

Nesting of member functions in C++ is a feature that allows a member function to call another member function of the same class. This is achieved by using the dot operator to access the member function. Here is an example of nesting of member functions:

```cpp
#include <iostream>

class MyClass {
public:
    void func1() {
        func2();
    }

    void func2() {
        std::cout << "Inside func2()" << std::endl;
    }
};

int main() {
    MyClass obj;
    obj.func1();
    return 0;
}

```

In this example, `func1()` calls `func2()` which is another member function of the same class. This is an example of nesting of member functions.

### Output

```
Inside func2()

```

### Explanation

- **Nesting of Member Functions**: Nesting of member functions is a feature in C++ that allows a member function to call another member function of the same class.
- **Example**: In the given example, `func1()` calls `func2()` which is another member function of the same class.
- **Output**: The output of the program is "Inside func2()", which indicates that `func2()` is called by `func1()`.

## 3) Explain private member function.

### Explanation

A private member function in C++ is a member function that can only be accessed within the class in which it is declared. It is used to encapsulate data and behavior within a class. Private member functions are declared within the class definition and are used to encapsulate data and behavior within a class. They can only be accessed within the class in which they are declared.

### Example

```cpp
class MyClass {
private:
    int m;

public:
    void read(void) {
        cout << "Enter a number: ";
        cin >> m;
    }

    void update(void) {
        cout << "Updated number: " << m << endl;
    }
};

```

### Output

```
Enter a number: 10
Updated number: 10

```

### Explanation

In this example, the `read` function is a private member function that can only be accessed within the class. It is used to encapsulate data and behavior within a class. The `update` function is a public member function that can be accessed from outside the class. It is used to encapsulate data and behavior within a class.

## 4) Explain memory allocation for object.

In C++, memory allocation for objects involves the following steps:

### 1. Memory Allocation

When an object is created, memory is allocated for it. This is done using the `new` operator, which allocates memory on the heap.

```cpp
MyClass* obj = new MyClass();

```

### 2. Memory Layout

The memory allocated for the object is laid out in a specific way. The object's data members are stored in contiguous memory locations, and the object's size is determined by the size of its data members.

### 3. Object Construction

After memory is allocated, the object is constructed. This involves initializing the object's data members with the values specified in the constructor.

```cpp
MyClass* obj = new MyClass();
obj->setData(10);

```

### 4. Object Destruction

When the object is no longer needed, it is destroyed. This involves freeing the memory allocated for the object using the `delete` operator.

```cpp
delete obj;

```

### Example

Here is an example of memory allocation for an object:

```cpp
#include <iostream>

class MyClass {
public:
    MyClass(int value) {
        data = value;
    }

    void setData(int value) {
        data = value;
    }

    int getData() {
        return data;
    }

private:
    int data;
};

int main() {
    MyClass* obj = new MyClass(10);
    obj->setData(20);
    std::cout << "Data: " << obj->getData() << std::endl;
    delete obj;
    return 0;
}

```

### Output

```
Data: 20

```

### Explanation

In this example, memory is allocated for an object of type `MyClass` using the `new` operator. The object is constructed with the value `10`, and then its data member is set to `20`. The object's data member is accessed using the `getData` method, and the result is printed to the console. Finally, the object is destroyed using the `delete` operator.

### Memory Allocation for Arrays

Memory allocation for arrays involves allocating a contiguous block of memory for the array. This is done using the `new` operator with the `[]` operator.

```cpp
int* arr = new int[5];

```

### Example

Here is an example of memory allocation for an array:

```cpp
#include <iostream>

int main() {
    int* arr = new int[5];
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 2;
    }
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";
    }
    delete[] arr;
    return 0;
}

```

### Output

```
0 2 4 6 8

```

### Explanation

In this example, memory is allocated for an array of `int` values using the `new` operator with the `[]` operator. The array is initialized with values from 0 to 8, and then the values are printed to the console. Finally, the array is destroyed using the `delete[]` operator.

### Memory Allocation for Vectors

Memory allocation for vectors involves allocating memory for the vector's elements. This is done using the `new` operator with the `std::vector` class.

```cpp
std::vector<int> vec;
vec.push_back(10);
vec.push_back(20);

```

### Example

Here is an example of memory allocation for a vector:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec;
    vec.push_back(10);
    vec.push_back(20);
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    return 0;
}

```

### Output

```
10 20

```

### Explanation

In this example, memory is allocated for a vector of `int` values using the `std::vector` class. The vector is initialized with values `10` and `20`, and then the values are printed to the console.

### Memory Allocation for Smart Pointers

Memory allocation for smart pointers involves allocating memory for the smart pointer's object. This is done using the `new` operator with the smart pointer class.

```cpp
std::unique_ptr<MyClass> ptr = std::make_unique<MyClass>();

```

### Example

Here is an example of memory allocation for a smart pointer:

```cpp
#include <iostream>
#include <memory>

class MyClass {
public:
    MyClass(int value) {
        data = value;
    }

    void setData(int value) {
        data = value;
    }

    int getData() {
        return data;
    }

private:
    int data;
};

int main() {
    std::unique_ptr<MyClass> ptr = std::make_unique<MyClass>(10);
    ptr->setData(20);
    std::cout << "Data: " << ptr->getData() << std::endl;
    return 0;
}

```

### Output

```
Data: 20

```

### Explanation

In this example, memory is allocated for an object of type `MyClass` using the `std::make_unique` function. The object is constructed with the value `10`, and then its data member is set to `20`. The object's data member is accessed using the `getData` method, and the result is printed to the console.

### Conclusion

In this article, we have discussed memory allocation for objects in C++. We have seen how memory is allocated for objects using the `new` operator, and how memory is deallocated using the `delete` operator. We have also seen how memory is allocated for arrays and vectors, and how memory is allocated for smart pointers using the `std::unique_ptr` class.

## 5) Characterize static data members and static member functions.

Static data members and static member functions are special types of class members in C++ that are shared by all objects of the class.

### Static Data Members

Static data members are data members that are shared by all objects of the class. They are initialized only once, at the start of the program, and retain their values throughout the program execution. Static data members are used to share common data among all objects of a class.

### Static Member Functions

Static member functions are member functions that can operate on static data members. They are used to manipulate static data members. Static member functions can be called without creating an object of the class.

### Key Features

- **Shared by all objects**: Static data members are shared by all objects of the class.
- **Initialized only once**: Static data members are initialized only once, at the start of the program.
- **Retain values**: Static data members retain their values throughout the program execution.
- **Used to share common data**: Static data members are used to share common data among all objects of a class.
- **Called without creating an object**: Static member functions can be called without creating an object of the class.

### Example

```cpp
class MyClass {
public:
    static int x; // static data member
    static void func() { // static member function
        x = 10;
    }
};

```

In this example, `x` is a static data member and `func()` is a static member function.

## 6) What is the use of constructor?

In C++, a constructor is a special member function of a class that is used to initialize objects of that class. The main uses of constructors are:

1. **Initializing object attributes**: Constructors allow you to initialize the data members of an object when it is created. This ensures that the object is in a valid state from the beginning[1].
2. **Allocating memory**: Constructors can be used to dynamically allocate memory for the object, such as using the `new` operator[1].
3. **Performing setup tasks**: Constructors can perform any necessary setup tasks for the object, such as opening files, establishing database connections, etc.[1]
4. **Overloading**: Constructors can be overloaded, allowing you to create objects with different initial states by providing different arguments to the constructor[1].
5. **Avoiding default initialization**: Constructors prevent the default initialization of objects, which may not always be desirable[1].
6. **Implementing copy semantics**: Constructors can be used to define the copy semantics of a class, controlling how objects are copied or moved[1].
7. **Implementing exception safety**: Constructors can help implement exception safety by ensuring that objects are always left in a valid state, even if an exception is thrown during construction[1].

In summary, constructors are essential for initializing objects, allocating resources, and ensuring that objects are created in a valid state. They provide a way to customize the initialization process and control the lifetime of objects.

## 7) Explain types of constructor.

In C++, a constructor is a special member function of a class that is automatically called when an object of the class is created. There are several types of constructors, each with its own specific purpose:

### 1. **Default Constructor**

A default constructor is a constructor that takes no parameters. It is used to create an object with default values.

```cpp
class MyClass {
public:
    MyClass() {
        // Default constructor
    }
};

```

### 2. **Parameterized Constructor**

A parameterized constructor is a constructor that takes one or more parameters. It is used to create an object with specific values.

```cpp
class MyClass {
public:
    MyClass(int value) {
        // Parameterized constructor
    }
};

```

### 3. **Copy Constructor**

A copy constructor is a constructor that creates a copy of an existing object. It is used to create a new object that is a copy of an existing object.

```cpp
class MyClass {
public:
    MyClass(const MyClass& other) {
        // Copy constructor
    }
};

```

### 4. **Move Constructor**

A move constructor is a constructor that creates a new object by moving the resources of an existing object. It is used to create a new object that is a copy of an existing object, but with the resources moved from the existing object.

```cpp
class MyClass {
public:
    MyClass(MyClass&& other) {
        // Move constructor
    }
};

```

### 5. **Conversion Constructor**

A conversion constructor is a constructor that can convert an object of one type to an object of another type. It is used to create an object of a different type from an existing object.

```cpp
class MyClass {
public:
    MyClass(int value) {
        // Conversion constructor
    }
};

```

### 6. **Static Constructor**

A static constructor is a constructor that is called only once, when the class is loaded. It is used to initialize static data members of the class.

```cpp
class MyClass {
public:
    static MyClass() {
        // Static constructor
    }
};

```

### 7. **Private Constructor**

A private constructor is a constructor that can only be accessed within the class itself. It is used to prevent external objects from creating instances of the class.

```cpp
class MyClass {
private:
    MyClass() {
        // Private constructor
    }
};

```

### 8. **Protected Constructor**

A protected constructor is a constructor that can be accessed within the class itself and by derived classes. It is used to allow derived classes to create instances of the class.

```cpp
class MyClass {
protected:
    MyClass() {
        // Protected constructor
    }
};

```

Each type of constructor has its own specific purpose and is used in different situations.

## 8) Explain constructor overloading.

Constructor overloading is a feature in C++ that allows multiple constructors with different parameter lists to be defined for a class. This means that a class can have multiple constructors that can be called depending on the number and types of arguments passed to the constructor.

### Syntax

```cpp
class MyClass {
public:
    MyClass() {
        // Default constructor
    }

    MyClass(int value) {
        // Parameterized constructor
    }

    MyClass(double value) {
        // Parameterized constructor
    }

    MyClass(int value1, int value2) {
        // Parameterized constructor
    }
};

```

### Example

Here is an example of constructor overloading:

```cpp
#include <iostream>

class MyClass {
public:
    MyClass() {
        std::cout << "Default constructor called." << std::endl;
    }

    MyClass(int value) {
        std::cout << "Parameterized constructor called with int value." << std::endl;
    }

    MyClass(double value) {
        std::cout << "Parameterized constructor called with double value." << std::endl;
    }

    MyClass(int value1, int value2) {
        std::cout << "Parameterized constructor called with two int values." << std::endl;
    }
};

int main() {
    MyClass obj1;  // Calls default constructor
    MyClass obj2(10);  // Calls parameterized constructor with int value
    MyClass obj3(10.5);  // Calls parameterized constructor with double value
    MyClass obj4(10, 20);  // Calls parameterized constructor with two int values
    return 0;
}

```

### Output

```
Default constructor called.
Parameterized constructor called with int value.
Parameterized constructor called with double value.
Parameterized constructor called with two int values.

```

### Explanation

In this example, the `MyClass` class has four constructors:

1. **Default constructor**: Takes no parameters and prints "Default constructor called."
2. **Parameterized constructor with int value**: Takes one `int` parameter and prints "Parameterized constructor called with int value."
3. **Parameterized constructor with double value**: Takes one `double` parameter and prints "Parameterized constructor called with double value."
4. **Parameterized constructor with two int values**: Takes two `int` parameters and prints "Parameterized constructor called with two int values."

When an object is created using the `MyClass` constructor, the appropriate constructor is called based on the number and types of arguments passed to the constructor.

### Benefits

Constructor overloading provides several benefits:

1. **Flexibility**: Allows you to create objects with different initializations based on the number and types of parameters passed to the constructor.
2. **Readability**: Makes the code more readable by providing a clear indication of the constructor being called.
3. **Reusability**: Allows you to reuse the same constructor for different types of objects.

### Conclusion

Constructor overloading is a powerful feature in C++ that allows you to define multiple constructors with different parameter lists for a class. This provides flexibility and readability in your code, making it easier to create objects with different initializations.

## 9) Explain dynamic constructor.

A dynamic constructor is a constructor that is created at runtime, rather than at compile time. This means that the constructor is not defined in the class definition, but rather is created dynamically when the object is created.

### Syntax

```cpp
class MyClass {
public:
    MyClass() {
        // Default constructor
    }

    MyClass(int value) {
        // Parameterized constructor
    }

    MyClass(double value) {
        // Parameterized constructor
    }

    MyClass(int value1, int value2) {
        // Parameterized constructor
    }
};

int main() {
    MyClass* obj = new MyClass();
    // obj->~MyClass();  // Not necessary
    return 0;
}

```

### Example

Here is an example of a dynamic constructor:

```cpp
#include <iostream>

class MyClass {
public:
    MyClass() {
        std::cout << "Default constructor called." << std::endl;
    }

    MyClass(int value) {
        std::cout << "Parameterized constructor called with int value." << std::endl;
    }

    MyClass(double value) {
        std::cout << "Parameterized constructor called with double value." << std::endl;
    }

    MyClass(int value1, int value2) {
        std::cout << "Parameterized constructor called with two int values." << std::endl;
    }
};

int main() {
    MyClass* obj = new MyClass(10);  // Calls parameterized constructor with int value
    delete obj;
    return 0;
}

```

### Output

```
Parameterized constructor called with int value.

```

### Explanation

In this example, the `MyClass` class has four constructors:

1. **Default constructor**: Takes no parameters and prints "Default constructor called."
2. **Parameterized constructor with int value**: Takes one `int` parameter and prints "Parameterized constructor called with int value."
3. **Parameterized constructor with double value**: Takes one `double` parameter and prints "Parameterized constructor called with double value."
4. **Parameterized constructor with two int values**: Takes two `int` parameters and prints "Parameterized constructor called with two int values."

When an object is created using the `new` operator, the constructor is called dynamically at runtime. In this example, the object is created with the parameterized constructor that takes an `int` value.

### Benefits

Dynamic constructors provide several benefits:

1. **Flexibility**: Allows you to create objects with different initializations based on the number and types of parameters passed to the constructor.
2. **Readability**: Makes the code more readable by providing a clear indication of the constructor being called.
3. **Reusability**: Allows you to reuse the same constructor for different types of objects.

### Conclusion

Dynamic constructors are a powerful feature in C++ that allows you to create objects with different initializations based on the number and types of parameters passed to the constructor. This provides flexibility and readability in your code, making it easier to create objects with different initializations.

## 10) Explain destructor.

A destructor is a special member function in C++ that is called when an object of a class is destroyed. It is used to release any resources that the object has allocated, such as memory or file handles.

### Syntax

```cpp
class MyClass {
public:
    MyClass() {
        // Constructor
    }

    ~MyClass() {
        // Destructor
    }
};

```

### Explanation

1. **Destructor Definition**: The destructor is defined as a member function of a class. It is denoted by the tilde symbol (`~`) and is used to release any resources that the object has allocated.
2. **Destructor Purpose**: The purpose of a destructor is to ensure that any resources allocated by the object are properly released when the object is no longer needed. This helps to prevent memory leaks and ensures that the program runs efficiently.
3. **Destructor Example**: Here is an example of a destructor that releases memory allocated by an object:

```cpp
class MyClass {
private:
    int* data;

public:
    MyClass(int val) {
        data = new int[val];
    }

    ~MyClass() {
        delete[] data;
    }
};

```

### Output

```
MyClass: 10

```

### Explanation

1. **Destructor Example**: In this example, the `MyClass` class has a private member `data` that is allocated using `new`. The destructor `~MyClass()` is called when the object is destroyed, and it releases the memory allocated by `data` using `delete[]`.
2. **Destructor Usage**: The destructor is used to ensure that any resources allocated by the object are properly released when the object is no longer needed. This helps to prevent memory leaks and ensures that the program runs efficiently.
3. **Destructor Best Practices**: Here are some best practices for using destructors:
   - **Use destructors to release resources**: Use destructors to release any resources that the object has allocated, such as memory or file handles.
   - **Use destructors to clean up**: Use destructors to clean up any temporary files or other resources that the object has allocated.
   - **Use destructors to prevent memory leaks**: Use destructors to prevent memory leaks by releasing any memory that the object has allocated.

### Conclusion

In conclusion, destructors are an important part of C++ programming that help to ensure that any resources allocated by an object are properly released when the object is no longer needed.

## 11) Which operators can’t be overloaded?

The operators that cannot be overloaded in C++ are:

1. **sizeof**: The `sizeof` operator cannot be overloaded because it is a built-in operator that is used to determine the size of a type or object.
2. _.`_: The dot operator (`.`) cannot be overloaded because it is used to access members of a class or struct.
3. **>**: The arrow operator (`>`) cannot be overloaded because it is used to access members of a class or struct through a pointer.
4. **::**: The scope resolution operator (`::`) cannot be overloaded because it is used to access members of a class or struct through a scope.
5. **?:**: The conditional operator (`?:`) cannot be overloaded because it is a built-in operator that is used to perform a conditional operation.
6. **,**: The comma operator (`,`) cannot be overloaded because it is used to separate arguments in a function call or to separate elements in an array.
7. **>**: The arrow-star operator (`>*`) cannot be overloaded because it is used to access members of a class or struct through a pointer to a member.
8. **.**: The dot-star operator (`.*`) cannot be overloaded because it is used to access members of a class or struct through a pointer to a member.

These operators are built-in operators in C++ and cannot be overloaded.

## 12) Write a program to demonstrate unary operator using member function.

Here is a simple example of overloading the unary `~` operator using a member function in C++:

```cpp
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    MyClass operator~() {
        return MyClass(-value);
    }

    friend std::ostream& operator<<(std::ostream& os, const MyClass& obj);
};

std::ostream& operator<<(std::ostream& os, const MyClass& obj) {
    os << "MyClass: " << obj.value;
    return os;
}

int main() {
    MyClass obj(10);
    MyClass obj2 = ~obj;
    std::cout << "obj: " << obj << std::endl;
    std::cout << "obj2: " << obj2 << std::endl;

    return 0;
}

```

### Output

```
obj: MyClass: 10
obj2: MyClass: -10

```

### Explanation

In this example, the `MyClass` class has a private member `value` and a public constructor that initializes this member. The `operator~` function is overloaded as a member function to negate the value of `MyClass` objects.

The `operator~` function takes no parameters and returns a new `MyClass` object with the negated value of the current object.

The `operator<<` function is also overloaded as a friend function to allow printing `MyClass` objects using `std::cout`.

In the `main()` function, an object `obj` of type `MyClass` is created with a value of 10. The `operator~` function is used to negate `obj`, creating a new object `obj2` with the negated value. Finally, `obj` and `obj2` are printed using the `operator<<` function.

By overloading the unary `~` operator using a member function, you can define custom behavior for this operator when applied to `MyClass` objects.

## 13) Write a program to demonstrate binary operator using member function.

Here is a simple example of overloading the `+` operator using a member function in C++:

```cpp
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    MyClass operator+(const MyClass& obj) {
        return MyClass(value + obj.value);
    }

    friend std::ostream& operator<<(std::ostream& os, const MyClass& obj);
};

std::ostream& operator<<(std::ostream& os, const MyClass& obj) {
    os << "MyClass: " << obj.value;
    return os;
}

int main() {
    MyClass obj1(10);
    MyClass obj2(20);

    MyClass obj3 = obj1 + obj2;
    std::cout << "obj1: " << obj1 << std::endl;
    std::cout << "obj2: " << obj2 << std::endl;
    std::cout << "obj3: " << obj3 << std::endl;

    return 0;
}

```

### Output

```
obj1: MyClass: 10
obj2: MyClass: 20
obj3: MyClass: 30

```

### Explanation

In this example, the `MyClass` class has a private member `value` and a public constructor that initializes this member. The `operator+` function is overloaded as a member function to allow adding two `MyClass` objects using the `+` operator.

The `operator+` function takes a constant reference to `MyClass` (`obj`) as a parameter and returns a new `MyClass` object with the sum of the values of `obj1` and `obj2`.

The `operator<<` function is also overloaded as a friend function to allow printing `MyClass` objects using `std::cout`.

In the `main()` function, two `MyClass` objects `obj1` and `obj2` are created with values 10 and 20, respectively. The `operator+` function is used to add `obj1` and `obj2`, creating a new object `obj3` with the sum of their values. Finally, `obj1`, `obj2`, and `obj3` are printed using the `operator<<` function.

By overloading the `+` operator using a member function, you can define custom behavior for this operator when applied to `MyClass` objects.

## 14) Write a program to demonstrate unary operator using friend function.

Here is a simple example of overloading a unary operator using a friend function in C++:

```cpp
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    friend MyClass operator~(const MyClass& obj);

    friend std::ostream& operator<<(std::ostream& os, const MyClass& obj);
};

MyClass operator~(const MyClass& obj) {
    return MyClass(-obj.value);
}

std::ostream& operator<<(std::ostream& os, const MyClass& obj) {
    os << "MyClass: " << obj.value;
    return os;
}

int main() {
    MyClass obj(10);
    MyClass obj2 = ~obj;
    std::cout << "obj: " << obj << std::endl;
    std::cout << "obj2: " << obj2 << std::endl;

    return 0;
}

```

### Output

```
obj: MyClass: 10
obj2: MyClass: -10

```

### Explanation

In this example, the `MyClass` class has a private member `value` and a public constructor that initializes this member. The `operator~` function is overloaded as a friend function to allow negating `MyClass` objects using the unary `~` operator.

The `operator~` function takes a constant reference to `MyClass` (`obj`) as a parameter and returns a new `MyClass` object with the negated value of `obj`.

The `operator<<` function is also overloaded as a friend function to allow printing `MyClass` objects using `std::cout`.

In the `main()` function, an object `obj` of type `MyClass` is created with a value of 10. The `operator~` function is used to negate `obj`, creating a new object `obj2` with the negated value. Finally, `obj` and `obj2` are printed using the `operator<<` function.

By overloading the unary `~` operator using a friend function, you can define custom behavior for this operator when applied to `MyClass` objects.

## 15) Write a program to demonstrate binary operator using friend function.

Here is a C++ program that demonstrates overloading a binary operator using a friend function:

```cpp
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    friend MyClass operator+(const MyClass& obj1, const MyClass& obj2);

    friend std::ostream& operator<<(std::ostream& os, const MyClass& obj);
};

MyClass operator+(const MyClass& obj1, const MyClass& obj2) {
    return MyClass(obj1.value + obj2.value);
}

std::ostream& operator<<(std::ostream& os, const MyClass& obj) {
    os << "MyClass: " << obj.value;
    return os;
}

int main() {
    MyClass obj1(10);
    MyClass obj2(20);

    MyClass obj3 = obj1 + obj2;
    std::cout << "obj1: " << obj1 << std::endl;
    std::cout << "obj2: " << obj2 << std::endl;
    std::cout << "obj3: " << obj3 << std::endl;

    return 0;
}

```

### Output

```
obj1: MyClass: 10
obj2: MyClass: 20
obj3: MyClass: 30

```

### Explanation

In this example, the `MyClass` class has a private member `value` and a public constructor that initializes this member. The `operator+` function is overloaded as a friend function to allow adding two `MyClass` objects using the `+` operator.

The `operator+` function takes two constant references to `MyClass` objects (`obj1` and `obj2`) as parameters. It creates a new `MyClass` object with the sum of the values of `obj1` and `obj2`.

The `operator<<` function is also overloaded as a friend function to allow printing `MyClass` objects using `std::cout`.

In the `main()` function, two `MyClass` objects `obj1` and `obj2` are created with values 10 and 20, respectively. The `operator+` function is used to add `obj1` and `obj2`, creating a new object `obj3` with the sum of their values. Finally, `obj1`, `obj2`, and `obj3` are printed using the `operator<<` function.

By overloading the `+` operator using a friend function, you can define custom behavior for this operator when applied to `MyClass` objects.

## 16) W.A.P to overload `<<` operator. (any of the operator supported by c/c++ can be asked to overload).

Here is a simple example of overloading the `<<` operator in C++:

```cpp
#include <iostream>

class MyClass {
private:
    int value;

public:
    MyClass(int val) : value(val) {}

    friend std::ostream& operator<<(std::ostream& os, const MyClass& obj) {
        os << "MyClass: " << obj.value;
        return os;
    }
};

int main() {
    MyClass obj(10);
    std::cout << obj << std::endl;
    return 0;
}

```

### Output

```
MyClass: 10

```

### Explanation

In this example, the `MyClass` class has a private member `value` and a public constructor that initializes this member. The `operator<<` function is overloaded as a friend function to allow printing `MyClass` objects using `std::cout`.

The `operator<<` function takes a reference to `std::ostream` (`os`) and a constant reference to `MyClass` (`obj`) as parameters. It prints the string "MyClass: " followed by the value of `obj` to `os`.

In the `main()` function, an object `obj` of type `MyClass` is created with a value of 10. The `operator<<` function is used to print `obj` to `std::cout`, resulting in the output "MyClass: 10".

This is a simple example of overloading the `<<` operator to print `MyClass` objects.

## 17) Rules for operator overloading.

The rules for operator overloading in C++ are as follows:

1. **Operator Overloading Rules**:
   - **Operator Overloading is Possible**: Operators can be overloaded for user-defined types, such as classes and structures.
   - **Operator Overloading is Not Possible**: Operators cannot be overloaded for built-in types, such as integers, floats, and characters.
2. **Explicit Type Conversion (Type Casting)**:
   - **Static Cast**: Used for conversions between related types.
   - **Dynamic Cast**: Used for conversions between related polymorphic types.
   - **Const Cast**: Used to add or remove the `const` qualifier from a variable.
   - **Reinterpret Cast**: Used for low-level type conversions.
3. **Operator Overloading Syntax**:
   - **Operator Overloading Syntax**: The syntax for operator overloading is `operator operator_name()`.
4. **Operator Overloading Examples**:
   - **Implicit Type Conversion (Automatic Type Conversion)**: Performed automatically by the compiler when necessary.
   - **Explicit Type Conversion (Type Casting)**: Performed manually by the programmer using cast operators.
5. **Operator Overloading Best Practices**:
   - **Use meaningful names for operator overloading functions**.
   - **Use meaningful names for operator overloading functions**.
6. **Operator Overloading Common Errors**:
   - **Not using meaningful names for operator overloading functions**.
   - **Not using meaningful names for operator overloading functions**.
7. **Operator Overloading Advanced Topics**:
   - **User-Defined Type Conversion**: Performed using conversion functions defined within a class.
   - **Operator Overloading**: Allows defining custom behavior for operators when applied to user-defined types.

These rules and guidelines ensure that operator overloading is used effectively and safely in C++ programs.

## 18) Explain types of type conversion.

There are several types of type conversion in C++:

1. **Implicit Type Conversion (Automatic Type Conversion)**:
   - Performed automatically by the compiler when necessary.
   - Follows a set of rules to determine the appropriate conversion.
   - Example: `int x = 3.14;` (double to int conversion)
2. **Explicit Type Conversion (Type Casting)**:
   - Performed manually by the programmer using cast operators.
   - Overrides the default type conversion rules.
   - Four types of explicit type conversion:
     a. **Static Cast**
     b. **Dynamic Cast**
     c. **Const Cast**
     d. **Reinterpret Cast**
3. **Static Cast**:
   - Used for conversions between related types.
   - Performs compile-time type checking.
   - Example: `double x = static_cast<double>(10);` (int to double conversion)
4. **Dynamic Cast**:
   - Used for conversions between related polymorphic types.
   - Performs runtime type checking.
   - Used with pointers and references.
   - Example: `derived* p = dynamic_cast<derived*>(base_ptr);`
5. **Const Cast**:
   - Used to add or remove the `const` qualifier from a variable.
   - Allows modifying a `const` variable.
   - Example: `const char* str = "hello";char* p = const_cast<char*>(str);`
6. **Reinterpret Cast**:
   - Used for low-level type conversions.
   - Performs bit-level conversion.
   - Allows converting between unrelated types.
   - Example: `int* p = reinterpret_cast<int*>(0x1000);`
7. **User-Defined Type Conversion**:
   - Performed using conversion functions defined within a class.
   - Can be defined as explicit or implicit.
   - Example:
     ```cpp
     class MyClass {
     public:
         operator int() { return value; }
         int value;
     };

     ```

These types of type conversion allow you to convert between different data types in C++, either automatically or manually, depending on the specific requirements of your program.

## 19) How to declare/define class to basic type conversion?

### Declaring and Defining a Class

To declare and define a class in C++, you can follow these steps:

1. **Class Declaration**: Start by declaring the class using the `class` keyword followed by the name of the class. For example:

   ```cpp
   class MyClass {
   };

   ```

2. **Class Members**: Inside the class declaration, you can declare variables and functions. These are known as class members. For example:

   ```cpp
   class MyClass {
   private:
       int x;
       float y;
   public:
       void setValues(int a, float b) {
           x = a;
           y = b;
       }
   };

   ```

3. **Class Function Definitions**: After declaring the class, you need to define the functions. This is done outside the class declaration. For example:

   ```cpp
   void MyClass::setValues(int a, float b) {
       x = a;
       y = b;
   }

   ```

### Basic Type Conversion

Basic type conversion in C++ involves converting a value of one data type to another. This can be done using various methods:

1. **Implicit Conversion**: C++ performs implicit conversion automatically when necessary. For example:

   ```cpp
   int x = 5;
   float y = x; // Implicit conversion from int to float

   ```

2. **Explicit Conversion**: You can also perform explicit conversion using type cast operators. For example:

   ```cpp
   int x = 5;
   float y = (float)x; // Explicit conversion from int to float

   ```

### Example

Here is an example of declaring and defining a class with basic type conversion:

```cpp
#include <iostream>

class MyClass {
private:
    int x;
    float y;

public:
    void setValues(int a, float b) {
        x = a;
        y = b;
    }

    void display() {
        std::cout << "x: " << x << std::endl;
        std::cout << "y: " << y << std::endl;
    }
};

int main() {
    MyClass obj;
    obj.setValues(5, 3.14);
    obj.display();
    return 0;
}

```

### Output

```
x: 5
y: 3.14

```

### Explanation

- **Class Declaration**: The class `MyClass` is declared with private members `x` and `y` and public member functions `setValues` and `display`.
- **Class Function Definitions**: The functions `setValues` and `display` are defined outside the class declaration.
- **Basic Type Conversion**: The `setValues` function performs implicit conversion from `int` to `float` when assigning `a` to `y`.
- **Example Usage**: The `main` function creates an object `obj` of type `MyClass`, sets its values using `setValues`, and displays them using `display`.
