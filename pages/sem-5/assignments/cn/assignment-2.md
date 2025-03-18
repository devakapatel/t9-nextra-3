# Assignment 2

## 1) Name and categorizes different multiple access protocols.

Multiple access protocols are essential for managing how multiple devices share a communication channel in a network. Below are the main categories of multiple access protocols along with their descriptions:

### 1. Random Access Protocols

These protocols allow multiple devices to transmit data whenever they have data to send, leading to potential collisions. They include:

- **ALOHA**: A simple protocol where devices transmit whenever they have data. It can be further categorized into:
  - **Pure ALOHA**: No synchronization; devices transmit immediately.
  - **Slotted ALOHA**: Time is divided into slots, and devices can only transmit at the beginning of a time slot.
- **Carrier Sense Multiple Access (CSMA)**: Devices sense the channel before transmitting. Variants include:
  - **Non-persistent CSMA**: If the channel is busy, the device waits a random time before checking again.
  - **1-persistent CSMA**: If the channel is busy, the device continuously listens until the channel is idle and then transmits immediately.
  - **p-persistent CSMA**: Used in slotted channels, where devices transmit with a probability p when the channel is idle.

### 2. Controlled Access Protocols

These protocols manage access to the channel more systematically to avoid collisions. They include:

- **Polling**: A central controller polls each device to check if it has data to send. Only the polled device can transmit.
- **Reservation**: Devices reserve a time slot or channel before transmitting data, ensuring no collisions occur.
- **Token Passing**: A token circulates in the network, and only the device holding the token can transmit. This method is used in:
  - **Token Ring**: Devices are arranged in a logical ring, and the token passes around the ring.

### 3. Channelization Protocols

These protocols divide the channel into smaller, separate channels, allowing simultaneous transmissions. They include:

- **Frequency Division Multiple Access (FDMA)**: The channel is divided into frequency bands, and each device is assigned a specific frequency for transmission.
- **Time Division Multiple Access (TDMA)**: The channel is divided into time slots, and each device is assigned a specific time slot for transmission.
- **Code Division Multiple Access (CDMA)**: Each device is assigned a unique code, allowing multiple devices to transmit simultaneously over the same frequency band without interference.

## 2) Compare and explain the pure and slotted ALOHA system

### Comparison of Pure ALOHA and Slotted ALOHA

**Overview:**
Both Pure ALOHA and Slotted ALOHA are random access protocols used for managing how multiple devices share a communication channel. They are particularly useful in scenarios where the network traffic is sporadic and unpredictable.

---

### 1. Pure ALOHA

**Definition:**
Pure ALOHA allows devices to transmit data whenever they have data to send, without waiting for a specific time slot.

**Characteristics:**

- **Transmission Timing:** Devices can transmit at any time.
- **Collision Handling:** If a collision occurs (when two devices transmit simultaneously), both frames are lost, and the devices must wait a random amount of time before attempting to retransmit.
- **Efficiency:** The maximum throughput is approximately 18.4%. This is because the protocol allows for a high probability of collisions due to the lack of synchronization.

**Advantages:**

- **Simplicity:** Easy to implement as there are no time slots or synchronization requirements.
- **Flexibility:** Devices can transmit whenever they have data.

**Disadvantages:**

- **High Collision Rate:** Since devices can transmit at any time, the likelihood of collisions is high, especially as the number of devices increases.
- **Low Efficiency:** The protocol's efficiency is limited due to the high rate of collisions.

---

### 2. Slotted ALOHA

**Definition:**
Slotted ALOHA improves upon Pure ALOHA by dividing time into discrete slots, allowing devices to transmit only at the beginning of a time slot.

**Characteristics:**

- **Transmission Timing:** Devices can only begin transmitting at the start of a time slot.
- **Collision Handling:** Similar to Pure ALOHA, if a collision occurs, the frames are lost, and the devices must wait a random amount of time before retransmitting. However, since transmissions are synchronized to time slots, the chances of collisions are reduced.
- **Efficiency:** The maximum throughput is approximately 36.8%, which is significantly higher than that of Pure ALOHA.

