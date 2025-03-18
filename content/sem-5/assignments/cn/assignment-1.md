# Assignment 1

## 1) What is network topology? Explain different types of network topology.

Network topology refers to the physical and logical arrangement of devices in a network. It describes how the nodes and links in a network are interconnected. There are several types of network topologies:

### Mesh Topology

- In a mesh topology, every device has a dedicated point-to-point link to every other device.
- The number of physical links in a fully connected mesh network with n nodes is n(n-1)/2.
- Advantages: robust, easy fault diagnosis, provides privacy and security.
- Disadvantages: higher cost of implementation and maintenance, difficult configuration and installation, suitable for fewer devices due to high cable cost.

### Bus Topology

- In a bus topology, one long cable acts as a backbone to link all the devices.
- Nodes are connected to the bus cable by drop lines and taps.
- Advantages: easy to connect devices, quick setup, best for small networks, easy to expand.
- Disadvantages: if the backbone cable fails the whole network goes down, no bi-directional communication, not suitable for heavy traffic due to collision risk.

### Star Topology

- In a star topology, each device has a dedicated point-to-point link only to a central controller called a hub.
- Devices are not directly linked to one another.
- Advantages: very reliable, high-performing with no collisions, less expensive, easier to install.
- Disadvantages: requires more cables than bus, if the hub fails everything goes down, hub requires more resources and maintenance.

### Ring Topology

- In a ring topology, each device has a dedicated point-to-point connection with only the two devices on either side of it.
- Signals pass along the ring in one direction from device to device.
- Advantages: data flows in one direction reducing collisions, equal access to resources, no need for a server, cheap to install and expand, high data transfer speed.
- Disadvantages: data packets must pass through all nodes, slower performance than bus, difficult to add/remove nodes, total dependence on one cable, not scalable.

### Tree Topology

- A variation of star topology with a hierarchical data flow.
- Secondary hubs are connected to a central hub with a repeater.
- Advantages: allows more devices to be attached to a single hub, decreases signal travel distance, allows isolation and prioritization of computers.
- Disadvantages: if the backbone fails the whole topology crashes, a multi-point connection, not robust.

Network topologies determine the data flow, performance, and robustness of a network. The choice depends on factors like cost, reliability, and scalability requirements.

## 2) What is the purpose of cladding in an optical fiber? Discuss its density relative to the core.

The purpose of cladding in an optical fiber is to confine the light within the core of the fiber. Cladding is a layer of material that surrounds the core of an optical fiber and has a lower refractive index than the core. This difference in refractive index allows for total internal reflection, which is the principle that enables light to propagate through the fiber with minimal loss.

### Density of Cladding Relative to the Core

The density of the cladding material relative to the core is an important factor in the performance and characteristics of an optical fiber. In general:

- The core has a higher refractive index than the cladding, which is necessary for total internal reflection to occur.
- The cladding material is typically made of a different type of glass or polymer with a lower refractive index than the core.
- The density of the cladding material is usually slightly lower than the density of the core material.

The exact densities of the core and cladding materials depend on the specific composition and manufacturing process used to create the optical fiber. However, the density difference is typically small and does not significantly affect the overall performance of the fiber.

The main purpose of the cladding is to provide a layer with a lower refractive index than the core, which allows for efficient light confinement and propagation through the fiber. The cladding also protects the core from external factors such as scratches, moisture, and mechanical stress, which can cause signal loss or fiber damage.

## 3) Discuss different types of guided and unguided media used to transmit data in network.

In data communication, the transmission medium is the physical path through which data travels from sender to receiver. Transmission media can be categorized into two main types: **guided media** and **unguided media**. Each type has its own characteristics, advantages, and applications.

### Guided Media

Guided media, also known as wired or bounded media, involve physical connections that guide the data signals along a specific path. Here are the primary types of guided media:

#### 1. Twisted Pair Cable

- **Description**: Consists of pairs of insulated copper wires twisted together to reduce electromagnetic interference.
- **Types**:
  - **Unshielded Twisted Pair (UTP)**: Commonly used in LANs; less expensive but more susceptible to interference.
  - **Shielded Twisted Pair (STP)**: Has shielding to protect against interference; used in environments with high electromagnetic interference.
- **Applications**: Telephone networks, local area networks (LANs), and data transmission.

#### 2. Coaxial Cable

