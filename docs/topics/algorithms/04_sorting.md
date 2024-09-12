---
title: Sorting Algorithms
image: algorithms.jpg
filename: '_data/algorithms_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

     - To **understand** and **explain** how the Bubble Sort algorithm works.
     - To learn the **mechanics** of the algorithm, with examples and key concepts.
     - To **understand** and **explain** how the Insertion Sort algorithm works.
     - To learn the **mechanics** of the algorithm, with examples and key concepts.
     - To **understand** and **explain** how the Merge Sort algorithm works.
     - To learn the **mechanics** of the algorithm, with examples and key concepts.


The task of a sorting algorithm is organise a list of items into a defined order.  A list of numbers could be organised into ascending or descending order based on their value, a list of strings could be sorted according to the length of each string (smallest or largest first) or put into lexicographic order i.e. `apple` would come before `banana`, and `banana` would come before `basket` etc..

It is a common problem and one that has been of interest to computer scientists for a long time and there a number of different algorithms that have been devised to solve this problem.  It's an excellent way of being introduced to the idea that some algorithms are "better" than others.  How "better" is defined there is dependent on the requirements of the task such as the time needed to complete the task, or how much memory is available and how much data is needing to be sorted.

Here we'll consider three sorting algorithms:

- Bubble Sort
- Insertion Sort
- Merge Sort

!!! note
     There are many others worth exploring e.g. selection sort or quick sort but these are not required by the syllabus.


## Bubble Sort

Bubble Sort is a **simple comparison-based** sorting algorithm. It repeatedly steps through a list, compares adjacent items, and **swaps** them if they are in the wrong order. The process is repeated until the entire list is sorted.

Bubble Sort gets its name because the smaller (or larger, depending on the order) elements gradually "bubble" to the top (beginning) of the list with each pass through the data.

1. **Compare adjacent elements**: Starting from the beginning of the list, compare each pair of adjacent elements.
2. **Swap if needed**: If the two elements are in the wrong order, swap them so that the larger element moves to the right (or smaller element moves to the left if sorting in descending order).
3. **Repeat** the process: Continue comparing adjacent elements, moving from the start to the end of the list.
4. **Reduce the range**: After each pass, the largest (or smallest) unsorted element is in its correct position, so the algorithm can ignore the last element during the next pass.
5. **Stop when sorted**: Repeat the process until no swaps are needed, meaning the list is fully sorted.

### Example

Let's sort the following list using Bubble Sort:

**Unsorted List:**
```
[38, 27, 43, 3, 9, 82, 10]
```

**Step 1: First Pass**
- Compare `38` and `27`. Since 38 > 27, we swap them:
  ```
  [27, 38, 43, 3, 9, 82, 10]
  ```
- Compare `38` and `43`. No swap needed.
- Compare `43` and `3`. Since 43 > 3, we swap:
  ```
  [27, 38, 3, 43, 9, 82, 10]
  ```
- Compare `43` and `9`. Swap:
  ```
  [27, 38, 3, 9, 43, 82, 10]
  ```
- Compare `43` and `82`. No swap needed.
- Compare `82` and `10`. Swap:
  ```
  [27, 38, 3, 9, 43, 10, 82]
  ```

After the first pass, the largest element `82` has "bubbled" to the last position.

**Step 2: Second Pass**
- Compare `27` and `38`. No swap needed.
- Compare `38` and `3`. Swap:
  ```
  [27, 3, 38, 9, 43, 10, 82]
  ```
- Compare `38` and `9`. Swap:
  ```
  [27, 3, 9, 38, 43, 10, 82]
  ```
- Compare `38` and `43`. No swap needed.
- Compare `43` and `10`. Swap:
  ```
  [27, 3, 9, 38, 10, 43, 82]
  ```

After the second pass, `43` is in its correct position, and we continue for the remaining elements.

**Step 3: Third Pass**
- Compare `27` and `3`. Swap:
  ```
  [3, 27, 9, 38, 10, 43, 82]
  ```
- Compare `27` and `9`. Swap:
  ```
  [3, 9, 27, 38, 10, 43, 82]
  ```
- Compare `27` and `38`. No swap needed.
- Compare `38` and `10`. Swap:
  ```
  [3, 9, 27, 10, 38, 43, 82]
  ```

**Step 4: Fourth Pass**
- Compare `3` and `9`. No swap needed.
- Compare `9` and `27`. No swap needed.
- Compare `27` and `10`. Swap:
  ```
  [3, 9, 10, 27, 38, 43, 82]
  ```

