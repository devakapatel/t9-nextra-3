# Unit 1

# _Check for correctness of answers._

## 1) What is data compression? Why is it used?

Data compression is the process of reducing the size of a data file or data stream without significant loss of information. This is achieved by identifying and eliminating redundancy in the data. The compressed data can then be restored to its original form (decompressed) using a corresponding decompression algorithm.

Data compression is used for a multitude of reasons, including:

- **Reduced storage space:** Smaller files require less storage capacity on hard drives, SSDs, cloud storage, etc. This is particularly crucial when dealing with large datasets like videos, images, and databases.

- **Faster transmission speeds:** Smaller files transmit faster over networks, leading to improved download speeds, reduced latency, and better user experience, especially important for streaming services and online gaming.

- **Reduced bandwidth costs:** Smaller files consume less bandwidth, leading to lower costs for internet service providers and users, particularly beneficial for mobile devices with limited data plans.

- **Improved efficiency:** Compression can make data processing more efficient, as smaller files require less processing power and memory.

- **Data archiving:** Compression can help reduce the amount of storage space needed for archival data, making long-term storage more cost-effective.

- **Data backup:** Compressed backups take up less space and can be created and restored more quickly.

In short, data compression is a crucial technique for managing and efficiently utilizing data resources in today's digital world. It improves storage, transmission, and overall efficiency in numerous applications.

## 2) Explain the types of data compression.

Data compression techniques are broadly classified into two main categories: lossless and lossy. The choice between them depends on the type of data and the acceptable level of information loss.

**1. Lossless Compression:**

Lossless compression algorithms reduce file size without discarding any data. This means the original data can be perfectly reconstructed from the compressed file. They're ideal for situations where data integrity is paramount, such as text files, source code, and spreadsheets. Examples include:

- **Run-Length Encoding (RLE):** Replaces repeating sequences of data with a single instance of the data and the count of repetitions. Effective for images with large areas of the same color.

- **Huffman Coding:** Assigns shorter codes to frequently occurring data and longer codes to less frequent data, thereby reducing the average code length. Used in many file formats like JPEG and PNG (though PNG uses it in conjunction with other techniques).

- **Lempel-Ziv (LZ) algorithms:** Identify repeating patterns within the data and replace them with references to previously seen patterns. Variations include LZ77, LZ78, and LZW (used in GIF). These are very effective for text and other compressible data.

- **Arithmetic Coding:** Represents the data as a single fractional number representing the probability of the data sequence. Generally more efficient than Huffman coding, but computationally more expensive.

- **Dictionary-based compression:** Builds a dictionary of frequently occurring sequences and replaces them with pointers to the dictionary. DEFLATE (used in ZIP, gzip, PNG) is a common example which combines LZ77 and Huffman coding.

**2. Lossy Compression:**

Lossy compression algorithms reduce file size by discarding some data deemed less important or imperceptible. This results in smaller file sizes but at the cost of some information loss. The original data cannot be perfectly reconstructed. It's suitable for applications where a slight degradation in quality is acceptable in exchange for significant size reduction, such as images, audio, and video. Examples include:

- **JPEG (Joint Photographic Experts Group):** Uses Discrete Cosine Transform (DCT) to represent image data in the frequency domain and then quantizes the coefficients, discarding high-frequency components that contribute less to the perceived image quality.

- **MPEG (Moving Picture Experts Group):** A family of standards for compressing video and audio, often employing techniques like motion compensation and DCT. Different MPEG versions offer varying levels of compression and quality.

- **MP3 (MPEG Audio Layer III):** Uses perceptual coding to discard audio frequencies that are less likely to be perceived by the human ear, resulting in significantly smaller file sizes.

- **AAC (Advanced Audio Coding):** A more modern audio compression format than MP3, often providing better quality at the same bitrate.

- **WebP:** A modern image format that supports both lossy and lossless compression and often provides better compression than JPEG or PNG.

In summary, the choice between lossless and lossy compression depends on the specific application and the trade-off between file size and data integrity. Lossless is preferred when preserving the original data is crucial, while lossy is suitable for multimedia applications where some data loss is acceptable. Some formats even use a hybrid approach, employing both lossy and lossless techniques for different components of the data.

## 3) Define a two-state Markov model for binary images with an example.

