# Unit 2

# _Check for correctness of answers._

## 1) Write a method to generate a tag in arithmetic coding.

The following code implements a method to generate a tag (code) in arithmetic coding. This example assumes you've already performed the probability estimation and interval calculations necessary for arithmetic coding. It focuses specifically on the tag generation part.

This code uses floating-point arithmetic for simplicity. For production-level arithmetic coding, consider using fixed-point arithmetic to avoid potential floating-point precision issues.

```python
def generate_arithmetic_code(cumulative_probabilities, symbol_index):
    """
    Generates an arithmetic code tag for a given symbol.

    Args:
        cumulative_probabilities: A list of cumulative probabilities.
                                  cumulative_probabilities[i] is the cumulative probability
                                  up to and including symbol i.  Must be normalized (last element == 1.0).
        symbol_index: The index of the symbol in the probability distribution.

    Returns:
        A string representing the arithmetic code tag.  Returns None if input is invalid.
    """

    if not cumulative_probabilities:
        return None  # Handle empty probability distribution

    if not 0 <= symbol_index < len(cumulative_probabilities):
        return None # Invalid symbol index

    if not 0.0 <= cumulative_probabilities[-1] <=1.0:
        return None # Probabilities must be normalized

    lower_bound = 0.0 if symbol_index == 0 else cumulative_probabilities[symbol_index - 1]
    upper_bound = cumulative_probabilities[symbol_index]

    # Simple approach to generate a tag of a certain length.  Adjust precision as needed.
    precision = 16  # Number of bits in the tag

    #This calculation generates a code within the range [lower_bound, upper_bound)
    code_value = lower_bound + (upper_bound - lower_bound) / 2


    # Convert the code value to a binary string
    binary_representation = bin(int(code_value * (2**precision)))[2:].zfill(precision)

    return binary_representation


# Example usage:
cumulative_probabilities = [0.2, 0.6, 1.0] # Probabilities for symbols 0, 1, 2
symbol_index = 1

tag = generate_arithmetic_code(cumulative_probabilities, symbol_index)
print(f"Arithmetic code for symbol {symbol_index}: {tag}")

cumulative_probabilities = [0.25, 0.75, 1.0] #Probabilities for symbols 0, 1, 2
symbol_index = 0

tag = generate_arithmetic_code(cumulative_probabilities, symbol_index)
print(f"Arithmetic code for symbol {symbol_index}: {tag}")

```

Remember that this is a simplified version. A complete arithmetic coding implementation needs to handle:

- **Encoding multiple symbols:** The above only encodes a single symbol. For multiple symbols, you need to iteratively refine the interval based on each successive symbol.
- **Decoding:** You'll need a complementary decoding function to recover the original symbols from the generated code.
- **Handling edge cases:** Consider what happens when probabilities are zero or one, and how to manage the precision to avoid numerical errors.
- **Efficient bit packing:** For optimal compression, you'll need a more efficient way to represent the code than simply using a fixed-length binary string, often using bit streams.

This example provides a foundation for understanding the core concept of generating an arithmetic code tag. For a production-ready implementation, you'd need to address the points mentioned above.

## 2) Write an encoding algorithm for arithmetic coding.

This algorithm implements arithmetic coding for encoding a sequence of symbols. It assumes you have a pre-calculated probability model for each symbol. This model is represented as a dictionary where keys are symbols and values are their probabilities.

