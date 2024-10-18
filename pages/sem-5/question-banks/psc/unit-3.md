# Unit 3

## 1) What are the different ways to create arrays in Python?

In Python, there are several ways to create arrays, which are data structures that store multiple items of the same type. Below are some common methods for creating arrays in Python, along with examples:

#### 1. Using the `array` Module

The `array` module provides a way to create arrays that are more efficient than lists for storing large amounts of data. You can create an array of a specific type by specifying a type code.

```python
import array

## Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)

## Create an array of floats
float_array = array.array('f', [1.0, 2.5, 3.5])
print("Float Array:", float_array)

```

#### 2. Using Lists

While lists are not strictly arrays, they can be used as dynamic arrays in Python. Lists can hold elements of different types and can be resized.

```python
## Create a list (dynamic array)
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

## Create a mixed-type list
mixed_list = [1, "two", 3.0]
print("Mixed List:", mixed_list)

```

#### 3. Using NumPy Arrays

NumPy is a powerful library for numerical computing in Python that provides support for large multi-dimensional arrays and matrices. It is widely used for scientific computing.

```python
import numpy as np

## Create a NumPy array from a list
numpy_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", numpy_array)

## Create a multi-dimensional NumPy array (matrix)
matrix_array = np.array([[1, 2], [3, 4]])
print("Matrix Array:\\n", matrix_array)

```

#### 4. Using List Comprehensions

You can use list comprehensions to create lists (arrays) in a concise way.

```python
## Create an array of squares using list comprehension
squares = [x**2 for x in range(10)]
print("Squares Array:", squares)

```

#### 5. Using the `copy` Module

If you want to create a copy of an existing array or list, you can use the `copy` module or the built-in methods.

```python
import copy

original_list = [1, 2, 3]
copied_list = copy.copy(original_list)  ## Shallow copy
print("Copied List:", copied_list)

## Deep copy example (for nested structures)
nested_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(nested_list)
print("Deep Copied List:", deep_copied_list)

```

#### Summary

- **Using the `array` module**: For creating fixed-type arrays.
- **Using lists**: Dynamic arrays that can hold mixed types.
- **Using NumPy**: For efficient numerical operations and multi-dimensional arrays.
- **Using list comprehensions**: For creating lists concisely.
- **Using the `copy` module**: For copying existing arrays or lists.

These methods provide flexibility depending on your needs for performance and functionality when working with collections of data in Python.

## 2) Explain the concept of array computing in Python. How does NumPy facilitate efficient array operations compared to standard Python lists? Provide examples.

#### Concept of Array Computing in Python

**Array computing** refers to the ability to perform operations on arrays (or collections of data) efficiently. In Python, array computing is primarily facilitated by libraries like **NumPy**, which provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

#### Why Use Array Computing?

1. **Performance**: Array operations can be significantly faster than equivalent operations using standard Python lists, especially for large datasets.
2. **Convenience**: NumPy provides a wide range of functions that make it easier to perform mathematical operations on arrays.
3. **Memory Efficiency**: NumPy arrays consume less memory compared to Python lists because they are homogeneously typed.
4. **Element-wise Operations**: NumPy allows for element-wise operations on arrays, which means you can apply operations directly to each element without needing explicit loops.

#### How NumPy Facilitates Efficient Array Operations

NumPy improves performance and efficiency in several ways:

1. **Contiguous Memory Allocation**: NumPy arrays are stored in contiguous blocks of memory, which makes accessing elements faster compared to lists that may have scattered memory locations.
2. **Vectorized Operations**: NumPy allows you to perform operations on entire arrays without the need for explicit loops. This is known as vectorization and is achieved through optimized C and Fortran code under the hood.
3. **Broadcasting**: NumPy supports broadcasting, which allows you to perform arithmetic operations on arrays of different shapes in a seamless manner.
4. **Built-in Functions**: NumPy provides a rich set of built-in functions that are optimized for performance, enabling complex mathematical computations with minimal code.

#### Examples

#### 1. Creating Arrays with NumPy

```python
import numpy as np

## Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

## Create a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\\n", array_2d)

```

#### 2. Element-wise Operations

```python
## Element-wise addition
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
result = array_a + array_b
print("Element-wise Addition:", result)  ## Output: [5 7 9]

## Element-wise multiplication
result = array_a * array_b
print("Element-wise Multiplication:", result)  ## Output: [4 10 18]

```

