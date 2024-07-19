---
title: Binary Arithmetic
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

## Unsigned binary

> [!NOTE] The purpose of this section is to ...
> - Know how to calculate the range of a given number of bits, $n$
> - Know the difference between unsigned binary and signed binary
> - Know that in unsigned binary the minimum and maximum values fora given number of bits, $n$, and 0 and $2^n - 1$ respectively
> - Be able to add two unsigned binary integers
> - Be able to multiply two unsigned binary integers

--- 

Unsigned binary is used for positive whole numbers (integers).  The range of values that be coded in this way is dependent on the number of bits allocated to represent the number:

| No. of bits | No. of values | Maximum (decimal) | Unsigned binary | Compact decimal |
|-------------|---------------|-------------------|-----------------|-----------------|
| 1           | 2             | 1                 | 1               | $2^1 - 1$       |
| 2           | 4             | 3                 | 11              | $2^2 - 1$       |
| 3           | 8             | 7                 | 111             | $2^3 - 1$       |
| 4           | 16            | 15                | 1111            | $2^4 - 1$       |
| 5           | 32            | 31                | 11111           | $2^5 - 1$       |
| 6           | 64            | 63                | 111111          | $2^6 - 1$       |
| 7           | 128           | 127               | 1111111         | $2^7 - 1$       |
| 8           | 256           | 255               | 11111111        | $2^8 - 1$       |

## Unsigned binary arithmetic

Adding binary numbers follows the same rules as for denary.  Add each column starting with the least significant bit and move to the right.  Any carry from a column is added into the next column and so on.  It's relatively trivial as their are only four possible outcomes when adding two binary digits:

- $0_2 + 0_2 = 0_2$
- $0_2 + 1_2 = 1_2$
- $1_2 + 0_2 = 1_2$
- $1_2 + 1_2 = 0_2$ carry $1_2$

Bearing the carry in mind, four additional rules should be referenced:

- $0_2 + 0_2 + 1_2 = 1_2$
- $0_2 + 1_2 + 1_2 = 0_2$ carry $1_2$
- $1_2 + 0_2 + 1_2 = 0_2$ carry $1_2$
- $1_2 + 1_2 + 1_2 = 1_2$ carry $1_2$

For example, adding the binary number $01101110_2$ and $00011100_2$:

	01101110
	00011100 +
	--------
	10001010
	--------
	1111

## Unsigned binary multiplication

Multiplying binary numbers follows the same algorithm as for denary.  The multiplicand is multiplied by each digit in the multiplier in turn and the partial products are then added together to produce the result.  For example, multiplying the binary number $110_2$ by $11_2$:

		110
		 11 x
	-------
	    110
	   1100 +
	-------
	  10010
	-------
	   1

This can be simplified when it is observed that the multiplier only has 0s and 1s so each multiplication step will produce either zeros or a copy of the multiplicand.  So, binary multiplication is repeated binary addition!  A further example to illustrate the shifting of the partial product:

		1011
		 110
	--------
	       0
	   1011
	  1011
	--------
	 1000010
	--------
	 1111   

## Questions

1. Add the following binary numbers together, show your working:
		a. 11010 + 101
		b. 1001 + 101
		c. 10011 + 1011
		d. 10011 + 10011
		e. 10110 + 1011
		f. 101101 + 101101
		g. 101011 + 10110
		h. 1101111 + 1011101

2.  Multiply the following binary numbers together, show your working:
		a. 110 x 11
		b. 1001 x 101
		c. 1011 x 1001
		d. 1101 x 11
		e. 1100 x 110
		f. 1001 x 1001
		g. 10111 x 1010
		h. 10011 x 111

		