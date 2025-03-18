# Practical 4

### AIM:
To compare the OSI and TCP/IP protocol models.

### OSI Model
The **OSI (Open Systems Interconnection) model** is a seven-layer framework that defines how data is transmitted across a network, providing a theoretical foundation for understanding network communication. Created by the **International Organization for Standardization (ISO)** in 1984, the OSI model is non-proprietary and divides communication tasks into the following layers:

1. **Physical Layer**
2. **Data Link Layer**
3. **Network Layer**
4. **Transport Layer**
5. **Session Layer**
6. **Presentation Layer**
7. **Application Layer**

The OSI model is generally not implemented fully in real-world networking hardware or software but serves as a conceptual guideline for network architecture and protocol design.

### TCP/IP Model
The **TCP/IP (Transmission Control Protocol/Internet Protocol) model** is a four-layer framework essential for data communication over networks, especially the Internet. Developed by the **Department of Defense (DoD)** in the 1960s, it simplifies communication into four layers:

1. **Link Layer**
2. **Internet Layer**
3. **Transport Layer**
4. **Application Layer**

Unlike the OSI model, TCP/IP is widely implemented in practical networking systems, focusing on ensuring reliable and accurate data transmission across devices.

### Comparison Between OSI and TCP/IP Models

| SR. NO | OSI Model (Open System Interconnection)                           | TCP/IP Model (Transmission Control Protocol)                          |
|--------|--------------------------------------------------------------------|------------------------------------------------------------------------|
| 1      | Stands for Open System Interconnection.                           | Stands for Transmission Control Protocol.                              |
| 2      | Comprises seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application. | Comprises four layers: Link, Internet, Transport, and Application.      |
| 3      | Less commonly used in practical applications.                     | Widely used, especially for Internet communications.                   |
| 4      | Transport layer ensures packet delivery.                          | Transport layer does not ensure packet delivery.                       |
| 5      | Follows a vertical approach.                                      | Follows a horizontal approach.                                         |
| 6      | Easier to replace or update components.                           | Components are more difficult to replace compared to OSI.              |
| 7      | Serves as a reference model for network design and protocols.     | An implemented model of OSI, providing practical network functionality. |
| 8      | Network layer offers both connection-oriented and connectionless services. | Network layer provides only connectionless services.                    |
| 9      | Less reliable due to theoretical design.                          | More reliable, with protocols that directly support implementation.    |
| 10     | Standardizes hardware like routers, switches, and motherboards.   | Focuses on creating connections between devices without hardware standardization. |
| 11     | Distinguishes between services, protocols, and interfaces.        | Does not distinguish between services, protocols, and interfaces.      |
