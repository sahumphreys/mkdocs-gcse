---
title: Rounding errors
image: binary.jpg
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}


> [!NOTE] The purpose of this section is to ...
> 
> - Know and be able to explain why both fixed point and floating point representation of decimal numbers may be inaccurate
> - Be able to calculate the absolute error of numerical data stored and processed in computer systems.
> - Be able to calculate the relative error of numerical data stored and processed in computer systems.
> - Compare absolute and relative errors for large and small magnitude numbers, and numbers close to one.
> - Compare the advantages and disadvantages of fixed point and floating point forms in terms of range, precision and speed of calculation.

---

Consider this example, in C\#.  What is the value displayed in line 13?

~~~cs
using System;

namespace matherrors
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What will be the output ....?!");
			float price = 4.99f;
			int q = 17;
			float total = price * q;
			Console.WriteLine("The total price is £{0}", total);
        }
    }
}
~~~

The result ought to be £84.83 but it's not, it's £84.82999.  It illustrates that we need to be on our guard when doing any mathematical operation and sometimes things are not what we might expect.  If one understands the underlying operations then such errors are rare but they do happen and the following sections will explain why.

There are infinitely many real numbers but in computer systems we have a finite number of bits.  Although there are infinitely many integers in most programs the results can be stored in either 32 or 64 bits but calculations with real numbers will produce values that cannot be exactly represented in the number of bits available.  The whole number part is not the problem, it's the fractional part.  There are many numbers $<1$ that cannot be created by adding a fixed number of fractions of the form $\frac{1}{2}$,  $\frac{1}{4}$, $\frac{1}{8}$ etc..  The classic example is $0.1$ ($\frac{1}{10})$.  You can see the issue when, using a Python interpreter trying to add $0.1$ to $0.2$:

~~~py
Python 2.7.16 (default, Oct 10 2019, 22:02:15)
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 0.1+0.2
0.30000000000000004
>>>
~~~

As the following table shows there are many binary equivalents to decimal fractions that contain repeating sequences of 0s and 1s:

| Fixed point decimal | Fixed point binary   |
|---------------------|----------------------|
| $0.1$               | $0.0\overline{0011}$ |
| $0.2$               | $0.\overline{0011}$  |
| $0.25$              | $0.01$               |
| $0.3$               | $0.0\overline{1001}$ |
| $0.4$               | $0.\overline{0110}$  |
| $0.5$               | $0.1$                |
| $0.6$               | $0.\overline{1001}$  |
| $0.7$               | $0.1\overline{0110}$ |
| $0.75$              | $0.11$               |
| $0.8$               | $0.\overline{1100}$  |
| $0.9$               | $0.1\overline{1100}$ |

Therefore, such numbers have to be __rounded__, sacrificing **precision**. The issue affects both fixed and floating point representations though floating point is usually more efficient as modern systems use a large number of digits for floating point representations[^1] but if there are a lot of divisions and multiplications involved these errors can quickly add up (!).  There are also irrational numbers to consider which cannot be represented by a regular fraction at all and will always require an infinite number of recurring digits.

The __rounding error__ is the difference between the round off numerical value and its actual value.  The final digit has to be set to the value that will have the least impact on this difference.  There are various methods that can be used:

- Rounding towards zero (rounding down): truncate the extra digits.  It's simple but introduces larger errors than necessary e.g. 
- Rounding halfway from zero (rounding off): where the truncated fraction is greater than or equal to the base increase the last digit.  This reduces errors but tends to introduce a bias away from zero.

Taking the second of these let's look at a few examples:

| Value            | Binary       | Rounded   | Action                      | Rounded value   |
|------------------|--------------|-----------|-----------------------------|-----------------|
| $2 \frac{3}{32}$ | $10.00011_2$ | $10.00_2$ | (<$\frac{1}{2} \downarrow$) | $2$             |
| $2 \frac{3}{16}$ | $10.00110_2$ | $10.01_2$ | (<$\frac{1}{2} \uparrow$)   | $2 \frac{1}{4}$ |
| $2 \frac{7}{8}$  | $10.11100_2$ | $11.00_2$ | ($\frac{1}{2} \uparrow$)    | $3$             |
| $2 \frac{5}{8}$  | $10.10100_2$ | $10.10_2$ | ($\frac{1}{2} \downarrow$)  | $2 \frac{1}{2}$ |

Remember, it makes no difference if the number is signed or unsigned.

## Absolute and relative errors

There are two important was to describe errors, both are common sense really but are expressed as __absolute errors__ and __relative errors__.

The  __absolute error__ is the difference between the actual value and the computed value in binary i.e. the value obtained by the computer after it has been processed (along the way there might have been a decimal to binary conversion error, followed by a truncation error, followed by a binary to decimal conversion error.

Let's take the example of $0.6_{10}$ which is a recurring binary number $0.100110011001_2...$.  It will have to be either rounded or truncated to fit in the available number of bits.  

For example, with 8 bits (with the implied binary point in the usual place):

- $0.1001100_2 = 0.59375_{10}$ using truncation
- the absolute error is $0.6_{10} - 0.59375_{10} = 0.00625_{10}$
- $0.1001101_2 = 0.6015625_{10}$ using rounding
- the absolute error is $0.6_{10} - 0.6015625_{10} = 0.0015625_{10}$

A further example, this time using $0.1_{10}$ which is $0.00011\overline{0011}_2$: 

- $0.0001100_2 = 0.09375_{10}$ using truncation
- the absolute error is $0.09375_{10} - 0.1_{10} = 0.00625_{10}$
- $0.0001101_2 = 0.1015625_{10}$ using rounding
- the absolute error is $0.1015625_{10} - 0.1{10} = 0.0015625_{10}$

> [!NOTE] The sign is ignored.

The absolute error can be misleading.  An error of $0.000001_{10}$ sounds better than an error of $10_{10}$ but this depends on the size of the original number hence the need for the __relative error__.

The __relative error__ expresses how large the absolute error is compared with the original value.  To get the relative error we need to have calculated the absolute value then divide that by the actual value.  The relative error is usually expressed as a percentage when it is more properly termed a __percentage error__.

Using the values in the previous examples:

- $0.6_{10} = 0.\overline{1001}_2$ 
    - with truncation: $0.00625/0.6 = 0.0104166667_{10} \approx 1.04\%$
	- with rounding: $0.0015625/0.6 = 0.0026041667_{10}\approx 0.26\%$
- $0.1_{10} = 0.00011\overline{0011}_2$
    - with truncation: $0.00625_{10}/0.1_{10} = 0.0625_{10} \approx 6.25\%$
    - with rounding: $0.0015625_{10}/0.1_{10} = .015625_{10} \approx 1.56\%$

So, the __absolute error__ tells us how much the value represented differs from the actual value i.e. what has been stored and what should have been stored.  The __relative error__ tells us whether that difference is big or small, it is the ratio of the difference and consequently of more value.

The magnitude of the value is an important consideration.  If the absolute error for $1000000$ is $1.0_{10}$ the relative error will be $0.0001\%$, but if the value was $10_{10}$ then the relative error would be $10\%$. As a general rule, the bigger the original number, the smaller the impact of the error.

## Range and precision

Fixed point and floating point both have the task of representing numbers with a fractional part but each have their own advantages and disadvantages.  To discuss these we need to understand the concepts of __range__, __precision__ and __accuracy__.

- range: the distance between  the smallest to the largest value that can be represented in a given format
- accuracy: how close a number is to its true value
- precision: how much information is used to represent the value (the distance between two adjacent numbers)

Thinking of these using fixed point decimal (and positive) is perhaps easier before turning to binary.  Using three digits and a decimal point after the most significant bit the range will be $0.00_{10}$ to $9.99_{10}$ inclusive.  The precision is $0.1_{10}$.  There is a trade-off between range and precision.  With the decimal point on the far right the range will be $000_{10}$ to $999_{10}$ and the precision is $1.0$, with the decimal point to the far left the range will be $.000_{10}$ to $.999_{10}$ and the precision is $0.001_{10}$.  In each case, there will only be $10^3$ numbers regardless of where the decimal point is placed.

Turning to binary, if we have only 3 bits, there will will be $2^3$ different bit patterns; if there are 8 bits there will be $2^8$ different bit patterns and so on.  Thus for positive integers with 8 bits the range available will be $0$ - $7$, for 8 bits it will be $0$ - $255$.  To allow for negative numbers the number of numbers will be the same but the range will now be $-4$ to $3$ and $-128$ - $127$ respectively.  This principle holds for fixed or floating point representation, the total number of possible values remains the same and will be distributed across the range but there will be gaps, of course.

Let's take a simple example using four bits, twos complement, with the binary point after the most significant bit.  Four bits will give us $16$ possible values, with the range being between $-1_{10}$ and $0.875_{10}$:

- the largest positive number: $0.111_2$ or $0.875_{10}$
- the smallest positive number (excluding zero): $0.001_2$ or $0.125{10}$
- the smallest magnitude negative number (i.e closest to zero): $1.111_2$ or $-0.125_{10}$
- the largest magnitude positive number (i.e. furthest from zero): $1.000_2$ or $0-1_{10}$

The range can be increased by moving the binary point to the right but there will be a loss of precision.

Floating point representation allows a large range of numbers to be represented in a small number of digits by separating the digits used for precision (mantissa) from the digits used for range (exponent). Most computers will use the IEEE 754 standard for floating point numbers which uses 24 bits for the mantissa for a single precision floating point number and 53 bits for a double precision floating point number.  Our examples, however, will use a simpler form of 8 bits, 4 for the mantissa and 4 for the exponent, both in twos complement.  Thus:

- the largest exponent will be $0111_{2}$, and the largest mantissa will be $0111_2$, the binary point can then float 7 places to the right giving $112_{10}$ which is the largest positive value that can be represented using this format
- the largest magnitude negative exponent will be $1000_{2}$ which when combined with the smallest possible mantissa, $0001_2$, the binary point can float 8 places to the left giving $0.000488281_{10}$ as the smallest positive number to be represented in this format.

Thus the positive range will be $0.00048821_{10}$ - $112_{10}$ and there will be a lot of other values, but also a lot of gaps.

Let's see the effect of allocating 5 bits to the mantissa and 3 bits to the exponent:

- the largest positive number will be $01111011_2$ which is $7.5_{10}$
- the smallest positive number will be $00001100_2$ which is $0.00390625_{10}$

The range has decreased significantly but we can represent more values within that range, thus the range has decreased by reducing the number of bits for the exponent, but the precision has increased, by increasing the number of bit for the mantissa.  (But, still only 256 possible bit patterns distributed unevenly across this range.)

In summary:

- Floating point allows for the representation of a greater range of numbers with a given number of bits than fixed point. This is because floating point can take advantage of an exponent which can be either positive or negative. 
- The number of bits allocated to each part of a floating point number affects the numbers that can be represented.
- A large exponent and a small mantissa allows for a large range but little precision. 
- In contrast, a small exponent and a large mantissa allows for good precision but only a small range. 
- In a similar way, the placement of the binary point in fixed point notation determines the range and precision of the numbers that can be represented. A binary point close to the left of a number gives good precision but only a small range of numbers. However, move the binary point to the right and the range is increased while decreasing precision.

## What's the significance?

Try the following program in C\#:

~~~cs
using System;

namespace errors
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Spot the error!");
			float n = 0.0f;
			Console.WriteLine("n = {0}", n);
			n = n + 0.1f;
			Console.WriteLine("n + 0.1 = {0} (that's all good)", n);
			n = n - 0.1f;
			Console.WriteLine("n - 0.1 = {0} (OK)", n);

			n = 0.0f;
			for (int i = 0; i < 1000; i++) {
				n = n + 0.1f;
			}
			Console.WriteLine("{0} (oops ..)", n);

			Console.ReadLine();
        }
    }
}
~~~

