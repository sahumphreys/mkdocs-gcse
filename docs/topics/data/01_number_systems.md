---
title: Number Systems
image: binary.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
	- Be able to describe the binary number system, Base-2  
	- Be able to convert between decimal (denary) and binary number bases, Base-10 and Base-2

From an electronic perspective a computer is built of lots (lots and lots) of transistors - a type of semiconductor.  They are the building blocks of modern electronic circuits.  They act like a switch either allowing a voltage to pass through or not.  They can be in two **states** which can be represented by the digits $0$ and $1$ (or `True` and `False`).  This aligns neatly with a number system, the number base we call **binary** or base 2.

## Binary Number System

Imagine if we had to count up to say $5$ but only had the digits $0$ and $1$ to work with:

| Decimal | Binary |
|:-----: |:----: |
|    0    | 0   |
|    1    | 1 |
|    2    | 10 |
|    3    | 11 |
|    4    | 100 |
|    5    | 101 |

What is happening here?  How have we arrived at those binary numbers?  

Pause for a moment and consider how we work with decimal, or denary, numbers which is our norm.  Take the number $245$.  We know this is $2$ lots of $100$ plus $4$ lots of $10$ plus $5$.

Our decimal system is also know as **Base-10**.  It has **10** digits (0..9).  If we think of our number, $245$, as having three columns, each column will have, reading from right to left, place values that are powers of $10$:

| Hundreds |   Tens   |  Units   |
| :------: | :------: | :------: |
| $10^2$ | $10^1$ | $10^0$ |
|  **2**   |  **4**   |  **5**   |

Thousands would be $10^3$ and so on.

So, the binary (or Base-2) number system has the following pattern, where each column represents an increasing power of $2$:

| 16      |    8    |    4    |    2    |    1    |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| $2^4$   | $2^3$   | $2^2$   | $2^1$   | $2^0$   |
|         |         |  **1**  |  **0**  |  **1**  |

We can see that $101_2$ is 1 lot of 4 plus 1.

!!! note
	To distinguish the number 101 in decimal and 101 in binary we need to add a **subscript** to the number.  This $101_{10}$ is $101$ ("one hundred and one"), a decimal number; but $101_2$ is a binary number, Base-2, which converts to $5_{10}$.

## Decimal to Binary

There are two methods we can use to convert a decimal number to a binary number.  Let's use $245_{10}$ and convert it to a binary number:

**Method 1: "By inspection"**

- Find the nearest power of $2$ to the given value, in this case it's $128$ ($2^{7}$), put a $1$ in that column and then take $128$ away from the original value leaving $117$.  
- Repeat the process, this time with $117$ the remainder, putting a $1$ in the nearest column, $64$ ($2^{6}$) and take that away from $117$ leaving $53$.  
- Repeat, this time putting a $1$ in the closest column, $32$ ($2^{5}$), and take that away from $53$ leaving $21$.  
- Repeat, putting a $1$ in the next column, $16$ ($2^{4}$), and that away from $21$ leaving $5$  which can quickly be added in the remaining columns for $2^{2}$ and $2^{0}$.

|   128   |   64    |   32    |   16    |    8    |    4    |    2    |    1    |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
|  **1**  |  **1**  |  **1**  |  **1**  |  **0**  |  **1**  |  **0**  |  **1**  |

If you had up the column headings where there is a $1$, ($128 + 64 + 32 + 16 + 4 + 1$) you will get the sum: $245$.

**Method 2: Repeated division by 2**

Take the decimal number and repeatedly divide by $2$ writing down the remainder and stop when zero is reached:

| Quotient | New Number | Remainder |
| :------: | :--------: | :-------: |
|  245/2   |    122     |   **1**   |
|  122/2   |     61     |   **0**   |
|   61/2   |     30     |   **1**   |
|   30/2   |     15     |   **0**   |
|   15/2   |     7      |   **1**   |
|   7/2    |     3      |   **1**   |
|   3/2    |     1      |   **1**   |
|   1/2    |     0      |   **1**   |

Then read up from the bottom!

This can be described in pseudocode as:

~~~py
	number = positive integer
	while (number > 0) {
		bit = number mod 2
		number = number div 2
		put bit to left of any previous bits
	}
~~~

!!! note
	The "magic number" $2$ represents the target base and can be replaced by another value to convert the binary number into any other base.

## Binary to Decimal

Again, two methods can be applied:

**Method 1:**

Start from the left of the binary number, take your current total, multiply it by two and add the current digit and continue until there are no more digits left.  So, taking the binary number $11110101$:

$2 \times 0 + 1 = 1$  
$2 \times 1 + 1 = 3$  
$2 \times 3 + 1 = 7$  
$2 \times 7 + 1 = 15$  
$2 \times 15 + 0 = 30$  
$2 \times 30 + 1 = 61$  
$2 \times 61 + 0 = 122$  
$2 \times 122 + 1 = 245$  

Personally, this seems a little counter intuitive and method 2 is a preferred option.

**Method 2:**

The second method uses the positional notation and multiplies each digit by their corresponding power of two and sums these products:

$(1 \times 128) + (1 \times 64) + (1 \times 32) + (1 \times 16) + (1 \times 4) + (1 \times 1) = 245$  

This can be described in pseudocode as:

~~~py
	power = 1
	decimal = 0
	loop through all bits in the binary string
		decimal = decimal + power * bit
		power = power * 2
~~~

## Binary Numbers and Python

To convert character data to an integer we use the function `int()` as in:

```python
value = input("Enter a number: ")
value_int = int(value)
```

!!! note
	Remember: all data entered by the user at the keyboard is received by the computer as character data.  That is, you type the digit 4, but the computer receives it as '4'.

The related functions `float()` and `str()` can also be used to convert one data type to another, the first converting a string to a floating point number, the second converting numeric data to a string.

We can also use the function `bin()`.  This function takes an integer argument and returns its binary representation.

```python
value = int(input("Enter a number: "))		# e.g. 5
value_bin = bin(value)	  			# convert to binary
print(value_bin)				# => '101'
```

Running this in the Python interactive environment:

```bash
>>> value = int(input("Enter a number: "))
Enter a number: 5
>>> value_bin = bin(value)
>>> print(value_bin)
0b101
```

!!! note
	The output is prefixed with `0b` to indicate that the number is binary.

A binary string can be converted to its integer form by adding an additional argument to the `int()` function:

```python
binary_num = '0101'
decimal_num = int(binary_num, 2)
print(decimal_num)
```

And the output is:

```bash
>>> value_dec = int(value_bin, 2)
>>> print(value_dec)
5
```

Converting to other number bases is also possible just by changing that second argument to show the base of the number of be converted e.g. `int('FF', 16)` will return $255$.


## Questions

{{ show_questions(page.title, page.meta.filename) }}


