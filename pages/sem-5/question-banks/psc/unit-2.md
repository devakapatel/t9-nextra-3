# Unit 2

## 1) Explain various OOPS concepts used in Python.

### Object-Oriented Programming (OOP) Concepts in Python

Python is a multi-paradigm programming language, which means it supports both procedural and object-oriented programming (OOP) styles. OOP is a programming approach that focuses on creating objects that contain both data (attributes) and code (methods) that can interact with each other.

Here are some key OOP concepts used in Python:

#### 1. **Class**

A class is a blueprint or template for creating objects. It defines the structure and behavior of an object. In Python, you define a class using the `class` keyword followed by the class name.

```python
class Car:
    pass

```

#### 2. **Object**

An object is an instance of a class. It represents a specific entity with its own attributes and behaviors. You create an object by calling the class as if it were a function.

```python
my_car = Car()

```

#### 3. **Attribute**

Attributes are variables that hold data associated with a class or object. They can be defined inside or outside the class.

```python
class Car:
    wheels = 4  ## Class attribute

    def __init__(self, make, model):
        self.make = make  ## Instance attribute
        self.model = model

```

#### 4. **Method**

Methods are functions defined within a class that define the behavior of an object. They operate on the object's attributes and can also take parameters.

```python
class Car:
    def start(self):
        print("Starting the car.")

    def drive(self, speed):
        print(f"Driving the car at {speed} mph.")

```

#### 5. **Inheritance**

Inheritance allows a class to inherit attributes and methods from another class. The inheriting class is called the derived or child class, and the class being inherited from is called the base or parent class.

```python
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

```

#### 6. **Encapsulation**

Encapsulation is the practice of hiding the internal implementation details of an object from the outside world. In Python, you can achieve encapsulation using name mangling (adding a leading underscore).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  ## Private attribute

    def deposit(self, amount):
        self.__balance += amount

```

#### 7. **Polymorphism**

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the use of a single interface to represent different implementations.

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

```

These OOP concepts in Python allow you to write modular, reusable, and maintainable code by organizing it into classes and objects. They promote code encapsulation, abstraction, and polymorphism, making it easier to manage complex systems.

## 2) Explain the concept of class and object with a suitable Python script example.

### Concept of Class and Object in Python

In Python, **classes** and **objects** are fundamental concepts of Object-Oriented Programming (OOP). A class serves as a blueprint for creating objects, while an object is an instance of a class. This allows for encapsulation of data and functionality, making it easier to model real-world entities.

#### Class

A class is defined using the `class` keyword followed by the class name. It can contain attributes (variables) and methods (functions) that define the behavior of the objects created from the class.

#### Object

An object is an instance of a class. When you create an object, you allocate memory for it and initialize its attributes.

#### Example: Class and Object

Here’s a simple example demonstrating the concept of classes and objects in Python:

```python
## Define a class named 'Dog'
class Dog:
    ## Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  ## Instance attribute
        self.age = age    ## Instance attribute

    ## Method to make the dog bark
    def bark(self):
        return f"{self.name} says Woof!"

    ## Method to get the dog's age
    def get_age(self):
        return f"{self.name} is {self.age} years old."

## Create an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)

## Accessing attributes and methods
print(my_dog.bark())         ## Output: Buddy says Woof!
print(my_dog.get_age())      ## Output: Buddy is 3 years old.

```

#### Explanation:

1. **Class Definition**: The `Dog` class is defined with an `__init__` constructor method that initializes the `name` and `age` attributes when a new object is created.
2. **Methods**:
    - The `bark()` method returns a string indicating that the dog barks.
    - The `get_age()` method returns the age of the dog.
3. **Creating an Object**: An object named `my_dog` is created as an instance of the `Dog` class with the name "Buddy" and age 3.
4. **Accessing Methods**: The methods `bark()` and `get_age()` are called on the `my_dog` object, demonstrating how to interact with the object's behavior.

#### Conclusion

Classes and objects are essential components of OOP in Python. They allow you to encapsulate data and functionality, making your code more modular, reusable, and easier to manage. By defining classes and creating objects, you can model real-world entities effectively in your programs.

## 3) Explain the following concepts with suitable Python script examples:
- Single Inheritance
- Multilevel inheritance
- Multiple inheritance
- Hierarchical inheritance

In Python, inheritance is a fundamental concept of Object-Oriented Programming (OOP) that allows one class (the child class) to inherit attributes and methods from another class (the parent class). This promotes code reusability and establishes a hierarchical relationship between classes. Here are different types of inheritance with suitable examples:

#### 1. Single Inheritance

In single inheritance, a child class inherits from only one parent class.

#### Example:

```python
## Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

## Child class
class Dog(Animal):
    def bark(self):
        return "Dog barks"

## Creating an object of the Dog class
my_dog = Dog()
print(my_dog.speak())  ## Output: Animal speaks
print(my_dog.bark())   ## Output: Dog barks

```

#### 2. Multilevel Inheritance

In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another parent class. This creates a chain of inheritance.

#### Example:

```python
## Grandparent class
class Animal:
    def speak(self):
        return "Animal speaks"

## Parent class
class Dog(Animal):
    def bark(self):
        return "Dog barks"

## Child class
class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"

## Creating an object of the Puppy class
my_puppy = Puppy()
print(my_puppy.speak())  ## Output: Animal speaks
print(my_puppy.bark())   ## Output: Dog barks
print(my_puppy.weep())   ## Output: Puppy weeps

```

#### 3. Multiple Inheritance

In multiple inheritance, a child class can inherit from more than one parent class. This allows the child class to combine behaviors from multiple classes.

#### Example:

```python
## Parent class 1
class Flyer:
    def fly(self):
        return "Can fly"

## Parent class 2
class Swimmer:
    def swim(self):
        return "Can swim"

## Child class inheriting from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Duck quacks"

## Creating an object of the Duck class
my_duck = Duck()
print(my_duck.fly())     ## Output: Can fly
print(my_duck.swim())    ## Output: Can swim
print(my_duck.quack())    ## Output: Duck quacks

```

#### 4. Hierarchical Inheritance

In hierarchical inheritance, multiple child classes inherit from a single parent class. This establishes a hierarchy where several classes share common functionality.

#### Example:

```python
## Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

## Child class 1
class Dog(Animal):
    def bark(self):
        return "Dog barks"

## Child class 2
class Cat(Animal):
    def meow(self):
        return "Cat meows"

## Creating objects of Dog and Cat classes
my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  ## Output: Animal speaks
print(my_dog.bark())   ## Output: Dog barks

print(my_cat.speak())  ## Output: Animal speaks
print(my_cat.meow())   ## Output: Cat meows

```

#### Summary

- **Single Inheritance**: A child class inherits from one parent class.
- **Multilevel Inheritance**: A child class inherits from a parent that is also a child of another parent.
- **Multiple Inheritance**: A child class inherits from multiple parent classes.
- **Hierarchical Inheritance**: Multiple child classes inherit from the same parent class.

These concepts help in organizing code better, making it more modular and easier to maintain by promoting code reuse and establishing clear relationships between different classes.

## 4) Explain the concept of polymorphism in Python with method overloading and method overriding with a suitable Python example.

### Polymorphism in Python

Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism can be achieved through **method overriding** and **method overloading**.

#### 1. Method Overriding

Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows the subclass to customize or extend the behavior of the inherited method.

#### Example of Method Overriding:

```python
## Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

## Child class
class Dog(Animal):
    def speak(self):  ## Overriding the speak method
        return "Dog barks"

## Child class
class Cat(Animal):
    def speak(self):  ## Overriding the speak method
        return "Cat meows"

## Creating objects of Dog and Cat classes
my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  ## Output: Dog barks
print(my_cat.speak())  ## Output: Cat meows

```

#### Explanation:

- The `Animal` class has a method called `speak()`.
- Both `Dog` and `Cat` classes inherit from `Animal` and override the `speak()` method to provide their specific implementations.
- When calling `speak()` on instances of `Dog` and `Cat`, the overridden methods are executed.

#### 2. Method Overloading

Method overloading refers to the ability to define multiple methods with the same name but different parameters within the same class. However, Python does not support traditional method overloading as seen in some other languages (like Java or C++). Instead, you can achieve similar functionality by using default arguments or variable-length arguments.

#### Example of Method Overloading Using Default Arguments:

```python
class MathOperations:
    def add(self, a, b=0, c=0):  ## Default arguments allow for overloading behavior
        return a + b + c

math_ops = MathOperations()

print(math_ops.add(5))          ## Output: 5 (5 + 0 + 0)
print(math_ops.add(5, 10))      ## Output: 15 (5 + 10 + 0)
print(math_ops.add(5, 10, 15))   ## Output: 30 (5 + 10 + 15)

```

#### Explanation:

- The `MathOperations` class has an `add()` method that can take one, two, or three parameters.
- By providing default values for `b` and `c`, we can call `add()` with different numbers of arguments, demonstrating a form of method overloading.

