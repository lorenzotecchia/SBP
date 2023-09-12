### Transmission of data requires physical representation of data
A Signal is the physical representation of data  
An analog signal is a sequence of continuous values A digital signal is a sequence of discrete values

---
### Computers deal with digital signals

The physical layer transmits data based on signals through space

The need to convert - **Quantisation**  
- Computers can only deal with digital data => discrete signal  
- Physical mediums are by nature analog => continuous signal  
- Must convert from digital signal to analog signal (and vice versa)

The need to measure - **Sampling**
- Computers can only deal with discrete time  
- Physical mediums’ state vary continuously  
- Must rely on periodical measurements of the physical medium (> 2 * bandwidth of the signal)
![[Pasted image 20230626160741.png]]

---
### Definition of Bandwidth & Throughput
**Bandwidth**  
- Interval of the spectrum, difference between upper and lower frequencies, measured in Hertz
- Example: classical telephony over copper wires supports 300 – 3400Hz, thus bandwidth B = 3400Hz - 300Hz = 3100 Hz
**Throughput**  
- Amount of bits per second transmitted over a system, measured in bit/s

**_Shannon's_ algorithm** brings this together  
- Achievable data rate is limited by noise in real systems  
- More precisely: by relationship of signal strength compared to noise, i.e., Signal-to-Noise Ratio (SNR, S/N) - S: signal strength; N: noise level; B: bandwidth in Hz;  
- S/N commonly expressed in dB: S/N [dB] = 10×log10(S/N)
---
### Electromagnetic Spectrum
![[Pasted image 20230626161142.png]]

---
### Real technical systems are always bandwidth-limited
![[Pasted image 20230626161205.png]]

---
### Bit rate vs. bandwidth: Medium limiting harmonics
![[Pasted image 20230626161227.png]]

---
### Tasks of Physical Layer
Responsible for turning a logical sequence of bits into a physical signal that can propagate through a medium - Many forms of physical signals  
- Signals are limited by their propagation in a physical medium  
- Limited bandwidth, attenuation, dispersion, and by noise

Includes connectors, media types, voltages, ...

---
### Basic Service of Physical Layer: Transport Bits
Physical layer should enable transport of bits between two locations A and B Abstraction: Bit sequence (in order delivery)
- But no guarantee on correct transmission of bits
---
### Example: Transmit Bit Pattern for Character “b”
Represent character “b” as a sequence of bits  
Use ASCII code ➙ “b” = 98, as binary number 01100010 
Resulting current on the wire:
![[Pasted image 20230626162603.png]]
Use ASCII code ➙ “b” = 98, as binary number 01100010 
Typical pattern at the receiver:
![[Pasted image 20230626162634.png]]


---
### Interference
Noise  
- Background noise - Thermal

Echoes  
- E.g. at connections

Crosstalk  
- E.g. interference across wires

ELF  
- Extreme low frequency, e.g. 50/60 Hz AC

Spikes  
- Short, high amplitude
---
### Example: Results of Interference
![[Pasted image 20230626162750.png]]

---
### When to Sample Received Signal?
How does the receiver know _when_ to check the received signal for its value? - One typical convention: In the middle of each symbol  
- But when does a symbol start?
- The length of a symbol is usually known by convention via the symbol rate

The receiver has to be _synchronised_ with the sender at bit level - Link layer will have to deal with frame synchronisation  
- There is also character _synchronisation_ – omitted here
---
### Extract Clock Information from Signal
Put enough information into data signal itself so that receiver can know immediately when a bit starts/stops 
>Would the simple 0/low, 1/high mapping of bit/symbol work?

Receiver can use 0-1-0 transitions to detect length of a bit

Fails depending on bit sequences, e.g. long runs of 1s/0s 
>Receiver can loose synchronisation
>Not nice not to be able to transmit arbitrary data

---
### Manchester Encoding
Idea: At each bit, provide indication to receiver that this is where a bit starts/stops/has its middle 
- For a 0 bit, have symbol change in middle of bit from low to high  
- For a 1 bit, have the symbol change in middle of bit from high to low
![[Pasted image 20230626163042.png]]
The signal is self-clocking since one transition per period is guaranteed
>Disadvantage: bit rate is as half as high as baud rate (i.e. changes in signal values)

---
### Achievable Data Rate with Noise
Achievable data rate is limited by noise  
- More precisely: by relationship of signal strength compared to noise, i.e., Signal-to-Noise Ratio (SNR, S/N)

Shannon’s formula:
	**maximum data rate [bit/s] = H log2 (1 + S/N)**