A two-state Markov model for binary images assumes that each pixel's state (0 or 1, representing black or white, for instance) depends only on the state of the preceding pixel in a specified direction (e.g., horizontally). The "memory" extends only one pixel back. This is a first-order Markov model.

The model is defined by a transition probability matrix:

```
     State 0   State 1
State 0 |  P(0|0)   P(1|0) |
State 1 |  P(0|1)   P(1|1) |
```

- **P(0|0):** Probability of a pixel being 0 (black), given the previous pixel was 0.
- **P(1|0):** Probability of a pixel being 1 (white), given the previous pixel was 0.
- **P(0|1):** Probability of a pixel being 0 (black), given the previous pixel was 1.
- **P(1|1):** Probability of a pixel being 1 (white), given the previous pixel was 1.

The rows must sum to 1 (because the next pixel _must_ be either 0 or 1).

**Example:**

Let's consider a simple model for a horizontally scanned binary image representing a roughly striped pattern. We might estimate the transition probabilities as follows:

```
     State 0   State 1
State 0 |  0.8     0.2   |
State 1 |  0.3     0.7   |
```

This means:

- If a pixel is black (0), there's an 80% chance the next pixel will also be black, and a 20% chance it will be white.
- If a pixel is white (1), there's a 30% chance the next pixel will be black, and a 70% chance it will be white.

**Image Example:**

Let's say we have a small image: `1 0 0 1 1 0`

Using our model, the likelihood of this sequence is calculated as follows:

- **Start:** We need to assume a starting state. Let's assume the first pixel (1) is given.
- **1 -> 0:** P(0|1) = 0.3
- **0 -> 0:** P(0|0) = 0.8
- **0 -> 1:** P(1|0) = 0.2
- **1 -> 1:** P(1|1) = 0.7
- **1 -> 0:** P(0|1) = 0.3

The overall likelihood of this sequence, given our model, is 0.3 _ 0.8 _ 0.2 _ 0.7 _ 0.3 = 0.01008. This is a low likelihood, suggesting that the sequence is not very likely given our model's assumed tendencies. A sequence like `1 1 1 1 1 0` would have a much higher likelihood, reflecting our model's bias towards white pixels following white pixels.

This example demonstrates a simple two-state Markov model for binary images. More complex models could consider larger neighborhoods (second-order or higher Markov models) or incorporate more sophisticated dependencies. The key is the conditional probability defining the transition between states.

## 4) Explain physical model, composite source model and probability modeling.

Let's break down each of these modeling approaches:

**1. Physical Model:**

A physical model represents a system using physical components and their interactions. It's a scaled-down or simplified version of the real-world system, often built to mimic its behavior. The goal is to understand how the system works by observing the model's response to different inputs or conditions.

- **Characteristics:**

  - **Tangible representation:** The model is a physical object you can see and interact with.
  - **Direct analogy:** The model's components directly represent the components of the real system.
  - **Empirical observation:** Understanding comes from observing the model's behavior.
  - **Limitations:** Can be expensive, time-consuming to build, and may not perfectly capture all aspects of the real system. Scale limitations can also impact accuracy.

- **Examples:**
  - **Wind tunnel model of an airplane:** Tests aerodynamic properties.
  - **Scale model of a building:** Used to study structural integrity and wind resistance.
  - **Hydraulic model of a river system:** Simulates flood behavior.
  - **A miniature circuit board:** Representing a larger, more complex circuit.

**2. Composite Source Model:**

A composite source model, often used in environmental science or epidemiology, represents a complex phenomenon as a combination of simpler, identifiable sources. It aims to determine the relative contributions of each source to the overall effect. The "sources" can be anything contributing to the phenomenon, whether it's pollution, disease spread, or something else.

- **Characteristics:**

  - **Decomposition:** Breaks down a complex system into simpler, manageable sources.
  - **Source apportionment:** Determines the contribution of each source to the overall outcome.
  - **Data-driven:** Relies heavily on measurements and data analysis to quantify source contributions. Often involves statistical methods like receptor modeling.
  - **Uncertainty:** Acknowledges inherent uncertainties in identifying and quantifying individual source contributions.

