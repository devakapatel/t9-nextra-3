# Unit 1

## 1) What is network topology? Explain different types of network topology.

### Network Topology

Network topology refers to the physical or logical arrangement of devices in a network. It describes how the nodes and links in a network are interconnected and organized. The different types of network topologies are:

#### 1. Bus Topology

- In a bus topology, all devices are connected to a single cable or backbone.
- Data is transmitted in both directions along the backbone.
- If the backbone fails, the entire network goes down.
- Examples include Ethernet bus networks.

#### 2. Star Topology

- In a star topology, all devices are connected to a central node or hub.
- Data is transmitted through the central node.
- If the central node fails, the entire network goes down.
- Examples include home and small office networks.

#### 3. Ring Topology

- In a ring topology, devices are connected in a circular fashion, with data transmitted in one direction.
- Each device acts as a repeater, forwarding data to the next device.
- If one link fails, the entire network goes down.
- Examples include token ring networks.

#### 4. Mesh Topology

- In a mesh topology, devices are connected to multiple other devices, creating redundant paths.
- Data can take multiple paths to reach its destination.
- Mesh topologies are highly reliable as they can tolerate device or link failures.
- Examples include wireless mesh networks.

#### 5. Tree Topology

- In a tree topology, devices are arranged in a hierarchical fashion, with a root node and branches.
- Data flows from the root to the branches.
- If the root node fails, the entire network goes down.
- Examples include hierarchical enterprise networks.

The choice of network topology depends on factors such as cost, reliability, scalability, and the specific requirements of the network. Each topology has its own advantages and disadvantages, and the selection of the appropriate topology is crucial for the efficient and reliable operation of a network.

## 2) What is bit and byte stuffing? Explain with examples.

#### Bit Stuffing and Byte Stuffing

Bit stuffing and byte stuffing are techniques used in data communication to ensure that data frames are correctly framed and to prevent confusion between data and control information. Both methods help in maintaining the integrity of the data being transmitted.

### 1. Bit Stuffing

#### Definition:

Bit stuffing involves inserting non-information bits into a data stream to break up patterns that could be misinterpreted as control signals. This is often used in protocols like HDLC (High-Level Data Link Control).

#### How It Works:

- Whenever a specific bit pattern (often a sequence of consecutive bits) appears in the data stream, a "stuffed" bit is inserted to prevent misinterpretation.
- The most common pattern used for stuffing is a sequence of five consecutive 1s. When this pattern appears, a 0 is inserted after the fifth 1.

#### Example:

Consider the following data stream:

```
Data: 111110111111000

```

In this case, the sequence "11111" appears. To prevent confusion with the flag sequence (which might be "01111110"), we perform bit stuffing:

```
Stuffed Data: 111110011111000

```

Here, a 0 is added after the fifth 1 to break the sequence.

### 2. Byte Stuffing

#### Definition:

Byte stuffing involves inserting special bytes into the data stream to distinguish between data and control information. This is often used in protocols like PPP (Point-to-Point Protocol).

#### How It Works:

- A special byte (often called a "flag" byte) is used to indicate the start and end of a frame.
- If the data contains a byte that is the same as the flag byte, a special escape byte is inserted before the flag byte to differentiate it from control information.

#### Example:

Consider the following data stream where the flag byte is `0x7E`:

```
Data: 0x7E 0x45 0x67 0x7E

```

In this case, the data contains the flag byte `0x7E`. To prevent confusion, we perform byte stuffing:

```
Stuffed Data: 0x7E 0x7D 0x5E 0x45 0x67 0x7E

```

Here, the escape byte `0x7D` is inserted before the original flag byte, and the original `0x7E` is replaced with `0x5E` (which is `0x7E` XORed with `0x20`).

#### Summary of Differences

