# Practical 1

### AIM:

To study different types of network topologies.

**Network topology** defines the arrangement of elements like nodes, links, and devices in a computer network, establishing how these components connect and interact.

### Types of Network Topologies

### 1. Point-to-Point Topology

A direct connection between two nodes (sender and receiver) that enables high-bandwidth data transfer.

- **Advantages:**
    - Provides a dedicated channel for fast data transfer.
    - Simplifies troubleshooting since each node or connection can be tested individually.
    - Offers high security with direct data transmission, reducing data interception risks.
    - Performs well in high-traffic networks, with no intermediate nodes causing delays.
- **Disadvantages:**
    - Adding new devices is complex and costly due to the need for a separate link.
    - Lack of alternative routes can lead to disruptions if a link fails.
    - Unsuitable for large networks due to direct connection requirements.

### 2. Mesh Topology

Each device is connected to every other device, allowing for fast, reliable data transfer. Protocols like AHCP and DHCP are commonly used.

- **Advantages:**
    - Provides fast communication between nodes.
    - High robustness and easy fault diagnosis.
    - Reliable due to dedicated communication links.
    - Ensures privacy and security.
- **Disadvantages:**
    - Installation and configuration are challenging.
    - High cable costs make it suitable only for small networks.
    - High maintenance costs.

### 3. Star Topology

All devices connect to a central hub, which can be passive or active (with repeaters). Commonly uses Ethernet LAN protocols like CSMA.

- **Advantages:**
    - Only N cables are required for N devices.
    - Robust, as failure in one link only affects that link.
    - Easy fault identification and isolation.
    - Cost-effective, using inexpensive coaxial cable.
- **Disadvantages:**
    - Central hub failure crashes the entire network.
    - High installation costs.
    - Network performance depends on the hub.

### 4. Bus Topology

A single cable connects all devices. Common in smaller networks, it uses MAC protocols like CSMA/CD.

- **Advantages:**
    - Only one cable is needed for multiple devices.
    - Uses low-cost coaxial or twisted-pair cables, supporting up to 10 Mbps.
    - Simple and cost-effective for small networks.
- **Disadvantages:**
    - Heavy cabling is still required.
    - Network failure occurs if the common cable fails.
    - Increased collisions with high traffic.
    - Low security and slower performance with added devices.

### 5. Ring Topology

Forms a ring with each device connected to two neighboring devices, often with repeaters for large setups. Data flows in one or both directions.

- **Advantages:**
    - High-speed data transmission.
    - Minimal collision risk.
    - Inexpensive to install and expand.
    - More affordable than star topology.
- **Disadvantages:**
    - A single node failure can crash the network.
    - Troubleshooting can be challenging.
    - Adding or removing nodes disrupts the network.
    - Limited security.

### 6. Tree Topology

A variation of Star topology with a hierarchical data flow, using protocols like DHCP. Secondary hubs connect to a central hub.

- **Advantages:**
    - Supports more devices on a single hub.
    - Enables network isolation and prioritization.
    - Allows easy addition of devices.
    - Simple error detection and correction.
- **Disadvantages:**
    - Central hub failure affects the entire network.
    - High cabling costs.
    - Complex reconfiguration with new devices.

### 7. Hybrid Topology

A combination of multiple topologies, offering flexibility for network expansion.

- **Advantages:**
    - Highly flexible and adaptable.
    - Easy network expansion by adding new devices.
- **Disadvantages:**
    - Complex architecture design.
    - Expensive hubs.
    - High infrastructure costs due to extensive cabling.