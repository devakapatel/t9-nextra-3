# Practical 8

### AIM:
To configure routers using the RIP (Routing Information Protocol) for effective data packet routing.

### Introduction to RIP:
**Routing Information Protocol (RIP)** is a distance-vector routing protocol used primarily in smaller local and wide area networks. It enables routers to exchange routing information based on the hop count, guiding packets along the best available paths.

**Advantages of RIP:**
- **Simplicity:** Easy to configure, suitable for smaller networks.
- **Standardized Protocol:** Supported across various devices and platforms.
- **Low Overhead:** Minimal processing requirements using simple metrics.

**Disadvantages of RIP:**
- **Limited Scalability:** Maximum hop count of 15, making it unsuitable for large networks.
- **Slow Convergence:** Delays in propagating updates may cause temporary routing loops or outages.
- **Inefficient Routing:** Routes solely based on hop count, ignoring bandwidth or latency, which can lead to suboptimal routing.

### Step-by-Step Configuration:

#### Step 1: Configuring Routers

**Router 1 Configuration:**
1. **Open CLI** on Router 1 and press `ENTER` to begin configuration.
2. Type `enable` to activate privileged mode.
3. Type `config t` (configure terminal) to access the configuration menu.
4. Configure RIP protocol and assign networks:
    ```plaintext
    Router(config)# router rip
    Router(config-router)# network 192.168.1.0
    Router(config-router)# network 10.0.0.0
    Router(config-router)# exit
    ```

**Router 2 Configuration:**
1. Follow steps similar to Router 1 to enter CLI and configuration mode.
2. Configure RIP protocol and assign networks:
    ```plaintext
    Router(config)# router rip
    Router(config-router)# network 192.168.2.0
    Router(config-router)# network 10.0.0.0
    Router(config-router)# exit
    ```

#### Step 2: Configuring PCs

1. **Assign IP Addresses** to each PC in the network.
2. For each PC:
   - Go to **Desktop > IP Configuration**.
   - Assign an **IP address**, **Default Gateway**, and **Subnet Mask**.
3. Example Configuration:
   - PC0 Default Gateway: `192.168.10.1`
   - PC1 Default Gateway: `192.168.20.1`

#### Step 3: Connecting PCs to the Router

1. **PC0**: Connect the **FastEthernet0** port on PC0 to the **FastEthernet0/0** port on Router 1 using a copper straight-through cable.
2. **PC1**: Connect the **FastEthernet0** port on PC1 to the **FastEthernet0/1** port on Router 1 using a copper straight-through cable.
