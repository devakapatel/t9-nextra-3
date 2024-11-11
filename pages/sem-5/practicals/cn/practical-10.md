# Practical 10

### AIM:
To configure routers using the Border Gateway Protocol (BGP) to establish inter-domain routing between different autonomous systems (AS) in a network.

---

### Introduction to BGP:
**Border Gateway Protocol (BGP)** is a path-vector routing protocol crucial for routing data across different autonomous systems (AS) on the Internet. It enables routing information exchange on a global scale, making it the backbone of the Internet's routing structure.

**Advantages of BGP:**
- **Inter-domain Routing:** Essential for routing between different ASes, enabling global Internet connectivity.
- **Control over Routing Decisions:** Allows administrators to implement complex policies, offering fine control over data flow.
- **Robustness and Stability:** BGP is resilient to network changes, ensuring stable routing in dynamic environments.

**Disadvantages of BGP:**
- **Complex Configuration:** More complicated than IGPs like OSPF and RIP, requiring careful management.
- **Slow Convergence:** BGP may take longer to adapt to network changes, potentially causing temporary routing issues.
- **Resource Intensive:** Requires significant CPU and memory, especially in networks with numerous routes.

---

### Step-by-Step Configuration:

#### Step 1: Create the Network Topology
1. **Open Cisco Packet Tracer** and select the necessary devices.
2. Arrange devices to form the desired network topology.

#### Step 2: Configure PCs (Hosts) with IPv4 Addresses
1. For each PC, go to **Desktop > IP Configuration**.
2. Assign the **IPv4 address** and **Subnet Mask** as specified in the IP addressing table.
3. To verify IP settings, use the `ipconfig` command or configure directly in the command terminal:
   ```plaintext
   ipconfig <IPv4 address> <subnet mask> <default gateway>
   ```

#### Step 3: Configure Router with IP Address and Subnet Mask
1. Select Router0, go to **Config > Interfaces**.
2. Ensure that all required ports are enabled.
3. Assign IP addresses to the **FastEthernet** and **Serial ports** based on the IP addressing table.

#### Code: BGP Configuration for Routers

**Router 0 Configuration:**
```plaintext
Router(config)# router bgp 100
Router(config-router)# network 192.168.1.0
Router(config-router)# network 192.168.2.0
Router(config-router)# neighbor 192.168.2.3 remote-as 200
Router(config-router)# neighbor 192.168.3.2 remote-as 200
Router(config-router)# exit
```

**Router 1 Configuration:**
```plaintext
Router(config)# router bgp 200
Router(config-router)# network 192.168.2.0
Router(config-router)# network 192.168.3.0
Router(config-router)# neighbor 192.168.2.2 remote-as 100
Router(config-router)# neighbor 192.168.1.2 remote-as 200
Router(config-router)# exit
```

---

#### Step 4: Assign Routes to Routers
1. After configuring all devices, assign BGP routes for each router.
2. For each router, go to **CLI**, and type the relevant commands to assign routes:
   ```plaintext
   network <network id>
   ```

---

### Summary
This practical demonstrates the configuration of routers using BGP, highlighting how it enables efficient, inter-domain routing on the Internet, providing control over routing policies, and supporting stability in large networks.