#### 3. Broadcasting Example

```python
## Broadcasting example
array_c = np.array([[1, 2], [3, 4]])
scalar = 10
result = array_c + scalar
print("Broadcasting Result:\\n", result)
## Output:
## [[11 12]
##  [13 14]]

```

#### 4. Using Built-in Functions

```python
## Calculate the mean of an array
mean_value = np.mean(array_1d)
print("Mean Value:", mean_value)  ## Output: Mean Value: 3.0

## Calculate the sum of all elements in a matrix
sum_value = np.sum(array_2d)
print("Sum of All Elements:", sum_value)  ## Output: Sum of All Elements: 21

```

#### Comparison with Standard Python Lists

- **Performance**: Operations on NumPy arrays are generally faster than on Python lists due to optimized implementations.
- **Functionality**: NumPy provides a wide range of mathematical functions that can be applied directly to arrays.
- **Memory Usage**: NumPy arrays are more memory-efficient than lists because they store elements of the same type in contiguous memory locations.

#### Conclusion

Array computing in Python is efficiently handled by libraries like NumPy, which provide powerful tools for creating and manipulating arrays. The advantages of using NumPy over standard Python lists include better performance, ease of use through vectorized operations and broadcasting, and access to a rich set of mathematical functions. This makes NumPy an essential library for scientific computing and data analysis in Python.

## 3) How do you create a NumPy array? Explain with suitable examples.

#### Creating NumPy Arrays in Python

NumPy is a powerful library in Python that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. Creating arrays in NumPy is straightforward and can be done in several ways. Below are some common methods for creating NumPy arrays, along with examples.

#### 1. Creating an Array from a List or Tuple

You can create a NumPy array by passing a list or tuple to the `np.array()` function.

```python
import numpy as np

## Create a 1D array from a list
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

## Create a 2D array from a list of lists (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\\n", array_2d)

```

#### 2. Creating Arrays with Built-in Functions

NumPy provides several built-in functions to create arrays of specific shapes and values.

#### Example: Using `np.zeros()`, `np.ones()`, and `np.arange()`

```python
## Create an array of zeros
zeros_array = np.zeros((3, 4))  ## Shape: 3 rows, 4 columns
print("Array of Zeros:\\n", zeros_array)

## Create an array of ones
ones_array = np.ones((2, 3))  ## Shape: 2 rows, 3 columns
print("Array of Ones:\\n", ones_array)

## Create an array with a range of values
range_array = np.arange(10)  ## Array with values from 0 to 9
print("Range Array:", range_array)

```

#### 3. Creating Arrays with Random Values

You can create arrays filled with random numbers using the `numpy.random` module.

```python
## Create an array of random floats between 0 and 1
random_array = np.random.rand(3, 2)  ## Shape: 3 rows, 2 columns
print("Random Array:\\n", random_array)

## Create an array of random integers within a specified range
random_ints = np.random.randint(0, 10, size=(2, 3))  ## Values between 0 and 9
print("Random Integers Array:\\n", random_ints)

```

#### 4. Creating Identity Matrices

NumPy also allows you to create identity matrices using `np.eye()`.

```python
## Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\\n", identity_matrix)

```

#### Summary

NumPy provides various methods for creating arrays:

- **From Lists/Tuples**: Use `np.array()`.
- **Built-in Functions**: Use functions like `np.zeros()`, `np.ones()`, and `np.arange()` for specific shapes and values.
- **Random Values**: Use the `numpy.random` module for generating arrays with random numbers.
- **Identity Matrices**: Use `np.eye()` to create identity matrices.

These methods make it easy to create and manipulate arrays in Python for scientific computing and data analysis tasks.

## 4) Write the difference between rand, randn, and randint methods in numpy.

In NumPy, there are three primary functions for generating random numbers: `rand()`, `randn()`, and `randint()`. Each of these functions serves a different purpose and generates random numbers in distinct ways. Here’s a breakdown of the differences between them:

#### 1. `numpy.random.rand()`

- **Purpose**: Generates random numbers uniformly distributed between 0 and 1.
- **Usage**: You can specify the shape of the output array by passing the desired dimensions as arguments.

#### Example:

```python
import numpy as np

## Generate a 1D array of 5 random numbers
rand_array_1d = np.random.rand(5)
print("1D Array of Random Numbers (0 to 1):", rand_array_1d)

## Generate a 2D array (3 rows, 4 columns) of random numbers
rand_array_2d = np.random.rand(3, 4)
print("2D Array of Random Numbers (0 to 1):\\n", rand_array_2d)

```