**Advantages:**

- **Reduced Collision Rate:** By allowing transmissions only at the beginning of time slots, Slotted ALOHA reduces the chances of collisions.
- **Higher Efficiency:** The protocol achieves better throughput compared to Pure ALOHA due to reduced collisions.

**Disadvantages:**

- **Synchronization Required:** Devices must synchronize their transmissions to the time slots, which adds complexity.
- **Wasted Time Slots:** If a device has no data to send at the beginning of a time slot, that slot is wasted.

---

### Summary of Differences

| Feature                 | Pure ALOHA                   | Slotted ALOHA                    |
| ----------------------- | ---------------------------- | -------------------------------- |
| **Transmission Timing** | Anytime                      | At the beginning of time slots   |
| **Collision Handling**  | High collision rate          | Reduced collision rate           |
| **Maximum Throughput**  | ~18.4%                       | ~36.8%                           |
| **Complexity**          | Simple                       | Requires synchronization         |
| **Efficiency**          | Lower due to high collisions | Higher due to reduced collisions |

---

In conclusion, while both Pure ALOHA and Slotted ALOHA are effective in managing access to a shared communication channel, Slotted ALOHA offers improved efficiency and reduced collision rates at the cost of added complexity due to the need for synchronization.

## 3) What is CSMA/CA ?

CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) is a media access control (MAC) protocol used in wireless networks, such as IEEE 802.11 (Wi-Fi), to manage the sharing of the communication channel among multiple devices. It is designed to avoid collisions that occur when two or more stations transmit simultaneously.

Here's how CSMA/CA works:

1. When a station has a frame to send, it first listens to the channel to check if it is idle.
2. If the channel is idle for a specified time (called DIFS - Distributed Inter-Frame Space), the station can begin transmitting the frame.
3. If the channel is busy, the station defers transmission and enters a backoff process:
   - The station generates a random backoff time within a contention window.
   - The station decrements the backoff timer as long as the channel is sensed as idle.
   - If the channel is sensed as busy during the backoff process, the station freezes the backoff timer until the channel is sensed as idle again for a DIFS duration.
4. When the backoff timer reaches zero, the station can transmit the frame.
5. If the destination station successfully receives the frame, it waits for a short inter-frame space (SIFS) and then transmits an acknowledgment (ACK) frame back to the sender.
6. If the sender does not receive the ACK within a specified time, it assumes a collision occurred and retransmits the frame after a random backoff time.

The main differences between CSMA/CD (Collision Detection) and CSMA/CA are:

1. CSMA/CD is used in wired networks like Ethernet, while CSMA/CA is used in wireless networks.
2. CSMA/CD can detect collisions during transmission, while CSMA/CA cannot, as wireless stations cannot transmit and receive simultaneously.
3. CSMA/CA relies on collision avoidance mechanisms, such as random backoff and ACKs, to reduce the probability of collisions.

By using random backoff times and deferring transmission when the channel is busy, CSMA/CA helps to reduce the probability of collisions in wireless networks, improving overall performance and fairness in channel access.

## 4) What is CSMA/CD? Explain with Flow chart.

### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

CSMA/CD is a network protocol that controls how data packets are transmitted over a shared communication medium, primarily used in wired Ethernet networks. The protocol is designed to minimize collisions and ensure efficient use of the network.

### How CSMA/CD Works:

1. **Carrier Sense**:
   - Before a device (or station) transmits data, it first listens to the channel to determine if it is idle (not being used by another device).
   - If the channel is busy, the device will wait until it becomes idle.
2. **Transmission**:
   - Once the channel is sensed as idle, the device can begin transmitting its data packet.
3. **Collision Detection**:
   - While transmitting, the device continues to monitor the channel for any signs of collisions (i.e., if another device starts transmitting simultaneously).
   - If a collision is detected (the signal on the channel is different from what the transmitting device is sending), both devices involved in the collision will stop transmitting.
