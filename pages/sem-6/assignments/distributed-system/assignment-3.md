# Assignment 3

## <mark> 1) What are peer-to-peer (P2P) systems, and how do they differ from traditional client-server architectures? </mark>

Peer-to-peer (P2P) systems represent a decentralized approach to distributed computing, where individual computers, or "peers," directly share resources and communicate with each other. This contrasts sharply with the traditional client-server model.

Here's a breakdown:

**Peer-to-Peer (P2P) Systems:**

- **Decentralized Nature:**
  - P2P systems operate without a central server.
  - Each peer acts as both a client and a server, providing and consuming resources.
- **Equal Roles:**
  - Ideally, all peers have equal capabilities and responsibilities.
  - They can initiate and respond to requests.
- **Resource Sharing:**
  - Peers share resources like files, processing power, storage, and network bandwidth.
- **Dynamic Networks:**
  - P2P networks are often highly dynamic, with peers joining and leaving the network frequently.
- **Self-Organization:**
  - Peers discover and connect with each other, often without central coordination.

**Traditional Client-Server Architectures:**

- **Centralized Control:**
  - A central server provides resources and services to client computers.
  - Clients rely on the server for access to data and functionality.
- **Unequal Roles:**
  - Servers have dedicated roles, while clients make requests.
  - Servers provide, clients consume.
- **Centralized Resource Storage:**
  - Data and resources are typically stored on the server.
- **Static or Semi-Static Networks:**
  - The server is expected to be constantly available.
- **Centralized Management:**
  - The server dictates the rules of the network.

**Key Differences Summarized:**

| Feature               | Peer-to-Peer (P2P)                     | Client-Server                           |
| :-------------------- | :------------------------------------- | :-------------------------------------- |
| Centralization        | Decentralized                          | Centralized                             |
| Roles                 | Equal                                  | Unequal                                 |
| Resource Distribution | Distributed                            | Centralized                             |
| Scalability           | Potentially high (due to distribution) | Limited by server capacity              |
| Fault Tolerance       | High (due to redundancy)               | Low (single point of failure)           |
| Complexity            | Complex (distributed management)       | Relatively simple (centralized control) |
| Network dynamics      | Dynamic                                | Static or Semi-Static                   |

**Examples:**

- **P2P:** BitTorrent, distributed ledgers (blockchains), some file-sharing applications.
- **Client-Server:** Web browsing, email, online banking.

In essence, P2P systems distribute resources and responsibilities among peers, while client-server systems rely on a central server to provide services.

## <mark> 2) Explain the legacy of Napster and its impact on modern peer-to-peer networks. </mark>

Napster's legacy is profound and continues to shape the landscape of modern peer-to-peer (P2P) networks. While its original form was short-lived, its impact on technology, law, and culture is undeniable. Here's a breakdown:

**Napster's Legacy:**

1.  **Mainstream Popularization of P2P:**

    - Napster introduced millions of users to the concept of P2P file sharing.
    - It demonstrated the power and potential of decentralized networks for distributing digital content.
    - It proved that large scale file sharing was possible.

2.  **Legal Battles and Copyright Awareness:**

    - Napster's legal battles with the music industry highlighted the complexities of copyright infringement in the digital age.
    - It forced a re-evaluation of copyright laws and the rights of content creators.
    - It made digital copyright a major issue in the public eye.

3.  **Hybrid P2P Model's Influence:**

    - Napster's hybrid architecture (centralized indexing, decentralized file transfer) influenced the development of later P2P systems.
    - It showed the benefits of using a central server for search while distributing the bandwidth load.

4.  **Rise of Decentralized P2P Networks:**

    - The legal challenges faced by Napster spurred the development of more decentralized P2P networks like Gnutella and BitTorrent.
    - These networks aimed to eliminate the single point of failure and legal vulnerability associated with centralized servers.

5.  **Impact on Digital Distribution:**

    - Napster forced the music industry to adapt to the realities of digital distribution.
    - It contributed to the eventual rise of legal digital music services like iTunes and Spotify.
    - It changed the way that digital media is consumed.

6.  **Technological Innovation:**
    - Napster pushed the limits of network bandwidth and storage capabilities.
    - It created a surge of development in P2P networking technologies.

**Impact on Modern P2P Networks:**

- **Decentralization as a Core Principle:**
  - The legal battles surrounding Napster solidified the importance of decentralization in P2P systems.
  - Modern P2P networks prioritize distributed architectures to avoid centralized control and legal vulnerabilities.
- **Emphasis on Efficiency and Scalability:**
  - Napster's popularity demonstrated the need for efficient and scalable P2P systems.
  - Modern P2P networks employ sophisticated routing and resource management techniques to handle large numbers of users and files.
