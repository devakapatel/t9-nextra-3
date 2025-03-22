# Unit 3

## <mark> 1) Define peer-to-peer (P2P) systems and describe their key characteristics. </mark>

Peer-to-peer (P2P) systems represent a decentralized network architecture where computers, or "peers," share resources and communicate directly with each other, without relying on a central server. This contrasts with the traditional client-server model. Here's a breakdown of their key characteristics:

**Definition:**

- A P2P system is a distributed network where each node (peer) acts as both a client and a server, capable of providing and requesting resources.

**Key Characteristics:**

- **Decentralization:**
  - This is the defining feature. There's no central authority or server controlling the network.
  - Responsibility and resources are distributed among the peers.
- **Equality of Peers:**
  - Ideally, all peers have equal capabilities and responsibilities.
  - Each peer can initiate and respond to requests.
- **Resource Sharing:**
  - Peers share their resources, which can include files, processing power, storage, and network bandwidth.
  - This sharing is fundamental to the operation of P2P systems.
- **Scalability:**
  - P2P systems can often scale effectively, as adding more peers increases the network's overall resources and capacity.
  - This is because the work load is distributed.
- **Resilience:**
  - Due to their decentralized nature, P2P systems are often more resilient to failures.
  - If one or more peers go offline, the network can continue to function.
- **Dynamic Topology:**
  - P2P networks are typically dynamic, with peers joining and leaving the network frequently.
  - The network adapts to these changes.
- **Self-Organization:**
  - P2P networks often have self-organizing capabilities, allowing peers to discover and connect with each other.

**In essence:**

P2P systems leverage the collective power of individual computers to create a distributed and resilient network. This approach has led to various applications, from file sharing to blockchain technologies.

## <mark> 2) Describe the working of Napster and its impact on P2P networks. </mark>

Napster was a pioneering peer-to-peer (P2P) file-sharing service that significantly impacted the development and understanding of P2P networks. Here's how it worked and its impact:

**Working of Napster:**

- **Centralized Indexing:**
  - Napster used a hybrid P2P architecture. While file transfers occurred directly between users (peers), a central server maintained an index of available files.
  - When a user wanted to find a file, their Napster client would query the central server.
  - The server would return a list of users (peers) who had the requested file.
  - The client would then initiate a direct connection with the peer(s) to download the file.
- **File Transfer:**
  - The actual file transfer occurred directly between the client and the peer hosting the file, without passing through the central server.
- **MP3 Sharing:**
  - Napster primarily facilitated the sharing of MP3 audio files.

**Impact on P2P Networks:**

- **Popularization of P2P:**
  - Napster brought P2P technology to the mainstream, demonstrating its potential for large-scale file sharing.
  - It introduced millions of users to the concept of decentralized file exchange.
- **Legal Challenges and Copyright Issues:**
  - Napster faced numerous legal challenges from the music industry, which argued that the service facilitated widespread copyright infringement.
  - This led to the closure of the original Napster service and highlighted the legal and ethical complexities of P2P file sharing.
- **Hybrid P2P Model:**
  - Napster's hybrid P2P architecture, with its centralized indexing, influenced the development of subsequent P2P systems.
  - It demonstrated the efficiency of using a central server for indexing and search while distributing the actual file transfer load.
- **Rise of Decentralized P2P:**
  - The legal challenges faced by Napster paved the way for the development of more decentralized P2P networks, such as Gnutella and BitTorrent, which aimed to eliminate the single point of failure and legal vulnerability associated with centralized servers.
- **Impact on Digital Distribution:**
  - Napster forced the music industry to confront the realities of digital distribution and the changing landscape of media consumption.
  - It contributed to the eventual rise of legal digital music services.
- **Network traffic impact:**
  - Napster created huge amounts of network traffic, and showed how quickly and readily users would share files, creating a huge load on network infrastructure.

In summary, Napster's short but impactful existence revolutionized file sharing and significantly shaped the evolution of P2P networks, while also raising critical legal and ethical questions about copyright and digital distribution.

## <mark> 3) Analyze how overlay networks like Pastry and Tapestry improve routing efficiency in peer-to-peer systems. </mark>

