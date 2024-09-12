---
title: Negative Numbers
image: binary.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


!!! note "Objectives"
    - Know that signed binary can be used to represent negative integers and that one possible coding scheme is two's complement
    - Know how to represent negative and positive integers in two's complement
    - Know how to perform subtraction using two's complement


Using the binary number system to represent the voltages (on or off) presents a problem when needing a third symbol to represent a minus sign ('-'), we have to use the two symbols we have, '0' and '1', to represent both the size and sign of any number.  

There are two ways of doing this:

- Sign and Magnitude
- Twos Complement

## Sign and Magnitude

Sign and magnitude is a method for representing negative numbers in binary by using the most significant bit (MSB) as a sign indicator. In this system, the MSB (also called the sign bit) is set to `0` for positive numbers and `1` for negative numbers. The **remaining bits** represent the magnitude (absolute value) of the number.

For example, in an 8-bit system:

- `00001010` represents the positive number $+10_{10}$.
- `10001010` represents the negative number $-10_{10}$.

The main drawback of sign and magnitude representation is that it allows for two representations of zero (`00000000` for +0 and `10000000` for -0), which can complicate arithmetic operations. 

Additionally, arithmetic with sign and magnitude can be more complex compared to other methods, such as two's complement.

## Twos Complement

Twos complement representation again uses the most significant bit to act as the sign bit but it also contributes to the actual value.  If the MSB is 1, it represents a negative value equal to $-2^{(n-1)}$ in an n-bit system.  

Consider the following table:

| $2^{-2}$ | $2^{1}$ | $2^{0}$ | Decimal |
| :-------:  | :-------: | :-------: | :-------: |
|    0     |    0    |    0    |    0    |
|    0     |    0    |    1    |    1    |
|    0     |    1    |    0    |    2    |
|    0     |    1    |    1    |    3    |
|    1     |    0    |    0    |   -4    |
|    1     |    0    |    1    |   -3    |
|    1     |    1    |    0    |   -2    |
|    1     |    1    |    1    |   -1    |

Each of the negative numbers now has a $1$ as its most significant bit whereas the positive numbers have $0$ in that position.  

It also ensures there is only one representation of zero.

Take note of some other observations:

- The most negative value has $1$ in the most significant bit and all other values are set to $0$
- For $-1$, every bit is set to $1$
- The most positive value has a $1$ in every position except for the most significant bit which is $0$
- Using 3 bits the number of values possible is $2^3 = 8$ but the range is $-4 \text{ to } +3$

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
| :------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|    1     |    1    |    1    |    0    |    1    |    0    |    0    |    1    |

For example, using method 2, $-40$

- $00101000_2$	($40$ converted into binary)
- $11011000_2$	(copy all from the left up to the first $1$, then flip remaining bits)

To confirm:

| $2^{-7}$ | $2^{6}$ | $2^{5}$ | $2^{4}$ | $2^{3}$ | $2^{2}$ | $2^{1}$ | $2^{0}$ |
| :------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
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

{{ show_questions(page.title, page.meta.filename) }}
