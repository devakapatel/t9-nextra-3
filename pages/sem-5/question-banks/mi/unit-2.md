# Unit 2

## 1) Explain Addressing Modes of 8086 Processor with an example.

### Addressing Modes of the 8086 Processor

The **8086 microprocessor** supports several addressing modes, which determine how the operands of instructions are accessed. These modes allow programmers to specify the location of data in memory or registers, providing flexibility and efficiency in programming.

#### Types of Addressing Modes

Here are the primary addressing modes used in the 8086 architecture:

1. **Register Addressing Mode**
    - **Description**: The operand is located in a register. This mode provides fast access since no memory access is required.
    - **Example**:
        
        ```nasm
        MOV AX, BX  ; Move the contents of register BX into register AX
        ```
        
2. **Immediate Addressing Mode**
    - **Description**: The operand is specified directly in the instruction itself as a constant value.
    - **Example**:
        
        ```nasm
        MOV AX, 5   ; Move the immediate value 5 into register AX
        ```
        
3. **Direct Addressing Mode**
    - **Description**: The effective address of the operand is given explicitly in the instruction.
    - **Example**:
        
        ```nasm
        MOV AX, [1234H]  ; Move the contents of memory location 1234H into AX
        ```
        
4. **Indirect Addressing Mode**
    - **Description**: The effective address of the operand is specified indirectly through a register.
    - **Example**:
        
        ```nasm
        MOV AX, [SI]  ; Move the contents of memory location pointed to by SI into AX
        ```
        
5. **Based Addressing Mode**
    - **Description**: Combines a base register (like BX or BP) with a displacement to form the effective address.
    - **Example**:
        
        ```nasm
        MOV AX, [BX + 10]  ; Move the contents of memory location (BX + 10) into AX
        ```
        
6. **Indexed Addressing Mode**
    - **Description**: Combines an index register (like SI or DI) with a displacement to form the effective address.
    - **Example**:
        
        ```nasm
        MOV AX, [SI + 5]  ; Move the contents of memory location (SI + 5) into AX
        ```
        
7. **Based Indexed Addressing Mode**
    - **Description**: Combines both a base register and an index register with an optional displacement.
    - **Example**:
        
        ```nasm
        MOV AX, [BX + SI]  ; Move the contents of memory location (BX + SI) into AX
        ```
        

#### Example of Addressing Modes

Let’s illustrate these addressing modes with an example:

Assume we have the following data stored in memory:

- Memory Location `1000H`: `34H`
- Memory Location `1001H`: `12H`
- Register `BX`: `1000H`
- Register `SI`: `0001H`

Here’s how each addressing mode would access these values:

1. **Register Addressing Mode**:
    
    ```nasm
    MOV AL, BL      ; AL = BL (register to register)
    ```
    
2. **Immediate Addressing Mode**:
    
    ```nasm
    MOV AL, 34H    ; AL = 34H (immediate value)
    ```
    
3. **Direct Addressing Mode**:
    
    ```nasm
    MOV AL, [1000H]; AL = Memory[1000H] = 34H (direct memory access)
    ```
    
4. **Indirect Addressing Mode**:
    
    ```nasm
    MOV AL, [BX];  ; AL = Memory[BX] = Memory[1000H] = 34H (indirect access through BX)
    ```
    
5. **Based Addressing Mode**:
    
    ```nasm
    MOV AL, [BX + 1]; // AL = Memory[1000H + 1] = Memory[1001H] = 12H (based addressing)
    ```
    
6. **Indexed Addressing Mode**:
    
    ```nasm
    MOV AL, [SI];    // AL = Memory[0 + SI] = Memory[0001H] = 12H (indexed access)
    ```
    
7. **Based Indexed Addressing Mode**:
    
    ```nasm
    MOV AL, [BX + SI]; // AL = Memory[1000H + 0001H] = Memory[1001H] = 12H (combined base and index)
    ```
    

#### Conclusion

The addressing modes of the 8086 microprocessor provide flexibility in accessing data stored in registers and memory. By allowing various ways to specify operands, these modes enhance programming capabilities and optimize performance for different applications. Understanding these addressing modes is essential for effective assembly language programming on the 8086 architecture.

## 2) Discuss all the instructions of the 8086 microprocessor.

The 8086 microprocessor has a rich instruction set that allows it to perform a wide variety of operations. Below is a comprehensive overview of the instructions categorized by their functionality.

#### 1. Data Transfer Instructions

These instructions are used to transfer data from one location to another.

- **MOV**: Transfers data from source to destination.
    - Example: `MOV AX, BX` (Move contents of BX into AX)
- **PUSH**: Pushes data onto the stack.
    - Example: `PUSH AX` (Push contents of AX onto the stack)
- **POP**: Pops data from the stack into a register.
    - Example: `POP BX` (Pop the top of the stack into BX)
- **XCHG**: Exchanges data between two operands.
    - Example: `XCHG AX, BX` (Exchange contents of AX and BX)
- **IN**: Reads data from an I/O port.
    - Example: `IN AL, 60H` (Read byte from port 60H into AL)
- **OUT**: Sends data to an I/O port.
    - Example: `OUT 60H, AL` (Send byte in AL to port 60H)

#### 2. Arithmetic Instructions

These instructions perform arithmetic operations.

- **ADD**: Adds two operands.
    - Example: `ADD AX, BX` (Add BX to AX)