- **Legal and Ethical Considerations:**
  - The legal and ethical issues raised by Napster continue to be relevant in modern P2P networks.
  - Developers are increasingly aware of the need to address copyright and privacy concerns.
- **Influence on Blockchain Technology:**
  - The decentralized principles of P2P networking have influenced the development of blockchain technology.
  - Blockchain networks use P2P architectures to distribute and validate transactions.
- **File sharing and content distribution:**
  - BitTorrent, a direct descendent of the lessons learned from napster, is still a very important method of file sharing.

In essence, Napster's legacy is a complex mix of technological innovation, legal controversy, and cultural impact. It played a pivotal role in shaping the development of modern P2P networks and continues to influence the way we think about digital distribution and copyright.

## <mark> 3) Describe routing overlays in P2P networks and explain their significance. </mark>

Routing overlays in peer-to-peer (P2P) networks are virtual network structures built on top of the existing physical network (the "underlay"). They create an abstract routing layer that enables efficient data transfer and resource location in a decentralized environment. Here's a description and explanation of their significance:

**Description of Routing Overlays:**

- **Virtual Network Structure:**
  - Routing overlays create a logical network topology that is independent of the physical network's topology.
  - Peers in the P2P network form virtual connections, or "links," that define the overlay's routing paths.
- **Decentralized Routing:**
  - Routing decisions are made by the peers themselves, without relying on a central authority.
  - Each peer maintains routing information about other peers in the overlay.
- **Structured vs. Unstructured Overlays:**
  - **Structured Overlays (DHTs):**
    - Use a deterministic algorithm to organize peers and resources.
    - Examples: Pastry, Tapestry, Chord.
    - Provide efficient and predictable routing.
  - **Unstructured Overlays:**
    - Peers are connected randomly or based on ad-hoc criteria.
    - Examples: Gnutella.
    - Routing relies on flooding or random walks.

**Significance of Routing Overlays:**

1.  **Efficient Resource Location:**
    - Routing overlays enable efficient location of resources in decentralized environments.
    - Structured overlays, in particular, provide logarithmic or near-logarithmic search times.
2.  **Scalability:**
    - Routing overlays can scale to large numbers of peers, as routing decisions are distributed.
    - They reduce the burden on individual peers and the network as a whole.
3.  **Fault Tolerance:**
    - Routing overlays can tolerate peer failures, as routing paths can be dynamically adjusted.
    - This enhances the robustness and resilience of P2P networks.
4.  **Decentralization and Autonomy:**
    - Routing overlays promote decentralization by eliminating the need for central routing servers.
    - Peers have autonomy in routing decisions, enhancing the distributed nature of P2P systems.
5.  **Abstraction and Flexibility:**
    - Routing overlays abstract the complexities of the underlying physical network.
    - This allows for the creation of flexible and adaptable P2P applications.
6.  **Optimized Data Transfer:**
    - Routing overlays can be designed to optimize data transfer based on factors such as network latency and bandwidth.
    - Proximity awareness can be implemented.
7.  **Enabling Complex P2P Applications:**
    - Routing overlays are fundamental for building complex P2P applications such as distributed file sharing, content distribution networks (CDNs), and distributed databases.
    - They provide the underlying infrastructure for these applications to function efficiently.

In summary, routing overlays are crucial for enabling efficient, scalable, and fault-tolerant communication in P2P networks. They provide a vital abstraction layer that facilitates the development of decentralized applications.

## <mark> 4) Compare and contrast Pastry and Tapestry as overlay network protocols. </mark>

Pastry and Tapestry are both structured overlay network protocols, specifically Distributed Hash Tables (DHTs), designed for efficient routing and resource location in large-scale peer-to-peer (P2P) systems. While they share many similarities, they also have some key differences. Here's a comparison and contrast:

**Similarities:**

- **Structured Overlays:** Both Pastry and Tapestry are structured overlays, meaning they use a deterministic algorithm to organize peers and resources.
- **Distributed Hash Tables (DHTs):** They both implement DHT functionality, providing a distributed lookup service that maps keys to nodes.
- **Numeric Node IDs:** Both assign numeric IDs to nodes and resources using consistent hashing.
- **Prefix-Based Routing:** They employ prefix-based routing, where nodes route messages to other nodes that share increasingly longer prefixes of the destination ID.
- **Logarithmic Routing Complexity:** Both aim for logarithmic routing complexity, allowing for efficient routing in large networks.
- **Proximity Awareness:** They incorporate proximity awareness, attempting to route messages to nearby nodes in terms of network latency.
- **Fault Tolerance:** Both are designed to be fault-tolerant, allowing the network to function even when nodes fail.

