# Assignment 2 sums

## 10) Find the subnet mask, network ID, subnet address, broadcast ID and the host range from the following IP address.

A) 192.168.30.112/28, B) 172.160.16.224/20 C) 11.11.108.96/22.

Here’s how you can calculate the subnet mask, network ID, subnet address, broadcast ID, and host range for each of the given IP addresses:

#### A) 192.168.30.112/28

1. Subnet Mask:

   CIDR /28 means 28 bits for the network, so the subnet mask is `255.255.255.240`.

2. Network ID:

   `192.168.30.112` in binary is `11000000.10101000.00011110.01110000`.

   Applying the /28 mask, the first 28 bits remain unchanged, and the remaining bits are set to 0, giving the Network ID as `192.168.30.112`.

3. Subnet Address:

   Same as the network ID in this case: `192.168.30.112`.

4. Broadcast Address:

   Set the host bits to 1, which means the last 4 bits are `1111`. The broadcast address is `192.168.30.127`.

5. Host Range:

   The first usable address is `192.168.30.113` (Network ID + 1).

   The last usable address is `192.168.30.126` (Broadcast Address - 1).

   So, the host range is `192.168.30.113 - 192.168.30.126`.

#### B) 172.160.16.224/20

1. Subnet Mask:

   CIDR /20 means 20 bits for the network, so the subnet mask is `255.255.240.0`.

2. Network ID:

   `172.160.16.224` in binary is `10101100.10100000.00010000.11100000`.

   Applying the /20 mask, the first 20 bits remain unchanged, and the remaining bits are set to 0, giving the Network ID as `172.160.16.0`.

3. Subnet Address:

   Same as the network ID in this case: `172.160.16.0`.

4. Broadcast Address:

   Set the host bits to 1, meaning the last 12 bits are `11111111.11111111`. The broadcast address is `172.160.31.255`.

5. Host Range:

   The first usable address is `172.160.16.1` (Network ID + 1).

   The last usable address is `172.160.31.254` (Broadcast Address - 1).

   So, the host range is `172.160.16.1 - 172.160.31.254`.

#### C) 11.11.108.96/22

1. Subnet Mask:

   CIDR /22 means 22 bits for the network, so the subnet mask is `255.255.252.0`.

2. Network ID:

   `11.11.108.96` in binary is `00001011.00001011.01101100.01100000`.

   Applying the /22 mask, the first 22 bits remain unchanged, and the remaining bits are set to 0, giving the Network ID as `11.11.108.0`.

3. Subnet Address:

   Same as the network ID in this case: `11.11.108.0`.

4. Broadcast Address:

   Set the host bits to 1, meaning the last 10 bits are `11111111.11111111`. The broadcast address is `11.11.111.255`.

5. Host Range:

   The first usable address is `11.11.108.1` (Network ID + 1).

   The last usable address is `11.11.111.254` (Broadcast Address - 1).

   So, the host range is `11.11.108.1 - 11.11.111.254`.

These are the network details for each of the given IP addresses.

## 11) A company has three networks into three different cities, namely Ahmedabad Delhi and Chennai Ahmedabad has three branches. A has 120 PCs, B has 170 PCs and C has 60 PCs. Delhi branch has 29 PC and 14 PC respectively and Chennai branch has 14 ,6 and 4 PC respectively. Determine the IP address scheme using VLSM and submitting summaries of the design in tabular form. Use class C Private address for the Design.

To design an IP address scheme using VLSM (Variable Length Subnet Masking) for the given setup, we will:

1. Use a Class C private IP address range: `192.168.0.0/24`.
2. Subdivide this address space to allocate IP addresses efficiently based on the number of PCs in each branch while reserving addresses for future growth.

---

### Step 1: Calculate the Subnet Requirements

For each branch, calculate the required number of IP addresses (including network and broadcast addresses):