Overlay networks like Pastry and Tapestry significantly improve routing efficiency in peer-to-peer (P2P) systems by employing structured topologies and efficient routing algorithms. Here's an analysis:

**Key Concepts:**

- **Structured Overlay Networks:** Pastry and Tapestry are examples of structured overlay networks, also known as Distributed Hash Tables (DHTs).
- **Distributed Hash Tables (DHTs):** DHTs provide a distributed lookup service similar to a hash table. They map keys to nodes in the network, allowing efficient location of resources.

**How Pastry and Tapestry Improve Routing Efficiency:**

1.  **Consistent Hashing and Node IDs:**

    - Both Pastry and Tapestry use consistent hashing to assign unique numerical IDs to nodes and resources.
    - This ensures that similar resources are mapped to nodes with similar IDs, facilitating efficient routing.
    - Consistent hashing minimizes disruption when nodes join or leave the network.

2.  **Structured Routing Tables:**

    - Each node maintains a routing table that stores information about other nodes in the network.
    - These routing tables are structured to enable efficient routing based on the numerical IDs.
    - The routing tables are designed so that each step in the routing process reduces the distance to the destination node by a significant factor.

3.  **Prefix-Based Routing:**

    - Pastry and Tapestry employ prefix-based routing, where nodes route messages to other nodes that share increasingly longer prefixes of the destination ID.
    - This allows for logarithmic routing complexity, meaning that the number of routing hops required to reach a destination increases logarithmically with the size of the network.
    - For example, in a network with $2^n$ nodes, a message can typically be routed in $O(\log_{b} 2^n)$ hops, where b is the base of the node IDs.

4.  **Proximity Awareness:**

    - Pastry and Tapestry incorporate proximity awareness, where nodes attempt to route messages to nearby nodes in terms of network latency.
    - This minimizes network traffic and improves routing performance by reducing the physical distance that messages travel.
    - Nodes will attempt to keep routing table entries that are network close.

5.  **Fault Tolerance and Resilience:**
    - The structured topology and routing algorithms of Pastry and Tapestry provide inherent fault tolerance and resilience.
    - If a node fails, messages can be routed around the failed node to reach the destination.
    - The routing tables contain redundant information, so that if a node in a routing table fails, an alternate node can be used.
    - The consistent hashing ensures that when a node fails, the keys it was responsible for are distributed to other nodes.

**Benefits:**

- **Efficient Lookup:** DHTs enable efficient lookup of resources in large-scale P2P systems.
- **Scalability:** The logarithmic routing complexity allows these networks to scale to millions of nodes.
- **Fault Tolerance:** The structured topology and routing algorithms provide resilience to node failures.
- **Reduced Latency:** Proximity awareness minimizes network latency.

In summary, overlay networks like Pastry and Tapestry improve routing efficiency in P2P systems by using structured topologies, efficient routing algorithms, and proximity awareness. This allows for scalable, fault-tolerant, and low-latency communication in decentralized environments.

## <mark> 4) Evaluate the impact of file sharing semantics on the performance and consistency of distributed file systems. </mark>

File sharing semantics significantly impact the performance and consistency of distributed file systems. Here's an evaluation:

**File Sharing Semantics:**

File sharing semantics define how concurrent access to files is managed in a distributed environment. They determine the visibility of file modifications and the order in which operations are executed. Common semantics include:

- **Unix Semantics (Sequential Consistency):**
  - Every read operation returns the most recent write.
  - All operations are executed in a sequential order.
  - Provides strong consistency but can lead to performance bottlenecks.
- **Session Semantics:**
  - Modifications are visible only after a file is closed.
  - Reduces network traffic but can lead to stale data.
- **Immutable File Semantics:**
  - Files are read-only after creation.
  - Simplifies consistency management and improves performance.
- **Transactional Semantics:**
  - Provides ACID (Atomicity, Consistency, Isolation, Durability) properties for file operations.
  - Ensures strong consistency but can incur significant overhead.

**Impact on Performance:**