- **Description**: Comprises a central conductor, an insulating layer, a metallic shield, and an outer insulating layer. The design helps to reduce interference and allows for higher bandwidth.
- **Applications**: Cable television, broadband internet, and some LANs.

#### 3. Fiber-Optic Cable

- **Description**: Uses glass or plastic fibers to transmit data as light pulses. Fiber optics offer high bandwidth and long-distance transmission capabilities with minimal loss.
- **Types**:
  - **Single-mode Fiber**: Allows one mode of light to propagate, suitable for long-distance communication.
  - **Multi-mode Fiber**: Allows multiple light modes to propagate, suitable for shorter distances.
- **Applications**: High-speed internet, telecommunications, and data centers.

### Unguided Media

Unguided media, also known as wireless or unbounded media, transmit data without a physical medium. Instead, they use electromagnetic waves to carry signals through the air or vacuum. Here are the primary types of unguided media:

#### 1. Radio Waves

- **Description**: Electromagnetic waves with frequencies ranging from a few kilohertz to several gigahertz. They can travel long distances and penetrate obstacles.
- **Applications**: AM/FM radio, television broadcasts, and cellular networks.

#### 2. Microwaves

- **Description**: High-frequency radio waves (typically in the gigahertz range) that require line-of-sight transmission. They are used for point-to-point communication.
- **Applications**: Satellite communication, microwave links, and wireless LANs.

#### 3. Infrared

- **Description**: Electromagnetic radiation with wavelengths longer than visible light but shorter than microwaves. Infrared communication requires a direct line of sight.
- **Applications**: Remote controls, short-range communication devices, and some wireless LANs.

#### 4. Satellite Communication

- **Description**: Uses satellites in orbit to relay signals between ground stations. It can cover a vast geographical area.
- **Applications**: Global positioning systems (GPS), television broadcasting, and internet services in remote areas.

## Summary

The choice between guided and unguided media depends on various factors, including the required bandwidth, distance, cost, and environmental conditions. Guided media typically offer higher data rates and security, while unguided media provide flexibility and ease of installation, especially in areas where physical cabling is impractical. Understanding these media types is crucial for designing efficient and effective communication networks.

## 4) Draw the OSI reference model. Explain the functionality of each layer in brief.

The OSI (Open Systems Interconnection) reference model is a conceptual framework used to describe the functions of a networking system. It consists of seven layers, each with specific functions and responsibilities. Here's a brief explanation of each layer:

```
 Application
 Presentation
 Session
 Transport
 Network
 Data Link
 Physical

```

### Physical Layer

- Deals with the physical equipment involved in the network, such as cables, connectors, and network interface cards.
- Defines the electrical, mechanical, functional, and procedural specifications for activating, maintaining, and deactivating the physical link between communicating devices.
- Responsible for the transmission and reception of raw data bits over the physical medium.

### Data Link Layer

- Provides node-to-node data transfer, detecting and possibly correcting errors that may occur in the Physical layer.
- Responsible for establishing, maintaining, and synchronizing communication between devices.
- Performs error checking and flow control to ensure reliable data transfer.
- Divides the input data into data frames and adds header and trailer information to each frame.

### Network Layer

- Responsible for logical addressing and routing data from the source to the destination.
- Determines the path the data should take based on the logical address of the destination device.
- Performs congestion control to manage traffic flow and avoid network congestion.
- Provides logical-to-physical mapping for addressing and routing.

### Transport Layer

- Ensures complete data transfer by providing end-to-end communication.
- Segments the data received from the upper layers, numbers the segments, and sends them to the Network layer.
- Performs error recovery and flow control to ensure reliable data transfer.
- Provides segmentation, flow control, and error correction mechanisms.

### Session Layer

- Establishes, maintains, and synchronizes communication sessions between applications.
- Provides checkpointing, restart, and restart capabilities to handle failures during a session.
- Responsible for creating and maintaining communication sessions between applications.

### Presentation Layer

- Defines data formats, encryption, compression, and conversions for application data.
- Ensures that data sent by one application can be read by another, even if they use different data representations.
- Responsible for translating data between different formats and encodings.

### Application Layer

- Serves as the interface for network services to applications, such as email, file transfer, and web browsing.
- Provides services directly to the application processes, such as file transfer, directory services, and electronic mail.
- Defines protocols for specific applications, such as HTTP for web browsing and SMTP for email.

