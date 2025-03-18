# Practical 5

### AIM:
To demonstrate various networking and internetworking devices and topologies.

### Networking and Internetworking Devices

1. **Network Interface Card (NIC)**  
   A hardware component that enables a device to connect to a network, providing a unique MAC address for identification. NICs can be wired (Ethernet) or wireless (Wi-Fi).
   - **Advantages**:
     - Unique identification with a MAC address.
     - Supports both wired and wireless connectivity.
     - High data rate, improving network performance.
   - **Disadvantages**:
     - Additional cost for each network-enabled device.
     - May face compatibility issues with certain network standards.

2. **Switch**  
   Connects multiple devices within a local area network (LAN) and forwards data based on MAC addresses.
   - **Advantages**:
     - Efficient data handling reduces traffic and collisions.
     - Increased bandwidth with dedicated ports.
     - Scalable by adding more ports or switches.
   - **Disadvantages**:
     - Higher cost than hubs.
     - Complex configuration for managed switches.

3. **Hub**  
   A basic networking device that connects multiple Ethernet devices, broadcasting incoming data to all connected devices.
   - **Advantages**:
     - Simple and easy to set up.
     - Low cost.
   - **Disadvantages**:
     - Inefficient due to data broadcasting, leading to collisions.
     - Limited functionality and scalability.

4. **Router**  
   Connects multiple networks and directs data based on IP addresses.
   - **Advantages**:
     - Connects multiple networks efficiently.
     - Can manage traffic and includes security features like firewalls.
   - **Disadvantages**:
     - Complex configuration.
     - Higher cost compared to simpler devices.

5. **Gateway**  
   Acts as a bridge between networks with different protocols, enabling communication and data exchange.
   - **Advantages**:
     - Supports communication between networks with different protocols.
     - Can filter data for enhanced security.
   - **Disadvantages**:
     - Complex setup.
     - Performance overhead due to protocol translation.

6. **Repeater**  
   Extends the range of a network by amplifying signals.
   - **Advantages**:
     - Cost-effective way to boost network signal.
     - Simple to install.
   - **Disadvantages**:
     - Limited functionality (no traffic management).
     - May introduce noise if amplifying weak signals.

7. **Bridge**  
   Connects two or more network segments, allowing them to function as one network.
   - **Advantages**:
     - Reduces traffic by segmenting networks.
     - Improves performance for larger networks.
   - **Disadvantages**:
     - Limited range and primarily effective within a single network.

8. **Cables**  
   Physical media for data transmission; types include Ethernet cables, fiber optic, and coaxial cables.
   - **Advantages**:
     - Reliable and stable connections.
     - Variety of options suitable for different requirements.
   - **Disadvantages**:
     - Limited by physical distance.
     - Installation can be complex, especially for fiber optics.

### Network Topologies

1. **Bus Topology**  
   All devices connect to a single central cable, which is bi-directional. It is vulnerable to failure if the backbone cable breaks.

2. **Star Topology**  
   Devices connect to a central hub, which acts as the main point of communication. The hub can be passive or active.

3. **Ring Topology**  
   Forms a closed loop where each device is connected to two neighboring devices. Repeaters are often required for large networks.

4. **Mesh Topology**  
   Each device has a dedicated link to other devices, ensuring high redundancy and reliability. Protocols include AHCP and DHCP.

5. **Tree Topology**  
   A hierarchical structure similar to star topology but with multiple levels. Common protocols are DHCP and SAC (Standard Automatic Configuration).

6. **Hybrid Topology**  
   Combines different types of topologies, allowing flexible and scalable network design.