| Feature        | Bit Stuffing                                | Byte Stuffing                               |
| -------------- | ------------------------------------------- | ------------------------------------------- |
| **Purpose**    | Prevents misinterpretation of bit patterns. | Prevents misinterpretation of byte values.  |
| **Method**     | Inserts bits into the data stream.          | Inserts special bytes into the data stream. |
| **Common Use** | Protocols like HDLC.                        | Protocols like PPP.                         |

Both bit stuffing and byte stuffing are essential techniques in data communication, ensuring that the data is transmitted accurately without confusion with control signals.

## 3) Draw the OSI reference model. Explain the functionality of each layer in brief.

### OSI Reference Model

The OSI (Open Systems Interconnection) reference model consists of seven layers, each with a specific functionality:

```
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical

```

#### Physical Layer (Layer 1)

- Deals with the physical equipment involved in the network, such as cables, network interface cards, and connectors.
- Specifies the electrical, mechanical, functional, and procedural standards for activating, maintaining, and deactivating physical connections.
- Responsible for transmitting raw bits over the network.

#### Data Link Layer (Layer 2)

- Provides node-to-node data transfer, detecting and possibly correcting errors that may occur in the Physical layer.
- Organizes bits into frames and handles media access control (MAC) addressing.
- Ensures reliable and error-free transfer of data frames between two directly connected devices.

#### Network Layer (Layer 3)

- Responsible for logical addressing and routing data between different networks.
- Determines the path the data should take based on the destination address and network conditions.
- Handles congestion control and provides logical-to-physical address mapping.

#### Transport Layer (Layer 4)

- Ensures complete data transfer from one application to another.
- Provides end-to-end communication and error recovery.
- Segments and reassembles data, and manages flow control.

#### Session Layer (Layer 5)

- Establishes, maintains, and synchronizes communication sessions between applications.
- Provides checkpointing, recovery, and restart capabilities.
- Manages the exchange of data between presentation layer entities.

#### Presentation Layer (Layer 6)

- Defines data formats, encryption, compression, and conversions for application layer.
- Ensures that information sent by one application can be read by another.
- Translates between different data representations and encryption schemes.

#### Application Layer (Layer 7)

- Serves as the interface for network services to applications, such as email, file transfer, and web services.
- Defines protocols that applications use to communicate over the network.
- Provides services directly to the application processes, such as file transfer, directory services, and electronic mail.

The OSI model provides a standardized framework for network communication, allowing different systems and devices to interoperate. Each layer performs specific functions and communicates with the corresponding layer on the receiving end.

## 4) Give differences between Connection oriented versus Connection less Services.

The main differences between connection-oriented and connectionless services in computer networks are:

1. Connection Establishment:
   - Connection-oriented service requires an explicit connection establishment phase before data can be exchanged.
   - Connectionless service does not require a prior connection establishment, each data unit is sent independently.
2. State Maintenance:
   - Connection-oriented service maintains state information about the connection between the communicating devices.
   - Connectionless service is stateless, each data unit is treated independently without maintaining any connection state.
3. Reliability:
   - Connection-oriented service typically provides reliable data delivery with features like error checking, flow control, and retransmissions.
   - Connectionless service may not provide reliable delivery, data units can be lost, duplicated, or delivered out of order.
4. Overhead:
   - Connection-oriented service has higher overhead due to the connection establishment, maintenance, and termination phases.
   - Connectionless service has lower overhead as it does not require the overhead of connection management.
5. Applications:
   - Connection-oriented service is suitable for applications that require reliable and ordered data transfer, like file transfer, remote login, and video streaming.
   - Connectionless service is suitable for applications that can tolerate some data loss, like voice/video calls, DNS, and email.
6. Examples:
   - Connection-oriented protocols: TCP (Transmission Control Protocol)
   - Connectionless protocols: UDP (User Datagram Protocol), IP (Internet Protocol)

In summary, connection-oriented services provide reliable and ordered data delivery but with higher overhead, while connectionless services offer simpler and faster data transfer but with potentially unreliable delivery. The choice between the two depends on the specific requirements of the application and network.

