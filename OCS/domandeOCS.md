## Tutorial 4
Explain the following terms from the lecture slides:
RR, HRRN (Highest Response Ratio Next), SPN (Shortest Process Next), SRT (Shortest remaining time), FCFS.

You have learned about non-preemptive scheduling strategies in the
lecture. In the lecture, the strategies were presented for only one CPU at a time. However,
they can easily be extended to distribute incoming processes on multiple CPUs.
As an example, let's consider the checkouts of a supermarket. Each checkout
corresponds to a CPU and each customer that comes to the checkout represents a process.
The number of items purchased by a customer corresponds to the time a process takes to
execute. We assume that the time to register an item at the checkout is constant and set it to
one time unit, neglecting the actual payment process. Since customers in a supermarket
cannot be expected to let other customers go first, the FCFS strategy is usually used, i.e.
whoever reaches the checkout first is the first to be paid. Since customers in a supermarket
are concerned about their advantage, they always queue up at the checkout where the
waiting time is the shortest, i.e. the one in front of them.
the fewest items need to be registered.
A supermarket has three checkouts (K1, K2 and K3). There is no customer waiting at any
of the checkouts. Now customers arrive (almost simultaneously) with the following numbers
of items (in this order)
one:
6, 15, 23, 10, 3, 13, 15, 7, 20, 40, 19, 4, 6, 21
(14 customers).
O. B. d. A. the first customer lines up at K1, the second at K2, the third at K3.
Document the resulting queues at checkouts K1, K2, and K3.
How many time units on average does a customer have to wait until he arrives at the
checkout? After how many time units is he finished on average?

---
## Tutorial 5
First-Fit: Starting from the beginning, allocate the first free memory area that is large
enough to fulfill the request.
Rotating-First-Fit: Like First-Fit, but a suitable area is searched starting from the position
of the previous placement.
If the end of the memory is reached, the search continues at the beginning of the memory
(maximum up to the position of the previous placement). At the first request, the
search starts at the beginning of the memory.
Best-Fit: Occupy the smallest free memory area where the request fits.
What does the above memory look like when four requests of size 300 B, 512 B, 2048 B and
624 B arrive in succession? For each strategy, note the free memory areas after each request
and indicate for which methods the requests can be fulfilled!
Note that the data is always stored left-justified in a gap and once occupied memory areas
are not released again!

---
## Tutorial 6
Answer the following questions and discuss as appropriate:
1. What does Direct Memory Access (DMA) mean for the communication between
devices and CPU? How does the coordination work? What does DMA mean for
the security of our system?
2. What is the goal of I/O buffering and how is it achieved?
3. What are the different configurations of RAID and what are the advantages of each?
4. Where is the file name stored?
5. What is the function of pseudo file systems? Explain the UNIX principle
"Everything is a file" in this context.
6. What kind of abstraction does the Virtual File System provide?
7. What does an inode represent in a UNIX file system? What different
"types" can there be? Put this in context with the VFS and the pseudo file systems.
Describe the different ways to allocate storage space for files. These include contiguous
allocation,
chained allocation,
and indexed allocation.
Name the advantages and
disadvantages of each method, particularly with respect to file growth, jumping to specific file
locations, and administrative overhead. 

---
## Tutorial 07
1. What is the intranet, Internet, what is the World Wide Web (WWW)? Clearly distinguish the three terms from each other.
2. What does protocol mean in the context of the Internet; which protocols are used?
3. The concept of protocol stack is a way to model how the Internet works. We have learned about two models in this context; what are they, how do they differ, and what are the advantages and disadvantages of each?
    
    Do you accurately portray reality?

4. IPv6 was standardised by the Internet Engineering Task Force (IETF) back in 19961. What hurdles were (and are) encountered in the introduction of IPv6, what makes this protocol different from its predecessor?
5. 
6. Sockets are a possibility under UNIX to provide the programmer with communication interfaces between processes - possibly on different computers. Sockets are file descriptors on files or inodes of the type S_IFSOCK. This means that we can access sockets with the regular functions write or read and thus "send" or "receive" data.
    
    But there are also the special functions send and recv which offer even more options especially for sockets.
    
    How do stream sockets and datagram sockets differ?
    
