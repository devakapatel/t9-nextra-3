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

| Feature        | Data Abstraction                                 | Data Hiding                                        |
| -------------- | ------------------------------------------------ | -------------------------------------------------- |
| Definition     | Hiding complex implementation details            | Restricting access to certain details of an object |
| Purpose        | Simplifying user interaction with objects        | Protecting sensitive data from unauthorized access |
| Implementation | Achieved through abstract classes and interfaces | Achieved through private/protected attributes      |
| Focus          | What an object does                              | How an object's internal state is accessed         |

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

## 12) Write a Python script to implement Bubble/Selection/Tim sort.

Certainly! Below are Python implementations for three common sorting algorithms: Bubble Sort, Selection Sort, and Tim Sort. Each sorting algorithm is provided with a brief explanation of how it works, followed by the code implementation.

### 1. Bubble Sort

**Bubble Sort** is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

#### Bubble Sort Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sorted array:", bubble_sort(arr))
```

### 2. Selection Sort

**Selection Sort** is another simple comparison-based sorting algorithm. It divides the input list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.

#### Selection Sort Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Selection Sorted array:", selection_sort(arr))
```

### 3. Tim Sort

**Tim Sort** is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort. It is designed to perform well on many kinds of real-world data. Tim Sort divides the array into small segments (called "runs") and sorts them using Insertion Sort. Then it merges those runs to produce a sorted array.

#### Tim Sort Implementation

```python
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]

    left_index, right_index = 0, 0
    sorted_index = left

    while left_index < len(left_copy) and right_index < len(right_copy):
        if left_copy[left_index] <= right_copy[right_index]:
            arr[sorted_index] = left_copy[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_copy[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(left_copy):
        arr[sorted_index] = left_copy[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_copy):
        arr[sorted_index] = right_copy[right_index]
        right_index += 1
        sorted_index += 1

def tim_sort(arr):
    n = len(arr)
    run_size = 32

    for start in range(0, n, run_size):
        end = min(start + run_size - 1, n - 1)
        insertion_sort(arr, start, end)

    size = run_size
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

# Example usage
arr = [64, 25, 12, 22, 11]
tim_sort(arr)
print("Tim Sorted array:", arr)
```

### Summary of Sorting Algorithms

- **Bubble Sort**: Simple but inefficient for large datasets; O(n^2) time complexity.
- **Selection Sort**: Also O(n^2) time complexity; performs well on small datasets.
- **Tim Sort**: Efficient and stable; O(n log n) time complexity; used in Python's built-in `sort()` method.

These implementations provide a clear understanding of how each sorting algorithm works in Python. You can run these scripts to see how they sort arrays of integers effectively!

## 13) Explain the following concepts with suitable Python script examples: <br> - Encapsulation for private and protected members <br> - Discuss Encapsulation with getter and setter method. <br> - Differentiate between Data Abstraction and Data Hiding.

### Encapsulation in Python

**Encapsulation** is a fundamental concept in object-oriented programming (OOP) that involves bundling data (attributes) and methods (functions) that operate on the data within a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. In Python, encapsulation is achieved through access modifiers: public, protected, and private.

#### 1. Private and Protected Members

- **Private Members**: These are attributes or methods that cannot be accessed from outside the class. In Python, private members are indicated by a double underscore prefix (`__`).

- **Protected Members**: These are attributes or methods that can be accessed within the class and its subclasses but are not meant to be accessed from outside the class hierarchy. In Python, protected members are indicated by a single underscore prefix (`_`).

#### Example of Private and Protected Members

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f"Account holder: {self.__owner}, Balance: ${self.__balance}"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self._interest_rate = 0.05  # Protected attribute

    def apply_interest(self):
        interest = self.__balance * self._interest_rate
        self.deposit(interest)

# Example usage
account = SavingsAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
# Accessing private members directly will raise an AttributeError
# print(account.__balance)  # Uncommenting this line will cause an error
```

### 2. Encapsulation with Getter and Setter Methods

Getter and setter methods provide controlled access to private attributes. Getters retrieve the value of a private attribute, while setters allow modification of that attribute.

#### Example of Getter and Setter Methods

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    # Getter for salary
    def get_salary(self):
        return self.__salary

# Example usage
emp = Employee("John", 50000)
print(emp.get_name())  # Output: John
print(emp.get_salary())  # Output: 50000

emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000

emp.set_salary(-1000)  # Output: Salary cannot be negative
```

### 3. Data Abstraction vs. Data Hiding

- **Data Abstraction**:

  - Refers to the concept of exposing only the essential features of an object while hiding the complex implementation details.
  - It allows users to interact with an object at a high level without needing to understand the internal workings.
  - In Python, abstraction can be achieved using abstract classes and interfaces (via the `abc` module).

- **Data Hiding**:
  - Refers to restricting access to certain details of an object to protect its integrity.
  - It is primarily concerned with preventing unauthorized access to sensitive data within an object.
  - Data hiding is typically implemented through access modifiers (private and protected members).

#### Summary of Differences:

| Feature        | Data Abstraction                                              | Data Hiding                                                       |
| -------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| Purpose        | Simplifies complex systems by exposing only necessary details | Protects object integrity by restricting access to internal state |
| Implementation | Achieved through abstract classes/interfaces                  | Achieved using access modifiers (private/protected)               |
| Focus          | What an object does                                           | How an object does it                                             |