- **SUB**: Subtracts one operand from another.
    - Example: `SUB AX, 5` (Subtract 5 from AX)
- **MUL**: Unsigned multiplication of two operands.
    - Example: `MUL BL` (Multiply AX by BL)
- **IMUL**: Signed multiplication of two operands.
    - Example: `IMUL BL` (Signed multiply AX by BL)
- **DIV**: Unsigned division.
    - Example: `DIV BL` (Divide AX by BL)
- **IDIV**: Signed division.
    - Example: `IDIV BL` (Signed divide AX by BL)
- **INC**: Increments an operand by one.
    - Example: `INC AX` (Increment AX by 1)
- **DEC**: Decrements an operand by one.
    - Example: `DEC BX` (Decrement BX by 1)

#### 3. Logical Instructions

These instructions perform logical operations on operands.

- **AND**: Performs bitwise AND operation.
    - Example: `AND AL, 0Fh`
- **OR**: Performs bitwise OR operation.
    - Example: `OR AL, 0Fh`
- **XOR**: Performs bitwise XOR operation.
    - Example: `XOR AL, BL`
- **NOT**: Performs bitwise NOT operation.
    - Example: `NOT AL`

#### 4. Control Flow Instructions

These instructions control the flow of execution in a program.

- **JMP**: Unconditional jump to a specified address.
    - Example: `JMP LABEL`
- **CALL**: Calls a procedure or subroutine.
    - Example: `CALL SUBROUTINE`
- **RET**: Returns from a procedure or subroutine.
    - Example: `RET`
- **INT**: Generates a software interrupt.
    - Example: `INT 21H`
- **IRET**: Returns from an interrupt service routine.
    - Example: `IRET`

#### 5. String Instructions

These instructions operate on strings of data.

- **MOVS**: Moves string data from source to destination.
- **CMPS**: Compares two strings.
- **SCAS**: Scans a string for a specified value.
- **LODS**: Loads a string into the accumulator.
- **STOS**: Stores the accumulator into a string.

#### 6. Bit Manipulation Instructions

These instructions manipulate bits directly.

- **SHL/SAL**: Shift left arithmetic/logic.
- **SHR**: Shift right arithmetic/logic.
- **ROR**/RORC/RCL/RCR*: Rotate bits left/right with or without carry.

#### Examples of Instructions

Here are some examples demonstrating how these instructions can be used:

```nasm
; Data Transfer
MOV AX, [DATA]    ; Move data from memory location DATA into AX
PUSH CX           ; Push CX onto the stack

; Arithmetic Operations
ADD AX, BX        ; Add contents of BX to AX
SUB DX, 1         ; Subtracts 1 from DX

; Logical Operations
AND AL, 0Fh       ; Perform AND operation with AL and immediate value
OR BL, CL         ; Perform OR operation between BL and CL

; Control Flow
JMP START         ; Jump to label START
CALL FUNCTION      ; Call subroutine FUNCTION

; String Operations
MOVS              ; Move string from DS:[SI] to ES:[DI]
```

#### Conclusion

The instruction set of the **8086 microprocessor** is extensive and provides various functionalities for data manipulation, arithmetic operations, logical operations, control flow management, and string processing. Understanding these instructions is essential for programming in assembly language and effectively utilizing the capabilities of the microprocessor.

## 3) Assembler directives:
- EVEN
- OFFSET
- ASSUME
- END
- ENDS
- DUP
- PTR
- DW, DB, DQ, DT

Here are explanations of the 8086 assembly language directives you mentioned:

### EVEN

- Aligns the next item in the program to an even byte boundary in memory.
- Pads with a NOP instruction if necessary to achieve even alignment.
- Useful for ensuring word or double word alignment.

### OFFSET

- Returns the offset part of a memory address expression.
- Used to get the offset of a label or variable from the start of its segment.

### ASSUME

- Specifies the segment registers that point to the current code, data, extra and stack segments.
- Allows the assembler to generate correct segment override prefixes for memory references.

### END

- Marks the physical end of the assembly language source file.
- Any code or data after END will be ignored by the assembler.

### ENDS

- Marks the end of a named segment definition.
- Used in conjunction with the SEGMENT directive to define custom segments.

### DUP

- Duplicates an expression a specified number of times.
- Allows easily defining arrays or blocks of memory in a compact way.
- For example: `ARRAY DB 10 DUP(0)` defines a 10-byte array initialized to 0.

### PTR

- Explicitly specifies the type of a memory operand.
- Overrides the default type assumed by the assembler.
- For example: `MOV AX, WORD PTR [BX]` forces a word access.

### DW, DB, DQ, DT

- Directives to define initialized data in memory.
- DW - Define Word (16 bits)
- DB - Define Byte (8 bits)
- DQ - Define Quadword (32 bits)
- DT - Define Tenbytes (80 bits)
- For example: `BUFFER DB 'HELLO', 0AH, 0DH`

In summary, these directives provide the assembler with additional information about memory alignment, addressing, and data definition to facilitate generating the correct machine code. They are an essential part of 8086 assembly language programming.

## 4) Write a program to transfer a given string from one location to another.

Here's a simple assembly language program that transfers a given string from one location to another in memory using the 8086 microprocessor assembly language.

#### Program to Transfer a String