#### Summary

- **Polymorphism** allows methods to do different things based on the object it is acting upon.
- **Method Overriding** enables subclasses to provide specific implementations for methods defined in their parent classes.
- **Method Overloading** can be simulated in Python using default arguments or variable-length arguments since Python does not support traditional method overloading.

These concepts enhance code flexibility and reusability, allowing developers to write more general and adaptable code structures.

## 5) Explain Operator Overloading (for + operator) in Python with an example.

### Operator Overloading in Python

**Operator overloading** allows you to define how operators behave with user-defined classes. In Python, you can overload operators by defining special methods (also known as magic methods) in your class. For example, the `+` operator can be overloaded by defining the `__add__()` method in your class.

#### Example: Overloading the `+` Operator

Let's create a simple class called `Vector` that represents a mathematical vector. We will overload the `+` operator to allow vector addition.

#### Step-by-Step Implementation:

1. **Define the Vector Class**: We will define a class with an initializer to set the vector's components and implement the `__add__()` method to handle addition.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x  ## x-coordinate
        self.y = y  ## y-coordinate

    def __add__(self, other):
        """Overload the + operator to add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented  ## Return NotImplemented for unsupported types

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector({self.x}, {self.y})"

## Creating instances of Vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

## Using the overloaded + operator
result = v1 + v2

## Print the result
print("Result of v1 + v2:", result)  ## Output: Result of v1 + v2: Vector(6, 8)

```

#### Explanation:

1. **Class Definition**: The `Vector` class is defined with an initializer (`__init__`) that takes two parameters (`x` and `y`) representing the coordinates of the vector.
2. **Overloading the `+` Operator**:
    - The `__add__()` method is defined to handle addition.
    - It checks if the other object being added is also an instance of `Vector`. If it is, it returns a new `Vector` object with the sum of the respective components.
    - If the other object is not a `Vector`, it returns `NotImplemented`, which allows Python to handle unsupported operations gracefully.
3. **String Representation**: The `__repr__()` method provides a string representation of the vector for easier debugging and display.
4. **Creating Instances**: Two instances of `Vector`, `v1` and `v2`, are created.
5. **Using the Overloaded Operator**: The overloaded `+` operator is used to add two vectors, resulting in a new vector that is printed out.

#### Conclusion

Operator overloading in Python allows you to define how operators like `+`, `-`, etc., behave with instances of user-defined classes. This enhances code readability and allows for intuitive manipulation of objects. By implementing special methods such as `__add__()`, you can customize how operations are performed on your objects, making your classes more versatile and user-friendly.

## 6) Differentiate between Data Abstraction and Data Hiding.

### Difference Between Data Abstraction and Data Hiding

Data abstraction and data hiding are two fundamental concepts in Object-Oriented Programming (OOP) that help in managing complexity and enhancing the security of data. While they are closely related, they serve different purposes. Here's a detailed comparison:

#### Data Abstraction

- **Definition**: Data abstraction refers to the concept of exposing only the essential features of an object while hiding the complex implementation details. It focuses on what an object does rather than how it does it.
- **Purpose**: The main goal of data abstraction is to reduce complexity by providing a simplified view of the object to the user. It allows users to interact with objects without needing to understand their internal workings.
- **Implementation**: In Python, data abstraction is typically achieved through abstract classes and interfaces. Abstract classes can define abstract methods that must be implemented by subclasses.

#### Example of Data Abstraction:

```python
from abc import ABC, abstractmethod

## Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

## Concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

## Using the abstract class
rectangle = Rectangle(5, 10)
print("Area of rectangle:", rectangle.area())  ## Output: Area of rectangle: 50

```

#### Data Hiding

- **Definition**: Data hiding is a principle that restricts access to certain details of an object. It ensures that sensitive data is protected from unauthorized access and modification. This is often achieved by making attributes private or protected.
- **Purpose**: The main goal of data hiding is to safeguard an object's internal state and prevent unintended interference or misuse. It enhances security and integrity by controlling access to the object's data.
- **Implementation**: In Python, data hiding can be implemented using naming conventions (e.g., prefixing an attribute with an underscore `_` for protected or double underscores `__` for private attributes).

#### Example of Data Hiding:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  ## Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

## Using the BankAccount class
account = BankAccount(1000)
account.deposit(500)
print("Current Balance:", account.get_balance())  ## Output: Current Balance: 1500

## Attempting to access the private attribute will raise an error
## print(account.__balance)  ## Uncommenting this line will raise AttributeError

```

#### Summary of Differences

| Feature | Data Abstraction | Data Hiding |
| --- | --- | --- |
| Definition | Hiding complex implementation details | Restricting access to certain details of an object |
| Purpose | Simplifying user interaction with objects | Protecting sensitive data from unauthorized access |
| Implementation | Achieved through abstract classes and interfaces | Achieved through private/protected attributes |
| Focus | What an object does | How an object's internal state is accessed |

#### Conclusion

Both data abstraction and data hiding are essential in OOP for managing complexity and enhancing security. While abstraction focuses on simplifying interactions with objects by exposing only necessary features, hiding protects sensitive data from unauthorized access, ensuring that the internal state of objects remains secure and intact. Understanding these concepts helps in designing robust and maintainable software systems.

## 7) Explain isinstance(), issubclass(), super(), and init method.

Here's an explanation of the concepts you mentioned:

### isinstance()

The `isinstance()` function checks if an object is an instance of a specified class or any of its subclasses. It returns `True` if the object is an instance of the class or a subclass, and `False` otherwise.

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     ## True
print(isinstance(dog, Animal))  ## True

```

### issubclass()

The `issubclass()` function checks if a class is a subclass of a specified class or classes. It returns `True` if the first class is a subclass of the second class or classes, and `False` otherwise.

```python
print(issubclass(Dog, Animal))  ## True
print(issubclass(Animal, Dog))  ## False

```

### super()

The `super()` function is used to call a method in a superclass from a subclass. It allows you to reuse code from the superclass without having to repeat it in the subclass.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

```

In this example, the `Dog` class inherits from the `Animal` class. The `__init__` method in `Dog` calls the `__init__` method of the superclass `Animal` using `super()` to initialize the `name` attribute, and then it initializes the `breed` attribute.

### **init** method

The `__init__` method is a special method in Python classes that is used to initialize the object's attributes when an instance of the class is created. It is automatically called when you create an object of the class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
print(person.name)  ## Output: John
print(person.age)   ## Output: 30

```

In this example, the `__init__` method takes two parameters, `name` and `age`, and assigns them to the corresponding attributes of the `Person` object.

These concepts are fundamental in object-oriented programming and help in creating reusable, modular, and maintainable code in Python.

## 8) Discuss Encapsulation with getter and setter methods.

### Encapsulation in Python with Getter and Setter Methods

**Encapsulation** is one of the fundamental concepts in Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, typically a class. Encapsulation restricts direct access to some of an object's components, which is a means of preventing unintended interference and misuse of the methods and attributes.

#### Importance of Encapsulation

- **Data Protection**: Encapsulation helps protect the integrity of the data by restricting access to it.
- **Controlled Access**: It allows controlled access to the attributes through getter and setter methods.
- **Maintainability**: Changes to the internal implementation can be made without affecting external code that uses the class.

#### Getter and Setter Methods

Getter and setter methods are used to access and modify private attributes of a class. By using these methods, you can enforce validation rules or constraints when setting values.

- **Getter Method**: A method that retrieves the value of a private attribute.
- **Setter Method**: A method that sets or updates the value of a private attribute.

#### Example of Encapsulation with Getter and Setter Methods

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name      ## Private attribute
        self.__salary = salary  ## Private attribute

    ## Getter method for name
    def get_name(self):
        return self.__name

    ## Setter method for name
    def set_name(self, name):
        self.__name = name

    ## Getter method for salary
    def get_salary(self):
        return self.__salary

    ## Setter method for salary with validation
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

## Creating an object of Employee class
emp = Employee("Alice", 50000)

## Accessing attributes using getter methods
print("Employee Name:", emp.get_name())         ## Output: Employee Name: Alice
print("Employee Salary:", emp.get_salary())     ## Output: Employee Salary: 50000

## Modifying attributes using setter methods
emp.set_name("Bob")
emp.set_salary(60000)

print("Updated Employee Name:", emp.get_name())         ## Output: Updated Employee Name: Bob
print("Updated Employee Salary:", emp.get_salary())     ## Output: Updated Employee Salary: 60000

## Attempting to set a negative salary will raise an error
try:
    emp.set_salary(-1000)  ## This will raise ValueError
except ValueError as e:
    print(e)  ## Output: Salary cannot be negative

```

#### Explanation:

1. **Class Definition**: The `Employee` class encapsulates two private attributes: `__name` and `__salary`.
2. **Getter Methods**:
    - `get_name()`: Returns the value of the private attribute `__name`.
    - `get_salary()`: Returns the value of the private attribute `__salary`.
3. **Setter Methods**:
    - `set_name(name)`: Updates the value of `__name`.
    - `set_salary(salary)`: Updates the value of `__salary`, but includes validation to ensure that the salary cannot be negative.
4. **Object Creation**: An instance of the `Employee` class is created with initial values.
5. **Accessing Attributes**: The values are accessed using getter methods.
6. **Modifying Attributes**: The values are modified using setter methods, demonstrating how encapsulation allows controlled access to internal state.
7. **Validation in Setters**: The setter for salary checks if the new salary is valid before updating it, enforcing rules that help maintain data integrity.

#### Conclusion

Encapsulation is a powerful concept in OOP that enhances data security and integrity by restricting direct access to an object's attributes. By using getter and setter methods, you can control how attributes are accessed and modified, allowing for validation and maintaining consistency within your objects. This leads to more robust and maintainable code.

## 9) What is Abstract Data Types (ADT) in Python programming? Explain features and advantages of ADT.

### Abstract Data Types (ADT) in Python Programming

**Abstract Data Types (ADT)** are a theoretical concept used in computer science to define data types by their behavior (operations) rather than their implementation. An ADT specifies what operations can be performed on the data type and what the expected results of those operations are, without detailing how these operations are implemented.

#### Features of Abstract Data Types

1. **Encapsulation**: ADTs encapsulate the data and the operations that manipulate that data. This means that the implementation details are hidden from the user, allowing for a clean and clear interface.
2. **Data Abstraction**: ADTs provide a way to define complex data structures in terms of simpler ones. Users interact with the ADT through a defined interface, which abstracts away the complexities of the underlying implementation.
3. **Modularity**: By separating the interface from the implementation, ADTs promote modularity in programming. Changes to the implementation do not affect code that uses the ADT as long as the interface remains consistent.
4. **Flexibility**: ADTs allow for different implementations of the same data type. For example, a stack can be implemented using an array or a linked list, but both implementations can be treated as a stack ADT.

#### Advantages of Abstract Data Types

1. **Improved Code Readability**: By focusing on what operations are available rather than how they are implemented, code becomes easier to read and understand.
2. **Ease of Maintenance**: Changes to the implementation of an ADT do not affect code that relies on it, making maintenance easier and less error-prone.
3. **Reusability**: ADTs can be reused across different programs or modules without needing to change their internal workings.
4. **Enhanced Security**: By hiding implementation details, ADTs protect against unintended interference with the data structure's integrity.

#### Example of Abstract Data Type in Python

Let's illustrate an abstract data type using a simple example of a stack, which is an ADT that follows the Last In First Out (LIFO) principle.

```python
class Stack:
    def __init__(self):
        self.__items = []  ## Private attribute to hold stack items

    def push(self, item):
        """Add an item to the top of the stack."""
        self.__items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.__items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.__items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.__items)

## Using the Stack ADT
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top item:", my_stack.peek())  ## Output: Top item: 30
print("Stack size:", my_stack.size())  ## Output: Stack size: 3

print("Popped item:", my_stack.pop())  ## Output: Popped item: 30
print("Stack size after pop:", my_stack.size())  ## Output: Stack size after pop: 2

```

#### Explanation:

1. **Class Definition**: The `Stack` class encapsulates a private list `__items` that holds the elements of the stack.
2. **Methods**:
    - `push(item)`: Adds an item to the top of the stack.
    - `pop()`: Removes and returns the top item from the stack.
    - `peek()`: Returns the top item without removing it.
    - `is_empty()`: Checks if there are any items in the stack.
    - `size()`: Returns the number of items in the stack.
3. **Usage**: An instance of `Stack` is created, and various methods are used to manipulate and access its data.

#### Conclusion

Abstract Data Types (ADT) provide a powerful way to define and work with complex data structures while hiding implementation details from users. This leads to improved code readability, maintainability, reusability, and security. Understanding and utilizing ADTs is essential for building robust software systems in Python and other programming languages.

## 10) Write a short note on:
- Stack ADT
- Queue ADT
- List ADT

Here’s a short note on **Stack ADT**, **Queue ADT**, and **List ADT** in Python programming:

#### Stack ADT

**Definition**: A Stack is an Abstract Data Type (ADT) that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.

**Operations**:

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove and return the top element of the stack.
- **Peek/Top**: Return the top element without removing it.
- **isEmpty**: Check if the stack is empty.

#### Example:

```python
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.__items) == 0

## Using the Stack ADT
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  ## Output: 20

```

#### Queue ADT

**Definition**: A Queue is an Abstract Data Type (ADT) that follows the First In First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

**Operations**:

- **Enqueue**: Add an element to the back of the queue.
- **Dequeue**: Remove and return the front element of the queue.
- **Front/Peek**: Return the front element without removing it.
- **isEmpty**: Check if the queue is empty.

#### Example:

```python
class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__items.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.__items[0]
        raise IndexError("front from empty queue")

    def is_empty(self):
        return len(self.__items) == 0

## Using the Queue ADT
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  ## Output: 10

```

#### List ADT

**Definition**: A List is an Abstract Data Type (ADT) that represents a collection of ordered elements. Lists allow for dynamic resizing and can contain elements of different types.

**Operations**:

- **Insert**: Add an element at a specified position.
- **Delete**: Remove an element from a specified position.
- **Access**: Retrieve an element at a specified index.
- **Length**: Get the number of elements in the list.

#### Example:

```python
class ListADT:
    def __init__(self):
        self.__items = []

    def insert(self, index, item):
        self.__items.insert(index, item)

    def delete(self, index):
        if 0 <= index < len(self.__items):
            del self.__items[index]
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        raise IndexError("Index out of bounds")

    def length(self):
        return len(self.__items)

## Using the List ADT
my_list = ListADT()
my_list.insert(0, 'a')
my_list.insert(1, 'b')
print(my_list.access(1))  ## Output: b
my_list.delete(0)
print(my_list.length())    ## Output: 1

```

#### Summary

- **Stack ADT**: Follows LIFO principle; supports operations like push, pop, and peek.
- **Queue ADT**: Follows FIFO principle; supports operations like enqueue, dequeue, and front.
- **List ADT**: Represents a collection of ordered elements; supports operations like insert, delete, access, and length.

These abstract data types are fundamental in programming as they provide structured ways to manage data efficiently and effectively.

## 11) Write a Python script to implement linear search/binary search (Recursive/Non-Recursive).

Here's a Python script that implements linear search and binary search (recursive and non-recursive versions) on a sorted list:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

## Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]

## Linear search
print("Linear search:")
print(linear_search(sorted_list, 7))  ## Output: 3
print(linear_search(sorted_list, 10))  ## Output: -1

## Binary search (non-recursive)
print("\\nBinary search (non-recursive):")
print(binary_search(sorted_list, 7))  ## Output: 3
print(binary_search(sorted_list, 10))  ## Output: -1

## Binary search (recursive)
print("\\nBinary search (recursive):")
print(binary_search_recursive(sorted_list, 7))  ## Output: 3
print(binary_search_recursive(sorted_list, 10))  ## Output: -1

```

Explanation:

1. **Linear Search**:
    - The `linear_search` function takes an array `arr` and a target element `target` as input.
    - It iterates through the array using a `for` loop and checks if each element matches the target.
    - If a match is found, it returns the index of the element.
    - If no match is found, it returns `1`.
2. **Binary Search (Non-Recursive)**:
    - The `binary_search` function takes a sorted array `arr` and a target element `target` as input.
    - It initializes `left` and `right` pointers to the start and end of the array, respectively.
    - It enters a `while` loop that continues as long as `left` is less than or equal to `right`.
    - In each iteration, it calculates the middle index `mid` and compares the element at `mid` with the target.
    - If the element matches the target, it returns the index `mid`.
    - If the element is less than the target, it updates `left` to `mid + 1` to search in the right half.
    - If the element is greater than the target, it updates `right` to `mid - 1` to search in the left half.
    - If the target is not found, it returns `1`.
3. **Binary Search (Recursive)**:
    - The `binary_search_recursive` function takes a sorted array `arr`, a target element `target`, and optional `left` and `right` pointers as input.
    - If `right` is not provided, it initializes `right` to the last index of the array.
    - It checks if `left` is greater than `right`, indicating that the target is not found, and returns `1`.
    - Otherwise, it calculates the middle index `mid` and compares the element at `mid` with the target.
    - If the element matches the target, it returns the index `mid`.
    - If the element is less than the target, it recursively calls `binary_search_recursive` with `left` updated to `mid + 1`.
    - If the element is greater than the target, it recursively calls `binary_search_recursive` with `right` updated to `mid - 1`.

The script demonstrates the usage of each search algorithm by providing an example sorted list and searching for elements that exist and do not exist in the list.

Note: The list must be sorted for binary search to work correctly.