#### 2. `numpy.random.randn()`

- **Purpose**: Generates random numbers from the standard normal distribution (mean = 0, standard deviation = 1).
- **Usage**: Similar to `rand()`, you can specify the shape of the output array.

#### Example:

```python
## Generate a 1D array of 5 random numbers from a standard normal distribution
randn_array_1d = np.random.randn(5)
print("1D Array of Random Numbers (Standard Normal):", randn_array_1d)

## Generate a 2D array (2 rows, 3 columns) of random numbers from a standard normal distribution
randn_array_2d = np.random.randn(2, 3)
print("2D Array of Random Numbers (Standard Normal):\\n", randn_array_2d)

```

#### 3. `numpy.random.randint()`

- **Purpose**: Generates random integers within a specified range.
- **Usage**: You can specify the low and high bounds for the integers and the size of the output array.

#### Example:

```python
## Generate an array of 5 random integers between 0 (inclusive) and 10 (exclusive)
randint_array = np.random.randint(0, 10, size=5)
print("Array of Random Integers (0 to 9):", randint_array)

## Generate a 2D array (3 rows, 4 columns) of random integers between 1 and 100
randint_array_2d = np.random.randint(1, 100, size=(3, 4))
print("2D Array of Random Integers (1 to 99):\\n", randint_array_2d)

```

#### Summary of Differences

| Function | Distribution Type | Range | Output Shape Specification |
| --- | --- | --- | --- |
| `np.random.rand()` | Uniform [0, 1) | [0.0, 1.0) | Yes |
| `np.random.randn()` | Standard Normal (mean=0) | (-∞, ∞) | Yes |
| `np.random.randint()` | Uniform Integers | [low, high) | Yes |

#### Conclusion

- Use **`numpy.random.rand()`** when you need uniformly distributed floating-point numbers between 0 and 1.
- Use **`numpy.random.randn()`** when you need normally distributed floating-point numbers with mean = 0 and standard deviation = 1.
- Use **`numpy.random.randint()`** when you need random integers within a specified range.

These functions are essential for performing simulations, generating test data, or any scenario where randomness is required in numerical computations.

## 5) Explain a random module in python.

#### Random Module in Python

The **`random` module** in Python is a built-in library that provides functions to generate pseudo-random numbers and perform random operations. It is widely used for tasks such as simulations, games, and random sampling. The numbers generated by the `random` module are not truly random but are generated using algorithms that produce sequences of numbers that approximate the properties of random numbers.

#### Key Functions in the `random` Module

Here are some of the most commonly used functions in the `random` module:

1. **`random.random()`**:
    - Generates a random float number between `0.0` to `1.0`.
    
    ```python
    import random
    
    rand_float = random.random()
    print("Random Float:", rand_float)  ## Output: Random Float: (e.g., 0.37444887175646646)
    
    ```
    
2. **`random.randint(a, b)`**:
    - Returns a random integer `N` such that `a <= N <= b`.
    
    ```python
    rand_int = random.randint(1, 10)
    print("Random Integer between 1 and 10:", rand_int)  ## Output: Random Integer between 1 and 10: (e.g., 7)
    
    ```
    
3. **`random.choice(sequence)`**:
    - Returns a randomly selected element from a non-empty sequence (like a list or tuple).
    
    ```python
    items = ['apple', 'banana', 'cherry']
    rand_choice = random.choice(items)
    print("Random Choice from List:", rand_choice)  ## Output: Random Choice from List: (e.g., 'banana')
    
    ```
    
4. **`random.sample(population, k)`**:
    - Returns a list of `k` unique elements chosen from the population sequence or set.
    
    ```python
    population = range(100)  ## A population of numbers from 0 to 99
    sample = random.sample(population, 5)
    print("Random Sample of 5 Elements:", sample)  ## Output: Random Sample of 5 Elements: (e.g., [12, 45, 67, 89, 34])
    
    ```
    
5. **`random.shuffle(x)`**:
    - Shuffles the elements of the list `x` in place.
    
    ```python
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    random.shuffle(deck)
    print("Shuffled Deck:", deck)  ## Output: Shuffled Deck: (e.g., ['3', 'A', '10', '6', '2', ...])
    
    ```
    