- **Examples:**
  - **Air pollution modeling:** Identifying the contributions of traffic, industry, and natural sources to particulate matter levels.
  - **Disease outbreak investigation:** Tracing the sources of infection (e.g., contaminated food, water, or person-to-person contact).
  - **Estimating the sources of nutrient runoff into a lake:** Identifying agricultural fields, sewage treatment plants, and urban areas as contributors.

**3. Probability Modeling:**

Probability modeling uses mathematical tools to describe the likelihood of different outcomes in a system. It doesn't attempt to perfectly replicate the system's behavior but instead provides a framework for understanding the uncertainty and variability inherent in it.

- **Characteristics:**

  - **Stochastic nature:** Accounts for randomness and uncertainty.
  - **Statistical methods:** Employs probability distributions, statistical inference, and simulation techniques.
  - **Prediction and risk assessment:** Used to predict the probability of future events and assess risks.
  - **Abstraction:** Simplifies the system by focusing on key variables and their probabilistic relationships.

- **Examples:**
  - **Predicting weather:** Using probability to estimate the chance of rain or snow.
  - **Financial modeling:** Assessing the risk of investment portfolios.
  - **Queueing theory:** Modeling waiting times in systems like call centers.
  - **Epidemiological modeling:** Predicting the spread of infectious diseases.
  - **Reliability engineering:** Estimating the probability of equipment failure.

In summary, these three modeling approaches differ significantly in their methods and goals. Physical models offer a tangible representation, composite source models focus on decomposing complex systems into simpler sources, and probability models utilize statistical tools to handle uncertainty and predict outcomes. The best choice of model depends on the specific problem and the available data and resources.

## 5) Explain Huffman coding in detail with an example. Define minimum variance Huffman code.

## Huffman Coding Explained

Huffman coding is a lossless data compression algorithm. It works by assigning variable-length codes to characters based on their frequency of occurrence in the input text. More frequent characters get shorter codes, while less frequent characters get longer codes. This results in a shorter overall encoded message compared to fixed-length coding (like ASCII).

**How it works:**

1. **Frequency Analysis:** The algorithm first analyzes the input text to determine the frequency of each character.

2. **Tree Construction:** A binary tree is built based on character frequencies.

   - Start with each character as a leaf node, each having a weight equal to its frequency.
   - Repeatedly combine the two nodes with the lowest weights into a new parent node. The weight of the parent node is the sum of the weights of its children. This process continues until only one node (the root) remains.

3. **Code Assignment:** Codes are assigned to each character by traversing the tree from the root to the leaf node representing the character. A '0' is assigned for a left branch and a '1' for a right branch. The sequence of 0s and 1s along the path forms the Huffman code for that character.

**Example:**

Let's consider the following text: "this is a test string"

1. **Frequency Analysis:**

   - t: 3
   - i: 2
   - s: 3
   - h: 1
   - a: 1
   - e: 1
   - r: 1
   - n: 1
   - g: 1
   - : 2 (space)

2. **Tree Construction:**

   The steps are as follows, showing the weights in parenthesis:

   - Start with individual nodes: (3)t, (2)i, (3)s, (1)h, (1)a, (1)e, (1)r, (1)n, (1)g, (2)
   - Combine 'h', 'a', 'e', 'r', 'n', 'g' (all with frequency 1): (6) [h,a,e,r,n,g]
   - Combine (2)i and (2) : (4) [i, ]
   - Combine (6) [h,a,e,r,n,g] and (4)[i, ] : (10) [[h,a,e,r,n,g], [i,]]
   - Combine (3)t and (3)s: (6) [t,s]
   - Combine (10) [[h,a,e,r,n,g], [i,]] and (6)[t,s]: (16) [[[h,a,e,r,n,g], [i,]], [t,s]]

3. **Code Assignment:**

   Traversing the tree:

   - t: 00
   - s: 01
   - i: 100
   - : 101
   - h: 11000
   - a: 11001
   - e: 11010
   - r: 11011
   - n: 11100
   - g: 11101

4. **Encoding:**

The string "this is a test string" becomes: `001001011000101 00010011010100010101 110010110000101`

**Minimum Variance Huffman Code:**

