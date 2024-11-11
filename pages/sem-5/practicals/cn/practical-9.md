# Practical 9

### AIM:
To configure routers using the OSPF (Open Shortest Path First) protocol to establish efficient routing in IP networks.

---

### Introduction to OSPF:
**Open Shortest Path First (OSPF)** is a link-state routing protocol designed for IP networks, enabling routers to exchange link information and determine optimal paths for data packets based on a cost metric that considers bandwidth.

**Advantages of OSPF:**
- **Scalability:** Supports large, complex networks through its hierarchical structure and multi-area support.
- **Efficiency:** Uses a cost metric to select routes based on link performance, improving overall routing efficiency.
- **Robustness:** Quickly adapts to network changes, minimizing downtime and maintaining stability.

**Disadvantages of OSPF:**
- **Complex Configuration:** More challenging to set up than simpler protocols like RIP, requiring careful configuration.
- **Resource Intensive:** Consumes more CPU and memory resources due to its detailed network state management.

---

### Step-by-Step Configuration:

#### Step 1: Create the Network Topology
1. **Open Cisco Packet Tracer** and select the required network devices.
2. Arrange the devices to create the network topology.

#### Step 2: Configure PCs (Hosts) with IPv4 Addresses
1. Select each PC, go to **Desktop > IP Configuration**.
2. Assign an **IPv4 address** and **Subnet Mask** according to the IP addressing table.
3. Optionally, assign a **Default Gateway** for each PC.
4. To verify the IP configuration, use the command `ipconfig` or configure directly in the terminal:
   ```plaintext
   ipconfig <IPv4 address> <Subnet mask> <Default gateway>
   ```

#### Step 3: Configure Router with IP Address and Subnet Mask
1. To assign IP addresses in Router0, click on Router0 and navigate to **Config > Interfaces**.
2. Ensure all relevant ports are enabled.
3. Assign IP addresses to the **FastEthernet** and **Serial ports** as per the IP addressing table.

#### Code: OSPF Configuration for Routers

**Router 0 Configuration:**
```plaintext
Router(config)# router ospf 1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Router(config-router)# network 10.0.0.0 0.255.255.255 area 0
Router(config-router)# network 12.0.0.0 0.255.255.255 area 0
Router(config-router)# exit
```

**Router 1 Configuration:**
```plaintext
Router(config)# router ospf 1
Router(config-router)# network 10.0.0.0 0.255.255.255 area 0
Router(config-router)# network 11.0.0.0 0.255.255.255 area 0
Router(config-router)# exit
```

**Router 2 Configuration:**
```plaintext
Router(config)# router ospf 1
Router(config-router)# network 192.168.2.0 0.0.0.255 area 0
Router(config-router)# network 11.0.0.0 0.255.255.255 area 0
Router(config-router)# network 12.0.0.0 0.255.255.255 area 0
Router(config-router)# exit
```

---

#### Step 4: Assign Routes to Routers
1. After configuring all devices, assign routes for each router.
2. For each router, access the **CLI**, then type the relevant network commands to assign routes:
   ```plaintext
   network <network id>
   ```

---

### Summary
This practical demonstrates the configuration of routers using OSPF, showcasing how routers can efficiently exchange link information and make optimal routing decisions across IP networks.