4. **Jam Signal**:
   - After detecting a collision, the device sends a jam signal to notify all other devices on the network that a collision has occurred.
   - This ensures that all devices are aware of the collision and can take appropriate action.
5. **Backoff and Retransmission**:
   - After sending the jam signal, the device waits for a random backoff time before attempting to retransmit the data.
   - The backoff time is determined using a binary exponential backoff algorithm, which increases the waiting time exponentially with each successive collision.
   - Once the backoff time has elapsed, the device will return to the beginning of the CSMA/CD process (i.e., listen to the channel again).

### Advantages of CSMA/CD:

- **Efficiency**: By allowing devices to sense the channel before transmitting, CSMA/CD reduces the likelihood of collisions, leading to more efficient use of the network.
- **Simplicity**: The protocol is relatively straightforward to implement and does not require complex management.

### Disadvantages of CSMA/CD:

- **Collision Handling**: While CSMA/CD can detect collisions, the presence of collisions still degrades network performance, especially as the number of devices increases.
- **Limited Scalability**: As more devices are added to the network, the chances of collisions increase, which can lead to network congestion and reduced throughput.
- **Not Suitable for Wireless Networks**: CSMA/CD is primarily designed for wired networks. In wireless networks, CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) is used instead, as devices cannot transmit and receive simultaneously.

## 5) Compare static vs dynamic channel allocation.

| Feature                       | Static Channel Allocation                        | Dynamic Channel Allocation                               |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Definition**                | Fixed channels are assigned to each station.     | Channels are assigned based on real-time needs.          |
| **Flexibility**               | Limited; channels do not change.                 | High; channels can change based on conditions.           |
| **Implementation Complexity** | Simple to implement; low overhead.               | More complex; requires management of dynamic allocation. |
| **Efficiency**                | May lead to underutilization or overutilization. | More efficient use of channels based on demand.          |
| **Adaptability**              | No adaptation to changing network conditions.    | Adapts to changes in network traffic and interference.   |
| **Channel Utilization**       | Fixed allocation can lead to wasted resources.   | Better utilization as channels are allocated as needed.  |
| **Signaling Overhead**        | Minimal signaling required for allocation.       | Higher signaling overhead for updates and reallocations. |

## 6) Explain Reservation, Token Passing and POLLING.

Here’s an explanation of the three controlled access protocols: Reservation, Token Passing, and Polling.

### 1. Reservation Protocol

### Definition:

The reservation protocol allows devices to reserve a specific time slot or channel for transmission before sending data. This method helps to avoid collisions by ensuring that only the reserved device can transmit during its allocated time.

### How It Works:

- **Reservation Request**: A device sends a reservation request to the central controller or the network.
- **Allocation**: The controller allocates a time slot or channel based on the request.
- **Transmission**: The device transmits its data during the reserved time slot.
- **Release**: After transmission, the device releases the channel, making it available for others.

### Advantages:

- Reduces the chance of collisions since devices have reserved time slots.
- Efficient use of the channel when traffic is predictable.

### Disadvantages:

- Can lead to underutilization if many devices are idle and not using their reserved slots.
- Requires a mechanism to manage reservations and track channel availability.

---

### 2. Token Passing Protocol

### Definition:

Token passing is a method where a small data packet called a "token" circulates in the network. Only the device holding the token can transmit data, ensuring orderly access to the communication medium.

### How It Works:

- **Token Generation**: A token is generated and passed around the network in a logical ring or bus topology.
- **Token Possession**: A device can only transmit data if it possesses the token.
- **Transmission**: After transmitting, the device releases the token back into the network for others to use.
- **Token Loss**: If a token is lost, a mechanism must be in place to regenerate it.

### Advantages:

- Prevents collisions by ensuring that only one device transmits at a time.
- Fair access to the channel, as each device gets a chance to transmit.

### Disadvantages:

- If the token is lost or corrupted, it can lead to network downtime until the token is regenerated.
- The protocol can introduce delays if many devices are waiting for the token.

---