The OSI reference model provides a standardized framework for network communication, allowing devices from different vendors to interoperate. While not all networks strictly follow the OSI model, it serves as a conceptual guide for understanding the functions and interactions of various network components.

## 5) Give differences between Connection oriented versus Connection less services

Connection-oriented and connectionless services are two fundamental approaches to data transmission in networking. Each has distinct characteristics, advantages, and use cases. Here’s a detailed comparison of the two:

### Connection-Oriented Services

#### Definition

Connection-oriented services establish a dedicated communication path between the sender and receiver before any data is transmitted. This means that a connection is established, maintained, and terminated explicitly.

#### Characteristics

- **Connection Establishment**: A handshake process is used to establish a connection before data transfer begins. This typically involves exchanging control messages to negotiate parameters.
- **Reliability**: These services often provide error detection and correction, ensuring that data is delivered accurately and in the correct order.
- **Flow Control**: Mechanisms are in place to manage the rate of data transmission between sender and receiver, preventing overwhelming the receiver.
- **Resource Reservation**: Network resources (like bandwidth) may be reserved for the duration of the connection.

#### Examples

- **Protocols**: TCP (Transmission Control Protocol) is a primary example of a connection-oriented protocol, commonly used for applications requiring reliable communication, such as web browsing (HTTP) and file transfers (FTP).
- **Use Cases**: Suitable for applications where reliability and order are crucial, such as video conferencing, online gaming, and financial transactions.

#### Advantages

- Ensures reliable data delivery.
- Maintains the order of packets.
- Provides flow control and congestion management.

#### Disadvantages

- More overhead due to connection setup and teardown.
- Slower initial communication due to the handshake process.
- Resource-intensive, as it requires maintaining state information.

### Connectionless Services

#### Definition

Connectionless services allow data to be sent without establishing a dedicated end-to-end connection. Each packet is treated independently and may take different paths to reach the destination.

#### Characteristics

- **No Connection Establishment**: Data packets are sent without prior setup, meaning there is no handshake process.
- **Best Effort Delivery**: These services do not guarantee delivery, order, or error correction. Packets may arrive out of order or not at all.
- **No Resource Reservation**: Network resources are not reserved for the duration of the transmission, allowing for more flexible communication.

#### Examples

- **Protocols**: UDP (User Datagram Protocol) is a key example of a connectionless protocol, commonly used for applications where speed is more critical than reliability, such as streaming media and online gaming.
- **Use Cases**: Suitable for applications that can tolerate some data loss or require low latency, such as VoIP (Voice over Internet Protocol) and real-time video streaming.

#### Advantages

- Lower overhead due to the absence of connection management.
- Faster data transmission since there is no initial handshake.
- More efficient use of network resources.

#### Disadvantages

- No guarantee of delivery or order, which can lead to data loss or corruption.
- Lack of flow control may lead to network congestion.

## Summary of Differences

| Feature                      | Connection-Oriented Services          | Connectionless Services          |
| ---------------------------- | ------------------------------------- | -------------------------------- |
| **Connection Establishment** | Yes (requires handshake)              | No (no prior setup)              |
| **Reliability**              | High (error detection and correction) | Low (best-effort delivery)       |
| **Flow Control**             | Yes                                   | No                               |
| **Resource Reservation**     | Yes                                   | No                               |
| **Examples**                 | TCP                                   | UDP                              |
| **Use Cases**                | File transfers, web browsing          | Streaming, gaming                |
| **Overhead**                 | Higher (due to connection management) | Lower (no connection management) |
| **Speed**                    | Slower (due to setup time)            | Faster (no setup time)           |

In conclusion, the choice between connection-oriented and connectionless services depends on the specific requirements of the application, including the need for reliability, speed, and resource management.

## 6) Explain TCP/IP Reference Model.

The TCP/IP (Transmission Control Protocol/Internet Protocol) reference model is a foundational framework that guides the design and implementation of network protocols used in the Internet and similar networks. It consists of four layers, each with specific functions and responsibilities. Here’s a detailed explanation of the TCP/IP reference model:

### TCP/IP Reference Model Layers

#### 1. Application Layer

- **Functionality**: This layer provides network services directly to user applications. It enables communication between software applications and the underlying network.
- **Protocols**: Common protocols include:
  - **HTTP/HTTPS**: For web browsing.
  - **FTP**: For file transfer.
  - **SMTP/IMAP/POP3**: For email services.
