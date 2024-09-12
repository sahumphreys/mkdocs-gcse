---
title: Binary Arithmetic
image: binary.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


!!! note "Objectives"
	- To know how to add two binary numbers
	- Be able to add two binary numbers
	- Explain how the binary shift operator is used to perform multiplication and division of numbers by powers of 2
	- Apply the binary shift operators `>>` and `<<` to a range of numbers

As we saw in the last section all the data the computer processes has to be represented using the binary number system, Base-2.  The computer is made of electrical circuits and at the heart of these circuits are transistors.  The transistor can either hold a charge or not.  Those two states can be represented as $0$ and $1$ the two digits in the binary number system.

All operations have to be carried out using this system, including adding, subtracting, multiplying and dividing values.  Here we will examine how this is done. 

!!! note
	 We are only dealing with positive whole numbers in the range $0$ to $255$ i.e. one **byte**.

## Addition

Adding binary numbers follows the same rules as for denary.  Add each column starting with the least significant bit and move to the right.  Any carry from a column is added into the next column and so on.  It's relatively trivial as their are only four possible outcomes when adding two binary digits:

$0_2 + 0_2 = 0_2$  
$0_2 + 1_2 = 1_2$  
$1_2 + 0_2 = 1_2$  
$1_2 + 1_2 = 0_2$ carry $1_2$  

Bearing the carry in mind, four additional rules should be referenced:

$0_2 + 0_2 + 1_2 = 1_2$  
$0_2 + 1_2 + 1_2 = 0_2$ carry $1_2$  
$1_2 + 0_2 + 1_2 = 0_2$ carry $1_2$  
$1_2 + 1_2 + 1_2 = 1_2$ carry $1_2$  

For example, adding the binary number $01101110_2$ and $00011100_2$.  Work through the example, make sure you understand how the carry comes into play:

```pseudocode
	01101110
	00011100 +
	--------
	10001010
	--------
	1111
```

!!! note
	 To check you have the right answer, convert the result (and original numbers) into decimal

## Overflow Error

An **overflow error** occurs when the result of a calculation requires more bits than are in the available range.

For example, when using eight bits, the largest number that can be represented is $11111111_2$ (that is $255_{10}$). If we wanted to add $2$ to $254$ the following would occur:

```plain
1 1 1 1 1 1 1 0 +
0 0 0 0 0 0 1 0 
---------------
0 0 0 0 0 0 0 0
```

We know the actual result should be $100000000_2$ (that is $256_{10}$) but that requires nine bits and we only have 8.  An **overflow error** has occurred.  When this happens it can have serious consequences for the validity of calculations.

## Multiplication and Division

Binary numbers can be multiplied and divided by shifting the bits to the left or the right respectively.

!!! note
	- The **Most Significant Bit** is the bit on the left side of the binary number and, if changed, has the greatest impact on the magnitude of that number; 
	- the **Least Significant Bit** is the bit on the right side of the binary number ans, if changed, has the least impact on the magnitude of that number.

**Multiplication**

To multiply a number, a binary shift moves all the digits in the binary number along to the left and fills the gaps after the shift with 0:

- to multiply by two, all digits shift one place to the left
- to multiply by four, all digits shift two places to the left
- to multiply by eight, all digits shift three places to the left
- etc..

Observe the following binary numbers and their decimal equivalents:

$00000101_2 = 5_{10}$    
$00001010_2 = 10_{10}$  
$00010100_2 = 20_{10}$  

Notice how the binary pattern $101$ is being shifted to the left by one place, this is multiplying that number by $2$.  Shifting it $4$ places to the left multiplies it by $4$.

By applying a combination of shifting by a power of two and addition we can multiply any binary number.

**Division**

To divide a binary number shift in the other direction, to the right, and fill the gaps before the shift with $0$.  You should be able to see how this works by taking the previous example but not starting with $20$:

$00010100_2 = 20_{10}$ 
$00001010_2 = 10_{10}$  
$00000101_2 = 5_{10}$    

!!! note
	 To subtract one binary number the computer will add the **complement** of the second number, that is we add the negative.  we'll see how to do this later.

## Errors met when shifting

Consider the following example of shifting bits to the right:

Starting with $11_{10}$:  

$00001011_2 = 11_{10}$  

We shift the bits one place to the right, resulting in the value $5$:

$00000101_2 = 5_{10}$

The least significant bit has been lost, it's fallen off the end, thus the answer we're expecting of dividing by $2$ has been **rounded down**.

Consider too this situation when shifting to the left, and assuming we *only* have 8 bits to work with:

$10100000_2 = 160_{10}$  
$01000000_2 = 64_{10}$

Here, the most significant bit has been lost.  Instead of multiplying by $2$ we have been left with a wrong answer as we only have 8 bits to hold our result.  A further example of an **overflow error**.

## Python shift operators

We can observe this functionality using Python.  For example:

```python
>>> a = 5
>>> b = a << 1      # shift by 1 place to the left
>>> b
10
```

Experiment with this using different shift values to see how the original value is shifted by that power of 2 (the shift value).  Similarly, try with the right shift operator: `>>` to divide by a power of 2.

!!! note
	 Adding two binary numbers is also possible but not directly as they need to be converted into integers first e.g. `result = bin(int('1010',2) + int('1011', 2))`.

## Questions

{{ show_questions(page.title, page.meta.filename) }}

