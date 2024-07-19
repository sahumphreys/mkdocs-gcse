---
title: Binary Number System
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


> [!NOTE] The purpose of this section is to ...
> - Be familiar with the concept of a number base, in particular:
> 	- decimal (base 10)
> 	- binary (base 2)
> 	- hexadecimal (base 16)
> - Be able to convert between decimal, binary and hexadecimal number bases
> - Be familiar with, and able to use, hexadecimal as a shorthand for binary and to understand why it s used in this way


---

This section should be largely revision as it will have been covered by the GCSE
syllabus but will act as a useful reminder of one of the most fundamental
aspects of computer systems i.e. it's a digital machine and only processes
zeroes and ones!

## Numbering systems

Everything that takes place in the computer depends on two-state switches.  Each
switch can be either on or off which can more easily be represented as either a
`0` or a `1` (or, also, `False` or `True`).

We are familiar with the decimal (or denary) system where each digit occupies a
place equivalent to a power of 10, base 10.  With a two-state switch we only
need a two-number system, base 2, or __binary__ where each digit occupies a place
equivalent to a power of 2.

For convenience, we will also need to know the __hexadecimal__ number system, base
16, as a shorthand for representing binary.

All number systems share certain properties which are worth remembering:

- The digits are consecutive
- The number of available digits is always equal to the size of the base
- Zero is always the first digit
- The base number is never a digit
- When 1 is added to the largest digit , a sum of zero  and a carry of one
results
- Numeric values determined by the implicit positional value of the digits

These should be self-evident but it can be easy to get tripped up when thinking in a number base other than base 10.

Whichever base we are using the digit with the greatest impact on the value is known as the __most significant digit__, not surprisingly the digit with the least impact is known as the __least significant digit__.

## Number bases (binary and hexadecimal)

> Be familiar with the concept of a number base, in particular:
>
> - decimal (base 10)
> - binary (base 2)
> - hexadecimal (base 16)

So, lets' start with denary and take the number 245~10~ as an example.  This number consists of:

- $2$ hundreds
- $4$ tens
- $5$ ones (units)

Thus, $(2 \times 100) + (4 \times 10) + (5 \times 1) = 245$.

| $10^{3}$ | $10^{2}$ | $10^{1}$ | $10^{0}$ |
| -------- | -------- | -------- | -------- |
|     0    |     2    |    4     |    5     |


The system also accommodates numbers with fractional parts, thus $245.68$ would be:

| $10^{3}$ | $10^{2}$ | $10^{1}$ | $10^{0}$ | . | $10^{-1}$ | $10^{-2}$ | $10^{-3}$ |
| -------- | -------- | -------- | -------- |-- | --------- | --------- | --------- |
|    0     |    2     |    4     |    5     | . |     6     |     8     |     0     |

That is, $(2 \times 100) + (4 \times 10) + (5 \times 1) + (6 \times \frac{1}{10}) + (8 \times \frac{1}{100})$

Let's compare the principle of positional value with the binary representation of the decimal number 13~10~:

| $2^{3}$ | $2^{2}$ | $2^{1}$ | $2^{0}$ |
| ------- | ------- | ------- | ------- |
|    1    |    1    |    0    |    1    |

Thus, $(1 \times 8) + (1 \times 4) + (1 \times 1)$ = 13

As with denary, binary numbers with fractional parts works in the same way where the column headings after the binary point will be $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$ etc..