- **Responsibilities**: The Application layer handles user interface and application-level protocols, ensuring that data is formatted correctly for communication.

#### 2. Transport Layer

- **Functionality**: This layer is responsible for end-to-end communication, reliability, and flow control between devices. It ensures that data is delivered error-free and in the correct sequence.
- **Protocols**: Key protocols include:
  - **TCP (Transmission Control Protocol)**: Provides reliable, connection-oriented communication with error recovery and flow control.
  - **UDP (User Datagram Protocol)**: Offers a connectionless, faster service without guaranteed delivery, suitable for applications like streaming and gaming.
- **Responsibilities**: The Transport layer segments data from the Application layer, manages data flow, and ensures reliable communication.

#### 3. Internet Layer

- **Functionality**: This layer is responsible for logical addressing and routing of data packets across the network. It determines the best path for data to travel from the source to the destination.
- **Protocols**: The primary protocol is:
  - **IP (Internet Protocol)**: Responsible for addressing and routing packets. Variants include IPv4 and IPv6.
- **Responsibilities**: The Internet layer encapsulates packets into datagrams, adds source and destination IP addresses, and handles packet routing through routers.

#### 4. Link Layer (Network Interface Layer)

- **Functionality**: This layer deals with the physical transmission of data over various types of physical media. It provides the means for data transfer between adjacent network nodes.
- **Protocols**: Examples include:
  - **Ethernet**: A common LAN technology.
  - **Wi-Fi**: Wireless networking technology.
  - **PPP (Point-to-Point Protocol)**: Used for direct connections between two nodes.
- **Responsibilities**: The Link layer manages the physical addressing (MAC addresses), frames data for transmission, and handles error detection and correction at the physical level.

## Summary of the TCP/IP Model Layers

| Layer                 | Functionality                                         | Key Protocols               |
| --------------------- | ----------------------------------------------------- | --------------------------- |
| **Application Layer** | Provides network services to applications             | HTTP, FTP, SMTP, IMAP, POP3 |
| **Transport Layer**   | Ensures reliable communication and data integrity     | TCP, UDP                    |
| **Internet Layer**    | Manages addressing and routing of packets             | IP (IPv4, IPv6)             |
| **Link Layer**        | Handles physical data transmission over various media | Ethernet, Wi-Fi, PPP        |

## Conclusion

The TCP/IP reference model is essential for understanding how data is transmitted over networks, particularly the Internet. Its layered architecture allows for modular design, facilitating the development and interoperability of network protocols. Each layer has specific roles, ensuring efficient and reliable communication between devices in a networked environment.

## 7) Discuss the parity checks for error detection in data transfer.

Parity checks are a simple and widely used method for error detection in data transmission. They involve adding an extra bit, known as a parity bit, to a binary message to help determine whether the data has been transmitted correctly. Here’s a detailed overview of parity checks, including their types, functionality, advantages, and limitations.

### What is Parity Check?

A parity check adds a single bit to a string of binary data to make the total number of 1s either even or odd. This method helps in detecting errors that may occur during data transmission.

#### Types of Parity Checks

1. **Even Parity**
   - In even parity, the parity bit is set so that the total number of 1s in the data, including the parity bit, is even.
   - For example, if the data to be transmitted is `1011001` (which contains four 1s), the parity bit would be `0` (making the total number of 1s still even). If the data were `1011011` (which contains five 1s), the parity bit would be `1` (making the total number of 1s six, which is even).
2. **Odd Parity**
   - In odd parity, the parity bit is set so that the total number of 1s in the data, including the parity bit, is odd.
   - Using the same examples, for `1011001`, the parity bit would be `1` (making the total number of 1s five, which is odd), and for `1011011`, the parity bit would be `0` (keeping the total number of 1s five, which is odd).

#### Functionality of Parity Checks

- **Error Detection**: When the data is received, the receiver checks the number of 1s in the received data, including the parity bit. If the count does not match the expected parity (even or odd), an error is detected.
- **Simplicity**: Parity checks are simple to implement and require minimal additional computation, making them suitable for many applications, especially in low-error environments.

#### Advantages of Parity Checks

- **Simplicity**: Easy to implement in hardware and software.
- **Low Overhead**: Requires only one additional bit for each byte of data, making it efficient in terms of bandwidth.
- **Quick Error Detection**: Can quickly identify single-bit errors.