**Step 5: Fifth Pass**
- Compare `3` and `9`. No swap needed.
- Compare `9` and `10`. No swap needed.

The list is now fully sorted!

**Sorted List:**
```
[3, 9, 10, 27, 38, 43, 82]
```


### The Mechanics of Bubble Sort

a. **Comparing Adjacent Elements:**

  - The fundamental operation in Bubble Sort is comparing **adjacent elements** in the list and swapping them if they are in the wrong order.

b. **Multiple Passes:**
  
  - The algorithm requires **multiple passes** through the list. With each pass, the largest unsorted element gets moved to its correct position.
  - The process repeats until a full pass occurs with no swaps, meaning the list is sorted.

c. **Optimized Bubble Sort (Optional for Higher Understanding):**

  - A simple improvement can stop the algorithm early if no swaps are made during a pass. This is useful if the list becomes sorted before completing all possible passes.


### Why Bubble Sort is Considered Inefficient

a. **Time Complexity:**

  - Bubble Sort has a time complexity of **O(n²)**, where `n` is the number of elements in the list.
  - This means that as the size of the list increases, the time taken to sort grows **quadratically** (very quickly).
  - Bubble Sort is inefficient for large lists and is generally slower than more advanced algorithms like Merge Sort or Quick Sort.

b. **Best Used for Small Datasets:**

  - While inefficient for large datasets, Bubble Sort is easy to understand and can be used for small lists or as an introduction to sorting algorithms.


### Summary of Key Steps

  1. **Compare adjacent elements** in the list.
  2. **Swap them** if they are in the wrong order.
  3. **Repeat** until no more swaps are needed, indicating that the list is sorted.


### Bubble Sort in Pseudocode

Here’s a high-level pseudocode to help visualize the process:

```
function bubbleSort(list):
    n = length of list
    for i from 0 to n-1:
        swapped = false
        for j from 0 to n-i-1:
            if list[j] > list[j+1]:
                swap list[j] and list[j+1]
                swapped = true
        if swapped == false:
            break
```

- The variable `swapped` is used to optimize the algorithm. If no swaps are made during a pass, the algorithm stops early because the list is already sorted.

Bubble Sort is a simple but inefficient sorting algorithm that uses repeated comparison and swapping of adjacent elements to sort a list. While easy to understand, it is not practical for large datasets due to its time complexity of **O(n²)**. However, it is a great introduction to sorting algorithms for students and helps build the foundation for understanding more complex algorithms.

!!! warning
     If the animation does not appear, just refresh the page!


<div class="container">
    <h3>Bubble Sort Animation</h3>
    <canvas id="bubbleCanvas" width="600" height="400"></canvas>
    <button class="card-button" id="btnBubbleSort" onclick="startBubbleSort()">Start Bubble Sort</button>
</div>


!!! note
     Follow the animation closely.  You may be able to spot an improvement?  Depending on the values chosen (at random) and their starting positions a sorted result might be obtained before the number of iterations has been reached.  In this code, it continues to check for swaps even when no swaps have taken place on the previous iteration.

## Insertion Sort

Insertion Sort is a simple, intuitive sorting algorithm that builds the final sorted list one item at a time. It works similarly to how people arrange playing cards in their hands, inserting each new card into its correct position among the already sorted cards.

The algorithm starts with an initially sorted list of one element and **inserts** each subsequent element into the correct position relative to the already sorted portion.

It works as follows:

1. **Start with the second element**: Assume that the first element is already sorted. Start with the second element and compare it with the elements before it.
2. **Shift larger elements**: If the element to the left is larger than the current element, shift it to the right.
3. **Insert the current element**: Once you find the correct position for the current element, insert it in its correct place.
4. **Repeat** the process for the next element, gradually building up a larger sorted section of the list.

### Example of Insertion Sort

Let's sort the following list using Insertion Sort:

**Unsorted List:**
```
[38, 27, 43, 3, 9, 82, 10]
```

**Step 1: Starting with the second element (`27`)**
- Compare `27` with `38` (the element to the left).
- Since `27 < 38`, shift `38` to the right.
- Insert `27` in the first position:
  ```
  [27, 38, 43, 3, 9, 82, 10]
  ```

**Step 2: Move to the third element (`43`)**
- Compare `43` with `38`. Since `43 > 38`, no shifts are needed.
- `43` is already in its correct position:
  ```
  [27, 38, 43, 3, 9, 82, 10]
  ```

