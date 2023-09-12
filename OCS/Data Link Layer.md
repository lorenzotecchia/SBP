### Setting for Data Link Layer
---
Link Layer sits on top of [Physical Layer](Physical%20Layer.md) 
- Can thus use a bit stream transmission service
- But: service might have incorrect bits
Expectations of the higher layer ([Networking Layer](Networking%20Layer.md))
- Wants to use either a packet service 
	- Rarely, a bit strema service
- Doesn't really want to be bothered by errors
- Doesn't really want to care about issues at the other hand
![[Pasted image 20230626163335.png]]
### Services of Data Link Layer
---
Given settings and goals. the following services are required
<!--ID: 1688997324813-->


Transparent communication between two directly connected nodes

Framing of a physical bit stream into a structure of frames/packets
- Frames can be retransmitted, scheduled, ordered, ...
Error control
- Detection and correction
Connection setup and release
- Signaling and resource management on hosts
Acknowledgement-based protocols
- Make sure that a frame has been transmitted
Flow contro
- Arrange for appropriate transmission speed between hosts

### Framing
How to turn a bit stream into a sequence of frames?
> More precisely: how does a receiver know when a frame starts and when it ends?
![[Pasted image 20230626155307.png]]
Note: Physical layer might try to detect and deliver bits when the sender is not actually transmitting anything
>Receiver tries to get any information from the physical medium


### Framing by character / Byte count
---
Idea: Announce number of bits (bytes, characters) in a frame to the receiver
>Puts this information at beginning of a frame _frame header_
![[Pasted image 20230626155328.png]]
>Problem: What happens if _count_ information itself is damaged during transmission?
- Receiver will loose frame synchronisation and produce different sequence of frames than original one
![[Pasted image 20230626155343.png]]
<!--ID: 1688997324820-->


### Basic technique: Control header
---
Although "character count" is not a good framing technique, it illustrates an important technique: _headers_
- If sender has to communicate administrative or control data to receiver, it can be added to actual packet content -> ("payload")
- Usually at the start of the packet; sometimes at the end ("trailer")
- Receiver uses header to learn about sender's intention
> Same principle applicable to all packet-switched communication
![[Pasted image 20230626155438.png]]
<!--ID: 1688997324822-->


### Framing by Flag Bit Patterns / Bit Stuffing
---
<!--ID: 1688997324823-->


Use dedicated flag bits to demarcate start/stop of frame 
- Use bit pattern – often, 01111110  
- Bit stuffing process:
	- Whenever sender sends five 1s in a row, it automatically adds a 0 into bit stream – except in flag pattern - Receiver throws away (“destuffs”) any 0 after five 1s
![[Pasted image 20230626155538.png]]

### Link Layer Functions - Error Control
---
<!--ID: 1688997324824-->


Error detection – Check for incorrect bits
Error correction – Correct erroneous bits

- Forward error correction (FEC) – invest effort before error happened; avoid delays in dealing with it 
	- Redundancy / overhead

- Backward error correction – invest effort after error happened; try to repair it
	- ARQ (Automatic Repeat reQuest)
		- -> Delays
![[Pasted image 20230626155558.png]]


### Error Detection: Cyclic Redundancy check (CRC)
---
CRC can check arbitrary, unstructured sequence of bits  
A check sequence (CRC code) is appended to checked data
<!--ID: 1688997324825-->


- Typically calculated by a feedback shift register in hardware

When calculating the CRC code a generator polynomial is used which is known to both sender and receiver

Calculation of CRC code

1. View bit sequence as polynomial with binary coefficients:
    - **100010** is viewed as ***1*x5+0*x4+0*x3+0*x2+1*x1+0*x0***
1. Expand polynomial with n 0s, n is the degree of the generator polynomial
2. Divide expanded bit sequence (i.e. polynomial) by generator polynomial
     - CRC code is the remainder of the division, result is discarded  
3. Receiver again divides received bit sequence (including the CRC code) by generator polynomial 
	- If no error occurred the remainder is 0


## Flow Control
---
### Link layer Functions - Flow Control
Assumptions in an ideal world:  
- Sender/receiver are always ready to send/receive  
- Receiver can handle amount of incoming data  
- No errors occur that cannot be handled by Forward Error Correction (FEC)
![[Pasted image 20230626155634.png]]
>What happens if packets are lost?  
>What happens if the sender floods the receiver?
- Imagine a web server sending data to a mobile phone...
<!--ID: 1688997324827-->


### Very Simple Solution: Stop-and-Wait
---
Concentrate on one single packet  
Receiver acknowledges correct reception of the packet  
Sender has to wait for that acknowledgement before continuing with next packet
![[Pasted image 20230626155656.png]]
<!--ID: 1688997324828-->



## Network Topologies
### Topologies by Network Structure
---
![[Pasted image 20230626155118.png]]
<!--ID: 1688997324829-->



## Medium Access Control
---
Motivation: Satellite Medium Access
![[Pasted image 20230626155215.png]]
<!--ID: 1688997324830-->



### Approaches to Medium Access
---
Several stations want to access the same medium
- How to separate stations?
![[Pasted image 20230626155827.png]]
<!--ID: 1688997324831-->


### Dynamic / Controlled MAC: Polling
---
Single leader station  
One or more follower stations  
Typically bus topology (but also tree)  
Leader polls followers according to table or cyclically Followers may answer only after being polled
<!--ID: 1688997324832-->



### Dynamic / Contention MAC: ALOHA
---
No central control, no coordination between stations Stations start sending whenever they want to
>Collisions destroy frames  
<!--ID: 1688997324833-->


>Receiver may send acknowledgement after correct reception

![[Pasted image 20230626160127.png]]


### Dynamic / Contention MAC: Slotted ALOHA
---
Send packets of fixed length within fixed time-slots 
>Requires common time-base for synchronisation
<!--ID: 1688997324834-->


Transmission starts at begin of slot only, thus only complete collisions may occur
![[Pasted image 20230626160345.png]]
