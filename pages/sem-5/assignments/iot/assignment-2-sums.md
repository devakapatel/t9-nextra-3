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

---

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

---

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

---

These are the network details for each of the given IP addresses.

## 11) A company has three networks into three different cities, namely Ahmedabad Delhi and Chennai Ahmedabad has three branches. A has 120 PCs, B has 170 PCs and C has 60 PCs. Delhi branch has 29 PC and 14 PC respectively and Chennai branch has 14 ,6 and 4 PC respectively. Determine the IP address scheme using VLSM and submitting summaries of the design in tabular form. Use class C Private address for the Design.

To design an IP addressing scheme using Variable Length Subnet Masking (VLSM) for the company’s networks in Ahmedabad, Delhi, and Chennai, we'll proceed with the following steps:

1. Class C Private IP Address: We'll use the Class C private IP address range of `192.168.x.x`. A Class C address has a default subnet mask of `/24` (i.e., `255.255.255.0`), allowing for 256 total IP addresses per subnet (254 usable addresses).
2. VLSM Subnetting: We’ll allocate subnets based on the number of PCs in each branch and use VLSM to minimize wasted IPs. Each subnet needs at least one IP for the network ID and one for the broadcast address, so we’ll calculate the required subnets accordingly.

#### Step-by-Step Breakdown

#### 1. Ahmedabad Branch (3 branches)

- Branch A: 120 PCs
  Required IPs = 120 + 2 (network and broadcast) = 122
  Nearest power of 2 = 128 (requires 7 bits for hosts)
  Subnet Mask: `/25` (128 addresses)
- Branch B: 170 PCs
  Required IPs = 170 + 2 = 172
  Nearest power of 2 = 256 (requires 8 bits for hosts)
  Subnet Mask: `/24` (256 addresses)
- Branch C: 60 PCs
  Required IPs = 60 + 2 = 62
  Nearest power of 2 = 64 (requires 6 bits for hosts)
  Subnet Mask: `/26` (64 addresses)

#### 2. Delhi Branch (2 branches)

- Branch 1: 29 PCs
  Required IPs = 29 + 2 = 31
  Nearest power of 2 = 32 (requires 5 bits for hosts)
  Subnet Mask: `/27` (32 addresses)
- Branch 2: 14 PCs
  Required IPs = 14 + 2 = 16
  Nearest power of 2 = 16 (requires 4 bits for hosts)
  Subnet Mask: `/28` (16 addresses)

#### 3. Chennai Branch (3 branches)

- Branch 1: 14 PCs
  Required IPs = 14 + 2 = 16
  Nearest power of 2 = 16 (requires 4 bits for hosts)
  Subnet Mask: `/28` (16 addresses)
- Branch 2: 6 PCs
  Required IPs = 6 + 2 = 8
  Nearest power of 2 = 8 (requires 3 bits for hosts)
  Subnet Mask: `/29` (8 addresses)
- Branch 3: 4 PCs
  Required IPs = 4 + 2 = 6
  Nearest power of 2 = 8 (requires 3 bits for hosts)
  Subnet Mask: `/29` (8 addresses)

#### Assigning IP Addresses

We will use `192.168.0.0/24` as the starting base address.

| Branch           | Required PCs | Required IPs | Subnet Mask | Allocated Subnet   | Available IPs |
| ---------------- | ------------ | ------------ | ----------- | ------------------ | ------------- |
| Ahmedabad A      | 120          | 128          | `/25`       | `192.168.0.0/25`   | 128           |
| Ahmedabad B      | 170          | 256          | `/24`       | `192.168.1.0/24`   | 256           |
| Ahmedabad C      | 60           | 64           | `/26`       | `192.168.2.0/26`   | 64            |
| Delhi Branch 1   | 29           | 32           | `/27`       | `192.168.2.64/27`  | 32            |
| Delhi Branch 2   | 14           | 16           | `/28`       | `192.168.2.96/28`  | 16            |
| Chennai Branch 1 | 14           | 16           | `/28`       | `192.168.2.112/28` | 16            |
| Chennai Branch 2 | 6            | 8            | `/29`       | `192.168.2.128/29` | 8             |
| Chennai Branch 3 | 4            | 8            | `/29`       | `192.168.2.136/29` | 8             |

#### Summary:

- Ahmedabad:
  - Branch A uses `192.168.0.0/25` (120 PCs).
  - Branch B uses `192.168.1.0/24` (170 PCs).
  - Branch C uses `192.168.2.0/26` (60 PCs).
- Delhi:
  - Branch 1 uses `192.168.2.64/27` (29 PCs).
  - Branch 2 uses `192.168.2.96/28` (14 PCs).
- Chennai:
  - Branch 1 uses `192.168.2.112/28` (14 PCs).
  - Branch 2 uses `192.168.2.128/29` (6 PCs).
  - Branch 3 uses `192.168.2.136/29` (4 PCs).

This design efficiently uses VLSM to allocate IPs to each branch without wasting address space.