This program will copy a string from one memory location to another using the `MOVS` instruction, which is designed for string operations.

#### Program Code

```nasm
.model small          ; Define the memory model
.data                 ; Data segment
sourceString db 'Hello, World!', '$' ; Source string with a terminator
destinationString db 20 dup(0)        ; Destination string initialized to 20 bytes of 0s

.code                 ; Code segment
main:
    mov ax, @data     ; Load data segment address into AX
    mov ds, ax        ; Initialize DS register

    lea si, sourceString   ; Load address of source string into SI
    lea di, destinationString ; Load address of destination string into DI

    mov cx, 13         ; Set CX to the length of the string (13 characters)
    rep movsb          ; Repeat MOVSB (move byte from DS:SI to ES:DI)

    ; Terminate program (if running in DOS)
    mov ax, 4C00h     ; DOS terminate program function
    int 21h           ; Call DOS interrupt

end main              ; End of the program
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies the small memory model, meaning that both code and data fit within a single segment.
2. **Data Segment**:
    - `sourceString db 'Hello, World!', '$'`: Defines a string in memory that ends with a `$` character as a terminator.
    - `destinationString db 20 dup(0)`: Allocates space for the destination string initialized with zeros.
3. **Code Segment**:
    - The `main` label marks the beginning of the code.
    - `mov ax, @data` and `mov ds, ax`: Initializes the data segment register (DS) with the address of the data segment.
    - `lea si, sourceString`: Loads the effective address of `sourceString` into the Source Index register (SI).
    - `lea di, destinationString`: Loads the effective address of `destinationString` into the Destination Index register (DI).
    - `mov cx, 13`: Sets up the counter register (CX) with the number of bytes to copy (length of "Hello, World!").
    - `rep movsb`: Repeats the move byte instruction until CX reaches zero. This instruction copies bytes from the address pointed to by DS:SI to ES:DI.
4. **Program Termination**:
    - The program uses DOS interrupt `int 21h` with function code `4C00h` to terminate cleanly.

#### Conclusion

This simple assembly program demonstrates how to transfer a string from one memory location to another using basic instructions and registers in the 8086 microprocessor. The use of string instructions like `MOVSB` makes it efficient and straightforward to manipulate strings in assembly language.

## 5) Write a program to find if a given number is even or odd.

Here is a simple assembly language program for the 8086 microprocessor that checks if a given number is even or odd. The program prompts the user to enter a number, reads the input, and then determines whether the number is even or odd by checking the least significant bit.

#### Program to Check Even or Odd

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt db 'Enter a number: $' ; Prompt message
evenMsg db 'The number is even.$' ; Message for even number
oddMsg db 'The number is odd.$'   ; Message for odd number
number db ?            ; Variable to store the input number

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Display prompt message
    mov ah, 09h        ; Function to display string
    lea dx, prompt     ; Load address of prompt message
    int 21h            ; Call DOS interrupt

    ; Read a character from keyboard
    mov ah, 01h        ; Function to read character
    int 21h            ; Call DOS interrupt
    sub al, '0'        ; Convert ASCII to integer (assuming single digit)
    mov number, al     ; Store the number

    ; Check if the number is even or odd
    mov al, number     ; Move the number into AL register
    and al, 01h        ; AND with 1 to check LSB

    cmp al, 0          ; Compare result with 0
    je even            ; If zero (even), jump to even label

odd:
    ; Display odd message
    mov ah, 09h        ; Function to display string
    lea dx, oddMsg     ; Load address of odd message
    int 21h            ; Call DOS interrupt
    jmp endProgram      ; Jump to end of program

even:
    ; Display even message
    mov ah, 09h        ; Function to display string
    lea dx, evenMsg     ; Load address of even message
    int 21h            ; Call DOS interrupt

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition

```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt`: A string that prompts the user to enter a number.
    - `evenMsg` and `oddMsg`: Messages indicating whether the entered number is even or odd.
    - `number`: A variable to store the input number.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays a prompt message using DOS interrupt `int 21h`.
    - It reads a single character input from the keyboard and converts it from ASCII to an integer by subtracting `'0'`.
    - The program checks if the entered number is even or odd by performing a bitwise AND operation with `1`. If the least significant bit (LSB) is `0`, it means the number is even; otherwise, it is odd.
    - Depending on whether the result is zero or not, it displays either the "even" or "odd" message.
    - Finally, it terminates using another DOS interrupt.

#### Conclusion

This simple assembly language program demonstrates how to check if a given number is even or odd using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for interaction with users.

## 6) Write a program to find if a given number is positive or negative.

Here’s a simple assembly language program for the 8086 microprocessor that checks if a given number is positive or negative. The program prompts the user to enter a number, reads the input, and then determines whether the number is positive or negative by checking the sign bit.

#### Program to Check if a Number is Positive or Negative

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt db 'Enter a number (0-255): $' ; Prompt message
posMsg db 'The number is positive.$'    ; Message for positive number
negMsg db 'The number is negative.$'    ; Message for negative number
number db ?            ; Variable to store the input number

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Display prompt message
    mov ah, 09h        ; Function to display string
    lea dx, prompt     ; Load address of prompt message
    int 21h            ; Call DOS interrupt

    ; Read a character from keyboard
    mov ah, 01h        ; Function to read character
    int 21h            ; Call DOS interrupt
    sub al, '0'        ; Convert ASCII to integer (assuming single digit)
    mov number, al     ; Store the number

    ; Check if the number is positive or negative
    mov al, number     ; Move the number into AL register

    cmp al, 0          ; Compare AL with 0
    jge positive        ; If greater or equal (positive), jump to positive label

negative:
    ; Display negative message
    mov ah, 09h        ; Function to display string
    lea dx, negMsg     ; Load address of negative message
    int 21h            ; Call DOS interrupt
    jmp endProgram      ; Jump to end of program

positive:
    ; Display positive message
    mov ah, 09h        ; Function to display string
    lea dx, posMsg     ; Load address of positive message
    int 21h            ; Call DOS interrupt

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition

```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt`: A string that prompts the user to enter a number.
    - `posMsg` and `negMsg`: Messages indicating whether the entered number is positive or negative.
    - `number`: A variable to store the input number.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays a prompt message using DOS interrupt `int 21h`.
    - It reads a single character input from the keyboard and converts it from ASCII to an integer by subtracting `'0'`.
    - The program checks if the entered number is positive or negative by comparing it with zero. If it is greater than or equal to zero, it jumps to the "positive" label; otherwise, it goes to "negative."
    - Depending on whether the result is zero or not, it displays either the "positive" or "negative" message.
    - Finally, it terminates using another DOS interrupt.

#### Conclusion

This simple assembly language program demonstrates how to check if a given number is positive or negative using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for interaction with users.

## 7) Write a program to find the factorial of a number.

Here’s a simple assembly language program for the 8086 microprocessor that calculates the factorial of a given number. The program uses a loop to multiply the numbers from 1 up to the given number.

#### Program to Calculate Factorial

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt db 'Enter a number (0-9): $' ; Prompt message
resultMsg db 'Factorial is: $'        ; Message for result
number db ?            ; Variable to store the input number
factorial db 1        ; Variable to store the factorial result (1 is the initial value)

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Display prompt message
    mov ah, 09h        ; Function to display string
    lea dx, prompt     ; Load address of prompt message
    int 21h            ; Call DOS interrupt

    ; Read a character from keyboard
    mov ah, 01h        ; Function to read character
    int 21h            ; Call DOS interrupt
    sub al, '0'        ; Convert ASCII to integer (assuming single digit)
    mov number, al     ; Store the number

    ; Check if number is 0 (factorial of 0 is 1)
    cmp al, 0          ; Compare AL with 0
    je printResult      ; If equal, jump to print result

    ; Calculate factorial using a loop
    mov cl, number     ; Move the number into CL (loop counter)

factorial_loop:
    mul cl             ; Multiply AL by CL (AL = AL * CL)
    dec cl             ; Decrement CL by 1
    jnz factorial_loop  ; Repeat until CL is zero

printResult:
    ; Display result message
    mov ah, 09h        ; Function to display string
    lea dx, resultMsg  ; Load address of result message
    int 21h            ; Call DOS interrupt

    ; Convert factorial result to ASCII for display
    add ax, '0'        ; Convert result in AX to ASCII by adding '0'

    mov dl, al         ; Move result into DL for printing
    mov ah, 02h        ; Function to display character in DL
    int 21h            ; Call DOS interrupt

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition

```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt`: A string that prompts the user to enter a number.
    - `resultMsg`: A message indicating that the factorial will be displayed.
    - `number`: A variable to store the input number.
    - `factorial`: A variable initialized to `1` to store the factorial result.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays a prompt message using DOS interrupt `int 21h`.
    - It reads a single character input from the keyboard and converts it from ASCII to an integer by subtracting `'0'`.
    - The program checks if the entered number is `0`. If it is, it jumps directly to print the result since `0! = 1`.
    - If not zero, it enters a loop where it multiplies the current value of `AL` (which starts as `1`) by `CL`, which holds the current value of `number`. The loop continues until `CL` reaches zero.
    - After calculating the factorial, it displays a message indicating that it will show the result.
    - Finally, it converts the factorial result from binary to ASCII and prints it.

#### Conclusion

This assembly language program demonstrates how to calculate the factorial of a given number using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for user interaction. Note that this example assumes that only single-digit numbers (0-9) are entered for simplicity.

## 8) Write a program to multiply two 16-bit numbers.

Here’s a simple assembly language program for the 8086 microprocessor that multiplies two 16-bit numbers. The program takes two numbers as input, multiplies them, and displays the result.

#### Program to Multiply Two 16-Bit Numbers

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt1 db 'Enter first number (0-65535): $' ; Prompt for first number
prompt2 db 'Enter second number (0-65535): $' ; Prompt for second number
resultMsg db 'The product is: $'              ; Message for result
num1 dw ?             ; Variable to store the first number
num2 dw ?             ; Variable to store the second number
product dw ?          ; Variable to store the product (max 65535)

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Prompt for first number
    mov ah, 09h        ; Function to display string
    lea dx, prompt1    ; Load address of first prompt message
    int 21h            ; Call DOS interrupt

    ; Read first number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num1, ax       ; Store the first number

    ; Prompt for second number
    mov ah, 09h        ; Function to display string
    lea dx, prompt2     ; Load address of second prompt message
    int 21h            ; Call DOS interrupt

    ; Read second number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num2, ax       ; Store the second number

    ; Multiply the two numbers
    mov ax, num1       ; Load first number into AX
    mul num2           ; Multiply AX by num2 (result in DX:AX)

    mov product, ax     ; Store the lower 16 bits of the product

    ; Display result message
    mov ah, 09h        ; Function to display string
    lea dx, resultMsg   ; Load address of result message
    int 21h            ; Call DOS interrupt

    call PrintNumber     ; Call subroutine to print product

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

; Subroutine to read a number from keyboard (assumes input is valid)
ReadNumber:
    xor ax, ax         ; Clear AX register for input storage
    mov cx, 0          ; Clear CX register (digit counter)

ReadLoop:
    mov ah, 01h        ; Function to read character from keyboard
    int 21h            ; Call DOS interrupt
    sub al, '0'        ; Convert ASCII to integer (assuming single digit)

    cmp al, 9          ; Check if digit is valid (0-9)
    jae DoneRead       ; If greater than 9, end reading

    mov bx, 10         ; Prepare for decimal conversion (base 10)

    mul bx             ; AX = AX * 10 (shift left)

    add ax, num1       ; Add new digit to AX

    jmp ReadLoop       ; Repeat loop for next digit

DoneRead:
    ret

; Subroutine to print a number in AX as decimal (assumes AX < 65536)
PrintNumber:
    xor cx, cx         ; Clear CX for digit count

ConvertLoop:
    xor dx, dx         ; Clear DX before division
    mov bx, 10         ; Prepare for decimal conversion (base 10)

    div bx             ; Divide AX by 10; quotient in AL, remainder in AH

    push dx            ; Push remainder onto stack (digit)

    inc cx             ; Increment digit count

    test ax, ax        ; Check if quotient is zero
    jnz ConvertLoop     ; If not zero, continue converting

PrintLoop:
    pop dx             ; Pop digit from stack into DX

    add dl, '0'        ; Convert digit back to ASCII

    mov ah, 02h        ; Function to display character in DL
    int 21h            ; Call DOS interrupt

    loop PrintLoop      ; Loop until all digits are printed

    ret

end main               ; End of program definition

```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt1` and `prompt2`: Strings that prompt the user to enter two numbers.
    - `resultMsg`: A message indicating that the product will be displayed.
    - `num1` and `num2`: Variables to store the two input numbers.
    - `product`: A variable to store the result of the multiplication.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays prompts for both numbers and calls a subroutine (`ReadNumber`) to read each number from the keyboard.
    - After reading both numbers and storing them in `num1` and `num2`, it performs multiplication using the `mul` instruction. The result is stored in `product`.
    - It then displays a message indicating that it will show the result and calls another subroutine (`PrintNumber`) to print the product.
4. **Subroutines**:
    - **ReadNumber**: Reads a multi-digit integer from keyboard input and converts it from ASCII characters to a binary value stored in `AX`.
    - **PrintNumber**: Converts a binary value in `AX` back into ASCII characters and prints it out one digit at a time.
5. **Program Termination**:
    - Finally, it terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to multiply two 16-bit numbers using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for interaction with users. The multiplication is performed using built-in instructions while handling user input and output efficiently.

## 9) Write a program to ADD two 32-bit numbers.

Here's a simple assembly language program for the 8086 microprocessor that adds two 32-bit numbers. The program prompts the user to enter two 32-bit numbers, performs the addition, and displays the result.

#### Program to Add Two 32-Bit Numbers

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt1 db 'Enter first number (0-4294967295): $' ; Prompt for first number
prompt2 db 'Enter second number (0-4294967295): $' ; Prompt for second number
resultMsg db 'The sum is: $'                       ; Message for result
num1 dd ?            ; Variable to store the first number (32-bit)
num2 dd ?            ; Variable to store the second number (32-bit)
sum dd ?             ; Variable to store the sum (32-bit)

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Prompt for first number
    mov ah, 09h        ; Function to display string
    lea dx, prompt1    ; Load address of first prompt message
    int 21h            ; Call DOS interrupt

    ; Read first number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num1, eax      ; Store the first number

    ; Prompt for second number
    mov ah, 09h        ; Function to display string
    lea dx, prompt2     ; Load address of second prompt message
    int 21h            ; Call DOS interrupt

    ; Read second number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num2, eax      ; Store the second number

    ; Add the two numbers
    mov eax, num1      ; Load first number into EAX
    add eax, num2      ; Add second number to EAX (EAX = EAX + num2)

    mov sum, eax       ; Store the result in sum

    ; Display result message
    mov ah, 09h        ; Function to display string
    lea dx, resultMsg   ; Load address of result message
    int 21h            ; Call DOS interrupt

    call PrintNumber     ; Call subroutine to print sum

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

; Subroutine to read a number from keyboard (assumes input is valid)
ReadNumber:
    xor eax, eax        ; Clear EAX register for input storage

ReadLoop:
    mov ah, 01h        ; Function to read character from keyboard
    int 21h            ; Call DOS interrupt

    sub al, '0'        ; Convert ASCII to integer (assuming single digit)

    cmp al, 9          ; Check if digit is valid (0-9)
    jae DoneRead       ; If greater than 9, end reading

    mov ebx, 10        ; Prepare for decimal conversion (base 10)

    mul ebx            ; EAX = EAX * 10 (shift left)

    add eax, al        ; Add new digit to EAX

    jmp ReadLoop       ; Repeat loop for next digit

DoneRead:
    ret

; Subroutine to print a number in EAX as decimal (assumes EAX < 4294967296)
PrintNumber:
    xor ecx, ecx       ; Clear ECX for digit count

ConvertLoop:
    xor edx, edx       ; Clear EDX before division
    mov ebx, 10        ; Prepare for decimal conversion (base 10)

    div ebx            ; Divide EAX by 10; quotient in EAX, remainder in EDX

    push edx           ; Push remainder onto stack (digit)

    inc ecx            ; Increment digit count

    test eax, eax      ; Check if quotient is zero
    jnz ConvertLoop     ; If not zero, continue converting

PrintLoop:
    pop edx            ; Pop digit from stack into EDX

    add dl, '0'        ; Convert digit back to ASCII

    mov ah, 02h        ; Function to display character in DL
    int 21h            ; Call DOS interrupt

    loop PrintLoop      ; Loop until all digits are printed

    ret

end main               ; End of program definition

```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt1` and `prompt2`: Strings that prompt the user to enter two numbers.
    - `resultMsg`: A message indicating that the sum will be displayed.
    - `num1`, `num2`, and `sum`: Variables defined as double words (`dd`) to store two input numbers and their sum.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays prompts for both numbers and calls a subroutine (`ReadNumber`) to read each number from the keyboard.
    - After reading both numbers and storing them in `num1` and `num2`, it performs addition using the `add` instruction. The result is stored in `sum`.
    - It then displays a message indicating that it will show the result and calls another subroutine (`PrintNumber`) to print the sum.
4. **Subroutines**:
    - **ReadNumber**: Reads a multi-digit integer from keyboard input and converts it from ASCII characters to a binary value stored in `EAX`.
    - **PrintNumber**: Converts a binary value in `EAX` back into ASCII characters and prints it out one digit at a time.
5. **Program Termination**:
    - Finally, it terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to add two 32-bit numbers using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for interaction with users. The addition is performed using built-in instructions while handling user input and output efficiently.

## 10) Write a program to ADD two 16-bit numbers.

Here's a simple assembly language program for the 8086 microprocessor that adds two 16-bit numbers. The program prompts the user to enter two 16-bit numbers, performs the addition, and displays the result.

#### Program to Add Two 16-Bit Numbers

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
prompt1 db 'Enter first number (0-65535): $' ; Prompt for first number
prompt2 db 'Enter second number (0-65535): $' ; Prompt for second number
resultMsg db 'The sum is: $'                  ; Message for result
num1 dw ?            ; Variable to store the first number (16-bit)
num2 dw ?            ; Variable to store the second number (16-bit)
sum dw ?             ; Variable to store the sum (16-bit)

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Prompt for first number
    mov ah, 09h        ; Function to display string
    lea dx, prompt1    ; Load address of first prompt message
    int 21h            ; Call DOS interrupt

    ; Read first number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num1, ax       ; Store the first number

    ; Prompt for second number
    mov ah, 09h        ; Function to display string
    lea dx, prompt2     ; Load address of second prompt message
    int 21h            ; Call DOS interrupt

    ; Read second number from keyboard
    call ReadNumber     ; Call subroutine to read number
    mov num2, ax       ; Store the second number

    ; Add the two numbers
    mov ax, num1       ; Load first number into AX
    add ax, num2       ; Add second number to AX (AX = AX + num2)

    mov sum, ax        ; Store the result in sum

    ; Display result message
    mov ah, 09h        ; Function to display string
    lea dx, resultMsg   ; Load address of result message
    int 21h            ; Call DOS interrupt

    call PrintNumber     ; Call subroutine to print sum

endProgram:
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

; Subroutine to read a number from keyboard (assumes input is valid)
ReadNumber:
    xor ax, ax         ; Clear AX register for input storage

ReadLoop:
    mov ah, 01h        ; Function to read character from keyboard
    int 21h            ; Call DOS interrupt

    sub al, '0'        ; Convert ASCII to integer (assuming single digit)

    cmp al, 9          ; Check if digit is valid (0-9)
    jae DoneRead       ; If greater than 9, end reading

    mov bx, 10         ; Prepare for decimal conversion (base 10)

    mul bx             ; AX = AX * 10 (shift left)

    add ax, al         ; Add new digit to AX

    jmp ReadLoop       ; Repeat loop for next digit

DoneRead:
    ret

; Subroutine to print a number in AX as decimal (assumes AX < 65536)
PrintNumber:
    xor cx, cx         ; Clear CX for digit count

ConvertLoop:
    xor dx, dx         ; Clear DX before division
    mov bx, 10         ; Prepare for decimal conversion (base 10)

    div bx             ; Divide AX by 10; quotient in AL, remainder in AH

    push dx            ; Push remainder onto stack (digit)

    inc cx             ; Increment digit count

    test ax, ax        ; Check if quotient is zero
    jnz ConvertLoop     ; If not zero, continue converting

PrintLoop:
    pop dx             ; Pop digit from stack into DX

    add dl, '0'        ; Convert digit back to ASCII

    mov ah, 02h        ; Function to display character in DL
    int 21h            ; Call DOS interrupt

    loop PrintLoop      ; Loop until all digits are printed

    ret

end main               ; End of program definition
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `prompt1` and `prompt2`: Strings that prompt the user to enter two numbers.
    - `resultMsg`: A message indicating that the sum will be displayed.
    - `num1`, `num2`, and `sum`: Variables defined as words (`dw`) to store two input numbers and their sum.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It displays prompts for both numbers and calls a subroutine (`ReadNumber`) to read each number from the keyboard.
    - After reading both numbers and storing them in `num1` and `num2`, it performs addition using the `add` instruction. The result is stored in `sum`.
    - It then displays a message indicating that it will show the result and calls another subroutine (`PrintNumber`) to print the sum.
4. **Subroutines**:
    - **ReadNumber**: Reads a multi-digit integer from keyboard input and converts it from ASCII characters to a binary value stored in `AX`.
    - **PrintNumber**: Converts a binary value in `AX` back into ASCII characters and prints it out one digit at a time.
5. **Program Termination**:
    - Finally, it terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to add two 16-bit numbers using basic instructions in the 8086 microprocessor. It utilizes string output and input functions provided by DOS interrupts for interaction with users. The addition is performed using built-in instructions while handling user input and output efficiently.

## 11) Write a program to find the smallest number from a given array of 10 numbers.

Here’s a simple assembly language program for the 8086 microprocessor that finds the smallest number from a given array of 10 numbers. The program initializes an array with predefined values, iterates through the array to find the smallest number, and then displays the result.

#### Program to Find the Smallest Number in an Array

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
array db 15, 3, 9, 27, 4, 8, 1, 20, 12, 5 ; Array of 10 numbers
arraySize db 10        ; Size of the array
smallest db ?          ; Variable to store the smallest number

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    mov cx, arraySize   ; Load the number of elements in CX
    lea si, array       ; Load address of the array into SI

    mov al, [si]        ; Load first element into AL (assume it's the smallest)
    inc si              ; Move to the next element
    dec cx              ; Decrement count

find_smallest:
    cmp cx, 0           ; Check if we've processed all elements
    je done             ; If CX is zero, we're done

    mov bl, [si]        ; Load current element into BL
    cmp bl, al          ; Compare current element with smallest found so far
    jge skip            ; If current element is greater or equal, skip

    mov al, bl          ; Update smallest number found

skip:
    inc si              ; Move to the next element
    dec cx              ; Decrement count
    jmp find_smallest   ; Repeat until all elements are checked

done:
    mov smallest, al     ; Store the smallest number found

    ; Display result message (for simplicity we will just end here)
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `array`: An array of 10 numbers initialized with values.
    - `arraySize`: A variable that stores the size of the array.
    - `smallest`: A variable to store the smallest number found in the array.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It loads the size of the array into `CX` and initializes `SI` with the address of `array`.
    - The first element of the array is loaded into `AL`, assuming it to be the smallest initially.
    - The program enters a loop (`find_smallest`) to iterate through each element of the array:
        - It compares each subsequent element with the current smallest value stored in `AL`.
        - If a smaller value is found, it updates `AL`.
        - The loop continues until all elements have been checked.
    - After finding the smallest number, it stores it in `smallest`.
4. **Program Termination**:
    - Finally, it terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to find the smallest number in an array using basic instructions in the 8086 microprocessor. It efficiently iterates through an array and uses comparisons to determine which value is smallest. This example can be easily modified for different sizes or values in the array as needed.

## 12) Write a program to find the largest number from a given array of 10 numbers.

Here’s a simple assembly language program for the 8086 microprocessor that finds the largest number from a given array of 10 numbers. The program initializes an array with predefined values, iterates through the array to find the largest number, and then displays the result.

#### Program to Find the Largest Number in an Array

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
array db 15, 3, 9, 27, 4, 8, 1, 20, 12, 5 ; Array of 10 numbers
arraySize db 10        ; Size of the array
largest db ?           ; Variable to store the largest number

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    mov cx, arraySize   ; Load the number of elements in CX
    lea si, array       ; Load address of the array into SI

    mov al, [si]        ; Load first element into AL (assume it's the largest)
    inc si              ; Move to the next element
    dec cx              ; Decrement count

find_largest:
    cmp cx, 0           ; Check if we've processed all elements
    je done             ; If CX is zero, we're done

    mov bl, [si]        ; Load current element into BL
    cmp bl, al          ; Compare current element with largest found so far
    jle skip            ; If current element is less than or equal to largest, skip

    mov al, bl          ; Update largest number found

skip:
    inc si              ; Move to the next element
    dec cx              ; Decrement count
    jmp find_largest    ; Repeat until all elements are checked

done:
    mov largest, al      ; Store the largest number found

    ; Display result message (for simplicity we will just end here)
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `array`: An array of 10 numbers initialized with values.
    - `arraySize`: A variable that stores the size of the array.
    - `largest`: A variable to store the largest number found in the array.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It loads the size of the array into `CX` and initializes `SI` with the address of `array`.
    - The first element of the array is loaded into `AL`, assuming it to be the largest initially.
    - The program enters a loop (`find_largest`) to iterate through each element of the array:
        - It compares each subsequent element with the current largest value stored in `AL`.
        - If a larger value is found, it updates `AL`.
        - The loop continues until all elements have been checked.
    - After finding the largest number, it stores it in `largest`.
4. **Program Termination**:
    - Finally, it terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to find the largest number in an array using basic instructions in the 8086 microprocessor. It efficiently iterates through an array and uses comparisons to determine which value is largest. This example can be easily modified for different sizes or values in the array as needed.

## 13) Write a program to arrange a given array of 10 numbers in ascending order.

Here's a simple assembly language program for the 8086 microprocessor that sorts a given array of 10 numbers in ascending order using the bubble sort algorithm.

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
array db 15, 3, 9, 27, 4, 8, 1, 20, 12, 5 ; Array of 10 numbers
arraySize equ 10        ; Size of the array

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Outer loop (n-1 passes)
    mov cx, arraySize - 1 ; Loop counter (n-1)

outerLoop:
    push cx            ; Save outer loop counter

    ; Inner loop (n-i comparisons)
    mov si, 0           ; Initialize index to 0
    mov cl, arraySize - 1 ; Loop counter (n-i)

innerLoop:
    mov al, array[si]   ; Load element i
    cmp al, array[si+1] ; Compare with element i+1
    jbe skip           ; If i <= i+1, skip swap

    ; Swap elements i and i+1
    xchg al, array[si+1]
    mov array[si], al

skip:
    inc si             ; Increment index
    loop innerLoop     ; Repeat inner loop

    pop cx             ; Restore outer loop counter
    loop outerLoop     ; Repeat outer loop

    ; Display sorted array (for simplicity we will just end here)
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `array`: An array of 10 numbers initialized with values.
    - `arraySize`: A constant that stores the size of the array.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It enters an outer loop that runs `arraySize-1` times. This loop represents the number of passes needed to sort the array.
    - Inside the outer loop, an inner loop runs `arraySize-1` times. This inner loop compares adjacent elements and swaps them if they are in the wrong order.
    - The inner loop uses `mov al, array[si]` to load an element into `al` and compares it with the next element using `cmp al, array[si+1]`.
    - If the elements are in the wrong order, they are swapped using `xchg al, array[si+1]` and `mov array[si], al`.
    - The outer loop counter is saved and restored using `push cx` and `pop cx` to preserve it across the inner loop.
    - After the sorting is complete, the program terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to sort an array of numbers in ascending order using the bubble sort algorithm. It efficiently compares and swaps elements within nested loops until the entire array is sorted. The program can be easily modified to sort arrays of different sizes or with different initial values.

## 14) Write a program to arrange a given array of 10 numbers in descending order.

Here’s a simple assembly language program for the 8086 microprocessor that arranges a given array of 10 numbers in descending order using the bubble sort algorithm.

#### Program to Sort an Array in Descending Order

```nasm
.model small            ; Define the small memory model
.stack 100h             ; Define stack size
.data                   ; Data segment
array db 15, 3, 9, 27, 4, 8, 1, 20, 12, 5 ; Array of 10 numbers
arraySize db 10        ; Size of the array

