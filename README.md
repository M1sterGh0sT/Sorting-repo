# Sorting Algorithms in Python

This repository contains implementations of various sorting algorithms in Python. Each algorithm has its own strengths and use cases. 
Below are the details for each sorting function included in this repository.

## 1. Bubble Sort

**Function:** `bubble_sort(arr)`

Bubble Sort is a simple comparison-based algorithm where each pair of adjacent elements is compared, and the elements are swapped if they are not in order. 
This process is repeated until the array is sorted. Although it is easy to understand and implement, Bubble Sort is not suitable for large datasets due to its O(n^2) time complexity.

**Usage:**
```python
sorted_array = bubble_sort([64, 34, 25, 12, 22, 11, 90])


## 2. Selection Sort

**Function**: `selection_sort(arr)`

Selection Sort repeatedly finds the minimum element from the unsorted portion and moves it to the beginning. It maintains two subarrays in a given array: the subarray which is already sorted and the remaining subarray which is unsorted. It is not efficient for large lists as it performs O(n^2) comparisons.

**Usage:**
```python
sorted_array = selection_sort([64, 25, 12, 22, 11])