The problem of not being able to represent $0.1_{10}$ in binary has begun to accumulate.  What difference is made by storing the variable $n$ as a $double$?

## Underflow and overflow

These errors are related as both occur when there are insufficient bits to represent the intended value.  __Underflow__ occurs when the absolute value is too close to zero to represent it in the space available; __Overflow__ occurs when the absolute value is too high to represent it in the space available.  Overflow can occur with both integers and floating point numbers but underflow will only occur with floating point numbers.

This can be demonstrated quite simply with C\#, and also shows one way of checking for this exception:

~~~cs
using System;

namespace overflow
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Overflow and underflow");
			Console.WriteLine("Integer (32 bits)");
			int x = int.MaxValue;		// set to maximum for an int
			x = x + 1;					// increment
			Console.WriteLine("{0} x has overflowed!", x);
			// this can be checked ...
			checked {
				try {
					x = int.MaxValue;
					x = x + 1;
				} catch (OverflowException) {
					Console.WriteLine("Overflow exception has been caught");
				}
			}
        }
    }
}
~~~

### Overflow

__Overflow__ occurs when a number is too large in magnitude to be represented in the given number of bits.

If we only have 8 bits to store a twos complement integer the largest positive number that can be represented will be $01111111_2$.  If $1$ is added to this value then the stored binary value will be $10000000_2$, which has produced a change of sign and the value has overflowed.  Checking for this sign change is one way of detecting overflow though many compilers will include built-in methods to catch this.

