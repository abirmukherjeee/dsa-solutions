# Selection Sort

## Problem Statement

Given an array of integers `nums`, sort the array in **non-decreasing order** using the **selection sort** algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.

### Example 1
**Input:**  
`nums = [7, 4, 1, 5, 3]`

**Output:**  
`[1, 3, 4, 5, 7]`

**Explanation:**  
`1 ≤ 3 ≤ 4 ≤ 5 ≤ 7`, hence the array is sorted.

---

### Example 2
**Input:**  
`nums = [5, 4, 4, 1, 1]`

**Output:**  
`[1, 1, 4, 4, 5]`

**Explanation:**  
`1 ≤ 1 ≤ 4 ≤ 4 ≤ 5`, hence the array is sorted.

---

## Intuition

Selection sort works by **repeatedly selecting the minimum element from the unsorted part of the array and placing it at the beginning**.

After each iteration:
- The smallest element of the unsorted part is placed in its correct position.
- The sorted portion of the array grows from the left.
- The largest elements automatically move toward the end.

---

## Dry Run (Step-by-Step Example)

Consider the array:

`nums = [13, 46, 24, 52, 20, 9]`

---

### Step 1 (Iteration 1)
- Select the smallest element from the entire array.
- Smallest element = `9`
- Swap it with the first element.

`[9, 46, 24, 52, 20, 13]`

After this step, the **first element is in its correct position**.

---

### Step 2 (Iteration 2)
- Consider the unsorted part starting from index `1`.
- Smallest element = `13`
- Swap it with the second element.

`[9, 13, 24, 52, 20, 46]`

Now, the **first two elements are sorted**.

---

### Step 3 (Iteration 3)
- Consider the unsorted part starting from index `2`.
- Smallest element = `20`
- Swap it with the third element.

`[9, 13, 20, 52, 24, 46]`

The array is now sorted till the third element.

---

### Step 4 (Iteration 4)
- Consider the unsorted part starting from index `3`.
- Smallest element = `24`
- Swap it with the element at index `3`.

`[9, 13, 20, 24, 52, 46]`

---

### Step 5 (Iteration 5)
- Consider the remaining unsorted part.
- Smallest element = `46`
- Swap it with the element at index `4`.

`[9, 13, 20, 24, 46, 52]`

---

### Key Observation

Notice that:
- The **largest element automatically ends up at the last index**.
- After placing the first `n-1` elements, the array is already sorted.

➡️ Therefore, **only `n-1` iterations are required** for an array of size `n`.

---

## Approach

1. Start from index `i = 0` and treat it as the beginning of the unsorted part.
2. Find the smallest element in the range `i` to `n-1` using an inner loop.
3. Keep track of the index of the smallest element.
4. Swap the smallest element with the element at index `i`.
5. Move to the next index and repeat until the array is sorted.

---

## Final Solution Code

Refer to `solution.py` for the complete implementation.

```python
def selectionSort(self, nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```

---

## Complexity Analysis

### Time Complexity

**O(N²)**

Selection sort uses two nested loops:
- The outer loop runs from index `0` to `n-2`, fixing one element in its correct position per iteration.
- For each iteration of the outer loop, the inner loop scans the remaining unsorted portion of the array to find the minimum element.

As a result, the total number of comparisons is proportional to:

`(N - 1) + (N - 2) + ... + 1 = O(N²)`

---

### Space Complexity

**O(1)**

Selection sort is an **in-place sorting algorithm**.  
It only uses a constant amount of extra memory (variables for indices and temporary swapping), regardless of the input size.

No additional data structures proportional to `N` are used.

---

## Tags

- Sorting
- Arrays
- In-place Algorithm
- Comparison Sort

---

## When to Use Selection Sort

- Best suited for **very small datasets**
- Useful when **memory writes are expensive**, as it performs at most `n-1` swaps
- Easy to understand and implement for learning basic sorting concepts
- Often used in interviews to test **fundamental algorithmic understanding**

---

## Limitations

- Inefficient for large inputs due to **O(N²)** time complexity
- Performance does **not improve for nearly sorted arrays**
- Not suitable for real-world production systems with large datasets

---

## Stability

Selection sort is **not stable** by default.

If two elements have the same value, their **relative order may change** because of swapping.

To make it stable, additional logic or memory is required.

---

## Comparison with Other Simple Sorting Algorithms

| Algorithm       | Time Complexity | Space Complexity | Stable | Adaptive |
|-----------------|-----------------|------------------|--------|----------|
| Selection Sort  | O(N²)           | O(1)             | ❌     | ❌       |
| Bubble Sort     | O(N²)           | O(1)             | ✅     | ✅       |
| Insertion Sort  | O(N²)           | O(1)             | ✅     | ✅       |

---

## Interview Notes

- Selection sort always performs the **same number of comparisons**, regardless of input order
- It minimizes swaps, not comparisons
- Often asked to explain **why it is O(N²)** even for sorted arrays

---

### Time Complexity

**O(N²)** — *Best, Average, and Worst Case*

Selection sort always performs the **same number of comparisons**, regardless of the initial order of the array.

#### Why?

- In the **first iteration**, the algorithm scans all `N` elements to find the minimum.
- In the **second iteration**, it scans the remaining `N - 1` elements.
- This continues until only one element remains.

Total number of comparisons:

`(N - 1) + (N - 2) + ... + 1 = O(N²)`

---

#### Best Case: O(N²)

Even if the array is already sorted:
- Selection sort **still scans the remaining unsorted part** to confirm the minimum.
- No early termination is possible.

➡️ Therefore, the best case is **O(N²)**.

---

#### Average Case: O(N²)

For a randomly ordered array:
- The algorithm performs the same full scan in each iteration.
- The number of comparisons remains unchanged.

➡️ Hence, the average case is **O(N²)**.

---

#### Worst Case: O(N²)

In a reverse-sorted array:
- Every iteration still requires scanning the unsorted portion.
- The number of swaps may increase, but **comparisons remain the same**.

➡️ Thus, the worst case is also **O(N²)**.

---

#### Key Insight

Selection sort is **non-adaptive**:
- Its time complexity **does not depend on input order**
- Only the **number of swaps** may vary, not comparisons

---

## One-Line Summary

"Repeatedly select the minimum element from the unsorted part and place it at the beginning."