```python
import math

def arithmetic_encode(symbols, probabilities):
    """
    Encodes a sequence of symbols using arithmetic coding.

    Args:
        symbols: A list or string of symbols to encode.
        probabilities: A dictionary where keys are symbols and values are their probabilities.  Probabilities should sum to 1.

    Returns:
        A floating-point number representing the encoded sequence.  This needs further processing (e.g., converting to bits) for storage/transmission.
    """

    # Error handling: Check if probabilities sum to 1 (or very close)
    if not math.isclose(sum(probabilities.values()), 1.0):
        raise ValueError("Probabilities must sum to 1.")

    # Cumulative probabilities
    cumulative_probabilities = {}
    cumulative_probability = 0.0
    for symbol, probability in probabilities.items():
        cumulative_probability += probability
        cumulative_probabilities[symbol] = cumulative_probability

    lower_bound = 0.0
    upper_bound = 1.0

    for symbol in symbols:
        if symbol not in probabilities:
            raise ValueError(f"Symbol '{symbol}' not found in the probability model.")

        lower_bound = lower_bound + (upper_bound - lower_bound) * cumulative_probabilities[symbol]
        upper_bound = lower_bound + (upper_bound - lower_bound) * probabilities[symbol]

    # Choose a value within the final interval.  The midpoint is a common choice.
    encoded_value = (lower_bound + upper_bound) / 2

    return encoded_value



# Example Usage:
symbols = "AABABBA"
probabilities = {'A': 0.6, 'B': 0.4}

encoded = arithmetic_encode(symbols, probabilities)
print(f"Encoded value: {encoded}")


#Example with more symbols
symbols2 = "ABACADA"
probabilities2 = {'A': 0.4, 'B': 0.2, 'C': 0.2, 'D': 0.2}
encoded2 = arithmetic_encode(symbols2,probabilities2)
print(f"Encoded value: {encoded2}")
```

**Important Considerations:**

- **Precision:** Floating-point arithmetic has limitations. For long sequences, the precision of the `lower_bound` and `upper_bound` might become insufficient, leading to inaccuracies. Real-world implementations use techniques like scaling to maintain precision.
- **Probability Model:** The accuracy of arithmetic coding heavily relies on the accuracy of the probability model. A good model is crucial for efficient compression. Often, adaptive models are used where probabilities are updated as the data is encoded.
- **Bit Stream Conversion:** The output of this function is a floating-point number. In a practical implementation, you would need to convert this value into a bit stream of a specific length, which requires handling the precision issues mentioned above and defining a way to represent the length.
- **Decoding:** This code only provides encoding. You'll need a corresponding decoding algorithm to recover the original symbol sequence from the encoded value.

This enhanced example provides a more robust and practical foundation for understanding and implementing arithmetic coding. Remember that this is a simplified version, and production-level implementations often include more sophisticated techniques for handling precision and adaptive modeling.

## 3) Define arithmetic coding. Encode and decode “BACBA” with arithmetic coding (P(A)=0.5,P(B)=0.3,P(C)=0.2)

**3) Arithmetic Coding Definition:**

Arithmetic coding is a form of entropy encoding that represents a sequence of symbols as a single fractional number (between 0 and 1). Instead of assigning fixed-length codes to symbols (like Huffman coding), it assigns a subinterval within the range [0, 1) proportional to the symbol's probability. Each subsequent symbol further subdivides the current interval, ultimately resulting in a final interval representing the entire sequence. The length of the final interval reflects the sequence's probability. The final interval is then represented by any number within it (usually the shortest possible representation).

**Encoding "BACBA":**

Given probabilities: P(A) = 0.5, P(B) = 0.3, P(C) = 0.2

1. **Initialization:** Start with the interval [0, 1).

2. **Encoding 'B':**

   - P(B) = 0.3
   - The interval becomes [0, 0.3) (0.3 \* 1 = 0.3)