## 5) Explain functionality of Repeater, HUB, Bridge, Switch, Router and Gateway.

Here is an explanation of the functionality of common network devices:

#### Repeater

- Operates at the physical layer of the OSI model
- Amplifies and retransmits the signal to extend the reach of the network
- Connects network segments using the same protocol and media type
- Does not perform any filtering or addressing

#### Hub

- Operates at the physical layer of the OSI model
- Connects multiple devices on a network
- Receives frames on one port and broadcasts them out of all other ports
- Provides no filtering or addressing capabilities
- Inefficient as it transmits frames to all ports even if the destination is connected to a specific port

#### Bridge

- Operates at the data link layer of the OSI model
- Connects two or more network segments using the same protocol
- Learns MAC addresses of devices and builds a filtering database
- Forwards frames between segments based on destination MAC address
- Filters out frames not destined for the other segment, reducing traffic

#### Switch

- Operates at the data link layer of the OSI model
- Connects multiple devices on a network
- Learns MAC addresses and builds a filtering database for each port
- Forwards frames to the appropriate destination port based on MAC address
- Provides dedicated bandwidth to each port, improving performance

#### Router

- Operates at the network layer of the OSI model
- Connects two or more networks using different protocols
- Routes packets between networks based on logical network addresses (IP addresses)
- Performs logical addressing, routing, and path determination
- Provides logical segmentation of networks and enforces security policies

#### Gateway

- Operates at multiple layers of the OSI model
- Connects networks using different protocols and architectures
- Performs protocol conversion between different network types
- Provides access to remote networks and the Internet
- Serves as an entry and exit point for a network

In summary, these devices differ in the OSI layers they operate at, the functionality they provide, and the types of networks they connect. Repeaters and hubs operate at layer 1, bridges and switches at layer 2, routers at layer 3, and gateways at multiple layers.

## 6) Describe Go Back N and Selective Repeat protocol.

Go Back N and Selective Repeat are two different data link layer protocols that address the issue of reliable data transfer over unreliable channels.

1. Go Back N Protocol:
   - In the Go Back N protocol, the sender can have multiple unacknowledged frames in transit at any given time, up to a predefined window size.
   - If the receiver detects an error in a frame, it discards that frame and all subsequent frames in the window.
   - The sender, upon detecting a missing acknowledgment or receiving a negative acknowledgment, retransmits all the frames starting from the first unacknowledged frame.
   - This approach is simple to implement, but it can be inefficient, as the sender has to retransmit all frames, even if only one frame was corrupted.
2. Selective Repeat Protocol:
   - The Selective Repeat protocol is more efficient than Go Back N.
   - In Selective Repeat, the receiver can individually acknowledge correctly received frames, and the sender only retransmits the frames that were not acknowledged.
   - The sender maintains a window of frames that have been sent but not yet acknowledged.
   - The receiver buffers the correctly received out-of-order frames and waits for the missing frames to be retransmitted.
   - When the missing frames arrive, the receiver can reorder the frames and deliver them to the upper layer.
   - Selective Repeat is more complex to implement than Go Back N, but it can achieve higher throughput, especially in high-latency or high-error-rate environments.

The key differences between the two protocols are:

1. Retransmission Approach:
   - Go Back N retransmits all frames starting from the first unacknowledged frame.
   - Selective Repeat retransmits only the specific frames that were not acknowledged.
2. Receiver Buffering:
   - Go Back N does not require the receiver to buffer out-of-order frames.
   - Selective Repeat requires the receiver to buffer correctly received out-of-order frames.
3. Efficiency:
   - Go Back N is simpler to implement but less efficient, especially in high-latency or high-error-rate environments.
   - Selective Repeat is more complex but can achieve higher throughput in such environments.

The choice between Go Back N and Selective Repeat depends on the specific requirements of the network, such as the expected error rate, latency, and the available resources for buffering and processing at the sender and receiver.

## 7) What is the difference between error detection and correction? Explain any One error correction technique with suitable example.

