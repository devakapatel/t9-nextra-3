# Unit 4

## <mark> 1) Show the comparisons that naïve string matcher makes for the pattern p=0001 in the text T=000010001010001. </mark>

To demonstrate the comparisons made by the naïve string matcher for the pattern $$ p = 0001 $$ in the text $$ T = 000010001010001 $$, we will simulate the matching process step-by-step.

#### Naïve String Matching Algorithm

The naïve string matching algorithm checks for the presence of a pattern in a text by comparing the pattern with substrings of the text. It starts at each position in the text and checks if the subsequent characters match the pattern.

#### Text and Pattern

- Pattern (p): `0001`
- Text (T): `000010001010001`

#### Lengths

- Length of pattern $$ |p| = 4 $$
- Length of text $$ |T| = 15 $$

#### Comparisons Made

The algorithm will attempt to match the pattern at each possible starting position in the text where it can fit. The starting positions for matching are from index 0 to index $$ |T| - |p| $$ (i.e., from index 0 to index 11).

#### Step-by-Step Comparison

1. Starting at index 0:
   - Compare `T` (0) with `p` (0) → Match
   - Compare `T[1]` (0) with `p[1]` (0) → Match
   - Compare `T[2]` (0) with `p[2]` (0) → Match
   - Compare `T` (1) with `p` (1) → Match
   - Result: Match found at index 0.
2. Starting at index 1:
   - Compare `T[1]` (0) with `p` (0) → Match
   - Compare `T[2]` (0) with `p[1]` (0) → Match
   - Compare `T` (0) with `p[2]` (0) → Match
   - Compare `T` (1) with `p` (1) → Match
   - Result: Match found at index 1.
3. Starting at index 2:
   - Compare `T[2]` (0) with `p` (0) → Match
   - Compare `T` (0) with `p[1]` (0) → Match
   - Compare `T` (0) with `p[2]` (0) → Match
   - Compare `T` (1) with `p` (1) → Match
   - Result: Match found at index 2.
4. Starting at index 3:
   - Compare `T` (0) with `p` (0) → No match.
   - Result: No match found.
5. Starting at index 4:
   - Compare `T` (1) with `p` (0) → No match.
   - Result: No match found.
6. Starting at index 5:
   - Compare `T` (0) with `p` (0) → Match
   - Compare `T` (0) with `p[1]` (0) → Match
   - Compare `T` (1) with `p[2]` (0) → No match.
   - Result: No match found.
7. Starting at index 6:
   - Compare `T` (0) with `p` (0) → Match
   - Compare `T` (1) with `p[1]` (0) → No match.
   - Result: No match found.
8. Starting at index 7:
   - Compare `T` (1) with `p` (0) → No match.
   - Result: No match found.
9. Starting at index 8:
   - Compare `T` (0) with `p` (0) → Match
   - Compare `T` (1) with `p[1]` (0) → No match.
   - Result: No match found.
10. Starting at index 9:
    - Compare `T` (1) with `p` (0) → No match.
    - Result: No match found.
11. Starting at index 10:
    - Compare `T` (0) with `p` (0) → Match
    - Compare `T` (0) with `p[1]` (0) → Match
    - Compare `T` (1) with `p[2]` (0) → No match.
    - Result: No match found.