6. **`random.uniform(a, b)`**:
    - Returns a random float number between `a` and `b`.
    
    ```python
    rand_uniform = random.uniform(1.5, 10.5)
    print("Random Float between 1.5 and 10.5:", rand_uniform)  ## Output: Random Float between 1.5 and 10.5: (e.g., 7.234)
    
    ```
    

#### Example Usage

Here’s an example that combines several functions from the `random` module:

```python
import random

## Generate a random float
print("Random Float:", random.random())

## Generate a random integer
print("Random Integer between 1 and 100:", random.randint(1, 100))

## Choose a random item from a list
fruits = ['apple', 'banana', 'cherry', 'date']
print("Random Fruit:", random.choice(fruits))

## Sample multiple unique items from a list
print("Random Sample of Fruits:", random.sample(fruits, k=2))

## Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled Numbers:", numbers)

## Generate a uniform float
print("Random Float between -10 and 10:", random.uniform(-10, 10))

```

#### Conclusion

The `random` module in Python provides a variety of functions for generating pseudo-random numbers and performing random operations. It is an essential tool for simulations, games, and any application that requires randomness. Understanding how to use this module can significantly enhance your ability to create dynamic and interactive programs.

## 6) Explain reshape, arange, linspace, eye, ones, zeros, transpose, shape, flatten.

In NumPy, several functions are essential for creating and manipulating arrays. Below is an explanation of the following functions: `reshape`, `arange`, `linspace`, `eye`, `ones`, `zeros`, `transpose`, `shape`, and `flatten`.

#### 1. `reshape()`

- **Purpose**: Changes the shape of an existing array without changing its data.
- **Usage**: The new shape must be compatible with the original shape (i.e., the total number of elements must remain the same).

#### Example:

```python
import numpy as np

## Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])
## Reshape it to a 2D array (2 rows, 3 columns)
array_2d = array_1d.reshape((2, 3))
print("Reshaped Array:\\n", array_2d)

```

#### 2. `arange()`

- **Purpose**: Creates an array with evenly spaced values within a specified range.
- **Usage**: Similar to Python's built-in `range()` function but returns an array.

#### Example:

```python
## Create an array with values from 0 to 9
array_range = np.arange(10)
print("Array from arange:", array_range)

## Create an array with values from 1 to 10 with a step of 2
array_range_step = np.arange(1, 10, 2)
print("Array with step of 2:", array_range_step)

```

#### 3. `linspace()`

- **Purpose**: Creates an array of evenly spaced values over a specified interval.
- **Usage**: You can specify the start and end values and the number of samples.

#### Example:

```python
## Create an array of 5 evenly spaced values between 0 and 1
array_linspace = np.linspace(0, 1, num=5)
print("Array from linspace:", array_linspace)

```

#### 4. `eye()`

- **Purpose**: Creates a square identity matrix (a matrix with ones on the diagonal and zeros elsewhere).
- **Usage**: You can specify the size of the identity matrix.

#### Example:

```python
## Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\\n", identity_matrix)

```

#### 5. `ones()`

- **Purpose**: Creates an array filled with ones.
- **Usage**: You can specify the shape of the output array.

#### Example:

```python
## Create a 2D array of ones (3 rows, 4 columns)
array_ones = np.ones((3, 4))
print("Array of Ones:\\n", array_ones)

```

#### 6. `zeros()`

- **Purpose**: Creates an array filled with zeros.
- **Usage**: You can specify the shape of the output array.

#### Example:

```python
## Create a 2D array of zeros (2 rows, 3 columns)
array_zeros = np.zeros((2, 3))
print("Array of Zeros:\\n", array_zeros)

```

#### 7. `transpose()`

- **Purpose**: Transposes the dimensions of an array (flips it over its diagonal).
- **Usage**: The shape is changed such that rows become columns and vice versa.

#### Example:

```python
## Create a 2D array
array_to_transpose = np.array([[1, 2, 3], [4, 5, 6]])
transposed_array = np.transpose(array_to_transpose)
print("Transposed Array:\\n", transposed_array)

```

#### 8. `shape`

- **Purpose**: Returns a tuple representing the dimensions of an array.
- **Usage**: Useful for understanding the structure of multi-dimensional arrays.

#### Example:

```python
## Create a sample array
sample_array = np.array([[1, 2], [3, 4], [5, 6]])
print("Shape of Array:", sample_array.shape) ## Output: (3, 2)

```

#### 9. `flatten()`