### 3. Polling Protocol

### Definition:

Polling is a controlled access method where a central controller (master) polls each device (slave) in turn to check if it has data to send. Only the polled device can transmit.

### How It Works:

- **Polling Request**: The master device sends a polling request to each slave device in a predetermined order.
- **Response**: Each slave responds to the poll, indicating whether it has data to send.
- **Transmission**: If a slave has data, it transmits during its allocated time.
- **Next Poll**: The master continues polling the next device in the sequence.

### Advantages:

- Ensures that only one device transmits at a time, reducing the chance of collisions.
- Simple to implement and manage.

### Disadvantages:

- Can lead to delays if a device has no data to send, as the master must wait to poll each device.
- The master device can become a bottleneck if it cannot keep up with the polling requests.

## 7) How CSMA/CA differs from CSMA/CD. Explain in brief.

### Key Differences Between CSMA/CA and CSMA/CD

| Feature                       | CSMA/CD (Collision Detection)                                       | CSMA/CA (Collision Avoidance)                                                  |
| ----------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Network Type**              | Primarily used in wired networks (e.g., Ethernet)                   | Primarily used in wireless networks (e.g., Wi-Fi)                              |
| **Collision Handling**        | Detects collisions during transmission.                             | Avoids collisions by using a backoff mechanism.                                |
| **Transmission**              | Devices can transmit immediately after sensing the channel is idle. | Devices must wait for a specific time period (DIFS) before transmitting.       |
| **Acknowledgment**            | No explicit acknowledgment; relies on collision detection.          | Uses acknowledgment (ACK) frames to confirm successful transmission.           |
| **Efficiency**                | Can be more efficient in wired environments with fewer collisions.  | More efficient in wireless environments where collisions are harder to detect. |
| **Implementation Complexity** | Simpler, as it only requires collision detection.                   | More complex due to the need for collision avoidance mechanisms.               |

## 8) Frequency Division Multiple Access (FDMA)

### Frequency Division Multiple Access (FDMA)

**Definition:**
Frequency Division Multiple Access (FDMA) is a channel access method used in communication systems where multiple users share the same frequency band by allocating distinct frequency ranges to each user. This allows simultaneous transmission of multiple signals over the same medium without interference.

### How FDMA Works:

1. **Frequency Allocation**: The total available bandwidth is divided into smaller frequency bands or channels. Each user is assigned a specific frequency band for their communication.
2. **Simultaneous Transmission**: Multiple users can transmit simultaneously, each on their assigned frequency band, without interfering with each other.
3. **Guard Bands**: To prevent interference between adjacent frequency bands, guard bands (small frequency ranges) are often used between channels.

### Characteristics of FDMA:

- **Fixed Bandwidth**: Each user has a fixed bandwidth allocation, which does not change during the communication session.
- **Simple Implementation**: FDMA systems are relatively simple to implement, as they do not require complex signaling or coordination mechanisms.
- **Low Latency**: Since each user has a dedicated frequency band, there is minimal delay in transmission.

### Advantages of FDMA:

- **No Collisions**: Since each user operates on a separate frequency, collisions are avoided.
- **Simplicity**: The protocol is straightforward and easy to manage.
- **Continuous Transmission**: Users can continuously transmit data without interruptions.

### Disadvantages of FDMA:

- **Inefficient Bandwidth Usage**: Fixed bandwidth allocation can lead to underutilization if some users are inactive while others require more bandwidth.
- **Limited Flexibility**: Once allocated, the frequency bands cannot be easily reallocated based on changing demands.
- **Interference**: Although guard bands are used, there is still a potential for interference between adjacent channels.

### Applications of FDMA:

- **Cellular Networks**: Early mobile communication systems used FDMA to allocate different frequency bands to different users.
- **Satellite Communication**: FDMA is commonly used in satellite communications to allocate different frequency channels to various users.
- **Radio Broadcasting**: FM and AM radio stations use FDMA to broadcast on different frequency channels.

### Conclusion:

FDMA is a fundamental multiple access technique that allows multiple users to share a communication medium by allocating distinct frequency bands. While it offers simplicity and collision-free transmission, it may lead to inefficient bandwidth usage and limited flexibility compared to other methods like Time Division Multiple Access (TDMA) or Code Division Multiple Access (CDMA).

## 9) Code Division Multiple Access (CDMA)

Here is an explanation of Code Division Multiple Access (CDMA):

### Code Division Multiple Access (CDMA)

**Definition:**
Code Division Multiple Access (CDMA) is a channel access method used in various communication systems. It allows multiple users to transmit data over a single communication channel by using unique codes for each user. CDMA is a form of multiple access that divides the channel by using different codes instead of time slots (TDMA) or frequency bands (FDMA).

### How CDMA Works:

1. **Unique Codes**: Each user is assigned a unique code, known as a spreading code or chipping code, which is used to encode the user's data.
2. **Spreading**: The user's data is multiplied by its assigned spreading code, which spreads the signal across the entire available frequency band.
3. **Simultaneous Transmission**: Multiple users can transmit simultaneously using different spreading codes, allowing their signals to occupy the same frequency band.
4. **Despreading**: At the receiver, the received signal is multiplied by the same spreading code used by the transmitter. This process despreads the signal and recovers the original data.

### Characteristics of CDMA:

- **Spread Spectrum Technology**: CDMA uses spread spectrum technology, where the signal is spread over a wide frequency band.
- **Pseudorandom Codes**: The spreading codes used in CDMA are pseudorandom, ensuring that the codes are nearly orthogonal to each other, minimizing interference between users.
- **Power Control**: Proper power control is essential in CDMA systems to ensure that all signals are received with the same power level, preventing the near-far problem.

### Advantages of CDMA:

- **Increased Capacity**: CDMA can support more users compared to FDMA and TDMA, as multiple users can transmit simultaneously.
- **Soft Capacity**: CDMA has a soft capacity, meaning that the system can support more users than the theoretical limit, with a gradual decrease in quality.
- **Improved Security**: The use of spreading codes provides a level of security, as it is difficult for unauthorized users to intercept and decode the transmitted data.

### Disadvantages of CDMA:

- **Power Control**: Maintaining proper power control is crucial in CDMA systems, and any imbalance can lead to the near-far problem and performance degradation.
- **Complexity**: CDMA systems are more complex compared to FDMA and TDMA, as they require precise power control, synchronization, and code management.

### Applications of CDMA:

- **Cellular Networks**: CDMA is used in various cellular network standards, such as CDMA2000 and WCDMA (Wideband CDMA).
- **Satellite Communication**: CDMA is used in satellite communication systems to allow multiple users to access the same satellite transponder.
- **Military Applications**: CDMA was initially developed for military applications due to its resistance to jamming and interception.

### Conclusion:

CDMA is a powerful multiple access technique that allows multiple users to share a communication channel by using unique spreading codes. It offers increased capacity, improved security, and soft capacity compared to other multiple access methods. However, CDMA systems require careful power control and are more complex to implement.

## 10) Explain Manchester encoding for the bit stream 10100111001

Manchester encoding is a digital encoding scheme used to represent binary data. In Manchester encoding, each bit is represented by a transition in the middle of the bit period. For a 1 bit, the transition is from low to high, and for a 0 bit, the transition is from high to low.

For the bit stream 10100111001, the Manchester encoding would be:

```
    1       0       1       0       0       1       1       1       0       0       1
┌───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┴───┐
│       │       │       │       │       │       │       │       │       │       │       │
└───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘

```

The key characteristics of Manchester encoding are:

1. There is always a transition in the middle of each bit period.
2. For a 1 bit, the transition is from low to high.
3. For a 0 bit, the transition is from high to low.
4. The encoding is self-clocking, meaning the clock can be recovered from the encoded data stream.

Manchester encoding is commonly used in various communication protocols, such as Ethernet, due to its simplicity and ability to provide clock recovery without the need for a separate clock signal.