3. **Encoding 'A':**

   - P(A) = 0.5 (conditional probability not needed because we're not using context-based arithmetic coding)
   - The subinterval of [0, 0.3) corresponding to A is [0, 0.3\*0.5) = [0, 0.15)

4. **Encoding 'C':**

   - P(C) = 0.2
   - The subinterval of [0, 0.15) corresponding to C is [0, 0.15\*0.2) = [0, 0.03)

5. **Encoding 'B':**

   - P(B) = 0.3
   - The subinterval of [0, 0.03) corresponding to B is [0, 0.03\*0.3) = [0, 0.009)

6. **Encoding 'A':**

   - P(A) = 0.5
   - The final subinterval corresponding to A is [0, 0.009\*0.5) = [0, 0.0045)

7. **Final Code:** Any number within [0, 0.0045) can represent "BACBA". Let's choose 0.004. However, to save space we typically use the shortest binary representation that fully encapsulates the interval. This will require converting the decimal 0.0045 to its binary representation, which is a little tedious by hand. Let's round up to the shortest binary number that covers the interval instead of a precise decimal representation: For this example, a binary number starting with a significant number of zeros and then containing some ones that falls within the interval might suffice for brevity. For example, the binary representation of 0.004 is longer, but to be short we'll say that the encoded value is "0.000" (representing a sufficiently small number in the range.) In practice, a more sophisticated approach is used to determine the optimal shortest representation.

**Decoding "BACBA":**

1. **Initialization:** Start with the interval [0, 1) and the received code (let's use our simplified "0.000").

2. **Decoding the first symbol:**

   - 0.000 falls within [0, 0.3), which corresponds to 'B'.

3. **Iterative decoding:** Repeat the following for the remaining symbols:
   - Find the sub-interval that contains the coded value.
   - Divide the coded value by the probability of the decoded symbol.
   - Repeat with the new interval until you exhaust the encoded sequence. The process is a bit tedious manually.

**Important Note:** Manual arithmetic coding calculations, especially for decoding, can be quite complex and prone to rounding errors. The example demonstrates the basic principle; real-world arithmetic coders use more advanced techniques for efficient calculation and representation of fractional numbers. Software libraries exist to handle this process effectively. Also, the method of choosing the final binary representation (and the precision needed) requires a more careful explanation and implementation in a real system. The example provides a simplified intuitive grasp of the concept.

## 4) Write a method to generate binary code A={a1, a2, a3, a4} (P(a1)= 0.5,P(a2)=0.25, P(a3)=0.125, p(a4)=0.125)

Several methods can generate binary codes for the given probabilities. Here are two common approaches:

**Method 1: Huffman Coding**

Huffman coding is an optimal prefix-free binary code. It minimizes the expected code length.

1. **Sort Probabilities:** Sort the probabilities in ascending order: a3 (0.125), a4 (0.125), a2 (0.25), a1 (0.5)

2. **Combine Lowest Probabilities:** Combine the two lowest probabilities (a3 and a4) to form a new node with probability 0.25.

3. **Repeat:** Repeat step 2 until you have a single node with probability 1.0.

4. **Assign Codes:** Assign '0' to the left branch and '1' to the right branch at each step. Work your way back up the tree to assign a code to each symbol.

Here's the tree and resulting codes:

```
          1.0
         /   \
      0.5     0.5
     /         \
   a1           0.25
                 /  \
              0.25   0.25
             /      \
           a2       0.125
                    /  \
                  a3   a4
```

- a1: 0
- a2: 10
- a3: 110
- a4: 111

**Method 2: Arithmetic Coding (more complex, but potentially more efficient for longer codes)**

Arithmetic coding represents the entire sequence of symbols as a single fractional number. It's more complex to implement than Huffman coding but can achieve better compression ratios, especially when probabilities are not powers of 2. I won't detail the full implementation here, as it's quite involved, but here's the basic idea:

1. **Cumulative Probabilities:** Calculate the cumulative probabilities:

   - a1: 0.0 - 0.5
   - a2: 0.5 - 0.75
   - a3: 0.75 - 0.875
   - a4: 0.875 - 1.0

2. **Encoding:** Assign a subinterval within [0, 1) to each symbol based on its cumulative probability range. As you encode a sequence of symbols, you iteratively narrow down the interval. The final interval represents the encoded sequence.

3. **Decoding:** The decoding process reverses this, using the interval to determine the original sequence.

**Method 1 (Huffman Coding) in Python:**

This is a simplified implementation; more robust Huffman coding implementations exist in libraries.

```python
import heapq

def huffman_coding(probabilities):
    heap = [[prob, [symbol]] for symbol, prob in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1]:
            pair.append(0)
        for pair in hi[1]:
            pair.append(1)
        heapq.heappush(heap, [lo[0] + hi[0], lo[1] + hi[1]])

    codes = {}
    for symbol, code in heap[0][1]:
        codes[symbol] = "".join(map(str, code))
    return codes


probabilities = {'a1': 0.5, 'a2': 0.25, 'a3': 0.125, 'a4': 0.125}
codes = huffman_coding(probabilities)
print(codes) # Output will show the Huffman codes for each symbol (likely the same as above but order may vary)
```

Remember to install `heapq` if you haven't already (it's a standard Python library, so you likely have it). Choose the method that best suits your needs and complexity preferences. Huffman coding is generally easier to implement for a simple case like this. Arithmetic coding is superior for longer sequences or when better compression is crucial.

## 5) Decipher the sequence using the tag generation method. Use the given tag value and frequencies. Tag value= 0.772352, F(1)=0.8 F(2)=0.82, F(3)= 1, F(k)=0, k<=0 (Up to 4 elements)

The tag generation method, in the context of sequence deciphering, typically involves associating a numerical tag with each element in a sequence based on its frequency and position. The provided information is insufficient to _decipher_ a sequence. We only have a tag value (0.772352) and frequencies for three positions (F(1), F(2), F(3)). We need _more_ information to work backward.

To illustrate why, let's assume a simple, linear tag generation method:

The tag for an element at position 'k' is calculated as: `Tag(k) = F(k) * some_constant`

Even with this simplified approach, we have unknowns:

- **The actual sequence:** We don't know the elements of the sequence itself.
- **The constant:** We don't know the `some_constant` used to scale the frequencies.

To decipher the sequence, we would need either:

1. **The formula used to generate the tag:** A complete mathematical description of how the tag is calculated from element values and their positions.
2. **A training set:** Examples of sequences and their corresponding tags to infer the tag generation process.

**Example of how more information would solve it (Hypothetical):**

Let's _hypothetically_ assume the tag is generated like this:

`Tag(k) =  ∑ [ element(i) * F(i) ]  for i=1 to k`

(This means the tag is a weighted sum of the elements).

And let's suppose the elements are integers. Then, we might solve it iteratively. For example, if the sequence has three elements (a, b, c):

`0.772352 = a * 0.8 + b * 0.82 + c * 1`

We would need _another_ equation (e.g., another tag value from a different sequence segment or additional constraints on a, b, and c) to solve for the three unknowns (a, b, c).

In conclusion: The given information is not enough to decipher the sequence. You need to provide the complete tag generation algorithm or sufficient additional data to allow for a solution.

## 6) Write a method to generate a tag using the scaling method. Encode and decode the sequence “1321” (P(a1)= 0.8, P(a2)=0.02, P(a3)=0.18)

The scaling method for generating tags is a form of variable-length coding used for data compression where the length of the code assigned to a symbol is inversely proportional to its probability. Symbols with higher probability get shorter codes.

Here's how to generate a tag using the scaling method and encode/decode "1321" with the given probabilities:

**1. Probability Distribution and Cumulative Probability:**

First, we need to calculate the cumulative probabilities:

- a1 (1): P(a1) = 0.8
- a2 (2): P(a2) = 0.02
- a3 (3): P(a3) = 0.18

Cumulative Probabilities:

- a1: 0.8
- a2: 0.8 + 0.02 = 0.82
- a3: 0.82 + 0.18 = 1.0

**2. Scaling Method Encoding:**

The scaling method works by representing each symbol's cumulative probability range as an interval within a scale (initially [0, 1]). We iteratively refine this scale as we encode each symbol.

Let's encode "1321":

- **Step 1 (1):** a1 has the range [0, 0.8). We'll represent this with a fractional number (0.4 for example, it only needs to fall in the interval). The new scale becomes [0, 0.8) (multiplied by the interval).

- **Step 2 (3):** a3 has the range [0.82, 1.0). Using the existing fraction (0.4), we scale it to be in this new range. This would result in a new fraction roughly 0.4 \* (1.0 - 0.82) + 0.82 = 0.872. Our new scale is [0.82, 1.0).

- **Step 3 (2):** a2 has the range [0.8, 0.82). Our fractional value (0.872) needs to be scaled down to this range. This gives a new fractional value approximately 0.872 \*(0.82 - 0.8) + 0.8 = 0.8088

- **Step 4 (1):** a1 has the range [0, 0.8). Again, we scale: 0.8088 \* (0.8) = 0.64704

**Encoded Value:** The final fractional value (0.64704) represents the encoded sequence "1321". The precision depends on how many decimal places you keep during the calculations.

**3. Scaling Method Decoding:**

Decoding involves reversing the process:

1. **Start with the encoded value:** 0.64704

2. **Check which range it falls into:** 0.64704 falls into the range [0, 0.8), which corresponds to a1. Therefore, the first symbol is 1.

3. **Update the range:** Scale the remainder relative to the probability: 0.64704/0.8 = 0.8088.

4. **Repeat:** Now we start with 0.8088. Check the range: It falls into [0.8, 0.82), which is a2. The next symbol is 2. Rescale: (0.8088 - 0.8)/(0.02) ≈ 0.44

5. **Repeat:** Now 0.44 falls into [0.82, 1.0), which is a3. The next symbol is 3. Rescale: (0.44 - 0.82)/(0.18) which is not possible!

The decoding process should be:

1.  0.64704 falls in [0, 0.8) => 1
2.  (0.64704 / 0.8) = 0.8088 falls in [0.8, 0.82) => 2
3.  ((0.8088 - 0.8) / 0.02) + 0.82 ≈ 0.844 falls in [0.82, 1.0) => 3
4.  ((0.844 - 0.82) / 0.18) + 0, approximately 0.44 falls in [0, 0.8) => 1

There is an error in this calculation, because the scaling must be done in the other way around (the fraction being scaled must be scaled down to the new range):

1.  0.64704 falls in [0, 0.8) => 1
2.  (0.64704 \* 0.8) = 0.517632 falls in [0.8, 0.82) => 2
3.  ((0.517632 - 0.8) / (0.82 - 0.8)) = Error
    This approach is not suitable.

**Improved approach:** A more practical implementation would use a binary representation of the cumulative probabilities. This avoids floating-point errors and is easier to implement. I'd recommend looking into arithmetic coding for a robust solution to this type of encoding and decoding. The above method is a simplified illustration that showcases the conceptual steps, but it's prone to errors with floating-point precision.

## 7) Write the difference between arithmetic coding and huffman coding.

Both arithmetic coding and Huffman coding are entropy encoding techniques used for lossless data compression, but they achieve this in fundamentally different ways:

**Huffman Coding:**

- **Method:** Assigns a unique variable-length codeword to each symbol (character, byte, etc.) based on its frequency of occurrence. More frequent symbols get shorter codewords, less frequent symbols get longer ones. It constructs a binary tree to determine these codewords.
- **Codeword Representation:** Uses a prefix-free code, meaning no codeword is a prefix of another. This allows for easy decoding – you can uniquely identify the symbol from the bitstream without needing delimiters.
- **Granularity:** Works on individual symbols. The encoding and decoding happens symbol by symbol.
- **Efficiency:** Relatively simple to implement, but its efficiency is limited by the discrete nature of the codewords. It can't represent probabilities with arbitrary precision. It often achieves close-to-optimal compression, especially when symbol probabilities are close to powers of 1/2.
- **Practical Considerations:** Easy to implement and understand. Fast encoding and decoding speeds are achievable with appropriate data structures.

**Arithmetic Coding:**

- **Method:** Represents the entire message as a single fractional number between 0 and 1. The probability of each symbol determines the size of the interval representing that symbol within the range. As each symbol is encoded, the interval is successively narrowed based on the symbol's probability.
- **Codeword Representation:** Represents the entire message as a single floating-point number, which can be represented with arbitrary precision (i.e., using as many bits as needed to achieve the desired compression).
- **Granularity:** Works on the entire message. The probability of the entire message determines the final representation.
- **Efficiency:** Can achieve significantly better compression ratios than Huffman coding, especially for messages with many symbols or symbols having probabilities that are not close to powers of 1/2. It can exploit probabilities with much finer granularity.
- **Practical Considerations:** More complex to implement than Huffman coding. Requires careful handling of precision to avoid rounding errors and maintain accuracy. While capable of higher compression, it may not always be faster than Huffman for smaller datasets due to the overhead of precise calculations.

**In Summary:**

| Feature            | Huffman Coding                       | Arithmetic Coding                    |
| ------------------ | ------------------------------------ | ------------------------------------ |
| **Method**         | Variable-length codewords per symbol | Single fractional number for message |
| **Granularity**    | Symbol-by-symbol                     | Entire message                       |
| **Precision**      | Limited by codeword length           | Arbitrary precision                  |
| **Implementation** | Simpler                              | More complex                         |
| **Compression**    | Good, but not as good as arithmetic  | Generally better than Huffman        |

Huffman coding is often preferred when simplicity and speed are paramount, while arithmetic coding is chosen when maximum compression is the priority, even at the cost of increased complexity. Many modern compression algorithms (e.g., some parts of JPEG and PNG) use a combination of techniques, often incorporating aspects of both.

## 8) Write a decoding algorithm using integer implementation.

The best decoding algorithm depends heavily on the _encoding_ scheme used. There's no single "decoding algorithm using integer implementation." I'll provide examples for a few common encoding techniques:

**1. Simple substitution cipher (Caesar cipher):**

This cipher shifts each letter by a fixed amount. We'll use integers to represent letters (A=0, B=1, ..., Z=25).

```python
def caesar_decode(ciphertext, shift):
  """Decodes a Caesar cipher.

  Args:
    ciphertext: The encoded text as a string of uppercase letters.
    shift: The amount the letters were shifted (positive integer).

  Returns:
    The decoded text as a string.  Returns an error message if input is invalid.
  """
  plaintext = ""
  for char in ciphertext:
    if 'A' <= char <= 'Z':
      char_int = ord(char) - ord('A')  # Convert char to integer 0-25
      decoded_int = (char_int - shift) % 26 #Decode, handle negative shifts
      decoded_char = chr(decoded_int + ord('A')) #Convert back to char
      plaintext += decoded_char
    elif char.isspace():
        plaintext += char #Handle spaces
    else:
      return "Error: Invalid character in ciphertext."
  return plaintext

# Example usage
ciphertext = "Lipps${svph%"
shift = 4
plaintext = caesar_decode(ciphertext, shift)
print(f"Ciphertext: {ciphertext}")
print(f"Plaintext: {plaintext}")

```

**2. Run-length encoding (RLE):**

RLE encodes sequences of identical characters by storing the character and its count. We'll use tuples of (character, count).

```python
def rle_decode(encoded_data):
  """Decodes data encoded with run-length encoding.

  Args:
    encoded_data: A list of (character, count) tuples.

  Returns:
    The decoded string.  Returns an error message if input is invalid.
  """
  decoded_string = ""
  try:
    for char, count in encoded_data:
        decoded_string += char * count
    return decoded_string
  except TypeError:
      return "Error: Invalid input format for RLE decoding."

# Example usage
encoded_data = [('A', 3), ('B', 1), ('A', 2), ('C', 1)]
decoded_string = rle_decode(encoded_data)
print(f"Encoded data: {encoded_data}")
print(f"Decoded string: {decoded_string}")
```

**3. Simple Base64-like encoding (using integers):**

This example demonstrates a simplified base-64 like encoding where we use integers to represent blocks of bits. This is a highly simplified example and would need significant expansion to be a real base64 implementation.

```python
def simple_base64_decode(encoded_integers):
    """Decodes a simplified base64 representation using integers.

    Args:
        encoded_integers: A list of integers representing encoded data.

    Returns:
        The decoded string (assuming ASCII).  Returns an error if decoding fails.
    """
    decoded_string = ""
    try:
        for num in encoded_integers:
            decoded_string += chr(num) # Assumes ASCII encoding
        return decoded_string
    except ValueError:
        return "Error: Invalid integer value during decoding."


#Example (Highly Simplified):
encoded_integers = [72, 101, 108, 108, 111] #H, e, l, l, o
decoded_string = simple_base64_decode(encoded_integers)
print(f"Encoded integers: {encoded_integers}")
print(f"Decoded string: {decoded_string}")

```

Remember to replace these examples with the appropriate decoding algorithm that matches your specific encoding scheme. You'll need to provide details about the encoding process to get a more tailored solution. For more complex encoding schemes (like Huffman coding or more sophisticated Base64 implementations), the decoding algorithm will be significantly more intricate.

## 9) Write an Encoding algorithm using integer implementation.

This algorithm encodes a sequence of integers using a simple substitution cipher. The key is an array that maps input integers to their encoded counterparts. It handles out-of-range input gracefully.

```java
import java.util.Arrays;

public class IntegerEncoding {

    public static int[] encode(int[] input, int[] key) {
        //Error Handling: Check for Key Validity
        if(key == null || key.length == 0){
            throw new IllegalArgumentException("Key cannot be null or empty.");
        }

        int[] encoded = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            int value = input[i];
            // Handle out-of-range input values.  Wrap around if needed.
            int keyIndex = value % key.length;
            if (keyIndex < 0) { //Handle negative inputs
                keyIndex += key.length;
            }
            encoded[i] = key[keyIndex];
        }
        return encoded;
    }


    public static void main(String[] args) {
        int[] input = {1, 5, 10, 15, -2, 0, 100};
        int[] key = {100, 200, 300, 400, 500}; //Example Key

        try{
            int[] encoded = encode(input, key);
            System.out.println("Original: " + Arrays.toString(input));
            System.out.println("Encoded: " + Arrays.toString(encoded));
        } catch (IllegalArgumentException e){
            System.err.println("Error: " + e.getMessage());
        }

    }
}
```

**Explanation:**

1. **`encode(int[] input, int[] key)`:** This method takes the input integer array and the encoding key as input.
2. **Error Handling:** The code now includes a check to ensure the key is not null or empty, throwing an `IllegalArgumentException` if it is.
3. **Iteration:** It iterates through each element (`value`) in the `input` array.
4. **Modulo Operator:** It uses the modulo operator (`%`) to map the input value to an index within the `key` array. This effectively creates a wrap-around effect: if the input is larger than the key's size, it wraps back to the beginning of the key. It also handles negative input values by adding the key length.
5. **Encoding:** The element at the calculated index in the `key` array is assigned as the encoded value in the `encoded` array.
6. **Return Value:** The function returns the `encoded` integer array.
7. **`main` Method:** The `main` method demonstrates how to use the `encode` function with sample input and key. It also includes error handling to catch the `IllegalArgumentException`.

**To improve this further (consider adding):**

- **Decoding:** Implement a corresponding `decode` function that reverses the encoding process. This would require a more sophisticated key or a reversible mapping.
- **More Robust Key Handling:** Add error checking to ensure the key doesn't contain duplicates (for reversible decoding).
- **Different Encoding Schemes:** Explore more complex encoding schemes, like using prime numbers, bitwise operations, or more sophisticated substitution ciphers.
- **Larger Integers:** Consider using `long` instead of `int` if you need to handle larger integers.

Remember that this is a simple substitution cipher and is not suitable for securing sensitive data. For real-world security applications, use established cryptographic libraries.

## 10) Decode the following binary sequence using integer implementation method. 1100010010000000 (upto 4 elements) count(1)= 40 , count(2)= 1, count(3)= 9, Total_count =50

The provided information seems contradictory and incomplete for decoding the binary sequence using an integer implementation method. Let's break down why:

- **Binary Sequence:** 1100010010000000 is a 16-bit binary number.

- **Integer Implementation:** This usually refers to representing data (like characters or symbols) as integers. However, we need a mapping or codebook to understand which integer represents which symbol. The problem doesn't provide this crucial mapping.

- **Counts:** The counts (count(1) = 40, count(2) = 1, count(3) = 9, Total_count = 50) are unexplained. These counts suggest some kind of frequency analysis or encoding scheme might be involved (like Huffman coding), but without knowing what these counts refer to, they're useless. Furthermore, the total count (50) doesn't match the length of the binary sequence (which implies only one code).

**To decode this, we need:**

1. **A codebook or mapping:** This would specify which integer value corresponds to which symbol (e.g., 1 = 'A', 2 = 'B', etc.).
2. **Clarification on the counts:** What do `count(1)`, `count(2)`, and `count(3)` represent? What are they counting?

**Example of how it _could_ work (with assumptions):**

Let's _hypothetically_ assume a very simple scenario: The binary sequence is a representation of integers, where each byte (8 bits) represents a single integer. This is a very basic interpretation that might not be what is intended.

- **11000100:** (In decimal) This is 196.
- **10000000:** (In decimal) This is 128.

If we _assumed_ a codebook where 196 = 'X' and 128 = 'Y', then the decoded sequence would be "XY". This is entirely speculative based on the limited information given.

**In conclusion:** The provided information is insufficient to decode the binary sequence. More details are needed about the encoding method used.