**Step 3: Move to the fourth element (`3`)**
- Compare `3` with `43`. Since `3 < 43`, shift `43` to the right.
- Compare `3` with `38`. Since `3 < 38`, shift `38` to the right.
- Compare `3` with `27`. Since `3 < 27`, shift `27` to the right.
- Insert `3` in the first position:
  ```
  [3, 27, 38, 43, 9, 82, 10]
  ```

**Step 4: Move to the fifth element (`9`)**
- Compare `9` with `43`. Since `9 < 43`, shift `43` to the right.
- Compare `9` with `38`. Since `9 < 38`, shift `38` to the right.
- Compare `9` with `27`. Since `9 < 27`, shift `27` to the right.
- Insert `9` in the second position:
  ```
  [3, 9, 27, 38, 43, 82, 10]
  ```

**Step 5: Move to the sixth element (`82`)**
- Compare `82` with `43`. Since `82 > 43`, no shifts are needed.
- `82` is already in its correct position:
  ```
  [3, 9, 27, 38, 43, 82, 10]
  ```

**Step 6: Move to the seventh element (`10`)**
- Compare `10` with `82`. Since `10 < 82`, shift `82` to the right.
- Compare `10` with `43`. Since `10 < 43`, shift `43` to the right.
- Compare `10` with `38`. Since `10 < 38`, shift `38` to the right.
- Compare `10` with `27`. Since `10 < 27`, shift `27` to the right.
- Insert `10` in the third position:
  ```
  [3, 9, 10, 27, 38, 43, 82]
  ```

**Sorted List:**
```
[3, 9, 10, 27, 38, 43, 82]
```

### **The Mechanics of Insertion Sort**

a. **Building the Sorted List:**

  - Insertion Sort works by maintaining a growing, **sorted portion** of the list.
  - For each element, the algorithm inserts it into its correct position in the already sorted part of the list by **shifting larger elements** to the right.

b. **Efficient for Small or Nearly Sorted Data:**

  - Insertion Sort is very efficient for **small datasets** or when the input list is **nearly sorted**.
  - For small lists or nearly sorted data, it can outperform more complex algorithms like Merge Sort.

c. **Comparisons and Shifts:**

  - Insertion Sort makes comparisons between the current element and the elements in the sorted portion of the list, shifting the larger elements to make room for the current element.

### Why Use Insertion Sort?

a. **Time Complexity:**

  - Insertion Sort has a time complexity of **O(n²)** in the worst case, where `n` is the number of elements in the list.
  - However, in the **best case**, when the list is already sorted, its time complexity is **O(n)**, making it quite efficient for nearly sorted data.

b. **Best Used for Small or Partially Sorted Data:**

  - While not efficient for large datasets, Insertion Sort works well for small datasets or datasets that are already partially sorted.

c. **Stable Sorting Algorithm:**

  - Insertion Sort is **stable**, meaning it preserves the relative order of equal elements, which can be important in certain situations, such as sorting records by multiple fields.

### Summary of Key Steps

  1. Start from the second element and **compare** it to the elements on its left.
  2. **Shift** the larger elements to the right to make room for the current element.
  3. **Insert** the current element into its correct position.
  4. Repeat this process until the entire list is sorted.

---

### Insertion Sort in Pseudocode

Here’s a high-level pseudocode to help you visualize the process:

```
function insertionSort(list):
    for i from 1 to length of list:
        currentValue = list[i]
        j = i - 1
        while j >= 0 and list[j] > currentValue:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = currentValue
```

- In this pseudocode, the variable `currentValue` stores the element being inserted into the sorted portion of the list, while `j` is used to shift elements in the sorted section to the right.

<div class="container">
    <h3>Insertion Sort Animation</h3>
    <canvas id="insertionCanvas" width="600" height="400"></canvas>
    <button class="card-button" id="btnInsertionSort" onclick="startInsertionSort()">Start Insertion Sort</button>
</div>

Insertion Sort is an easy-to-understand sorting algorithm that sorts a list by **inserting** each element into its correct position within a growing sorted section of the list. Though it has a time complexity of **O(n²)** in the worst case, it is efficient for small lists and nearly sorted data. Understanding Insertion Sort provides a strong foundation for more complex sorting algorithms, as it introduces the idea of comparisons and shifts, key concepts in sorting.

## Merge Sort