### Conclusion

Encapsulation is a key principle in OOP that enhances data security and maintainability by controlling access to class members. By using private and protected members along with getter and setter methods, developers can ensure that internal states are modified only in controlled ways. Understanding the distinction between data abstraction and data hiding further helps in designing robust systems that prioritize user interaction simplicity while safeguarding internal complexities.

## 14) Write a Python script to implement linear search/binary search (Recursive/Non-Recursive).

Certainly! Below are Python implementations for both **Linear Search** and **Binary Search** (both recursive and non-recursive). Each search algorithm is explained, followed by the code implementation.

### 1. Linear Search

**Linear Search** is a straightforward algorithm that checks each element in a list sequentially until the desired element is found or the list ends. It has a time complexity of O(n), where n is the number of elements in the list.

#### Non-Recursive Linear Search Implementation

```python
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage
arr = [5, 3, 8, 4, 2]
target = 4
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
```

#### Recursive Linear Search Implementation

```python
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):  # Base case: if index exceeds array length
        return -1
    if arr[index] == target:  # Element found
        return index
    return linear_search_recursive(arr, target, index + 1)  # Recursive call

# Example usage
arr = [5, 3, 8, 4, 2]
target = 8
result = linear_search_recursive(arr, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
```

### 2. Binary Search

**Binary Search** is a more efficient algorithm that works on sorted arrays. It repeatedly divides the search interval in half. If the target value is less than the middle element, it narrows the interval to the lower half; otherwise, it narrows it to the upper half. It has a time complexity of O(log n).

#### Non-Recursive Binary Search Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid index

        if arr[mid] == target:  # Element found
            return mid
        elif arr[mid] < target:  # Target is in right half
            left = mid + 1
        else:  # Target is in left half
            right = mid - 1

    return -1  # Return -1 if the element is not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