- **Strong Consistency (Unix Semantics):**
  - **Performance:** Can significantly degrade performance due to the need for immediate synchronization and locking. Every write operation must be immediately propagated, which causes latency.
  - **Advantages:** Provides the strongest consistency guarantee, making it suitable for applications requiring strict data integrity.
- **Weak Consistency (Session Semantics):**
  - **Performance:** Improves performance by reducing network traffic and synchronization overhead.
  - **Disadvantages:** Can lead to stale data and inconsistencies, which may not be acceptable for all applications.
- **Immutable File Semantics:**
  - **Performance:** Offers excellent performance due to the absence of write operations and concurrent access conflicts.
  - **Advantages:** Simplifies caching and replication, leading to high throughput.
- **Transactional Semantics:**
  - **Performance:** Can introduce significant overhead due to the need for locking, concurrency control, and transaction management.
  - **Advantages:** Ensures strong consistency and data integrity, making it suitable for critical applications.

**Impact on Consistency:**

- **Strong Consistency:**
  - Ensures that all clients see the same, up-to-date view of the file system.
  - Minimizes the risk of data conflicts and inconsistencies.
- **Weak Consistency:**
  - Can lead to data inconsistencies and conflicts, especially in scenarios with frequent concurrent access.
  - Requires careful application design to handle potential inconsistencies.
- **Immutable File Semantics:**
  - Provides inherent consistency due to the absence of write operations.
  - Eliminates the risk of concurrent access conflicts.
- **Transactional Semantics:**
  - Ensures strong consistency and data integrity through ACID properties.
  - Provides a reliable mechanism for managing concurrent access and data modifications.

**Trade-offs:**

- There's a fundamental trade-off between performance and consistency. Strong consistency typically leads to lower performance, while weak consistency offers higher performance but at the cost of data integrity.
- The choice of file sharing semantics depends on the specific requirements of the application. Applications requiring strong data integrity may opt for Unix or transactional semantics, while those prioritizing performance may choose session or immutable semantics.
- Caching strategies greatly affect performance. Caching can greatly reduce network traffic. However, caching when using strong consistency semantics can be difficult.

In conclusion, file sharing semantics play a crucial role in balancing performance and consistency in distributed file systems. The choice of semantics should be carefully considered based on the application's specific requirements and tolerance for data inconsistencies.

## <mark> 5) Compare the features and architecture of the Andrew File System (AFS) with traditional file service architectures. </mark>

The Andrew File System (AFS) represents a significant departure from traditional file service architectures, focusing on scalability, security, and location transparency. Here's a comparison:

**Traditional File Service Architectures (e.g., NFS):**

- **Client-Server Model:**
  - Typically follows a simple client-server model.
  - Clients directly request files from a central server.
- **Stateless Server:**
  - Often employs stateless servers, meaning the server doesn't maintain client state.
  - Each request is treated independently.
- **Limited Scalability:**
  - Scalability can be limited due to the central server bottleneck.
  - Performance degrades as the number of clients increases.
- **Weak Security:**
  - Security relies on network-level authentication and access control.
  - Vulnerable to network-based attacks.
- **Location Dependence:**
  - Clients need to know the specific location of the file server.
  - File paths are often tied to server names.
- **Caching:**
  - Caching is often handled at the client side, but the consistency of the cache can be challenging.

**Andrew File System (AFS):**

- **Distributed Architecture:**
  - AFS uses a distributed architecture with multiple file servers and a distributed database (Vice).
  - This distributes the load and improves scalability.
- **Stateful Client Caching:**
  - AFS employs extensive client-side caching, where entire files are cached locally.
  - This significantly reduces network traffic and improves performance.
  - Client caches are kept consistent through callback mechanisms.
- **High Scalability:**
  - The distributed architecture and client-side caching enable AFS to scale to large numbers of users and files.
  - The system is designed for wide area network use.
- **Strong Security:**
  - AFS uses Kerberos for strong authentication and access control.
  - This provides robust security against unauthorized access.
- **Location Transparency:**
  - AFS provides location transparency, allowing clients to access files using consistent path names regardless of the file server's location.
  - Files are accessed using a global namespace.