The same principle applied to denary is at work here too but now with powers of 2 rather than powers of 10. Each binary digit is shorted to __bit__.  Each bit is literally representing the state of a switch, it is either "on" or "off".  (NB.  It doesn't matter if '1' is used to represent 'on' and '0' for 'off' or vice versa as long as we are consistent).  In the next section we'll look at how these bits are grouped into bytes and higher multiples.

Long strings of binary digits can be tedious to write and hard to understand so a convenient shorthand is often preferred:  __hexadecimal__.  Hexadecimal is __base 16__ because it has $16$ digits and each digit multiplier is a power of $16$:

| Hexadecimal | Binary (four digits) |
| ----------- | -------------------- |
|     0       |        0000          |
|     1       |        0001          |
|     2       |        0010          |
|     3       |        0011          |
|     4       |        0100          |
|     5       |        0101          |
|     6       |        0110          |
|     7       |        0111          |
|     8       |        1000          |
|     9       |        1001          |
|     A       |        1010          |
|     B       |        1011          |
|     C       |        1100          |
|     D       |        1101          |
|     E       |        1110          |
|     F       |        1111          |

The beauty of hex is that one hex digit can stand in for four binary digits so conversion between the two is very easy.  Hex is used as a shorthand for binary for this reason though I can also be used in some programming languages as is indicated by placing `x` before the value e.g. $0x32fa6c4$.  This is useful as it's rare for a programming language to specify a value in binary.

## Converting decimal to binary

There are two methods, the first could be called "by inspection" and is better suited for smaller values (a byte or less), the second is more algorithmic.  Let's explore both using the decimal value $245~10~$.

### By inspection

- Find the nearest power of $2$ to the given value, in this case it's $128$ ($2^{7}$), put a $1$ in that column and then take $128$ away from the original value leaving $117$.  
- Repeat the process, this time with $117$ the remainder, putting a $1$ in the nearest column, $64$ ($2^{6}$) and take that away from $117$ leaving $53$.  
- Repeat, this time putting a $1$ in the closest column, $32$ ($2^{5}$), and take that away from $53$ leaving $21$.  
- Repeat, putting a $1$ in the next column, $16$ ($2^{4}$), and that away from $21$ leaving $5$  which can quickly be added in the remaining columns for $2^{2}$ and $2^{0}$.

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | -- | -- | -- | - | - | - | - |
|  1  |  1 |  1 |  1 | 0 | 1 | 0 | 1 |

Nothing complex there and provides insight into the algorithmic process which involves repeated division.  

### Repeated division

Take the decimal number and repeatedly divide by $2$ writing down the remainder and stop when zero is reached:

| Quotient | New Number | Remainder |
| -------- | ---------- | --------- |
|  245/2   |    122     |    1      |
|  122/2   |     61     |    0      |
|   61/2   |     30     |    1      |
|   30/2   |     15     |    0      |
|   15/2   |      7     |    1      |
|    7/2   |      3     |    1      |
|    3/2   |      1     |    1      |
|    1/2   |      0     |    1      |

Then read up from the bottom!

This can be described in pseudocode as:

~~~
	number = positive integer
	while (number > 0) {
		bit = number mod 2
		number = number div 2
		put bit to left of any previous bits
	}
~~~

> [!NOTE] The "magic number" $2$ represents the target base and can be replaced by another value to convert the binary number into any other base.

## Converting binary to decimal

Again, two methods can be applied:

1. Start from the left of the binary number, take your current total, multiply it by two and add the current digit and continue until there are no more digits left.  So, taking the binary number $11110101$:

- $2 \times 0 + 1 = 1$
- $2 \times 1 + 1 = 3$
- $2 \times 3 + 1 = 7$
- $2 \times 7 + 1 = 15$
- $2 \times 15 + 0 = 30$
- $2 \times 30 + 1 = 61$
- $2 \times 61 + 0 = 122$
- $2 \times 122 + 1 = 245$

2.  The second method uses the positional notation and multiplies each digit by their corresponding power of two and sums these products:

- $(1 \times 128) + (1 \times 64) + (1 \times 32) + (1 \times 16) + (1 \times 4) + (1 \times 1) = 245$

This can be described in pseudocode as:

~~~
	power = 1
	decimal = 0
	loop through all bits in the binarystring
		decimal = decimal + power * bit
		power = power * 2
~~~

## Converting decimal to hexadecimal

The method applied earlier to convert binary to decimal can be reapplied but dividing by 16 rather than 2.  The algorithm described above can be adapted to convert decimal into any other number base quite easily by replacing the target base value with a parameter to the function specifying the target base.

## Converting hexadecimal into binary

Each hexadecimal character can be coded by using four binary digits.  To convert the hexadecimal into binary just replace each hex character by its binary equivalent:

- $A35C = 1010 0011 0101 1100$

## Converting binary into hexadecimal

This is just the reverse of converting hexadecimal into binary!

## Questions

1.  Write the following as denary numbers:
    	a.  00001101
    	b.  00010111
    	c.  00011010
    	d.  00110101
    	e.  00110100
    	f.  01011100
    	g.  01101000
    	h.  11010100

2.  Convert the following denary numbers into binary:
        a.  129
		b.  137
		c. 196
		d. 172
		e. 1161
		f. 174
		g. 185
		h. 1148

3. Convert the following binary numbers into hexadecimal
   		a. 01011001
		b. 01101101
		c. 1111101011001110
		d. 1010000111011110

4. Convert the following denary numbers into hexadecimal
		a. 37
		b. 72
		c. 140
		d. 119

5. Convert the following hexadecimal numbers into binary:
		a. 5A
		b. B0D
		c. FFFF
		d. 2C8E

6. Convert the following hexadecimal numbers into denary:
		a. 28
		b. A4
		c. 5B
		d. 12B

