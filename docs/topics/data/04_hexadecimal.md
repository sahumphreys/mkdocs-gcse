---
title: Hexadecimal
image: binary.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


!!! note "Objectives"

    - To be able to explain why hexadecimal is often used in computer science.
    - To understand how hexadecimal can be used to represent whole numbers.
    - To be able to convert a hexadecimal number into binary, and vice versa
    - To be able to convert a binary number into hexadecimal, and vice versa
    - To be able to convert a hexadecimal number into decimal, and vice versa 
    - To be able to convert a decimal number into hexadecimal, and vice versa

Everything that takes place in the computer depends on two-state switches. Each switch can be either on or off which can more easily be represented as either a $0$ or a $1$ (or, also, `False` or `True`).

For convenience, we also need to know the **hexadecimal** number system, Base-16, as a **shorthand** for representing binary.

!!! warning
     The computer only deals with the binary representation, the 0s and the 1s.  Obviously, as this represents the state of a particular transistor.  Hexadecimal is a shorthand for **us** as it helps make sense of long binary strings.

Given a 32-bit binary string such as $01110010101000001111001011100101$.  If we had to handle this number of bits it would be easy to make mistakes.  To make our lives a little easier we can represent this binary string as a **hexadecimal** number: $72A0F2E5_{16}$.

## Base-16

It looks a little weird, letters representing numbers but we borrow the first six letters from the alphabet to represent $10$ through to $15$.  Looking at the following table we can see how Base-16 numbers map directly to 4 binary digits:

| Base-10 | Base-2 | Base-16 |
| :-----: | :----: | :-----: |
|    0    |  0000  |    0    |
|    1    |  0001  |    1    |
|    2    |  0010  |    2    |
|    3    |  0011  |    3    |
|    4    |  0100  |    4    |
|    5    |  0101  |    5    |
|    6    |  0110  |    6    |
|    7    |  0111  |    7    |
|    8    |  1000  |    8    |
|    9    |  1001  |    9    |
|   10    |  1010  |    A    |
|   11    |  1011  |    B    |
|   12    |  1100  |    C    |
|   13    |  1101  |    D    |
|   14    |  1110  |    E    |
|   15    |  1111  |    F    |

It is easier to use hexadecimal rather than denary to represent binary numbers as it is also based on powers of 2.  It is easy to group the binary digits into groups of four (a **nibble**) and use the table above to convert into the hexadecimal equivalent.  

It saves a lot of space.  It takes 8 binary digits to represent a number between $0$ and $255$, but only ywo hexadecimal digits for the same range, $00$ and $FF$.

Returning to our previous 32-bit number: $01110010101000001111001011100101$.  To arrive at the hexadecimal equivalent:

- split the binary string into groups of four:

$0111 0010 1010 0000 1111 0010 1110 0101$

- Use the table above to look up the hexadecimal:

| $0111$ | $0010$ | $1010$ | $0000$ | $1111$ | $0010$ | $1110$ | $0101$ |
| :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
|  $7$   |  $2$   |  $A$   |  $0$   |  $F$   |  $2$   |  $E$   |  $5$   |

## Uses of hexadecimal

Repeating the point above:

!!! warning
     The computer only deals with the binary representation, the 0s and the 1s.  Obviously, as this represents the state of a particular transistor.  Hexadecimal is a shorthand for **us** as it helps make sense of long binary strings.

**We** use hexadecimal in computer science for a number of reasons:

- **Concise Representation**: Hexadecimal allows for a more compact and concise representation of binary data. Each hexadecimal digit represents 4 binary digits (bits), making it easier to read and write large binary numbers.

- **Memory Addresses**: Memory addresses in computer systems are often expressed in hexadecimal. This is because each digit in hexadecimal corresponds to 4 bits, making it a natural choice when dealing with memory locations in a system where memory is often addressed at the byte level.

- **Color Representation**: Hexadecimal is commonly used in representing colors in computing. In HTML, for example, colors are often specified using hexadecimal notation (e.g., `#RRGGBB`, where `RR`, `GG`, and `BB` represent the red, green, and blue components, respectively).

- **Binary Conversion**: When working with binary data, it's common to convert between binary and hexadecimal for readability. Hexadecimal is more concise than binary and is easier for humans to read and write.


Using hexadecimal is easier for programmers to work with than binary, and it can be more readable than decimal for certain tasks.

## Decimal to Hexadecimal conversion

There are two methods that be used here.

**Method 1 - Repeated division by 16**

As we say when converting a decimal number to binary we can divide the value by $2$ (the base) and note the remainder.  We can do the same here but using the number $16$:

For example, to convert $245_{10}$:

- Divide $245$ by $16 \rightarrow 15$ remainder $5$
- Find the hexadecimal equivalents ot both $15$ and $5$ and concatenate them together $\rightarrow F5$

**Method 2 - Via binary**

Alternatively, convert the decimal number into binary (using one of the previous algorithms) and then convert the binary number into hexadecimal.

For example, to convert $245_{10}$:

- Convert $245_{10}$ to binary $\rightarrow 11110101_2$
- Divide the binary string into groups of 4 bits: $1111$ and $0101$
- Use the look up table to get the equivalent hexadecimal digits, thus $F5$.

## Binary to hexadecimal conversion

- Split the binary string into groups of four bits
- Find the corresponding hex value for each group of four

For example: $01101100_2$

- Split into groups of 4: $0110_2$ and $1100_2$
- Using the look-up table: $0110_2$ is $6_{16}$, $1100_2$ is $C_{16}$
- Thus: $01101100_2$ is $6C_{16}$

## Hexadecimal to binary conversion

- Take each hex digit 
- Use the look up table to find the corresponding binary nibble
- Concatenate the results together

For example: $5D_{16}$

- Use the look up table to find the binary equivalent for both $5_{16}$ and $D_{16}$
- $5_{16}$ is $0101_2$, and $D_{16}$ is $1101_2$
- Thus, $5D_{16}$ is $0101 1101_2$

## Hexadecimal to decimal

The simplest approach here is to convert the hexadecimal number into binary and then convert the binary number into decimal.

For example: $B3_{16}$

- Look up the binary equivalent for $B_{16} \rightarrow 1011_2$
- Look up the binary equivalent for $3_{16} \rightarrow 0011_2$
- Concatenate the two together: $10110011_2$
- Convert to decimal: $((128 * 1) + (32 * 1) + (16 * 1) + (2 * 1) + ( 1 * 1)) \rightarrow 179$

## Questions

{{ show_questions(page.title, page.meta.filename) }}