The same thing can happen with floating point values, most commonly when the exponent is larger than the maximum allowed value for an exponent.  Try out the following lines of code to demonstrate (NB.  C\# implements the IEEE754 standard which replaces the floating point maths error with the special value "Infinity" which really means the result is undefined):

~~~cs

// floating point overflow
float bigN = float.MaxValue;
Console.WriteLine(bigN);
// no change here
float newBigN = bigN + 1.0f;
Console.WriteLine(newBigN);
// this will produce the result 'infinity'
float veryBigN = bigN * 2.0f;
Console.WriteLine(veryBigN);
~~~

Adding, or multiplying, two very large numbers with _the same sign_ can lead to overflow as can dividing a number by a very small number.

### Underflow

__Underflow__ occurs when a number is too small in magnitude to be represented in the given number of bits.

For example, if the computer needs to represent the number $0.0004_{10}$ but the underlying data type only handles 4 digits of precision than only the first four digits will be stored, $0.000_{10}$ creating an underflow.

Turning to binary, let's assume 8 bit fixed point with just 2 bits for the fractional part and we wanted to multiply together the binary equivalents of $0.5_{10}$, $0.10_2$, and $0.25_{10}$, $0.01_2$:

$000000.10_2 \times 000000.01_2 = 000000.00_2$

There are not enough bits to represent $000000.001_2$ so underflow has occurred.

There will be a range of numbers either side of zero (positive and negative) that cannot be represented and will lead to an underflow error.  This is due mainly to insufficient digits being allocated to the exponent.  The IEEE754 standard refers to these numbers as subnormal.  Knowing this standard is not required for the A Level course but it's helpful to be aware that your programming language will implement this standard.

---

[^1]: There are many classic examples of these errors causing significant problems e.g. the fate of the rocket Ariane 5 which after a successful launch in 1996 soon veered off course and self destructed.  This was due to the flight system trying to convert a 64 bit floating point number to a 16 bit integer.  The result was bigger that 32,767!  You can find out more about this here:  [https://itsfoss.com/a-floating-point-error-that-caused-a-damage-worth-half-a-billion](https://itsfoss.com/a-floating-point-error-that-caused-a-damage-worth-half-a-billion/).

## Questions