Merge Sort, like the binary search, is a **divide and conquer** sorting algorithm. It is efficient, particularly for large lists, and uses a recursive approach to sort data. 

- **Divide**: Split the list into smaller sub-lists until each sub-list contains only one element.
- **Conquer**: Merge the sub-lists in a sorted manner to produce the final sorted list.

Merge Sort is often considered better than simpler sorting algorithms like Bubble Sort or Insertion Sort, especially when dealing with large datasets, due to its predictable time efficiency.

**How Merge Sort Works**

1. **Splitting (Dividing) Phase:**
   - The unsorted list is repeatedly divided into two halves until all sub-lists contain **a single element**.
   - A single element is considered sorted by definition because there is nothing to compare it with.

2. **Merging (Conquering) Phase:**
   - The sub-lists are then **merged** together in pairs, and during each merge, the elements are placed in order.
   - This process of merging continues until all the sub-lists are merged back into one fully sorted list.

### Example

Let's look at how the Merge Sort works with a list of numbers:

**Unsorted List:**
```
[38, 27, 43, 3, 9, 82, 10]
```

**Step 1: Divide the List**
- First, we split the list into two halves:
```
Left:  [38, 27, 43]
Right: [3, 9, 82, 10]
```
- We continue splitting until we get sub-lists of one element:
```
Left:  [38], [27], [43]
Right: [3], [9], [82], [10]
```

**Step 2: Merge the Lists**
- Now, we begin merging the sub-lists while sorting them:
```
Merge [38] and [27] → [27, 38]
Merge [43] remains as is.
Merge [3] and [9] → [3, 9]
Merge [82] and [10] → [10, 82]
```
- The partially merged lists are now:
```
Left:  [27, 38, 43]
Right: [3, 9, 10, 82]
```
- Finally, merge the two large sorted lists:
```
Merge [27, 38, 43] and [3, 9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]
```

**Sorted List:**
```
[3, 9, 10, 27, 38, 43, 82]
```


### The Mechanics of Merge Sort

a. **Divide and Conquer Principle:**
  
  - **Divide**: The list is recursively split into smaller sub-lists.
  - **Conquer**: Each pair of sub-lists is merged in sorted order.

b. **Recursive Nature:**

  - Merge Sort is a **recursive** algorithm. This means that the function repeatedly calls itself to split the list into halves, until only single elements remain.

c. **Merging:**

  - The merge process takes two sorted sub-lists and combines them into one sorted list by comparing the smallest elements from both sub-lists and arranging them in order.


### Why Merge Sort is Efficient:

a. **Time Complexity:**

  - Merge Sort has a **time complexity of O(n log n)**, which means that as the size of the list (n) increases, the time taken to sort grows in proportion to n multiplied by the logarithm of n.
  - This is better than algorithms like Bubble Sort and Insertion Sort, which have time complexities of **O(n²)**.

b. **Stable Sorting Algorithm:**

  - Merge Sort is **stable**, meaning it preserves the relative order of items with equal values.
  - This can be important when sorting complex data types with multiple fields.

c. **Drawback:**

  - One of the downsides of Merge Sort is that it requires **extra memory** for the temporary storage of sub-lists during the merging process, which can be a limitation when working with large datasets in memory-constrained environments.


### Summary of Key Steps:

  1. **Split the list** recursively into halves until each sub-list has one element.
  2. **Merge the sub-lists** back together in a sorted manner.


### Merge Sort in Pseudocode

Here’s a high-level pseudocode to help visualize the process:

```
function mergeSort(list):
    if length of list <= 1:
        return list
    
    mid = length of list / 2
    leftHalf = mergeSort(list[0:mid])
    rightHalf = mergeSort(list[mid:])

    return merge(leftHalf, rightHalf)
    
function merge(left, right):
    result = []
    while left and right are not empty:
        if left[0] < right[0]:
            append left[0] to result
            remove left[0] from left
        else:
            append right[0] to result
            remove right[0] from right

    append remaining elements of left (if any) to result
    append remaining elements of right (if any) to result
    
    return result
```

Merge Sort is an efficient, recursive algorithm that uses the divide and conquer approach. It breaks down the problem of sorting into smaller, more manageable sub-problems and then merges them back together in a sorted order. While Merge Sort requires additional space to store sub-lists, its time complexity of **O(n log n)** makes it a preferred choice for sorting large datasets efficiently.

## Questions

{{ show_questions(page.title, page.meta.filename) }}