**Differences:**

- **Routing Table Structure:**
  - **Pastry:** Uses a routing table that is organized based on shared prefixes of the destination ID. Each entry in the table points to a node that shares a longer prefix with the destination.
  - **Tapestry:** Also uses a routing table based on shared prefixes, but its structure and organization differ slightly from Pastry. Tapestry's routing tables also take into account the location of the nodes.
- **Neighborhood Set:**
  - **Pastry:** Maintains a neighborhood set of nearby nodes in terms of network latency, used for proximity awareness.
  - **Tapestry:** Also considers proximity, but it may handle the neighborhood set differently and integrate it more tightly into the routing table.
- **Leaf Set/Node Set:**
  - **Pastry:** Maintains a leaf set of nodes with IDs numerically close to its own, used for fault tolerance and data replication.
  - **Tapestry:** Uses a node set, which serves a similar purpose, but the specific implementation may vary.
- **Routing Algorithm Details:**
  - While both use prefix-based routing, the precise algorithms for routing and node selection differ.
  - The way that the routing tables are populated and maintained is also different.
- **Implementation Details:**
  - There are some differences in the ways that these protocols are implemented, and in the focus of their implementations.

**Key Points of Contrast:**

- The key difference between Pastry and Tapestry lies in the precise structure of their routing tables and the specific algorithms they use for routing and node selection.
- While both aim for similar goals (efficient routing, scalability, fault tolerance), they achieve these goals through slightly different mechanisms.
- Both are very similar in the problem that they solve, and the general way they solve it.

**Significance:**

Both Pastry and Tapestry have been influential in the development of structured P2P networks. They demonstrate the feasibility of building efficient and scalable decentralized systems using DHTs. Their designs have influenced subsequent P2P protocols and applications.

## <mark> 5) Describe the Andrew File System (AFS) and its advantages over traditional file systems. </mark>

The Andrew File System (AFS) is a distributed file system designed for large-scale, distributed computing environments. It aims to provide location transparency, high availability, and strong security. Here's a description and its advantages over traditional file systems:

**Description of AFS:**

- **Distributed Architecture:** AFS uses a distributed architecture with multiple file servers (Vice servers) and a distributed database. This distributes the load and improves scalability.
- **Client-Side Caching:** AFS employs aggressive client-side caching, where entire files are cached locally on client machines. This significantly reduces network traffic and improves performance.
- **Location Transparency:** AFS provides a global namespace, allowing clients to access files using consistent path names regardless of the file server's physical location.
- **Strong Security:** AFS uses Kerberos for authentication and access control, providing robust security against unauthorized access.
- **Callback Mechanism:** AFS uses a callback mechanism to maintain cache consistency. When a file is modified, the server notifies clients that have cached the file, invalidating their local copies.

**Advantages of AFS over Traditional File Systems (e.g., NFS):**

1.  **Improved Scalability:**
    - AFS's distributed architecture and client-side caching enable it to scale to a large number of users and files.
    - Traditional file systems often suffer from performance bottlenecks as the number of clients increases.
2.  **Enhanced Performance:**
    - Client-side caching in AFS significantly reduces network traffic, leading to faster file access.
    - Traditional file systems often require frequent network requests for file operations.
3.  **Location Transparency:**
    - AFS provides a global namespace, simplifying file access for users.
    - Traditional file systems often require clients to know the specific location of file servers.
4.  **Stronger Security:**
    - AFS uses Kerberos for authentication, providing robust security against unauthorized access.
    - Traditional file systems may rely on weaker security mechanisms.
5.  **Better Cache Consistency:**
    - AFS's callback mechanism ensures cache consistency, preventing clients from accessing stale data.
    - Traditional file systems may have weaker cache consistency mechanisms, leading to inconsistencies.
6.  **Wide Area Network (WAN) Optimization:**
    - AFS was designed to work efficiently over wide area networks. The caching and callback mechanisms help to reduce the affect of network latency.
    - Traditional file systems often preform poorly over WANs.
7.  **Reduced Server Load:**
    - Due to client side caching, the server load is greatly reduced.

**In summary:**

AFS addresses many of the limitations of traditional file systems, particularly in terms of scalability, performance, security, and location transparency. Its distributed architecture and client-side caching make it well-suited for large-scale, distributed computing environments.

## <mark> 6) What is the difference between identifiers, addresses, and name resolution in distributed systems? </mark>