A minimum variance Huffman code is not a standard term or a specific variation of the Huffman coding algorithm. The standard Huffman coding algorithm aims to minimize the _average_ code length, not the variance. There is no inherent goal to minimize the _variance_ of code lengths in the standard approach. Modifying the algorithm to minimize variance would require a different objective function during the tree construction. You'd have to define what exactly 'minimum variance' means in the context of the code lengths and then adjust the algorithm accordingly – for instance, by using a different merging criteria in the tree building phase. This is not a trivial modification and has no generally accepted implementation.

## 6) Encode “acadebaa” using adaptive Huffman coding. Derive code and final tree.

Let's encode "acadebaa" using adaptive Huffman coding. Adaptive Huffman coding means the tree changes dynamically as we process each symbol. We'll use a method where we start with a single node for each symbol and build the tree as we go.

**Initialization:**

We begin with no tree. Each symbol ('a', 'c', 'd', 'b', 'e') has its own single-node tree. We'll keep track of the frequency of each symbol.

**Encoding Steps:**

1. **'a':** Frequency count: a=1. We encode 'a' with the code '0'. The tree remains a single node for 'a'.

2. **'c':** Frequency count: a=1, c=1. 'c' gets '10'. The tree is now:

```
   *
  / \
 a   c
```

3. **'a':** Frequency count: a=2, c=1. 'a' gets '0'. (We re-order to reflect frequency). The tree becomes:

```
    *
   / \
  a   *
     / \
    c   - (Empty Node)
```

4. **'d':** Frequency count: a=2, c=1, d=1. 'd' gets '110'. The tree becomes:

```
      *
     / \
    a   *
       / \
      *   -
     / \
    c   d
```

5. **'e':** Frequency count: a=2, c=1, d=1, e=1. 'e' gets '111'. The tree is:

```
        *
       / \
      a   *
         / \
        *   *
       / \   |
      c   d  e
```

6. **'b':** Frequency count: a=2, c=1, d=1, e=1, b=1. 'b' gets '100'. Note that the tree gets restructured again to reflect the updated frequencies. It's important to consider the frequency of each symbol after each update. The structure may vary slightly depending on the implementation of the algorithm used to ensure minimum weighted path length.

7. **'a':** Frequency count: a=3, c=1, d=1, e=1, b=1. 'a' gets '0'. The tree gets a further restructure based on frequency.

**Final Tree (approximate, as the precise shape depends on your specific algorithm):** The exact final tree might vary slightly depending on the tie-breaking rules used during the Huffman tree construction, but it will reflect the final frequencies (a=3, c=1, d=1, e=1, b=1). This is an example:

```
        *
       / \
      a   *
         / \
        *   *
       / \   \
      *   e   *
     / \     / \
    c   d   b   -
```

**Encoded String:**

The encoded string, based on our encoding steps and the evolving tree, is: `010001101111000`

**Important Note:** The exact code assigned to each symbol and the final tree shape might vary slightly depending on the specific adaptive Huffman coding algorithm implementation. Different algorithms might handle the merging of nodes with equal frequencies differently. The process described above demonstrates the general principle. A proper implementation would require a more formal algorithm to manage the dynamic tree updates efficiently.

## 7) Write the difference between lossless compression and lossy compression.

The key difference between lossless and lossy compression lies in whether information is lost during the compression process:

**Lossless Compression:**

- **Reversible:** This type of compression allows you to perfectly reconstruct the original data after decompression. No information is lost.
- **Smaller compression ratios:** Generally achieves smaller compression ratios than lossy compression because it must retain all data.
- **Suitable for:** Data where preserving every bit of information is critical, such as text files, source code, spreadsheets, and databases. Loss of even a single bit could render the data unusable.

**Lossy Compression:**

- **Irreversible:** Some information is discarded during compression to achieve higher compression ratios. The decompressed data is an approximation of the original, not an exact copy.
- **Higher compression ratios:** Achieves significantly higher compression ratios than lossless compression because it throws away data deemed less important.
- **Suitable for:** Data where some loss of fidelity is acceptable, such as images, audio, and video. The human eye and ear are not sensitive enough to notice the minor differences introduced by lossy compression in many cases. This allows for much smaller file sizes.

**In short:** Lossless compression is like perfectly packing a suitcase—everything goes in, and everything comes out exactly as it was. Lossy compression is like packing only the essentials, leaving some items behind to save space. The contents might be less complete but the suitcase is much smaller.

## 8) What is a measure of performance in a data compression algorithm? Explain it all.

