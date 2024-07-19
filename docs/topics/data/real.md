---
title: Real numbers
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


> [!NOTE] The purpose of this section is to ...
> 
> - Know how numbers with a fractional part can be represented:
>   - in fixed point form in binary in a given number of bits
>   - in floating point form in binary in a given number of bits
> - Be able to convert for each representation form:
>   - decimal to binary of a given number of bits
>   - binary to decimal of a given number of bits
> - Know why floating point numbers are normalised and be able to normalise un-normalised floating point numbers with positive or negative mantissas.

---

The next stage is to consider those numbers with a fractional part, i.e. $4.25$, $245.00003$ etc..

## Fixed point

When representing numbers with a fractional part we make use of an additional symbol, the decimal point, which we do not have in a digital system of '0s' and '1s'.  Most modern systems will have native support through hardware for floating-point numbers (see next section) but sometimes fixed point is all that is needed as it is much faster than floating-point.

To represent binary numbers with a fractional part we need a __binary point__ to separate the whole number part from the fractional part and to know how many bits to allocate for each part.  Let's assume, 8 bits, with 5 bits allocated for the whole part and to help with a later point we'll start by converting the whole number 59 into binary:

- $00111011_2 = 59_{10}$

Dividing $59$ by $2$ results in $29.5$, which in binary fixed point representation is:

- $0011101.1_2 = 29.5_{10}$

It should be noted that the bit pattern for each of these numbers is identical, the only difference being the position of the binary point.

The positional weights for the columns after the binary point are $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$, $\frac{1}{16}$ and so on.  

Fixed point numbers, signed or unsigned, are very closely related to whole number representation the only difference being the position of the binary point.  All arithmetic operations carried out on whole numbers can be used to apply to real numbers using a fixed point representation.  Thus, no additional circuitry is needed unlike floating point and they will perform better.  The downside is the limitation on the number of bits available to represent the number.

### Converting decimal to fixed point binary

For example, the decimal value $4.125$.