#### Limitations of Parity Checks

- **Limited Error Detection**: Parity checks can only detect an odd number of bit errors. If two bits are flipped (or any even number), the parity will still appear correct, and the error will go undetected.
- **No Error Correction**: Parity checks can indicate that an error has occurred but do not provide information on how to correct it.
- **Not Suitable for High-Reliability Applications**: In environments where data integrity is critical, such as financial transactions or medical data, more robust error detection and correction methods (like checksums or cyclic redundancy checks) are preferred.

## Conclusion

Parity checks are a fundamental method for error detection in data transmission, providing a simple way to check for single-bit errors. While they are easy to implement and require minimal overhead, their limitations in detecting multiple-bit errors and lack of correction capabilities make them less suitable for high-reliability applications. Understanding parity checks is essential for grasping the basic principles of data integrity in communication systems.

## 8) Explain framing and design issues in data link layer.

The data link layer is responsible for reliable and error-free data transfer between directly connected devices. One of its key functions is framing, which involves encapsulating the data from the network layer into frames. Here are the key aspects of framing and some design issues in the data link layer:

### Framing

- The data link layer takes the data from the network layer and adds header and trailer information to create a frame.
- The header typically contains source and destination addresses, control information, and synchronization bits.
- The trailer usually contains error detection and correction codes like CRC (Cyclic Redundancy Check).
- Framing allows the receiver to identify the beginning and end of each frame.
- Common framing methods include character count, flag bytes with byte stuffing, and bit stuffing.

#### Character Count Framing

- The header includes a count of the number of characters in the frame.
- The receiver knows the frame size in advance and can locate the end of the frame.
- If a character is lost or added, the count will be wrong, and the receiver will be unable to locate subsequent frames.

#### Flag Bytes with Byte Stuffing

- A special byte (flag) is used to mark the beginning and end of the frame.
- If the flag byte appears in the data, it is escaped or stuffed by adding a special byte before it.
- The receiver unstuffs the byte before processing the data.
- Byte stuffing can be inefficient if flags appear frequently in the data.

#### Bit Stuffing

- Instead of bytes, a sequence of bits (e.g., 01111110) is used as the flag.
- If this sequence appears in the data, an extra 0 is inserted after five consecutive 1s.
- The receiver detects the extra 0 and removes it.
- Bit stuffing is more efficient than byte stuffing but requires more processing.

### Design Issues in the Data Link Layer

1. **Error Detection and Correction**
   - Errors can occur due to noise, collisions, or equipment failure.
   - Techniques like parity checks, checksums, and CRC are used for error detection.
   - Error correction can be achieved through retransmission (ARQ protocols) or adding redundant bits (FEC).
2. **Flow Control**
   - Ensures that a fast sender does not overwhelm a slow receiver.
   - Methods include stop-and-wait, sliding window, and rate-based protocols.
3. **Media Access Control (MAC)**
   - Determines how devices share the transmission medium in a multiple access network.
   - Protocols like CSMA/CD (Ethernet) and token passing (Token Ring) are used.
4. **Addressing**
   - MAC addressing is used to identify devices on a local network.
   - MAC addresses are typically 48 bits long and are burned into the network interface card.
5. **Logical Link Control (LLC)**
   - Provides a standard interface to the network layer above.
   - Responsible for flow control, error checking, and frame synchronization.

In summary, framing is a crucial function of the data link layer, and various techniques like character count, flag bytes, and bit stuffing are used to implement it. The data link layer also deals with error detection and correction, flow control, media access control, addressing, and logical link control, all of which are important design considerations.

## 9) What is bit and byte stuffing? Explain with example.

Bit stuffing and byte stuffing are techniques used in data communication to ensure that special control characters used for framing do not appear in the data being transmitted. These methods help maintain the integrity of the data and prevent confusion between data and control information.

### Bit Stuffing

#### Definition

Bit stuffing is a technique where extra bits are inserted into the data stream to prevent the occurrence of a specific bit pattern that signifies the start or end of a frame. This is particularly useful in protocols that use a specific sequence of bits as a flag to indicate the boundaries of frames.

#### How It Works