The primary measure of performance in a data compression algorithm is its **compression ratio**, but other factors are also crucial. Let's break down the key metrics:

**1. Compression Ratio:**

This is the most fundamental metric. It represents the degree to which the algorithm reduces the size of the data. It's calculated as:

**Compression Ratio = (Original Data Size) / (Compressed Data Size)**

A higher compression ratio indicates better performance. For example:

- A ratio of 2:1 means the compressed data is half the size of the original.
- A ratio of 10:1 means the compressed data is one-tenth the size of the original.

However, the compression ratio alone isn't sufficient to evaluate an algorithm completely.

**2. Compression Speed (Encoding Time):**

How quickly the algorithm compresses the data is important. A high compression ratio is useless if it takes an unreasonably long time to achieve. This speed is usually measured in terms of:

- **Time taken to compress:** Measured in seconds, milliseconds, etc., depending on the size of the data.
- **Throughput:** Measured in bits per second or bytes per second, representing the rate at which data is processed.

**3. Decompression Speed (Decoding Time):**

Similarly, the speed at which the compressed data can be restored to its original form is crucial, especially in real-time applications. Metrics are similar to compression speed: time taken and throughput.

**4. Compression Efficiency (considering lossy vs. lossless):**

This depends on whether the algorithm is _lossless_ or _lossy_:

- **Lossless Compression:** The original data can be perfectly reconstructed from the compressed data. The focus here is maximizing the compression ratio without any data loss. Examples include ZIP, gzip, and FLAC.

- **Lossy Compression:** Some data is lost during compression to achieve higher compression ratios. The acceptable level of data loss depends heavily on the application. Examples include JPEG (images), MP3 (audio), and MPEG (video). For lossy algorithms, metrics like:
  - **Signal-to-noise ratio (SNR):** Measures the ratio of signal power to noise power, indicating the quality of the reconstructed data. A higher SNR implies better quality.
  - **Perceptual quality metrics:** Assess the perceived quality of reconstructed data (audio or video) based on human perception, often using subjective evaluations (e.g., Mean Opinion Score - MOS).

**5. Computational Complexity:**

The computational resources (CPU time and memory) required by the algorithm are important considerations, especially for large datasets. This is often expressed in terms of Big O notation (e.g., O(n), O(n log n)).

**6. Code Size:**

The size of the compression algorithm itself might matter, particularly in resource-constrained environments (e.g., embedded systems).

**In summary:** Choosing the best data compression algorithm involves a trade-off between these factors. A superior algorithm might not always have the highest compression ratio but could offer a better balance between compression ratio, speed, and resource usage depending on the specific application's needs.

## 9) Write the difference between static and dynamic compression.

The difference between static and dynamic compression lies primarily in _when_ the compression occurs and how it affects the data:

**Static Compression:**

- **When it happens:** Compression is performed _once_ on the original data. The resulting compressed file is then stored and used without further compression.
- **How it works:** It analyzes the entire data set to find patterns and redundancies _before_ compression. The algorithm determines the best way to represent the data using fewer bits based on this analysis.
- **Characteristics:**
  - **Faster decompression:** Because the compression is already done, decompression is typically faster.
  - **Larger compressed file size (potentially):** If the data changes frequently, a statically compressed file might be larger than a dynamically compressed one because it can't adapt to new patterns.
  - **Suitable for:** Archiving files that don't change frequently, such as images, documents, or software installations. Examples include ZIP, RAR, 7z.

**Dynamic Compression:**

- **When it happens:** Compression is performed _on-the-fly_ as the data is being generated or transmitted.
- **How it works:** It compresses data in smaller chunks or blocks. It often uses algorithms that adapt to the characteristics of the data stream as it changes.
- **Characteristics:**
  - **Slower decompression:** Decompression requires real-time processing of the data.
  - **Smaller compressed file size (potentially):** Adapting to the data stream can lead to better compression, especially for data with changing patterns.
  - **Suitable for:** Streaming data, network communications, and applications where the data changes frequently. Examples include DEFLATE (used in gzip and zlib), Lempel-Ziv algorithms.

**In short:** Static compression is a one-time process optimized for a fixed dataset, while dynamic compression is a continuous process adapting to a changing data stream. The best choice depends on the specific application and the nature of the data.