In distributed systems, identifiers, addresses, and name resolution are distinct concepts that play crucial roles in locating and accessing resources. Here's a breakdown of their differences:

**1. Identifiers:**

- **Definition:**
  - An identifier is a unique label or name that distinguishes a resource (e.g., a file, a service, a node) within a distributed system.
  - It's a logical name that remains constant regardless of the resource's physical location or network address.
- **Characteristics:**
  - Uniqueness: Identifiers must be unique to avoid ambiguity.
  - Location independence: Identifiers are independent of the resource's physical location.
  - Persistence: Identifiers should ideally be persistent, remaining valid even if the resource moves or changes its address.
- **Examples:**
  - Universally Unique Identifiers (UUIDs)
  - Uniform Resource Names (URNs)
  - Object IDs in distributed databases.

**2. Addresses:**

- **Definition:**
  - An address is a physical or network location that specifies where a resource is located.
  - It's a concrete representation of the resource's location in the network.
- **Characteristics:**
  - Location dependence: Addresses are tied to the resource's physical or network location.
  - Dynamic: Addresses can change over time (e.g., IP addresses in dynamic networks).
  - Routing information: Addresses are used by the network infrastructure to route messages to the resource.
- **Examples:**
  - IP addresses (IPv4, IPv6)
  - MAC addresses
  - Port numbers
  - URL's that contain ip addresses.

**3. Name Resolution:**

- **Definition:**
  - Name resolution is the process of translating an identifier (a logical name) into an address (a physical location).
  - It's the mechanism that bridges the gap between logical names and physical locations.
- **Characteristics:**
  - Mapping: Name resolution involves creating and maintaining mappings between identifiers and addresses.
  - Lookup: It involves looking up the address associated with a given identifier.
  - Distributed or centralized: Name resolution can be performed by distributed systems (e.g., DNS) or centralized systems.
- **Examples:**
  - Domain Name System (DNS)
  - LDAP directories
  - Distributed Hash Tables (DHTs)

**Key Differences Summarized:**

- **Identifiers:**
  - What the resource is called (logical name).
  - Location-independent.
- **Addresses:**
  - Where the resource is located (physical location).
  - Location-dependent.
- **Name Resolution:**
  - The process of finding the address given the identifier.
  - The translation mechanism.

In essence, identifiers provide a stable and abstract way to refer to resources, addresses provide the concrete location information, and name resolution provides the mechanism to connect the two.

## <mark> 7) Explain the role of LDAP in name resolution and directory services. </mark>

LDAP (Lightweight Directory Access Protocol) plays a crucial role in name resolution and directory services within distributed systems. Here's a breakdown of its role:

**Role of LDAP in Name Resolution:**

- **Mapping Identifiers to Addresses:**
  - LDAP acts as a directory service that stores mappings between identifiers (e.g., user names, service names) and their corresponding addresses or other attributes.
  - Clients can query the LDAP directory using identifiers to retrieve the associated address or location information.
- **Centralized or Distributed Name Resolution:**
  - LDAP can be used in both centralized and distributed name resolution scenarios.
  - In a centralized setup, a single LDAP server manages the directory.
  - In a distributed setup, LDAP servers can be replicated or federated to improve scalability and fault tolerance.
- **Beyond Simple Address Resolution:**
  - Unlike DNS, which primarily resolves domain names to IP addresses, LDAP can store a wider range of attributes associated with each entry.
  - This allows for more complex name resolution scenarios, where clients may need to retrieve additional information beyond just the address.

**Role of LDAP in Directory Services:**

- **Hierarchical Data Storage:**
  - LDAP organizes directory information in a hierarchical structure, typically using a tree-like representation.
  - This allows for efficient storage and retrieval of data based on organizational or logical relationships.
- **Attribute-Based Queries:**
  - LDAP allows clients to perform complex queries based on attributes associated with directory entries.
  - This enables flexible and efficient searching for information.
- **Authentication and Authorization:**
  - LDAP is often used for authentication and authorization purposes.
  - Clients can authenticate with the LDAP server to verify their credentials, and access control lists can be used to control access to directory information.
- **Information Storage and Retrieval:**
  - LDAP is used to store and retrieve a wide range of information, including user accounts, organizational data, network resources, and application configurations.
  - This information can be used by various applications and services within a distributed system.
- **Standardized Access:**
  - LDAP provides a standardized way to access and manage directory information. This interoperability allows different applications and systems to share directory data.

**In summary:**

LDAP serves as a powerful tool for name resolution and directory services in distributed systems. Its hierarchical data model, attribute-based queries, and authentication capabilities make it well-suited for managing and accessing directory information in a scalable and efficient manner.