.code                   ; Code segment
main:
    mov ax, @data      ; Load data segment address into AX
    mov ds, ax         ; Initialize DS register

    ; Outer loop (n-1 passes)
    mov cx, arraySize - 1 ; Loop counter (n-1)

outerLoop:
    push cx            ; Save outer loop counter

    ; Inner loop (n-i comparisons)
    mov si, 0           ; Initialize index to 0
    mov cl, arraySize - 1 ; Loop counter (n-i)

innerLoop:
    mov al, array[si]   ; Load element i into AL
    cmp al, array[si+1] ; Compare with element i+1
    jge skip            ; If i >= i+1 (AL >= array[si+1]), skip swap

    ; Swap elements i and i+1 if AL < array[si+1]
    xchg al, array[si+1]
    mov array[si], al

skip:
    inc si              ; Increment index
    loop innerLoop      ; Repeat inner loop

    pop cx              ; Restore outer loop counter
    loop outerLoop      ; Repeat outer loop

    ; Display sorted array (for simplicity we will just end here)
    mov ax, 4C00h      ; Terminate program function in DOS
    int 21h            ; Call DOS interrupt

end main               ; End of program definition
```

#### Explanation of the Program

1. **Model Declaration**:
    - `.model small`: Specifies that the program will use the small memory model.
    - `.stack 100h`: Reserves stack space.
2. **Data Segment**:
    - `array`: An array of 10 numbers initialized with values.
    - `arraySize`: A variable that stores the size of the array.
3. **Code Segment**:
    - The `main` label marks the start of the code.
    - The program initializes the data segment using `mov ax, @data` and `mov ds, ax`.
    - It enters an outer loop that runs `arraySize-1` times. This loop represents the number of passes needed to sort the array.
    - Inside the outer loop, an inner loop runs `arraySize-1` times. This inner loop compares adjacent elements and swaps them if they are in the wrong order (in this case, if the current element is less than the next element).
    - The inner loop uses `mov al, array[si]` to load an element into `al` and compares it with the next element using `cmp al, array[si+1]`.
    - If a swap is needed (i.e., if `AL < array[si+1]`), it swaps them using `xchg al, array[si+1]` and `mov array[si], al`.
    - The outer loop counter is saved and restored using `push cx` and `pop cx` to preserve it across the inner loop.
    - After sorting is complete, the program terminates using DOS interrupt `int 21h`.

#### Conclusion

This assembly language program demonstrates how to sort an array of numbers in descending order using the bubble sort algorithm. It efficiently compares and swaps elements within nested loops until the entire array is sorted. The program can be easily modified for different sizes or values in the array as needed.