- A predefined bit pattern (for example, `01111110`) is used as a flag to denote the beginning and end of a frame.
- If the data being transmitted contains five consecutive `1`s, a `0` is inserted after these five `1`s to prevent the flag from being misinterpreted as part of the data.
- The receiver, upon detecting five consecutive `1`s, knows to expect a `0` next and removes it before processing the data.

#### Example

Assume we want to transmit the following data: `111110111`. The flag for the frame is `01111110`.

1. Original Data: `111110111`
2. After Bit Stuffing: `1111100 111` (A `0` is added after the five `1`s)

When the receiver processes the data, it will see `1111100 111` and recognize the stuffed bit, removing it to retrieve the original data.

### Byte Stuffing

#### Definition

Byte stuffing is a method where a special byte (often a flag byte) is used to indicate the start and end of a frame. If the data contains the flag byte, it is escaped by inserting an additional byte before it.

#### How It Works

- A specific byte (e.g., `0x7E`) is used as a flag to mark the beginning and end of a frame.
- If the data contains the flag byte, it is replaced with an escape byte (e.g., `0x7D`) followed by a modified version of the flag byte.
- The receiver knows to look for the escape byte and correctly reconstructs the original data.

#### Example

Assume we want to transmit the following data: `0x7E 0x45 0x7E`. The flag for the frame is `0x7E`.

1. Original Data: `0x7E 0x45 0x7E`
2. After Byte Stuffing: `0x7D 0x5E 0x45 0x7D 0x5E` (The `0x7E` bytes are replaced with `0x7D` followed by `0x5E`, where `0x5E` is the modified version of the flag)

When the receiver processes the data, it will see `0x7D 0x5E 0x45 0x7D 0x5E`, recognize the escape sequences, and reconstruct the original data.

## Summary

- **Bit Stuffing**: Inserts a `0` after five consecutive `1`s to prevent confusion with frame delimiters.
- **Byte Stuffing**: Uses an escape byte to modify flag bytes that may appear in the data, ensuring that the data is transmitted correctly without misinterpretation.

Both techniques are essential for maintaining data integrity in communication protocols, allowing for reliable data transfer without errors caused by special control characters.

## 10) Compute CRC for a data sequence 10110111 for which the generator is 110011.

To compute the CRC (Cyclic Redundancy Check) for the data sequence `10110111` using the generator `110011`, we will follow these steps:

1. **Append Zeros**: Append a number of zeros to the end of the data sequence equal to the length of the generator minus one. The generator `110011` has a length of 6, so we append 5 zeros to the data sequence.
   - Data sequence: `10110111`
   - Appended data: `1011011100000`
2. **Binary Division**: Perform binary division of the appended data by the generator using XOR operations. The division process is similar to long division in decimal, but we use XOR instead of subtraction.

### Step-by-Step Calculation

1. **Initial Setup**:
   - Data: `1011011100000`
   - Generator: `110011`
2. **Performing the Division**:
   - Align the generator with the leftmost bits of the data.
   - Perform XOR operation and bring down the next bit, repeating until all bits have been processed.

### Division Process

- Initial Data: `1011011100000`
- Generator: `110011`

**1st Step**:

```
  1011011100000
- 110011
-----------
  011010

```

**2nd Step** (bring down the next bit):

```
  0110100
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0110100

```

**3rd Step**:

```
  0110100
- 110011
-----------
  001111

```

**4th Step** (bring down the next bit):

```
  0011110
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0011110

```

**5th Step**:

```
  0011110
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0011110

```

**6th Step**:

```
  0011110
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0011110

```

**7th Step**:

```
  0011110
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0011110

```

**8th Step**:

```
  0011110
- 110011
-----------
  000100

```

**9th Step** (bring down the next bit):

```
  0001000
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0001000

```

**10th Step**:

```
  0001000
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0001000

```

**11th Step**:

```
  0001000
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0001000

```

**12th Step**:

```
  0001000
- 0000000 (no XOR since generator can't be subtracted)
-----------
  0001000

```

**Final Remainder**: After processing all bits, the remainder is `000100`.

### Final CRC Calculation

The CRC is the remainder obtained after the division. Since we appended 5 zeros initially, the CRC will be the last few bits of the result. The remainder `000100` is the CRC.

### Conclusion

The CRC for the data sequence `10110111` using the generator `110011` is `000100`. Therefore, the complete transmitted data would be `10110111` followed by the CRC `000100`, resulting in `10110111000100`.