6. In any case, a socket must be assigned an address (struct sockaddr) before it can be
    
    used.  
    What "kind" of address this is depends on the specific protocol being used.
    
    What protocols can we use to communicate with sockets and what addresses are used for each of them?
---
## Tutorial 8
1. List at least three tasks of the Data link layer.
2. Consider the string consisting of the following two characters ~? (tilde, question mark).

1. a)  Specify the bit string of the characters. Assume that the characters are ASCII
    
    encoded.
    
2. b)  Add a CRC-16 checksum to the bit string. Indicate how you calculated this checksum.
    
    The CRC you should use is specified by the polynomial 0x8005 or x16 + x15 + x2 + 1, but you should assume that the input is LSB first. Furthermore the start value of the shift register is 0xFFFF and the final xor value is
    
    also 0xFFFF.
    
3. c)  Apply bit stuffing to the (supplemented) bit string. However, do not add
    
    additional flag bits at the beginning or end.
    
4. d)  Plot the voltage waveform that occurs when the resulting bit string is transmitted
    
    using Manchester encoding.
    

For this task, note the definitions of bitstuf- fing and Manchester encoding used in the slides.

--- 
## Tutorial 9
1. What is the difference between switches and routers? What protocols do they each need to understand?

2. Explain the following protocols and their function: a) Open Shortest Path First (OSPF)  
b) Border Gateway Protocol (BGP)  
c) Internet Protocol (IP)

d) Address Resolution Protocol (ARP)  
e) Internet Control Message Protocol (ICMP)

3. In the following image there are several routers including routing tables.

1. a)  Determine which path is taken by a packet sent from 1.1.1.1 with the destination 5.1.1.1. Name in each case why the routing decision is made in this way at the respective router.
    
2. b)  Assume that the following entry is added to Router 3.1.1.1 by mistake: 5.0.0.0 | 255.0.0.0 | 2.1.1.1 | 1.
    
    Does the path from 3a change? Do any problems arise? If so, how are these being addressed?
![[Pasted image 20230711130534.png]]
---
## Tutorial 10
1. Explain the difference between TCP and UDP. What other IP-based protocols are there?
    
2. What happens when a packet is sent with a TTL that is not sufficient to reach the destination? What kind of error information do we get and how?
    
    For example, suppose we send UDP packets to a destination, starting with a TTL of one. If the packet does not arrive, we send again with a higher TTL - until the packet arrives. Why would you want to do this other than to simply find out how "far" it is to the destination?
    
3. What does a typical connection setup and teardown look like for TCP? Why is there a handshake "in both directions"? What should a SYN signal, what FIN?
    
4. Let's assume you want to download the latest exercise sheet from the KVV site and are watching a livestream at the same time. Furthermore, there are no technical problems in your connection to the FU server. How can it still happen that you cannot download the exercise sheet from the KVV page?
    
5. For both UDP and TCP, name at least two example applications that use this protocol. Give reasons why this makes sense for this application.
---
## Tutorial 11
1. Why is it easier to introduce a new protocol on layer 4 (transport layer) than on layer 3 (internet / network layer)?

2. ISO/OSI and TCP/IP model.

1. a)  Draw all layers of the ISO/OSI model as well as the TCP/IP model and label each layer.
    
2. b)  If possible, assign the layers of the two models to each other.
    
3. c)  Name at least one protocol for each layer of the TCP/IP model.
    
4. d)  Assign actors (hardware, devices/software for forwarding) to the respective layers.
    

e) For the layers where it is possible, name addresses that are used on this layer. Are the addresses logical or physical addresses (not memory addresses)?

3. How is it possible that you receive an email with a fake sender?

4. You receive a supposed e-mail from your bank and click on the link there www.meinebank.de. How can it be that you do not land on the website of your bank?

5. What are the individual parts of a URL? What are they each used for?