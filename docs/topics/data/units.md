---
title: Units of Information
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


> [!NOTE] The purpose of this section is to ...
> 
> Know that:
> - the bit is a fundamental unit of information (either 0 or 1; a byte is a group of 8 bits)
> - $2^n$ different values can be represented with $n$ bits
> - quantities or bytes can be described using binary prefixes representing powers of 2, or using decimal prefixes representing powers of 10

---

The binary digit, or __bit__, is the fundamental unit of information for digital systems.  They are usually described in groups of 8 bits, known as a __byte__ (which as we'll see later gives enough space to score a single character like 'h' or 'W').  One bit can have two distinct values ($2^1$), two bits can have four distinct values ($2^2$), three bits provide eight ($2^3$).  Thus, one byte can have 128 distinct values (which as we'll see later provides enough space to store values representing characters, digits and punctuation).  


You will also meet the term __nibble__ to represent half a byte (which is an attempt at humour by computer scientists) and the __word__ which is the amount of data a processor can handle.  the most common word sizes are 32-bits and 64-bits.  The precise amount of data in a word is a bit fuzzy as some processors might have different word sizes for different tasks but will usually hold for the number of bits the CPU can process in one chunk.

Bytes are small so they are most often used to measure the amount of data, the characters in a text document or pixels in an image file, or the amount of storage available:

| Unit | Equivalent (bytes) |
| ---- | ---------- |
| 1 kilobyte (KB) | 1,024 |
| 1 megabyte (MB) | 1,048,576 |
| 1 gigabyte (GB) | 1,073,741,824 |
| 1 terabyte (TB) | 1,099,511,627,776 |
| 1 petabyte (PB) | 1,125,899,906,842,624 |

To provide some context for these larger values, 1TB is roughly equivalent to the amount of information as all the books in a large library and 1PB would create (roughly) a stack of CDs a mile high!

These values are used to define amounts of storage space available and useful to note that hard drive manufacturer's will usually use the decimal system to define storage e.g. 500GB to represent 5,000,000,000 bytes (that's $500 \times 10^9$ bytes).  However, your operating system will define the size of the drive using binary, $465 \times 2^{30} = 465 GB$, and it will appear as if you've lost 35 GB of storage space!

Whilst the above definitions remain as accepted terms they were actually replaced back in 2000.  To be up-to-date (!) we should all be using the following:

| Unit | Short form | Magnitude |
| ---- | ---------- | --------- |
| kibibyte | KiB | $2^{10}$ |
| mebibyte | MiB | $2^{20}$ |
| gibibyte | GiB | $2^{30}$ |
| tebibyte | TiB | $2^{40}$ |
| pebibyte | PiB | $2^{50}$ |

These have been slow to get adopted, perhaps because:

- they sound a bit ridiculous
- hard drive manufacturers do not use them
- it's hard to break out of a tradition
