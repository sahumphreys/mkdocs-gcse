---
title: Negative Numbers
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

> [!NOTE] The purpose of this section is to ...
> 
> - Know that signed binary can be used to represent negative integers and that one possible coding scheme is two's complement
> - Know how to represent negative and positive integers in two's complement
> - Know how to perform subtraction using two's complement
> - Be able to convert between unsigned binary and decimal and vice versa
> - Know that in unsigned binary the minimum and maximum values for a given number of bits, $n$, are 0 and $2{^n}-1$ respectively

---

Using the binary number system to represent the voltages (on or off) presents a problem when needing a third symbol to represent a minus sign ('-'), we have to use the two symbols we have, '0' and '1', to represent both the size and sign of any number.  There are different ways of doing this but the one we'll consider here is known as __two's complement__.  Twos complement representation uses the most significant bit to act as the sign bit and its weighting is always negative.  Consider the following table:

| $2^{-2}$ | $2^{1}$ | $2^{0}$ | Decimal |
| -------  | ------- | ------- | ------- |
|    0     |    0    |    0    |    0    |
|    0     |    0    |    1    |    1    |
|    0     |    1    |    0    |    2    |
|    0     |    1    |    1    |    3    |
|    1     |    0    |    0    |   -4    |
|    1     |    0    |    1    |   -3    |
|    1     |    1    |    0    |   -2    |
|    1     |    1    |    1    |   -1    |

Each of the negative numbers now has a $1$ as its most significant bit whereas the positive numbers have $0$ in that position.  Take note of some other observations:

> [!NOTE]
> - The most negative value has $1$ in the most significant bit and all other values are set to $0$
> - For $-1$, every bit is set to $1$
> - The most positive value has a $1$ in every position except for the most significant bit which is $0$
> - Using 3 bits the number of values possible is $2^3 = 8$ but the range is $-4 \text{ to } +3$

## Converting decimal to twos complement binary

There are two methods.  Before using either of these methods the decimal integer must be converted into binary using any of the methods, e.g. repeated division by two, outlined above.  Ignore whether the decimal number is negative, treat it as positive then follow either method 1 or 2 below:

1. Invert all of the binary values, and add 1
2. Start with the least significant bit, copy down all values up to and including the first $1$ encountered, then flip the remaining digits.

For example using method 1, $-23$:

- $00010111_2$	($23$ converted into binary)
- $11101000_2$	(Invert all the digits)
- $11101001_2$	(Added $1$)

To confirm:

| $2^{-7}$ | $2^{6}$ | $2^{5}$ | $2^{4}$ | $2^{3}$ | $2^{2}$ | $2^{1}$ | $2^{0}$ |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|    1     |    1    |    1    |    0    |    1    |    0    |    0    |    1    |

For example, using method 2, $-40$

- $00101000_2$	($40$ converted into binary)
- $11011000_2$	(copy all from the left up to the first $1$, then flip remaining bits)

To confirm:

| $2^{-7}$ | $2^{6}$ | $2^{5}$ | $2^{4}$ | $2^{3}$ | $2^{2}$ | $2^{1}$ | $2^{0}$ |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|    1     |    1    |    0    |    1    |    1    |    0    |    0    |    0    |


## Converting twos complement binary into decimal

As for converting unsigned binary number, sum the products of the column weightings.  Thus, for the example above, $-40_{10}$:

$(1 \times -128) + (1 \times 64) + (0 \times 32) + (1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (0 \times 1) = 40_{10}$

## Subtraction with twos complement

Taking advantage of the fact that $A - B = A + (-B)$ makes addition and subtraction very simple for designers of circuits as the same circuitry can be used for both.  So, to do e.g. $7 - 4$ we can do instead $7 + (-4)$:

$0111_2 - 0100_2 \rightarrow 0111_2 + (-0100_2) \rightarrow 0111_2 + 1100_2 = (1)0011_2$ 

The carry generated in the final answer is just ignored so that the answer uses the same number of bits as those used we started with.

## Range with a given number of bits

There are only so many bits that can be allocated to represent a number, we can't magic new circuitry out of thin air!  Therefore, knowing the range of twos complement integers that can be accessed with a given number of bits is really important.

The range can be calculated using the following formula:  $-2^{n-1}$ to $2^{n-1} - 1$.  Thus, the range for 8 bits will be $-2^7$ to $2^7 - 1$, or, $-128$ to $127$.

## Questions

1. Convert the following denary values into 8-bit binary (using twos complement)
        a. -26
        b. -23
        c. -33
        d. -85
        e. -65
        f. -120
        g. -112
        h. -91

2.  Convert the following 8-bit twos complement binary numbers into denary:
        a. 11100001
        b. 10001101
        c. 11001100
        d. 10101110
        e. 11110111
        f. 11110011
        g. 11011000
        h. 01001100

3.  How how a computer would carry out the following calculations in binary, show your working:
        a. 18 - 9
        b. 26 - 15
        c. 17 - 34
        d. 51 - 14
        e. 15 - 37
        f. 49 - 11
        g. 41 - 1
        h. -5 - 17