- **Callback Caching:**
  - AFS uses callback caching. When a client caches a file, the server records that fact. If the file is changed, the server calls back all clients with caches of that file, and they invalidate their local copies. This ensures consistency.

**Key Architectural Differences:**

- **Caching Strategy:**
  - AFS's extensive client-side caching with callback mechanisms is a major differentiator.
  - Traditional systems often rely on less robust caching strategies.
- **Security Model:**
  - AFS's use of Kerberos provides a more robust security model compared to traditional systems.
- **Scalability Approach:**
  - AFS's distributed architecture and client-side caching enable superior scalability compared to the centralized approach of traditional systems.
- **Location Transparency:**
  - AFS's global namespace and location independence is a key feature that traditional systems often lack.

**In summary:**

AFS was designed to address the limitations of traditional file service architectures, particularly in terms of scalability, security, and location transparency. Its distributed architecture, stateful client caching, and strong security model make it well-suited for large-scale distributed environments.

## <mark> 6) Propose an improvement to LDAP for better scalability and fault tolerance in large-scale distributed environments. </mark>

LDAP (Lightweight Directory Access Protocol) is a widely used protocol for accessing and maintaining distributed directory information services. However, in large-scale distributed environments, it can face challenges with scalability and fault tolerance. Here's a proposed improvement:

**Proposed Improvement: Distributed LDAP with Sharding and Replication**

1.  **Sharding (Horizontal Partitioning):**
    - **Problem:** A single LDAP server can become a bottleneck as the directory size and query load increase.
    - **Improvement:** Implement sharding to partition the directory data across multiple LDAP servers.
      - Divide the directory information based on attributes or organizational units.
      - Use a consistent hashing algorithm to distribute data and queries evenly.
      - This distributes the load and improves query performance.
2.  **Replication (Vertical Partitioning and Redundancy):**
    - **Problem:** Single LDAP server failures can cause service disruptions.
    - **Improvement:** Implement multi-master or master-slave replication to create redundant copies of the directory data.
      - **Multi-master replication:** Allows multiple servers to accept write operations, with changes propagated to other replicas.
      - **Master-slave replication:** Designate a single master server for write operations, with read-only replicas.
      - This enhances fault tolerance and read scalability.
3.  **Distributed Caching Layer:**
    - **Problem:** Frequent queries for the same data can strain LDAP servers.
    - **Improvement:** Introduce a distributed caching layer (e.g., using Redis or Memcached) to store frequently accessed data.
      - Cache query results at the application or middleware layer.
      - Use cache invalidation strategies to maintain data consistency.
      - This reduces the load on LDAP servers and improves query response times.
4.  **Federated LDAP:**
    - **Problem:** Managing multiple independent LDAP directories can be complex.
    - **Improvement:** Implement federated LDAP to create a unified view of multiple directories.
      - Use a meta-directory or virtual directory server to aggregate data from different LDAP servers.
      - Provide a single point of access for clients.
      - This simplifies directory management and improves interoperability.
5.  **Enhanced Load Balancing and Routing:**
    - **Problem:** Distributing queries evenly across LDAP servers is crucial for performance.
    - **Improvement:** Implement intelligent load balancing and routing mechanisms.
      - Use a load balancer to distribute queries based on server load and availability.
      - Implement query routing based on data sharding and replication strategies.
      - This ensures optimal resource utilization and performance.
6.  **Asynchronous Replication and Change Notification:**
    - **Problem:** synchronous replication can create latency.
    - **Improvement:** Use asynchronous replication where possible.
      - Use change notification mechanisms to alert clients of directory updates.
      - This increases the speed of write operations, and the system can handle higher write loads.

**Benefits:**

- **Improved Scalability:** Sharding and distributed caching enable LDAP to handle larger directory sizes and query loads.
- **Enhanced Fault Tolerance:** Replication and load balancing ensure high availability and resilience to server failures.
- **Increased Performance:** Distributed caching and optimized routing improve query response times.
- **Simplified Management:** Federated LDAP provides a unified view of multiple directories.

By implementing these improvements, LDAP can better meet the scalability and fault tolerance requirements of large-scale distributed environments.