| City/Branch | Number of PCs | Required IPs | Nearest Power of 2 | Subnet Mask           |
| ----------- | ------------- | ------------ | ------------------ | --------------------- |
| Ahmedabad-A | 120           | 122          | 128                | /25 (255.255.255.128) |
| Ahmedabad-B | 170           | 172          | 256                | /24 (255.255.255.0)   |
| Ahmedabad-C | 60            | 62           | 64                 | /26 (255.255.255.192) |
| Delhi-A     | 29            | 31           | 32                 | /27 (255.255.255.224) |
| Delhi-B     | 14            | 16           | 16                 | /28 (255.255.255.240) |
| Chennai-A   | 14            | 16           | 16                 | /28 (255.255.255.240) |
| Chennai-B   | 6             | 8            | 8                  | /29 (255.255.255.248) |
| Chennai-C   | 4             | 6            | 8                  | /29 (255.255.255.248) |

---

### Step 2: Assign Subnets

Allocate the subnets sequentially, starting from `192.168.0.0`.

| City/Branch | Subnet Address | Subnet Mask           | Usable IP Range             | Broadcast Address |
| ----------- | -------------- | --------------------- | --------------------------- | ----------------- |
| Ahmedabad-A | 192.168.0.0    | /25 (255.255.255.128) | 192.168.0.1–192.168.0.126   | 192.168.0.127     |
| Ahmedabad-B | 192.168.0.128  | /24 (255.255.255.0)   | 192.168.0.129–192.168.1.254 | 192.168.1.255     |
| Ahmedabad-C | 192.168.2.0    | /26 (255.255.255.192) | 192.168.2.1–192.168.2.62    | 192.168.2.63      |
| Delhi-A     | 192.168.2.64   | /27 (255.255.255.224) | 192.168.2.65–192.168.2.94   | 192.168.2.95      |
| Delhi-B     | 192.168.2.96   | /28 (255.255.255.240) | 192.168.2.97–192.168.2.110  | 192.168.2.111     |
| Chennai-A   | 192.168.2.112  | /28 (255.255.255.240) | 192.168.2.113–192.168.2.126 | 192.168.2.127     |
| Chennai-B   | 192.168.2.128  | /29 (255.255.255.248) | 192.168.2.129–192.168.2.134 | 192.168.2.135     |
| Chennai-C   | 192.168.2.136  | /29 (255.255.255.248) | 192.168.2.137–192.168.2.142 | 192.168.2.143     |

---

### Step 3: Summary in Tabular Form

| City      | Branch | Subnet Address | Subnet Mask           | Usable IPs                  | Broadcast Address |
| --------- | ------ | -------------- | --------------------- | --------------------------- | ----------------- |
| Ahmedabad | A      | 192.168.0.0    | /25 (255.255.255.128) | 192.168.0.1–192.168.0.126   | 192.168.0.127     |
| Ahmedabad | B      | 192.168.0.128  | /24 (255.255.255.0)   | 192.168.0.129–192.168.1.254 | 192.168.1.255     |
| Ahmedabad | C      | 192.168.2.0    | /26 (255.255.255.192) | 192.168.2.1–192.168.2.62    | 192.168.2.63      |
| Delhi     | A      | 192.168.2.64   | /27 (255.255.255.224) | 192.168.2.65–192.168.2.94   | 192.168.2.95      |
| Delhi     | B      | 192.168.2.96   | /28 (255.255.255.240) | 192.168.2.97–192.168.2.110  | 192.168.2.111     |
| Chennai   | A      | 192.168.2.112  | /28 (255.255.255.240) | 192.168.2.113–192.168.2.126 | 192.168.2.127     |
| Chennai   | B      | 192.168.2.128  | /29 (255.255.255.248) | 192.168.2.129–192.168.2.134 | 192.168.2.135     |
| Chennai   | C      | 192.168.2.136  | /29 (255.255.255.248) | 192.168.2.137–192.168.2.142 | 192.168.2.143     |

---

This design ensures efficient allocation with no wastage of IP addresses and meets the requirements using VLSM.
