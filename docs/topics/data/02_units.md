---
title: Units
image: binary.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
    - The bit is a fundamental unit of information (either 0 or 1)
    - A byte is a group of 8 bits
    - Explain the least significant bit and most significant bit in a binary number
    - Know how to identify whether a binary number is odd or even
    - Calculate the range of values for a given number of bits
    - Know the common names for multiples of bytes

In the last section we saw the binary digit, or __bit__, is the fundamental unit of information for digital systems, it is either a $0$ or a $1$.  One bit can have two possible values: 1 or 0.  

Bits are described in groups of 8 bits, known as a __byte__ (which as we'll see later gives enough space to score a single character like 'h' or 'W'). 

## MSB and LSB

In binary notation, MSB (**Most Significant Bit**) and LSB (**Least Significant Bit**) refer to the positions of the bits within a binary number, indicating their relative importance in terms of value.

**Most Significant Bit (MSB):**

- The MSB is the leftmost bit in a binary representation.
- It holds the highest value in the binary place value system.
- Changing the MSB can significantly affect the overall value of the binary number.
- In an 8-bit binary number, the MSB is the bit in the 128's place (2^7).

**Least Significant Bit (LSB):**

- The LSB is the rightmost bit in a binary representation.
- It holds the lowest value in the binary place value system.
- Changing the LSB has the smallest impact on the overall value of the binary number.
- In an 8-bit binary number, the LSB is the bit in the 1's place (2^0).

Here's an example of an 8-bit binary number with the MSB and LSB labeled:

```pseudocode
MSB                                LSB
 ↓                                  ↓
 1    0    1    1    0    0    1    0
2^7  2^6  2^5  2^4  2^3  2^2  2^1  2^0
```

In this example, the leftmost bit (1) is the MSB, and the rightmost bit (0) is the LSB. The MSB and LSB are essential concepts when working with binary numbers, especially in contexts where the relative importance of bits in a number is significant, such as in digital systems and data encoding.

## Odd or Even

For binary numbers the LSB determines whether a number is odd or even. If the LSB is 1 the number is odd, if the LSB is 0 the number is even.  For example:

- $00000101_2$: The LSB is a $1$ so it must be an odd number.  (It's the decimal value $5_{10}$.)
- $01010100_2$:  The LSB is a $0$ so it must be an even number. (It's the decimal value $84_{10}$.)

!!! note
    Although not technically required get into the habit of writing out ALL binary numbers in multiples of 8, as bytes, with leading zeros.

## Ranges of values

Note:

- One bit can have two distinct values ($2^1$), ranging between $0$ and $1$
- Two bits can have four distinct values ($2^2$), ranging between $0$ and $3$
- Three bits provide eight ($2^3$), randing between $0$ and $7$
 
Thus, one byte can have $256$ distinct values ranging between $0$ and $255$  (which as we'll see later provides enough space to store values representing characters, digits and punctuation) because $2^8$ is $256$.  

**REMEMBER**

For a given number of bits:

- The maximum number is: $2^{n-1}$. For instance, if we have 3 bits the maximum value is: $2^{3-1} = 7$
- The number of numbers is $2^n$. For unsigned integers the minimum and maximum values are $0$ and $2^{n-1}$ respectively where $n$ is the number of bits.

!!! warning
    - Do not get confused between the maximum value (2n-1) and number of values (2n) that can be represented for a given number of bits. 
    - The number of bits available determines the number, the range, of values that can be represented in that number of bits.

## Byte multiples

Bytes are small so they are most often used to measure the amount of data, the characters in a text document or pixels in an image file, or the amount of storage available:

| Unit | Equivalent (bytes) |
| ---- | ---------- |
| 1 kilobyte (KB) | 1,024 |
| 1 megabyte (MB) | 1,048,576 |
| 1 gigabyte (GB) | 1,073,741,824 |
| 1 terabyte (TB) | 1,099,511,627,776 |
| 1 petabyte (PB) | 1,125,899,906,842,624 |

!!! note
    Can you find out the names of even bigger byte multiples? How big is a **Zoogolplex**?

You will also meet the term __nibble__ to represent half a byte (which is an attempt at humour by computer scientists) and the __word__ which is the amount of data a processor can handle.  The most common word sizes are 32-bits and 64-bits.  The precise amount of data in a word is a bit fuzzy as some processors might have different word sizes for different tasks but will usually hold for the number of bits the CPU can process in one chunk.

To provide some context for these larger values, 1TB is roughly equivalent to the amount of information as all the books in a large library and 1PB would create (roughly) a stack of CDs a mile high!

These values are used to define amounts of storage space available and useful to note that hard drive manufacturer's will usually use the decimal system to define storage e.g. 500GB to represent 5,000,000,000 bytes (that's $5 \times 10^9$ bytes).  However, your operating system will define the size of the drive using binary, $5 \times 2^{30} = 465 GB$, it seems 35GB of storage space has been lost!

Whilst the above definitions remain as accepted terms they were actually replaced back in 2000.  To be up-to-date (!) we should all be using the following[^1]

[^1]: Some exam boards at GCSE require knowledge of these terms.

| Unit | Short form | Magnitude |
| ---- | ---------- | --------- |
| Kibibyte | KiB | $2^{10}$ |
| Mebibyte | MiB | $2^{20}$ |
| Gibibyte | GiB | $2^{30}$ |
| Tebibyte | TiB | $2^{40}$ |
| Pebibyte | PiB | $2^{50}$ |

These have been slow to get adopted, perhaps because:

- they sound a bit ridiculous
- hard drive manufacturers do not use them
- it's hard to break out of a tradition

## Questions

{{ show_questions(page.title, page.meta.filename) }}