- Convert the whole number part, $4$, to binary using the repeated division by two algorithm
- Convert the fractional part, $125$, to binary using a repeated multiplication by two taking the integer part of the result (which will be either $1$ or $0$, as the first bit and repeat until you've exhausted the number of bits available or hit $0$.

Thus:

- $4_{10}$ is $0100_2$
- $0.125 \times 2 = 0.250 \rightarrow 0$
- $0.250 \times 2 = 0.500 \rightarrow 0$
- $0.500 \times 2 = 1.000 \rightarrow 1$

$4.125_{10}$ is equivalent to $0100.0010_2$

NB.  With a fixed number of bits it may not be possible to represent the number precisely, for example $7.4$, taking the $0.4$ part:

- $0.4 \times 2 = 0.8 \rightarrow 0$
- $0.8 \times 2 = 1.6 \rightarrow 1$
- $0.6 \times 2 = 1.2 \rightarrow 1$
- $0.2 \times 2 = 0.4 \rightarrow 0$

And, now we've run out of bits!  So, the closest we can get with $8$ bits available is $0111.0110$ which is equivalent to $7.375$.

This can be improved upon, of course, by increasing the number of bits available to increase the **range**, and increasing the number of bits available after the binary point to increase **precision**.

If the decimal number is negative, e.g. $-7.4$, proceed as above and then complement the number by either flipping the bits and adding 1, or copy all digits from the right until the first $1$ is met and then flipping the bits.  So, $-7.4_{10}$ becomes $1000.1010_2$ which is also an approximation of course.  

Converting from fixed point binary into decimal is just a case of generating the sum of products by multiplying each digit by its equivalent power of two.

## Floating point

It's important to note that floating point numbers are not real numbers.  Remember real numbers are all numbers from $-\infty$ to  $+\infty$.  Computers are finite machines so there is an obvious limit on the maximum and minimum values but worse than that there will be significant gaps between adjacent floating point numbers.  These errors will be considered [later](errors.md).

When representing numbers with a fractional part in decimal we will often used __scientific notation__ which takes the form $m \times 10^{e}$, where $m$ is between $-10 > m < 10$, and $e$ is any integer.  Thus, $550,000,000$ can be written as $5.5 \times 10^8$.  The exponent, $e = 8$, tells us how many places to move the decimal point to return the mantissa, $m = 5.5$ to its actual value.  Scientific notation is usually reserved for numbers that are either too small or too big to represent using conveniently in decimal form.

A similar form is used when representing binary numbers with a fractional part using a floating point representation where the mantissa will be any real number greater than or equal to $-1_{10}$ and less than $+1_{10}$ and the exponent will be an integer.  Again, the exponent tells us how many places to shift the binary point.  Shifting the binary point one place to the right is equivalent to multiplying by $2$; shifting it one place to the left is the equivalent of dividing by $2$.

We need to be made aware of the number of bits reserved for the mantissa, and the number of bits for the exponent [^1].  The examples used here will use 10 bits for the mantissa, and 6 bits for the exponent.  The most significant bit can be regarded as the __sign bit__ with the implied binary point between it and the next most significant bit.  

For example, consider the following 16 bit binary number, $0100100100000100_2$, which uses 10 bits for the mantissa and 6 bits for the exponent with an implied binary point as indicated:

| mantissa    | exponent |
|-------------|----------|
| 0.100100100 | 000100   |

The exponent has the value $4$ so the implied binary point needs to be moved $4$ places to the right which gives the following::

- $01001.00100_2$

This can then be converted into decimal in the usual way:

- $(1 \times 8) + (1 \times 1) + (1 \times \frac{1}{8}) = 9.125_{10}$

If the exponent is negative the binary point needs to move to the left.

For example, consider the following 16 bit binary number, $0101000000111110_2$:

| mantissa    | exponent |
|-------------|----------|
| 0.101000000 | 111110   |

The value of the exponent is $-2_{10}$ ($-32 + 16 + 8 + 4 + 2$) so the implied binary point is moved $2$ places to the __left__ which leaves the following binary number:

- $0.0010100_2$

This can then be converted into binary in the usual way:

$(1 \times \frac{1}{8}) + (1 \times \frac{1}{32}) = 0.15625_{10}$

Finally, we'll look at an example with a negative mantissa: $1100100100000100_2$:

| mantissa    | exponent |
|-------------|----------|
| 1.100100100 | 000100   |

First convert the exponent to decimal: $4_{10}$.  The exponent is positive so the implied binary point has to move to the right $4$ places:

- $11001.00100_2$

Then convert this number into decimal in the usual way:

- $(1 \times -16) + (1 \times 8) + (1 \times 1) + (1 \times \frac{1}{8}) = -6.875_{10}$

NB.  Each of the above can also be worked out mathematically using the formula: $m_{10} \times 2^{e_{10}}$

## Normalisation of floating point numbers

Referring back to scientific notation, it is possible to represent the decimal number $123.456_{10}$ in several ways, e.g.

- $12345.6 \times 10^{-2}$
- $123.456 \times 10^{0}$
- $1.23456 \times 10^{2}$
- etc..

There needs to be a standard form.  For decimal the standard form for the mantissa must be at least $1$ and less than  $10$.  Thus the correct form for our number is $1.23456 \times 10^{2}$.  As well as clearing up some confusion the purpose of __normalising__ the format is to maximise precision by ensuring we use as many of the significant digits as possible.

Floating point binary numbers also need to be normalised to maximise precision i.e. to use as many of the significant digits as possible.  It also provides a unique representation of the number. Normalising the number ensures the digit to the right of the implied binary point will be a significant digit.  It will be a $1$ for a positive mantissa; and a $0$ for a negative mantissa.  NB.  The first two digits will always be different.

For example, using 10 bits for the mantissa and 6 bits for the exponent, written in groups of 4 bits to aid readability:

- $0.010 0000 00 | 00 0011$  We can see this number is not normalised because the two digits in both the mantissa and the exponent are the same.  So the first step is to correct this with the mantissa moving the binary point 1 place to the right and subtracting $1$ from the exponent to compensate:
- $0.100 0000 00 | 00 0010$  This number is now normalised.

It's a similar process for negative numbers:

- $1.110 0000 00 | 11 1110$  The binary point needs to be moved two places to the right to ensure the leading digits are different whilst preserving the sign, and the exponent is adjusted to be two less:
- $1.000 0000 00 | 11 1100$  This number is now normalised

Being able to convert a binary floating point normalised number into decimal (and back) is often an exam question so here is the algorithm and some further examples:

__Converting from binary to decimal__

Convert $0100100100 000100_2$ into decimal:

| \# | Step                                                                | Example                |
|----|---------------------------------------------------------------------|------------------------|
| 1  | Write down the mantissa, with the point inserted after the sign bit | $0.1001001$            |
| 2  | If negative, find the twos complement of the mantissa               | (Mantissa is positive) |
| 3  | If exponent is negative, find its twos complement                   | (Exponent is positive) |
| 4  | Calculate the value of the exponent                                 | $4_{10}$               |
| 5  | Move the binary point $4$ places to the right                       | $1001.001$             |
| 6  | Convert the result into decimal                                     | $9.125_{10}$           |

Convert $1010000000 000101_2$ into decimal:

| \# | Step                                                 | Example  |
|----|------------------------------------------------------|----------|
| 2  | Mantissa negative so find the twos complement        | $-0.11$  |
| 3  | Calculate exponent (000101) in denary                | $5$      |
| 4  | Adjust point in mantissa (move point 5 places right) | $-11000$ |
| 5  | Convert mantissa to denary                           | $-24$    |

Convert the number 1010000000 111101 to denary

| \# | Step                                                 | Example  |
|----|------------------------------------------------------|----------|
| 1  | Write down mantissa | $1.01$
| 2  | Mantissa negative so find the twos complement | $-0.11$ |
| 3  | Exponent negative so find the twos complement | $-000011$ |
| 4  | Calculate exponent (- 000011) in denary | $-3$ |
| 5  | Adjust point in mantissa (move point 3 places left) | $-0.00011$ |
| 6  | Convert mantissa to denary | $-0.09375$ |

__Converting from Denary to Binary__

Convert $123.5_{10}$ to floating point form

| \# | Step                                                 | Example  |
|----|------------------------------------------------------|----------|
| 1  | Convert number (123.5) to pure binary | $1111011.1$ |
| 2  | Normalise mantissa | $0.11110111$ |
| 3  | If negative, convert to twos complement | (not negative) |
| 4  | How far has the point moved? | 7 places |
| 5  | In which direction? (If left, positive) | left, so exponent = +7 |
| 6  | Convert exponent to twos complement binary |  $000111$ |
| 7  | Add 0's to the mantissa to fill bits | $0.111101110$ |
| 8  | Answer: | $0111101110 000111_2$ |

Convert $0.1875_{10}$ to floating point form

| \# | Step                                                 | Example  |
|----|------------------------------------------------------|----------|
| 1  | Convert number (0.1875) to pure binary | $0.0011$ |
| 2  | Normalise mantissa | $0.11$ |
| 3  | If negative, convert to twos complement | (not negative) |
| 4  | Point has moved 2 places right | exponent = $-2$ |
| 5  | Convert exponent to twos complement binary | $111110_2$ |
| 6  | Add 0's to the mantissa | $0.110000000$ |
| 7  | Answer: |$0110000000 111110_2$ |

Convert -0.375 to floating point form

| \# | Step                                                 | Example  |
|----|------------------------------------------------------|----------|
| 1  | Convert number (-0.375) to pure binary | $-0.011$ |
| 2  | Normalise mantissa |$-0.11$ |
| 3  | Number negative so find twos complement | $1.01$ |
| 4  | The point has moved 1 place right | exponent = $-1$ |
| 5  | Convert exponent to twos complement binary | 111111 |
| 6  | Add 0's to the mantissa | $1.010000000$ |
| 7  | Answer: |$1010000000 111111_2$ |

---

[^1]: NB.  The standard representation has been laid down by the IEEE and you can search for this with your favourite search engine.  For the A Level you only need to know, understand and use a simplified floating point representation used here.

## Questions

1. Write the following binary numbers as decimal numbers:
        a. 110.01
        b. 10.11
        c. 11.101
        d. 1101.0011
        e. 11010.0011
        f. 10111.1001
        g. 110.111
        h. 10101.0101

2.  Write the following denary numbers in binary:
        a. 5.25
        b. 133/4
        c. 113/8
        d. 35.5625
        e. 42.625
        f. 22.75
        g. 147/8
        h. 693/16