```

#### Recursive Binary Search Implementation

```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:  # Base case: no elements to search
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:  # Element found
        return mid
    elif arr[mid] < target:  # Target is in right half
        return binary_search_recursive(arr, target, mid + 1, right)
    else:  # Target is in left half
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 3
result = binary_search_recursive(arr, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
```

### Summary of Search Algorithms

- **Linear Search**: Simple and works on unsorted arrays but inefficient for large datasets (O(n)).
- **Binary Search**: Efficient for sorted arrays (O(log n)), but requires that the array be sorted beforehand.

These implementations provide clear examples of how to perform both linear and binary searches using Python. You can run these scripts to see how they work with different datasets!

## 15) What is a regular expression? How to use RegEx in Python? Explain any 4 metacharacters in Python with suitable examples.

### What is a Regular Expression?

A **regular expression** (often abbreviated as **regex** or **regexp**) is a special sequence of characters that defines a search pattern. These patterns are used for string searching algorithms, allowing for operations such as finding, matching, and manipulating text. Regular expressions are widely used in programming languages, text editors, and command-line utilities for tasks like input validation, data extraction, and text processing.

### Using Regular Expressions in Python

In Python, the `re` module provides support for working with regular expressions. This module allows you to compile regex patterns, search for matches, and perform various operations on strings.

#### Basic Usage of the `re` Module

1. **Import the `re` module**:

   ```python
   import re
   ```

2. **Compile a regular expression**:

   ```python
   pattern = re.compile(r'\d+')  # Matches one or more digits
   ```

3. **Search for matches**:

   ```python
   match = pattern.search('There are 123 apples')
   if match:
       print("Found:", match.group())  # Output: Found: 123
   ```

4. **Find all matches**:
   ```python
   matches = pattern.findall('There are 123 apples and 456 oranges')
   print("All matches:", matches)  # Output: All matches: ['123', '456']
   ```

### Four Metacharacters in Python Regular Expressions

Metacharacters are characters that have special meanings in regular expressions. Here are four commonly used metacharacters along with examples:

1. **Dot (`.`)**:

   - Matches any single character except a newline.
   - Example:

     ```python
     import re

     pattern = re.compile(r'a.b')  # Matches 'a' followed by any character and then 'b'
     result = pattern.match('a1b')
     print(result.group())  # Output: a1b
     ```

2. **Caret (`^`)**:

   - Matches the start of a string.
   - Example:

     ```python
     import re

     pattern = re.compile(r'^Hello')  # Matches 'Hello' at the beginning of the string
     result = pattern.match('Hello World')
     print(result.group())  # Output: Hello
     ```

3. **Dollar Sign (`$`)**:

   - Matches the end of a string.
   - Example:

     ```python
     import re

     pattern = re.compile(r'World$')  # Matches 'World' at the end of the string
     result = pattern.search('Hello World')
     print(result.group())  # Output: World
     ```

4. **Asterisk (`*`)**:

   - Matches zero or more occurrences of the preceding element.
   - Example:

     ```python
     import re

     pattern = re.compile(r'a*')  # Matches zero or more 'a's
     result = pattern.findall('aaa bcaad aa')
     print(result)  # Output: ['aaa', '', '', '', 'aa']
     ```

### Conclusion

Regular expressions are powerful tools for text processing and manipulation in Python. They allow you to define complex search patterns using metacharacters, enabling efficient data validation and extraction tasks. Understanding how to use regex effectively can significantly enhance your ability to work with strings in programming.

## 16) Describe various methods used for regular expressions in Python programming with suitable examples (re.search(), re.escape(), re.sub(), re.split(), re.compile(), re.findall()).

Regular expressions (regex) are powerful tools for pattern matching and manipulation in strings. In Python, the `re` module provides various methods to work with regular expressions. Below, I will describe several commonly used methods in the `re` module, along with suitable examples for each.

### 1. `re.search()`

The `re.search()` function scans through a string looking for the first location where the regex pattern produces a match. It returns a match object if found; otherwise, it returns `None`.

#### Example:

```python
import re

text = "The rain in Spain"
pattern = r"rain"

match = re.search(pattern, text)
if match:
    print(f"Match found: {match.group()}")  # Output: Match found: rain
else:
    print("No match found.")
```

### 2. `re.findall()`

The `re.findall()` function returns all non-overlapping matches of the pattern in the string as a list of strings. If no matches are found, it returns an empty list.

#### Example:

```python
import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"ain"

matches = re.findall(pattern, text)
print(f"Matches found: {matches}")  # Output: Matches found: ['ain', 'ain', 'ain']
```

### 3. `re.sub()`

The `re.sub()` function replaces occurrences of a pattern in a string with a specified replacement string. You can also specify how many occurrences to replace.

#### Example:

```python
import re

text = "The rain in Spain"
pattern = r"Spain"
replacement = "France"

new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: The rain in France
```

### 4. `re.split()`

The `re.split()` function splits a string by the occurrences of a pattern and returns a list of substrings.

#### Example:

```python
import re

text = "apple, banana; cherry orange"
pattern = r"[;, ]+"  # Split by comma, semicolon, or space

result = re.split(pattern, text)
print(result)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

### 5. `re.compile()`

The `re.compile()` function compiles a regex pattern into a regex object, which can be used for matching using methods like `search()`, `match()`, and `findall()`. This is useful for improving performance when the same pattern is used multiple times.

#### Example:

```python
import re

pattern = re.compile(r"\d+")  # Compile regex to match one or more digits
text = "There are 123 apples and 456 oranges."

matches = pattern.findall(text)
print(f"Digits found: {matches}")  # Output: Digits found: ['123', '456']
```

### 6. `re.escape()`

The `re.escape()` function escapes all non-alphanumeric characters in a string so that they can be used in a regex pattern without being interpreted as special characters.

#### Example:

```python
import re

special_string = "Hello? (How are you!)"
escaped_string = re.escape(special_string)

print(f"Escaped string: {escaped_string}")
# Output: Escaped string: Hello\? \(How\ are\ you\!\)
```

### Summary of Methods

- **`re.search(pattern, string)`**: Searches for the first occurrence of the pattern.
- **`re.findall(pattern, string)`**: Finds all occurrences of the pattern and returns them as a list.
- **`re.sub(pattern, replacement, string)`**: Replaces occurrences of the pattern with the specified replacement.
- **`re.split(pattern, string)`**: Splits the string by occurrences of the pattern.
- **`re.compile(pattern)`**: Compiles a regex pattern into a regex object for repeated use.
- **`re.escape(string)`**: Escapes special characters in a string for use in a regex pattern.

These methods provide powerful capabilities for working with strings and patterns in Python using regular expressions. You can use them to validate input, extract information, and manipulate text efficiently.

## 17) What is a special sequence character in a regular expression? Explain the use of any 4 of the special sequence characters with suitable examples.

In regular expressions, **special sequences** are predefined patterns that provide a shorthand way to match specific types of characters or positions in a string. They are typically denoted by a backslash (`\`) followed by a character. Special sequences simplify the creation of complex regex patterns by allowing you to express common matching criteria without having to write out the full character class.

### Common Special Sequences in Regular Expressions

Here are four commonly used special sequence characters in regular expressions, along with explanations and examples:

1. **`\d`**: Matches any digit character (equivalent to `[0-9]`).

   **Example**:

   ```python
   import re

   text = "The price is 100 dollars."
   pattern = r"\d+"  # Match one or more digits

   matches = re.findall(pattern, text)
   print("Digits found:", matches)  # Output: Digits found: ['100']
   ```

2. **`\D`**: Matches any non-digit character (equivalent to `[^0-9]`).

   **Example**:

   ```python
   import re

   text = "Room 101 is available."
   pattern = r"\D+"  # Match one or more non-digit characters

   matches = re.findall(pattern, text)
   print("Non-digits found:", matches)  # Output: Non-digits found: ['Room ', ' is available.']
   ```

3. **`\w`**: Matches any alphanumeric character (letters, digits, and underscores). It is equivalent to `[a-zA-Z0-9_]`.

   **Example**:

   ```python
   import re

   text = "Hello_World123!"
   pattern = r"\w+"  # Match one or more word characters

   matches = re.findall(pattern, text)
   print("Word characters found:", matches)  # Output: Word characters found: ['Hello_World123']
   ```

4. **`\s`**: Matches any whitespace character (spaces, tabs, newlines). It is equivalent to the character class `[ \t\n\r\f\v]`.

   **Example**:

   ```python
   import re

   text = "Hello World!\nWelcome to regex."
   pattern = r"\s+"  # Match one or more whitespace characters

   matches = re.split(pattern, text)
   print("Split by whitespace:", matches)
   # Output: Split by whitespace: ['Hello', 'World!', 'Welcome', 'to', 'regex.']
   ```

### Summary of Special Sequences

- **`\d`**: Matches any digit (0-9).
- **`\D`**: Matches any non-digit character.
- **`\w`**: Matches any alphanumeric character (letters, digits, underscore).
- **`\s`**: Matches any whitespace character.

### Conclusion

Special sequences in regular expressions provide a concise and powerful way to match specific patterns within strings. By using these sequences, you can simplify your regex patterns and make them easier to read and maintain. The examples above illustrate how to use these special sequences effectively in Python using the `re` module.

## 18) Explain the concept of sets in a regular expression with a suitable example.

### Concept of Sets in Regular Expressions

In regular expressions, a **set** is a collection of characters enclosed within square brackets (`[]`). A set allows you to define a character class that matches any single character from the specified set. This feature is particularly useful for matching one out of several possible characters without having to write out each option individually.

#### Characteristics of Sets

- **Character Inclusion**: A set matches any one character that is included in the brackets.
- **Ranges**: You can specify a range of characters using a hyphen (`-`). For example, `[a-z]` matches any lowercase letter from 'a' to 'z'.
- **Negation**: You can negate a set by placing a caret (`^`) at the beginning of the set. For example, `[^a-z]` matches any character that is not a lowercase letter.
- **No Special Meaning for Certain Characters**: Inside a set, certain characters lose their special meaning. For instance, `+`, `*`, and `.` are treated as literal characters when placed inside square brackets.

### Example of Using Sets in Regular Expressions

Here are some examples demonstrating how sets work in regular expressions:

#### Example 1: Basic Set

```python
import re

text = "The cat sat on the mat."
pattern = r"[aeiou]"  # Matches any vowel

matches = re.findall(pattern, text)
print("Vowels found:", matches)  # Output: Vowels found: ['e', 'a', 'a', 'o', 'e', 'a']
```

In this example, the regex pattern `[aeiou]` matches any single vowel in the string.

#### Example 2: Character Range

```python
import re

text = "The year is 2023."
pattern = r"[0-9]"  # Matches any digit

matches = re.findall(pattern, text)
print("Digits found:", matches)  # Output: Digits found: ['2', '0', '2', '3']
```

Here, the pattern `[0-9]` is used to find all digit characters in the string.

#### Example 3: Negated Set

```python
import re

text = "Hello World!"
pattern = r"[^aeiou ]"  # Matches any consonant or punctuation (not vowels or space)

matches = re.findall(pattern, text)
print("Non-vowel characters found:", matches)  # Output: Non-vowel characters found: ['H', 'l', 'l', 'W', 'r', 'l', 'd', '!']
```

In this example, the pattern `[^aeiou ]` matches all characters that are not vowels and not spaces.

#### Example 4: Mixed Characters and Ranges

```python
import re

text = "abc123XYZ!"
pattern = r"[a-zA-Z0-9]"  # Matches any alphanumeric character

matches = re.findall(pattern, text)
print("Alphanumeric characters found:", matches)  # Output: Alphanumeric characters found: ['a', 'b', 'c', '1', '2', '3', 'X', 'Y', 'Z']
```

Here, the regex pattern `[a-zA-Z0-9]` matches any alphanumeric character (both lowercase and uppercase letters and digits).

### Conclusion

Sets in regular expressions provide a powerful way to match specific groups of characters efficiently. By using square brackets to define sets, you can create more flexible and concise patterns for string matching. This feature is particularly useful when you need to match multiple potential characters without writing out each possibility explicitly.

## 19) Explain Decorators (wrapper function) in Python with a suitable example.

### Decorators in Python

**Decorators** in Python are a powerful and expressive way to modify the behavior of functions or methods. They allow you to wrap another function to extend its behavior without permanently modifying it. A decorator is essentially a function that takes another function as an argument, adds some functionality, and returns a new function (often called a wrapper).

### How Decorators Work

1. **Higher-Order Functions**: A decorator is a higher-order function, meaning it takes another function as an argument.
2. **Wrapper Function**: Inside the decorator, you define a nested function (the wrapper) that calls the original function and can add additional functionality before or after the call.
3. **Returning the Wrapper**: The decorator returns the wrapper function, which replaces the original function.

### Example of a Decorator

Here's a simple example demonstrating how decorators work:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
```

#### Output:

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### Explanation of the Example

1. **Decorator Definition**:

   - The `my_decorator` function takes another function `func` as an argument.
   - Inside `my_decorator`, we define a nested `wrapper` function that adds behavior before and after calling `func`.

2. **Applying the Decorator**:

   - The `@my_decorator` syntax is a shorthand for `say_hello = my_decorator(say_hello)`. It applies the decorator to the `say_hello` function.

3. **Calling the Decorated Function**:
   - When you call `say_hello()`, it actually calls `wrapper()`, which executes additional code before and after calling the original `say_hello()`.

### Using Decorators with Arguments

If you want to create decorators that accept arguments, you can add another layer of nesting. Here’s an example:

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function
greet("Alice")
```

#### Output:

```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

### Explanation of Using Decorators with Arguments

1. **Decorator with Arguments**:

   - The `repeat` function takes an argument `num_times` and returns a decorator (`decorator_repeat`).

2. **Inner Wrapper Function**:

   - The inner `wrapper` function calls `func` multiple times based on `num_times`.

3. **Applying the Decorator**:
   - The syntax `@repeat(3)` applies this decorator to the `greet` function, which will now print "Hello, Alice!" three times when called.

### Conclusion

Decorators in Python provide a flexible way to modify or enhance functions without changing their code directly. They are widely used for logging, access control, memoization, and more. Understanding how to create and use decorators can significantly improve your ability to write clean and maintainable code in Python.

## 20) Write a Python script using regular expressions to check if a binary string contains at least three 1s.

To check if a binary string contains at least three '1's using regular expressions in Python, you can use the `re` module. Specifically, you can create a regex pattern that matches three or more occurrences of '1'.

### Python Script

Here’s a simple script that demonstrates how to accomplish this:

```python
import re

def contains_at_least_three_ones(binary_string):
    # Regular expression pattern to match at least three '1's
    pattern = r'1.*1.*1'  # Matches a '1', followed by any characters (including none), followed by another '1', and so on.

    # Use re.search to find the pattern in the binary string
    if re.search(pattern, binary_string):
        return True
    else:
        return False

# Example usage
binary_strings = [
    "110010",      # Contains 3 ones
    "101",         # Contains 2 ones
    "0000",        # Contains 0 ones
    "11111",       # Contains 5 ones
    "001001",      # Contains 2 ones
]

for binary in binary_strings:
    result = contains_at_least_three_ones(binary)
    print(f"Binary string '{binary}' contains at least three 1s: {result}")
```

### Explanation of the Code

1. **Importing the `re` Module**: This module provides support for regular expressions.

2. **Defining the Function**:

   - The function `contains_at_least_three_ones` takes a binary string as an argument.
   - The regex pattern `r'1.*1.*1'` is used to check for at least three occurrences of '1':
     - `1` matches the first '1'.
     - `.*` matches any character (zero or more times) between the '1's.
     - The second `1` matches the second occurrence, and the third `1` matches the third occurrence.

3. **Using `re.search()`**: This function searches for the specified pattern in the provided binary string. If it finds a match, it returns a match object; otherwise, it returns `None`.

4. **Example Usage**: The script tests several binary strings and prints whether each contains at least three '1's.

### Output

When you run the script, you should see output similar to this:

```
Binary string '110010' contains at least three 1s: True
Binary string '101' contains at least three 1s: False
Binary string '0000' contains at least three 1s: False
Binary string '11111' contains at least three 1s: True
Binary string '001001' contains at least three 1s: False
```

This output indicates which binary strings contain at least three occurrences of '1'.

## 21) Write a Python script using regular expressions to check if a binary string starts with 0 and has an odd length, or starts with 1 and has an even length.

To check if a binary string meets the criteria of starting with '0' and having an odd length, or starting with '1' and having an even length using regular expressions in Python, you can use the `re` module.

### Criteria Breakdown

1. **Starts with '0' and has an odd length**: This means the string must start with '0' and the total number of characters in the string should be odd.
2. **Starts with '1' and has an even length**: This means the string must start with '1' and the total number of characters in the string should be even.

### Regular Expression Pattern

- To check for a string that starts with '0' and has an odd length, you can use the pattern: `^0(.{2})*$` (the `.{2}` matches pairs of characters, ensuring the total length is odd).
- To check for a string that starts with '1' and has an even length, you can use the pattern: `^1(.{2})*$` (the `.{2}` matches pairs of characters, ensuring the total length is even).

### Python Script

Here's a Python script that implements this logic:

```python
import re

def check_binary_string(binary_string):
    # Regular expression patterns
    pattern_odd = r'^0(.{2})*$'  # Starts with 0 and has odd length
    pattern_even = r'^1(.{2})*$'  # Starts with 1 and has even length

    # Check if the binary string matches either pattern
    if re.match(pattern_odd, binary_string) or re.match(pattern_even, binary_string):
        return True
    else:
        return False

# Example usage
binary_strings = [
    "0",      # Odd length (True)
    "00",     # Even length (False)
    "000",    # Odd length (True)
    "1",      # Odd length (False)
    "11",     # Even length (True)
    "111",     # Odd length (False)
    "010101",  # Even length (False)
    "10010"   # Odd length (True)
]

for binary in binary_strings:
    result = check_binary_string(binary)
    print(f"Binary string '{binary}' matches criteria: {result}")
```

### Explanation of the Code

1. **Importing the `re` Module**: This module provides support for regular expressions.

2. **Defining the Function**:

   - The function `check_binary_string` takes a binary string as an argument.
   - Two regex patterns are defined:
     - `pattern_odd`: Matches strings that start with '0' and have an odd number of characters.
     - `pattern_even`: Matches strings that start with '1' and have an even number of characters.

3. **Using `re.match()`**: This function checks if the string matches either of the defined patterns. If it does, it returns `True`; otherwise, it returns `False`.

4. **Example Usage**: The script tests several binary strings against the criteria and prints whether each one matches.

### Output

When you run the script, you should see output similar to this:

```
Binary string '0' matches criteria: True
Binary string '00' matches criteria: False
Binary string '000' matches criteria: True
Binary string '1' matches criteria: False
Binary string '11' matches criteria: True
Binary string '111' matches criteria: False
Binary string '010101' matches criteria: False
Binary string '10010' matches criteria: True
```

This output indicates which binary strings meet the specified conditions regarding their starting character and length.

## 22) What is networking in Python? Explain the concept of socket.

### Networking in Python

Networking in Python refers to the ability to communicate between different devices over a network. This is achieved through various protocols and technologies that allow data to be sent and received across different machines. Python provides built-in libraries, such as the `socket` module, which facilitate the implementation of network communication in applications. Networking can be used for various purposes, including web servers, chat applications, file transfers, and more.

### Concept of Sockets

A **socket** is an endpoint for sending or receiving data across a computer network. It acts as a communication channel between two processes, which can be on the same machine or on different machines connected via a network. Sockets provide a way for applications to communicate with each other using standard protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

#### Key Concepts of Sockets

1. **Socket Types**:

   - **TCP Sockets**: These are connection-oriented sockets that provide reliable communication. They ensure that data is delivered in the correct order and without loss.
   - **UDP Sockets**: These are connectionless sockets that do not guarantee reliable delivery or order of packets. They are faster but less reliable than TCP sockets.

2. **Address Families**:

   - **AF_INET**: This address family is used for IPv4 addresses.
   - **AF_INET6**: This address family is used for IPv6 addresses.
   - **AF_UNIX**: This address family is used for Unix domain sockets, allowing communication between processes on the same machine.

3. **Socket Operations**:
   - **Creating a Socket**: A socket is created using the `socket()` function from the `socket` module.
   - **Binding**: The `bind()` method associates the socket with a specific IP address and port number.
   - **Listening**: The `listen()` method allows the socket to accept incoming connection requests.
   - **Accepting Connections**: The `accept()` method is used by server sockets to accept incoming connections from clients.
   - **Connecting**: The `connect()` method is used by client sockets to establish a connection to a server.
   - **Sending and Receiving Data**: The `send()` and `recv()` methods are used to transmit data over the socket.
   - **Closing the Socket**: The `close()` method terminates the socket connection.

### Basic Example of Socket Programming in Python

Here’s a simple example demonstrating how to create a TCP server and client using Python's socket library.

#### Server Code (`server.py`)

```python
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 12345...")

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive data from the client
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                # Send response back to client
                connection.sendall(data)  # Echo back the received data
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
```

#### Client Code (`client.py`)

```python
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, Server!"
    client_socket.sendall(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode()}")
finally:
    # Close the socket
    client_socket.close()
```

### Running the Example

1. Save the server code in a file named `server.py` and run it in one terminal window.
2. Save the client code in another file named `client.py` and run it in another terminal window.

### Expected Output

When you run both scripts:

- The server will output something like:

  ```
  Server is listening on port 12345...
  Connection from ('127.0.0.1', <some_port>)
  Received: Hello, Server!
  ```

- The client will output:
  ```
  Response from server: Hello, Server!
  ```

### Conclusion

Networking in Python allows developers to create applications that can communicate over networks using sockets. Sockets serve as fundamental building blocks for establishing connections between clients and servers, enabling real-time data exchange across various applications. By utilizing Python's built-in `socket` module, developers can implement both simple and complex networking functionalities with ease.

## 23) Explain various methods for socket connection.

### Methods for Socket Connection in Python

Socket programming in Python allows for communication between devices over a network. The `socket` module provides various methods to create and manage socket connections. Below are the key methods used for establishing and managing socket connections, along with explanations and examples.

#### 1. `socket.socket()`

This method creates a new socket object. You need to specify the address family and the socket type.

- **Address Families**:
  - `socket.AF_INET`: For IPv4 addresses.
  - `socket.AF_INET6`: For IPv6 addresses.
- **Socket Types**:
  - `socket.SOCK_STREAM`: For TCP (connection-oriented).
  - `socket.SOCK_DGRAM`: For UDP (connectionless).

**Example**:

```python
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

#### 2. `socket.bind()`

The `bind()` method associates the socket with a specific IP address and port number. This is typically used on the server side to specify where it should listen for incoming connections.

**Example**:

```python
server_address = ('localhost', 12345)
sock.bind(server_address)  # Bind the socket to the address and port
```

#### 3. `socket.listen()`

The `listen()` method enables a server socket to accept connections. It puts the socket in a passive mode, waiting for client connection requests. The backlog parameter specifies the maximum number of queued connections.

**Example**:

```python
sock.listen(5)  # Allow up to 5 pending connections
print("Server is listening for connections...")
```

#### 4. `socket.accept()`

The `accept()` method blocks until a client connects to the server. It returns a new socket object representing the connection and the address of the client.

**Example**:

```python
connection, client_address = sock.accept()
print(f"Connection from {client_address} has been established.")
```

#### 5. `socket.connect()`

The `connect()` method is used by a client socket to establish a connection to a server at a specified address and port.

**Example**:

```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to server
```

#### 6. `socket.send()`

The `send()` method sends data to the connected socket. It requires data in bytes format.

**Example**:

```python
message = "Hello, Server!"
client_socket.send(message.encode())  # Send message to server
```

#### 7. `socket.recv()`

The `recv()` method receives data from the connected socket. You specify the maximum amount of data to be received at once.

**Example**:

```python
data = connection.recv(1024)  # Receive up to 1024 bytes from the client
print(f"Received: {data.decode()}")
```

#### 8. `socket.close()`

The `close()` method closes the socket connection, freeing up resources.

**Example**:

```python
client_socket.close()  # Close the client socket
connection.close()      # Close the server connection
```

### Complete Example: Simple Server and Client

Here’s a complete example that demonstrates how these methods work together:

#### Server Code (`server.py`)

```python
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening for connections...")

while True:
    # Accept a connection from a client
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address} has been established.")

        # Receive data from the client
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                # Send response back to client
                connection.sendall(data)  # Echo back the received data
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
```

#### Client Code (`client.py`)

```python
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, Server!"
    client_socket.sendall(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode()}")
finally:
    # Close the socket
    client_socket.close()
```

### Running the Example

1. Save the server code in a file named `server.py` and run it in one terminal window.
2. Save the client code in another file named `client.py` and run it in another terminal window.

### Conclusion

Socket programming in Python provides powerful capabilities for network communication through various methods available in the `socket` module. Understanding these methods allows developers to create robust client-server applications that can exchange data over networks efficiently.

## 24) Discuss Thread Control Block (TCB).

### Thread Control Block (TCB)

A **Thread Control Block (TCB)** is a data structure used by the operating system to manage information about a thread. Each thread in a system has its own TCB, which contains critical information necessary for the operating system to schedule and manage the thread effectively. The TCB serves as the manifestation of a thread within the operating system.

### Key Components of a TCB

1. **Thread Identifier (TID)**:

   - A unique identifier assigned to each thread when it is created. This allows the operating system to distinguish between different threads.

2. **Thread State**:

   - Indicates the current state of the thread, which can be one of several states, such as:
     - **New**: The thread has been created but not yet started.
     - **Runnable**: The thread is ready to run and waiting for CPU time.
     - **Running**: The thread is currently being executed by the CPU.
     - **Blocked/Waiting**: The thread is waiting for an event or resource (e.g., I/O operation).
     - **Terminated/Dead**: The thread has completed execution.

3. **Program Counter (PC)**:

   - A pointer that indicates the next instruction to be executed for the thread. It keeps track of where the thread is in its execution.

4. **Stack Pointer**:

   - Points to the top of the stack for the thread. Each thread has its own stack, which contains local variables, function parameters, and return addresses.

5. **Register Set**:

   - Contains the values of all registers used by the thread. During context switches, these values are saved and restored so that the thread can resume execution correctly.

6. **Pointer to Process Control Block (PCB)**:

   - A reference to the Process Control Block associated with the process that owns this thread. This allows the operating system to manage resources shared among threads in a process.

7. **Thread Priority**:
   - Indicates the priority level of the thread, which helps the scheduler decide which thread to run next when multiple threads are in a runnable state.

### Example Structure of a TCB

While TCBs are implemented differently across various operating systems, a simplified representation in pseudocode might look like this:

```python
class ThreadControlBlock:
    def __init__(self, tid):
        self.thread_id = tid          # Unique Thread ID
        self.state = "New"           # Initial state
        self.program_counter = 0      # Instruction pointer
        self.stack_pointer = None      # Stack pointer
        self.registers = {}           # Register values
        self.priority = 0             # Thread priority
        self.pcb_pointer = None       # Pointer to Process Control Block
```

### Importance of TCBs

- **Thread Management**: TCBs allow the operating system to manage multiple threads efficiently by storing all necessary information about each thread's state and context.
- **Context Switching**: During context switches (when switching from one thread to another), TCBs store and restore register values, program counters, and stack pointers, enabling threads to resume execution without loss of data.
- **Scheduling**: The scheduler uses information in TCBs, such as priority and state, to determine which thread should run next.

### Conclusion

The Thread Control Block (TCB) is a fundamental component of multithreading in operating systems. It encapsulates all essential information about a thread, enabling efficient management, scheduling, and execution of threads within processes. Understanding TCBs is crucial for grasping how modern operating systems handle concurrency and parallelism effectively.

## 25) Explain Multithreading in Python with Thread Creation Methods.

### Multithreading in Python

**Multithreading** is a programming technique that allows multiple threads to run concurrently within a single process. In Python, multithreading is primarily managed using the `threading` module, which provides a high-level interface for creating and managing threads. This allows for parallel execution of tasks, improving the efficiency of programs, especially when performing I/O-bound operations.

### Key Concepts of Multithreading

- **Thread**: A thread is the smallest unit of processing that can be scheduled by an operating system. It consists of a sequence of instructions that can be executed independently.
- **Concurrency**: Multithreading enables concurrent execution of tasks, allowing multiple threads to make progress within the same application.
- **GIL (Global Interpreter Lock)**: Python has a GIL that allows only one thread to execute at a time in CPython (the standard Python implementation). This means that while multithreading can improve I/O-bound task performance, it may not significantly enhance CPU-bound task performance.

### Thread Creation Methods in Python

There are several ways to create threads in Python using the `threading` module:

#### 1. Creating Threads Using Functions

You can create threads by defining a function and passing it as the target to the `Thread` class.

**Example**:

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Create a thread
thread = threading.Thread(target=print_numbers)
thread.start()  # Start the thread
thread.join()   # Wait for the thread to finish
```

#### 2. Creating Threads by Extending the Thread Class

You can create a custom thread class by extending the `Thread` class and overriding its `run()` method.

**Example**:

```python
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread {self.name}: {i}")
            time.sleep(1)

# Create and start the thread
my_thread = MyThread()
my_thread.start()
my_thread.join()  # Wait for the thread to finish
```

#### 3. Creating Threads Without Extending Thread Class

You can also create threads without subclassing by targeting instance methods.

**Example**:

```python
import threading
import time

class Worker:
    def task(self):
        for i in range(5):
            print(f"Worker Thread: {i}")
            time.sleep(1)

# Create an instance of Worker
worker = Worker()

# Create a thread targeting the instance method
worker_thread = threading.Thread(target=worker.task)
worker_thread.start()
worker_thread.join()  # Wait for the thread to finish
```

#### 4. Creating Multiple Threads

You can create multiple threads and run them concurrently.

**Example**:

```python
import threading
import time

def worker(num):
    for i in range(3):
        print(f"Worker {num}: {i}")
        time.sleep(1)

# Create multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for t in threads:
    t.join()
```

### Daemon Threads

Daemon threads are background threads that run without blocking the main program from exiting. When all non-daemon threads have completed, daemon threads are terminated automatically.

**Example**:

```python
import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True  # Set as daemon thread
daemon_thread.start()

time.sleep(5)  # Main program sleeps for 5 seconds
print("Main program finished.")
```

### Conclusion

Multithreading in Python allows developers to perform multiple operations concurrently, enhancing the efficiency of applications, especially those involving I/O operations. The `threading` module provides various methods to create and manage threads, including using functions, extending the `Thread` class, and creating daemon threads. Understanding these methods helps developers effectively utilize multithreading to improve application performance.

## 26) Explain Multithreading with lock() synchronization.

### Multithreading with Lock Synchronization in Python

**Multithreading** in Python allows for concurrent execution of tasks, which can improve the efficiency of programs, especially those that are I/O-bound. However, when multiple threads access shared resources simultaneously, it can lead to **race conditions**, where the outcome depends on the timing of thread execution. To manage these situations and ensure data integrity, Python provides synchronization mechanisms such as **locks**.

### What is a Lock?

A **lock** is a synchronization primitive that ensures only one thread can access a resource at a time. When a thread acquires a lock, other threads that attempt to acquire the same lock will be blocked until the lock is released. This prevents race conditions and ensures that critical sections of code are executed atomically.

### Using Locks in Python

The `threading` module in Python provides the `Lock` class to create and manage locks. Here’s how you can use locks for synchronization in multithreading:

#### Key Methods of Lock

- **`acquire(blocking=True)`**: This method is used to acquire the lock. If the lock is already held by another thread, the calling thread will block (wait) until the lock is released unless `blocking` is set to `False`.
- **`release()`**: This method releases the lock, allowing other threads to acquire it.

- **`locked()`**: This method returns `True` if the lock is currently held by any thread; otherwise, it returns `False`.

### Example of Multithreading with Lock Synchronization

Here’s an example demonstrating how to use locks to synchronize access to a shared resource:

```python
import threading
import time

# Shared resource
counter = 0

# Create a lock object
lock = threading.Lock()

def increment(lock, N):
    global counter
    for _ in range(N):
        # Acquire the lock before entering the critical section
        lock.acquire()
        try:
            # Critical section: safely increment the counter
            counter += 1
            print(f"Counter value: {counter}")
        finally:
            # Always release the lock in a finally block
            lock.release()

# Create multiple threads
t1 = threading.Thread(target=increment, args=(lock, 5))
t2 = threading.Thread(target=increment, args=(lock, 5))
t3 = threading.Thread(target=increment, args=(lock, 5))

# Start the threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("Final Counter Value:", counter)
```

### Explanation of the Example

1. **Shared Resource**: The variable `counter` is shared among multiple threads.

2. **Lock Creation**: A lock object is created using `lock = threading.Lock()`.

3. **Thread Function**: The `increment` function increments the shared counter. Before modifying the counter:

   - The thread acquires the lock using `lock.acquire()`.
   - The critical section (where the counter is modified) is executed.
   - The lock is released using `lock.release()` in a `finally` block to ensure it is released even if an error occurs.

4. **Creating Threads**: Three threads are created and started, each calling the `increment` function with the same lock.

5. **Joining Threads**: The main program waits for all threads to complete using `join()`.

### Output

When you run this code, you will see output similar to:

```
Counter value: 1
Counter value: 2
Counter value: 3
Counter value: 4
Counter value: 5
Counter value: 6
Counter value: 7
Counter value: 8
Counter value: 9
Counter value: 10
Final Counter Value: 15
```

The final counter value reflects that all increments were executed safely without any race conditions due to proper use of locks.

### Conclusion

Using locks in multithreading allows for safe access to shared resources by ensuring that only one thread can modify a resource at a time. This prevents race conditions and maintains data integrity. The `threading.Lock()` class provides methods to manage locking effectively, making it an essential tool for writing concurrent programs in Python.