12. Starting at index 11:
    - Compare `T`( 1 )with p [0](https://www.notion.so/nexaskore/0) →No match.
    - Result: No match found.

#### Summary of Comparisons

- Matches Found:
  - At indices: (Index 0, Index 1, Index 2).
- Total Comparisons Made:
  - At each starting position, up to four comparisons were made, leading to a total of approximately $$4 \times n$$, where $$n$$ is the length of the text minus the length of the pattern plus one.

#### Conclusion

The naïve string matcher checks every possible starting position in the text for a potential match against the pattern, making it straightforward but potentially inefficient for large texts or patterns due to its high number of comparisons. In this example, it successfully identified multiple matches for the pattern "0001" within the text "000010001010001".

## <mark> 2) Write Naïve sting matching algorithm. Find its time complexity and perform sting matching for given pattern P = “ACD” Text T = “CACDACAACDAC” </mark>

#### Naïve String Matching Algorithm

Definition: The naïve string matching algorithm checks for the presence of a pattern in a text by comparing the pattern with every possible substring of the text. It is a straightforward approach but can be inefficient for large texts.

#### Algorithm Steps

1. Input: A pattern $$ P $$ of length $$ m $$ and a text $$ T $$ of length $$ n $$.
2. For each possible starting position $$ i $$ in the text (from 0 to $$ n - m $$):
   - Compare the substring of $$ T $$ starting at $$ i $$ with the pattern $$ P $$.
   - If all characters match, report the position $$ i $$ as a match.
3. Output: The starting index of all occurrences of the pattern in the text.

#### Pseudocode

```
function naiveStringMatch(T, P):
    n = length(T)
    m = length(P)

    for i from 0 to n - m:
        match = true
        for j from 0 to m - 1:
            if T[i + j] != P[j]:
                match = false
                break
        if match:
            print("Pattern found at index:", i)

```

#### Time Complexity

- Best Case: $$ O(n) $$ when there are no matches and the algorithm only checks up to the first character of the pattern.
- Worst Case: $$ O(nm) $$ when every character in the text is checked against every character in the pattern, such as when the text and pattern have many similar characters.
- Average Case: Still approximated as $$ O(nm) $$, depending on the distribution of characters.

#### Example: String Matching for Pattern P = "ACD" in Text T = "CACDACAACDAC"

1. Pattern (P): "ACD"
2. Text (T): "CACDACAACDAC"

#### Step-by-Step Matching

- Length of Pattern $$ m = 3 $$
- Length of Text $$ n = 12 $$

#### Iteration through Text:

1. Starting at index 0:
   - Compare T (C) with P (A): No match.
2. Starting at index 1:
   - Compare T[1] (A) with P (A): Match.
   - Compare T[2] (C) with P[1] (C): Match.
   - Compare T (D) with P[2] (D): Match.
   - Result: Match found at index 1.
3. Starting at index 2:
   - Compare T[2] (C) with P (A): No match.
4. Starting at index 3:
   - Compare T (D) with P (A): No match.
5. Starting at index 4:
   - Compare T (A) with P (A): Match.
   - Compare T (C) with P[1] (C): Match.
   - Compare T (D) with P[2] (D): Match.
   - Result: Match found at index 4.
6. Starting at index 5:
   - Compare T (C) with P (A): No match.
7. Starting at index 6:
   - Compare T (A) with P (A): Match.
   - Compare T (C) with P[1] (C): Match.
   - Compare T (D) with P[2] (D): Match.
   - Result: Match found at index 6.
8. Starting at index 7:
   - Compare T (C) with P (A): No match.
9. Starting at index 8:
   - Compare T (A) with P (A): Match.
   - Compare T (C) with P[1] (C): Match.
   - Compare T (D) with P[2] (D): Match.
   - Result: Match found at index 8.
10. Starting at index 9:
    - Compare T (C) with P (A): No match.
11. Starting at index 10:
    - Compare T (D) with P (A): No match.

#### Summary of Results

- Matches Found At Indices:
  - Index 1
  - Index 4
  - Index 6
  - Index 8

#### Conclusion

The naïve string matching algorithm is simple but can be inefficient for larger texts or patterns due to its time complexity of $$ O(nm) $$. In this example, it successfully identified multiple occurrences of the pattern "ACD" within the text "CACDACAACDAC".

## <mark> 3) Explain spurious hits in Rabin-Karp string matching algorithm with example. Working modulo q=13, how many spurious hits does the Rabin-Karp matcher encounter in the text T = 2359023141526739921 when looking for the pattern P = 31415? </mark>

#### Rabin-Karp String Matching Algorithm

The Rabin-Karp algorithm is a string matching algorithm that uses hashing to find any one of a set of pattern strings in a text. It is particularly efficient for searching multiple patterns at once. The key idea is to compute a hash value for the pattern and for each substring of the text, and then compare these hash values.

#### Spurious Hits

Definition: A spurious hit occurs when the hash value of a substring in the text matches the hash value of the pattern, but the actual substring does not match the pattern. This can happen due to hash collisions, where two different strings produce the same hash value.

#### Example of Spurious Hits in Rabin-Karp

Let's illustrate this concept with the given pattern and text.

1. Pattern (P): `31415`
2. Text (T): `2359023141526739921`
3. Modulo (q): `13`

#### Step-by-Step Calculation

#### Step 1: Hash Function

We will use a simple polynomial rolling hash function defined as:

$$
\text{hash}(S) = \sum_{i=0}^{m-1} S[i] \cdot d^{m-1-i} \mod q
$$

Where:

- $$ S[i] $$ is the character at position $$ i $$.
- $$ d $$ is a constant base (commonly chosen as 10 for decimal digits).
- $$ m $$ is the length of the pattern.

For our example:

- $$ d = 10 $$
- Length of pattern $$ m = 5 $$

#### Step 2: Calculate Hash Values

1. Hash of Pattern P (`31415`):
   - Convert characters to integers: $$ 3, 1, 4, 1, 5 $$
   - Calculate hash:
     $$
     \text{hash}(P) = (3 \cdot 10^4 + 1 \cdot 10^3 + 4 \cdot 10^2 + 1 \cdot 10^1 + 5) \mod 13
     $$
     $$
     = (30000 + 1000 + 400 + 10 + 5) \mod 13
     $$
     $$
     = (31415) \mod 13 = 9
     $$
2. Calculate Hashes for Substrings in T:

Now we will calculate the rolling hashes for each substring of length $$ m = 5 $$ in $$ T = 2359023141526739921 $$.

- Substring `23590`:
  $$
  \text{hash} = (2 \cdot 10^4 + 3 \cdot 10^3 + 5 \cdot 10^2 + 9 \cdot 10^1 + 0) \mod 13
  = (20000 + 3000 + 500 + 90) \mod 13
  = (23590) \mod 13 = 8
  $$
- Substring `35902`:
  $$
  \text{hash} = (3 \cdot 10^4 + 5 \cdot 10^3 + 9 \cdot 10^2 + 0 \cdot 10^1 + 2) \mod 13
  = (30000 + 5000 +900+0+2) \mod 13
  = (35902) \mod 13 = 6
  $$
- Substring `59023`:
  $$
  \text{hash} = (5 \cdot 10^4 +9\cdot10^3+0\cdot10^2+2\cdot10^1+3)\mod13
  = (50000+9000+0+20+3)\mod13
  = (59023)\mod13=11
  $$
- Substring `90231`:
  $$
  \text{hash} = (9\cdot10^4+0\cdot10^3+2\cdot10^2+3\cdot10^1+1)\mod13
  = (90000+0+200+30+1)\mod13
  = (90231)\mod13=12
  $$
- Substring `02314`:
  $$
  \text{hash} = (0\cdot10^4+2\cdot10^3+3\cdot10^2+1\cdot10^1+4)\mod13
  = (0+2000+300+10+4)\mod13
  = (02314)\mod13=8
  $$
- Substring `23141`:
  $$
  \text{hash} = (2\cdot10^4+3\cdot10^3+1\cdot10^2+4\cdot10^1+1)\mod13
  = (20000+3000+100+40+1)\mod13
  = (23141)\mod13=9
  $$
- Substring `31415`:
  $$
  \text{hash} = (3\cdot10^4+1\cdot10^3+4\cdot10^2+1\cdot10^1+5)\mod13
  = (30000 +1000 +400 +40 +5)\mod13
  = (31415)\mod13=9
  $$
- Substring `14152`:
  $$
  \text{hash} = (1\cdot10^4 +4\cdot10^3 +1\cdot10^2 +5\cdot10^1 +2)\mod13
  = (10000 +4000 +100 +50 +2)\mod13
  = (14152)\mod13=8
  $$
- Substring `41526`:
  $$
  \text{hash} = (4\cdot10^4 +1\cdot10^3 +5\cdot10^2 +2\cdot10^1 +6)\mod13
  = (40000 +1000 +500 +20 +6)\mod13
  = (41526)\mod13=12
  $$
- Substring `15267`:
  $$
  \text{hash} = (1\cdot10^4 +5\cdot10^3 +2\cdot10^2 +6\cdot10^1 +7)\mod13
  = (10000 +5000 +200 +60 +7)\mod13
  = (15267)\mod13=6
  $$
- Substring `52673`:
  $$
  \text{hash} = (5\cdot10^4 +2\cdot10^3 +6\cdot10^2 +7\cdot10^1 )/ mod(13)
  =(50000+2000+600+70)/ mod(13)
  =(52673)/ mod(13)=11
  $$
- Substring `26739`:
  $$
  hash=(2*10000)+(6*1000)+(7*100)+(3*20)+(9)/ mod(13)
  =(20000)+(6000)+(700)+(60)+(9)/ mod(13)
  =(26739)/ mod(13)=12
  $$
- Substring `67399`:
  $$
  hash=(6*10000)+(7*1000)+(3*100)+(9*20)+9/ mod(13)
  =(60000)+(7000)+(300)+(180)+(9)/ mod(13)
  =(67399)/ mod(13)=8.
  $$

#### Summary of Hash Values and Matches Found:

| Substring | Hash Value | Matches Pattern? |
| --------- | ---------- | ---------------- |
| CACD      | -          | No               |
| ACD       | -          | Yes              |
| CAD       | -          | No               |
| DCA       | -          | No               |
| CAD       | -          | No               |
| ACD       | -          | Yes              |
| DCA       | -          | No               |

#### Spurious Hits Calculation:

In this example, we can see that there are two actual matches for the pattern "31415" in the text "CACDACAACDAC". The spurious hits would occur when a substring has the same hash value as "31415" but does not match it when compared character by character.

#### Conclusion:

The Rabin-Karp algorithm efficiently finds occurrences of a pattern within a text using hashing. However, it may encounter spurious hits due to hash collisions, which are false positives that require further verification through direct comparison. In this case, while checking against the pattern "31415", we found actual matches at positions where their hashes matched but also had to check against substrings that resulted in spurious hits.

## <mark> 4) Working module q = 11, how many spurious hits does the Rabin-Karp matcher encounter in the text T= 3141592653589793 when looking for the pattern P=26? </mark>

To determine how many spurious hits the Rabin-Karp matcher encounters while searching for the pattern $$ P = 26 $$ in the text $$ T = 3141592653589793 $$ using modulo $$ q = 11 $$, we will follow the steps of the Rabin-Karp algorithm.

#### Step 1: Hash Function

We will use a simple polynomial rolling hash function defined as:

$$
\text{hash}(S) = \sum_{i=0}^{m-1} S[i] \cdot d^{m-1-i} \mod q
$$

Where:

- $$ S[i] $$ is the character at position $$ i $$.
- $$ d $$ is a constant base (commonly chosen as 10 for decimal digits).
- $$ m $$ is the length of the pattern.

For our example:

- Pattern (P): `26`
- Text (T): `3141592653589793`
- Modulo (q): `11`
- Base (d): `10`

#### Step 2: Calculate Hash Values

1. Hash of Pattern P (`26`):
   - Convert characters to integers: $$ 2, 6 $$
   - Calculate hash:
     $$
     \text{hash}(P) = (2 \cdot 10^1 + 6) \mod 11
     $$
     $$
     = (20 + 6) \mod 11 = 26 \mod 11 = 4
     $$
2. Calculate Hashes for Substrings in T:

Now we will calculate the rolling hashes for each substring of length $$ m = 2 $$ in $$ T = 3141592653589793 $$.

#### Substring Hash Calculations

- Substring `31`:
  $$
  \text{hash} = (3 \cdot 10^1 + 1) \mod 11 = (30 + 1) \mod 11 = 31 \mod 11 = 9
  $$
- Substring `14`:
  $$
  \text{hash} = (1 \cdot 10^1 + 4) \mod 11 = (10 + 4) \mod 11 = 14 \mod 11 = 3
  $$
- Substring `41`:
  $$
  \text{hash} = (4 \cdot 10^1 + 1) \mod 11 = (40 + 1) \mod 11 = 41 \mod 11 = 8
  $$
- Substring `15`:
  $$
  \text{hash} = (1 \cdot 10^1 + 5) \mod 11 = (10 + 5) \mod 11 = 15 \mod 11 = 4
  $$
- Substring `59`:
  $$
  \text{hash} = (5 \cdot 10^1 + 9) \mod 11 = (50 + 9) \mod 11 = 59 \mod 11 = 4
  $$
- Substring `92`:
  $$
  \text{hash} = (9 \cdot 10^1 + 2) \mod 11 = (90 + 2) \mod 11 = 92 \mod 11 = 4
  $$
- Substring `26`:
  $$
  \text{hash} = (2 \cdot 10^1 +6 )\mod(11)= (20+6)\mod(11)=26\mod(11)=4
  $$
- Substring `63`:
  $$
  \text{hash} =(6\cdot10^1+3)\mod(11)= (60+3)\mod(11)=63\mod(11)=8
  $$
- Substring `35`:
  $$
  \text{hash} =(3\cdot10^1+5)\mod(11)= (30+5)\mod(11)=35\mod(11)=2
  $$
- Substring `58`:
  $$
  \text{hash} =(5\cdot10^1+8)\mod(11)= (50+8)\mod(11)=58\mod(11)=3
  $$
- Substring `79`:
  $$
  \text{hash} =(7\cdot10^1+9)\mod(11)= (70+9)\mod(11)=79\mod(11)=2
  $$

#### Summary of Hash Values and Matches Found:

| Substring | Hash Value | Matches Pattern? |
| --------- | ---------- | ---------------- |
| `31`      | `9`        | No               |
| `14`      | `3`        | No               |
| `41`      | `8`        | No               |
| `15`      | `4`        | Yes              |
| `59`      | `4`        | Yes              |
| `92`      | `4`        | Yes              |
| `26`      | `4`        | Yes              |
| `63`      | `8`        | No               |
| `35`      | `2`        | No               |
| `58`      | `3`        | No               |
| `79`      | `2`        | No               |

#### Spurious Hits Calculation:

In this case, we found that substrings "15", "59", "92", and "26" all produced a hash value of 4, which matches the hash value of the pattern "26". However, only "26" is an actual match.

Thus, we have:

- Spurious Hits:
  - Substrings "15", "59", and "92" are spurious hits because they share the same hash value as the pattern but do not match it when compared directly.

#### Conclusion:

The Rabin-Karp algorithm can encounter spurious hits due to hash collisions. In this example, there were three spurious hits ("15", "59", and "92") while looking for the pattern "26" in the text "3141592653589793".

## <mark> 5) Define Finite Automata? Explain its use for string matching with illustration. </mark>

#### Finite Automata

Definition: A finite automaton (or finite state machine) is a theoretical computational model used to represent and control execution flow. It consists of a finite number of states, transitions between those states, an initial state, and one or more accepting states. Finite automata can be classified into two types:

- Deterministic Finite Automaton (DFA): For each state and input symbol, there is exactly one transition to a next state.
- Nondeterministic Finite Automaton (NFA): For each state and input symbol, there can be multiple possible transitions, including transitions without consuming any input (epsilon transitions).

#### Use of Finite Automata for String Matching

Finite automata are widely used in string matching algorithms due to their ability to efficiently process input strings and determine whether they match a given pattern.

#### Steps Involved in String Matching Using Finite Automata

1. Constructing the Finite Automaton:
   - For a given pattern, construct a finite automaton that recognizes the pattern. This automaton will have states corresponding to the progress made in matching the pattern.
2. Processing the Input Text:
   - The automaton processes the input text symbol by symbol, transitioning between states according to the defined transitions.
3. Accepting States:
   - If the automaton reaches an accepting state after processing the input text, it indicates that the pattern has been found in the text.

#### Illustration

Let's illustrate this with an example.

#### Example Pattern and Text

- Pattern (P): `ab`
- Text (T): `abcabc`

#### Step 1: Constructing the Finite Automaton

For the pattern `ab`, we can construct a DFA as follows:

- States:
  - State 0: Start state
  - State 1: After reading `a`
  - State 2: After reading `ab` (accepting state)
- Transitions:
  - From State 0:
    - On input `a`, go to State 1.
    - On any other input (like `b` or `c`), stay in State 0.
  - From State 1:
    - On input `b`, go to State 2 (accepting state).
    - On input `a`, stay in State 1.
    - On any other input, go back to State 0.
  - From State 2 (accepting):
    - On any input (`a`, `b`, or `c`), transition back to State 0.

#### Transition Table

| Current State | Input | Next State |
| ------------- | ----- | ---------- |
| 0             | a     | 1          |
| 0             | b     | 0          |
| 0             | c     | 0          |
| 1             | a     | 1          |
| 1             | b     | 2          |
| 1             | c     | 0          |
| 2             | a     | 1          |
| 2             | b     | 0          |
| 2             | c     | 0          |

#### Step 2: Processing the Input Text

Now we process the text `abcabc` using the constructed DFA:

- Start at State 0.

1. Read `a`: Transition to State 1.
2. Read `b`: Transition to State 2 (accepting state).
3. Read `c`: Transition back to State 0.
4. Read `a`: Transition to State 1.
5. Read `b`: Transition to State 2 (accepting state).
6. Read `c`: Transition back to State 0.

#### Result

The DFA reaches an accepting state after reading both occurrences of the pattern "ab" in the text "abcabc". Therefore, the pattern is found at indices:

- Starting index 0 for the first occurrence.
- Starting index 3 for the second occurrence.

#### Conclusion

Finite automata provide an efficient method for string matching by constructing a model that recognizes patterns based on defined states and transitions. The DFA processes the input text in linear time relative to its length, making it suitable for applications such as lexical analysis in compilers and searching within texts.

## <mark> 6) Compare NP-Hard with NP-Complete problems. </mark>

#### Comparison of NP-Hard and NP-Complete Problems

NP-Hard Problems:

- Definition: NP-Hard problems are at least as hard as the hardest problems in NP (nondeterministic polynomial time). A problem is classified as NP-Hard if every problem in NP can be reduced to it in polynomial time. However, NP-Hard problems do not have to be in NP themselves, meaning they may not have a solution verifiable in polynomial time.
- Examples:
  - Traveling Salesman Problem (TSP)
  - Knapsack Problem
  - Hamiltonian Cycle Problem
- Characteristics:
  - There is no known polynomial-time algorithm to solve NP-Hard problems.
  - They can be decision problems, optimization problems, or search problems.

NP-Complete Problems:

- Definition: NP-Complete problems are a subset of NP problems that are both in NP and NP-Hard. A problem is classified as NP-Complete if it is in NP and every problem in NP can be reduced to it in polynomial time. Essentially, if any NP-Complete problem can be solved in polynomial time, then all problems in NP can also be solved in polynomial time.
- Examples:
  - Boolean Satisfiability Problem (SAT)
  - Vertex Cover Problem
  - Subset Sum Problem
- Characteristics:
  - They are decision problems with solutions that can be verified in polynomial time.
  - Finding a polynomial-time algorithm for any single NP-Complete problem would imply P = NP.

#### Key Differences

| Feature      | NP-Hard                                                                | NP-Complete                                                                                         |
| ------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Definition   | At least as hard as the hardest problems in NP; not necessarily in NP. | A subset of NP; both in NP and NP-Hard.                                                             |
| Verification | Solutions may not be verifiable in polynomial time.                    | Solutions can be verified in polynomial time.                                                       |
| Reduction    | Every problem in NP can be reduced to it.                              | Every problem in NP can be reduced to it, and it can also be reduced to other NP-Complete problems. |
| Examples     | TSP, Knapsack Problem                                                  | SAT, Vertex Cover                                                                                   |

#### Conclusion

In summary, while both NP-Hard and NP-Complete problems represent significant challenges in computational theory, they differ fundamentally in their definitions and characteristics. Understanding these differences is crucial for tackling complex algorithmic problems and determining the feasibility of finding efficient solutions.

## <mark> 7) Explain P and NP Problems giving examples. </mark>

#### P and NP Problems

P Problems:

- Definition: The class P consists of decision problems that can be solved by a deterministic Turing machine in polynomial time. In simpler terms, these are problems for which an algorithm exists that can find a solution in a time that scales polynomially with the input size.
- Examples:
  - Sorting Algorithms: Sorting a list of numbers (e.g., using Quick Sort or Merge Sort) is in P because these algorithms run in polynomial time.
  - Finding the Greatest Common Divisor (GCD): The Euclidean algorithm for finding the GCD of two integers operates in polynomial time.
  - Graph Traversal: Problems like Breadth-First Search (BFS) and Depth-First Search (DFS) for traversing graphs are also in P.

NP Problems:

- Definition: The class NP consists of decision problems for which a solution can be verified by a deterministic Turing machine in polynomial time. This means that if you are given a "yes" instance of the problem, you can check whether it is indeed a "yes" instance quickly (in polynomial time).
- Examples:
  - Boolean Satisfiability Problem (SAT): Given a Boolean formula, determining if there exists an assignment of variables that makes the formula true is in NP. If you have an assignment, you can easily verify its correctness.
  - Subset Sum Problem: Given a set of integers and a target sum, determining if any subset of the integers adds up to the target sum is in NP. If you provide a subset, you can quickly check if it sums to the target.
  - Traveling Salesman Problem (Decision Version): Given a set of cities and distances between them, determining if there exists a tour that visits each city exactly once with total distance less than or equal to a specified value is in NP.

#### Summary

In summary, P problems are those that can be solved efficiently (in polynomial time), while NP problems are those for which solutions can be verified efficiently. Understanding these classes is crucial for exploring computational complexity and algorithm design.

## <mark> 8) Write a short note on NP-Completeness Problem. </mark>

#### NP-Completeness Problem

Definition: NP-Completeness is a classification of decision problems in computational complexity theory. A problem is considered NP-Complete if it meets two criteria:

1. It is in NP, meaning that given a solution, it can be verified in polynomial time.
2. Every problem in NP can be reduced to it in polynomial time, which implies that it is at least as hard as the hardest problems in NP.

Significance: The significance of NP-Completeness lies in its implications for algorithm design and computational theory. If any NP-Complete problem can be solved in polynomial time, then all problems in NP can also be solved in polynomial time (this would imply P = NP). Conversely, if it can be proven that even one NP-Complete problem cannot be solved in polynomial time, it would imply that P ≠ NP.

Examples of NP-Complete Problems:

- Boolean Satisfiability Problem (SAT): The first problem proven to be NP-Complete. It asks whether there exists an assignment of variables that makes a given Boolean formula true.
- Traveling Salesman Problem (Decision Version): Given a set of cities and distances, the problem asks if there exists a tour that visits each city once with a total distance less than or equal to a specified value.
- Vertex Cover Problem: Given a graph and an integer k, the problem asks whether there exists a subset of vertices of size k such that every edge in the graph is incident to at least one vertex from this subset.

#### Conclusion

NP-Completeness plays a crucial role in understanding the limits of efficient computation. It helps researchers identify problems that are inherently difficult and guides the development of approximation algorithms and heuristics for practical applications where exact solutions are computationally infeasible.

## <mark> 9) Write a brief note on NP-Hard Problems. </mark>

#### NP-Hard Problems

Definition: NP-Hard problems are a class of problems that are at least as hard as the hardest problems in NP (nondeterministic polynomial time). A problem is classified as NP-Hard if every problem in NP can be reduced to it in polynomial time. Unlike NP-Complete problems, NP-Hard problems do not have to be decision problems; they can be optimization problems or search problems.

Characteristics:

- No Known Polynomial-Time Solutions: There is no known algorithm that can solve all NP-Hard problems in polynomial time.
- Not Necessarily in NP: NP-Hard problems may not have solutions that can be verified in polynomial time, meaning they might not even belong to the class NP.

Examples:

- Traveling Salesman Problem (TSP): Finding the shortest possible route that visits each city exactly once and returns to the origin city.
- Knapsack Problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- Hamiltonian Cycle Problem: Determining whether there exists a cycle in a graph that visits each vertex exactly once.

#### Conclusion

NP-Hard problems are significant in computational complexity theory because they represent some of the most challenging problems in computer science. Understanding their properties helps researchers develop approximation algorithms and heuristics for practical applications where exact solutions are computationally infeasible.

## <mark> 10) Define P, NP, NP Complete And NP-Hard problems. </mark>

#### Definitions of P, NP, NP-Complete, and NP-Hard Problems

P Problems:

- Definition: The class P consists of decision problems that can be solved by a deterministic Turing machine in polynomial time. In simpler terms, these are problems for which an algorithm exists that can find a solution in a time that scales polynomially with the input size.
- Example: Sorting a list of numbers or finding the greatest common divisor (GCD) using the Euclidean algorithm.

NP Problems:

- Definition: The class NP consists of decision problems for which a solution can be verified by a deterministic Turing machine in polynomial time. This means that if you are given a "yes" instance of the problem, you can check whether it is indeed a "yes" instance quickly (in polynomial time).
- Example: The Boolean satisfiability problem (SAT), where given a Boolean formula, determining if there exists an assignment of variables that makes the formula true.

NP-Complete Problems:

- Definition: NP-Complete problems are a subset of NP problems that are both in NP and NP-Hard. A problem is classified as NP-Complete if it is in NP and every problem in NP can be reduced to it in polynomial time. If any NP-Complete problem can be solved in polynomial time, then all problems in NP can also be solved in polynomial time.
- Example: The Traveling Salesman Problem (decision version), where given a set of cities and distances between them, determining if there exists a tour that visits each city exactly once with total distance less than or equal to a specified value.

NP-Hard Problems:

- Definition: NP-Hard problems are at least as hard as the hardest problems in NP. A problem is classified as NP-Hard if every problem in NP can be reduced to it in polynomial time. However, NP-Hard problems do not have to be in NP themselves, meaning they may not have a solution verifiable in polynomial time.
- Example: The Knapsack Problem and the Hamiltonian Cycle Problem.

#### Summary Table

| Class       | Definition                                                                                            | Example                                       |
| ----------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| P           | Problems solvable in polynomial time by a deterministic Turing machine.                               | Sorting algorithms (e.g., Quick Sort)         |
| NP          | Problems verifiable in polynomial time by a deterministic Turing machine.                             | Boolean Satisfiability Problem (SAT)          |
| NP-Complete | Problems that are both in NP and as hard as any problem in NP; if one can be solved quickly, all can. | Traveling Salesman Problem (decision version) |
| NP-Hard     | Problems at least as hard as the hardest problems in NP; may not be verifiable in polynomial time.    | Knapsack Problem                              |

These classifications help us understand the complexities involved in algorithm design and computational theory, guiding researchers and practitioners on how to approach various computational problems.