The main difference between error detection and error correction is:

Error Detection:

- Error detection techniques allow the receiver to identify the presence of errors in the received data.
- They do not attempt to correct the errors, but only identify that errors have occurred.
- Common error detection techniques include parity bits, checksums, and cyclic redundancy checks (CRC).

Error Correction:

- Error correction techniques allow the receiver to not only detect the presence of errors, but also identify and correct the errors.
- This is achieved by adding redundant information to the data, which the receiver can use to determine the original data.
- Common error correction techniques include Hamming codes, Reed-Solomon codes, and convolutional codes.

One example of an error correction technique is Hamming Codes:

Hamming Codes:

- Hamming codes are a class of linear error-correcting codes named after their inventor, Richard Hamming.
- They add extra parity bits to the original data bits to enable single-bit error correction.
- The number of parity bits added depends on the number of data bits:
  - For 4 data bits, 3 parity bits are added, creating a (7,4) Hamming code.
  - For 8 data bits, 4 parity bits are added, creating a (12,8) Hamming code.
- The parity bits are positioned at specific bit positions (1, 2, 4, 8, etc.) and their values are calculated based on the values of the data bits.
- When the receiver gets the encoded message, it can use the parity bit information to detect and correct single-bit errors.

Example:
Consider a (7,4) Hamming code with 4 data bits (1101) and 3 parity bits.

The encoded 7-bit codeword would be: 1101101

If the receiver gets the codeword as 1101111 (with a single-bit error in the last bit), the Hamming code can detect the error and correct it to the original 1101101.

This ability to both detect and correct errors makes Hamming codes a widely used error correction technique in digital communications and storage systems.

## 8) Explain TCP/IP Reference Model. Compare TCP/IP with OSI Model.

### TCP/IP Reference Model

The TCP/IP (Transmission Control Protocol/Internet Protocol) reference model is a conceptual framework used to describe the functions of the networking protocols used in the Internet. It consists of four layers:

#### 1. Application Layer

- Serves as the interface for network services to applications, such as email, file transfer, and web services.
- Defines protocols that applications use to communicate over the network.
- Provides services directly to the application processes, such as file transfer, directory services, and electronic mail.

#### 2. Transport Layer

- Ensures complete data transfer from one application to another.
- Provides end-to-end communication and error recovery.
- Segments and reassembles data, and manages flow control.

#### 3. Internet Layer

- Responsible for logical addressing and routing data between different networks.
- Determines the path the data should take based on the destination address and network conditions.
- Handles congestion control and provides logical-to-physical address mapping.

#### 4. Link Layer

- Provides node-to-node data transfer, detecting and possibly correcting errors that may occur in the Physical layer.
- Organizes bits into frames and handles media access control (MAC) addressing.
- Ensures reliable and error-free transfer of data frames between two directly connected devices.

The TCP/IP model is based on the actual protocols used in the Internet, while the OSI reference model is a more theoretical framework.

### Comparison with OSI Model

The OSI reference model consists of seven layers:

```
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical

```

The main differences between the TCP/IP and OSI models are:

1. **Number of layers**: TCP/IP has four layers, while OSI has seven.
2. **Functionality**: The OSI model clearly defines the services, interfaces, and protocols for each layer, while the TCP/IP model is more focused on the actual protocols used in the Internet.
3. **Presentation and Session layers**: The TCP/IP model does not have separate presentation and session layers, as it was designed to be more practical and focused on the protocols used in the Internet.
4. **Link layer**: The TCP/IP model treats the link layer as an interface between the network layer and the physical layer, while the OSI model considers it a separate layer.

Despite these differences, both models serve the same purpose of providing a framework for understanding and implementing network communication protocols.

## 9) Compute CRC for a data sequence 10110111 for which the generator is 110011.

To compute the Cyclic Redundancy Check (CRC) for the data sequence 10110111 using the generator 110011, we can follow these steps:

1. Append the data sequence with the same number of zeros as the length of the generator polynomial, which is 6 in this case. The resulting sequence is 10110111000000.
2. Divide the appended data sequence by the generator polynomial 110011 using binary division.
3. The remainder of the division is the CRC value.

Let's perform the binary division step-by-step:

10110111000000 ) 110011
110011

---

000001
110011

---

000000

The remainder is 000000, which means the CRC for the data sequence 10110111 with the generator 110011 is 000000.

Therefore, the complete codeword (data sequence + CRC) is 10110111000000.

## 10) What is Hamming Code? Explain with one Example.

Let us assume the even parity hamming code from the above example(111001101)is transmitted and the received code is (110001101). Now form received code, let us detect and correct errors.

#### Hamming Code

**Definition:**
Hamming Code is an error-correcting code that can detect and correct single-bit errors in data transmission. It uses redundancy bits, known as parity bits, to achieve error correction. The most common Hamming Code is the (7, 4) code, which encodes 4 bits of data into 7 bits by adding 3 parity bits.

#### How Hamming Code Works:

1. **Determine Positions of Parity Bits**: In a Hamming Code, the positions of the parity bits are powers of 2 (1, 2, 4, 8, etc.). For a (7, 4) Hamming Code, the parity bits are at positions 1, 2, and 4.
2. **Calculate Parity Bits**: Each parity bit checks specific bits in the codeword to ensure even parity (the total number of 1s is even).
3. **Transmit the Code**: The original data bits and the calculated parity bits are combined to form the final codeword.

#### Example:

Let's encode the data bits `1101` using Hamming Code.

1. **Positioning**:
   - Data bits: 1, 1, 0, 1
   - Codeword: P1, P2, D1, P4, D2, D3, D4 (where P represents parity bits and D represents data bits)
   - This gives: P1, P2, 1, P4, 1, 0, 1
2. **Calculate Parity Bits**:
   - **P1** checks bits 1, 3, 5, 7: P1 ⊕ D1 ⊕ D2 ⊕ D4 = 0 → P1 = 0
   - **P2** checks bits 2, 3, 6, 7: P2 ⊕ D1 ⊕ D3 ⊕ D4 = 0 → P2 = 1
   - **P4** checks bits 4, 5, 6, 7: P4 ⊕ D2 ⊕ D3 ⊕ D4 = 0 → P4 = 0
3. **Final Codeword**:
   - The final Hamming Codeword is `0111011`.

#### Error Detection and Correction Example

Let's assume the even parity Hamming code `1110011` is transmitted, but the received code is `1100011`. We will detect and correct the error.

1. **Received Code**: `1100011`
2. **Check Parity Bits**:
   - **P1** (checks bits 1, 3, 5, 7): 1 (P1) ⊕ 0 (D1) ⊕ 0 (D2) ⊕ 1 (D4) = 0 (even parity, so P1 is correct)
   - **P2** (checks bits 2, 3, 6, 7): 1 (P2) ⊕ 0 (D1) ⊕ 0 (D3) ⊕ 1 (D4) = 1 (odd parity, so P2 is incorrect)
   - **P4** (checks bits 4, 5, 6, 7): 0 (P4) ⊕ 0 (D2) ⊕ 0 (D3) ⊕ 1 (D4) = 1 (odd parity, so P4 is incorrect)
3. **Error Position**:
   - The parity bits indicate an error at positions:
     - P1 = 0 (correct)
     - P2 = 1 (incorrect)
     - P4 = 0 (incorrect)
   - The binary representation of the error position is `010` (P2 is incorrect, P4 is incorrect), which is 2 in decimal.
4. **Correct the Error**:
   - The bit at position 2 in the received code `1100011` is flipped from 1 to 0.
   - Corrected Code: `1000011`

#### Summary

Hamming Code is an effective method for error detection and correction in data transmission. By adding redundancy bits, it can identify and correct single-bit errors, ensuring data integrity. In our example, we successfully detected and corrected an error in the received code.
