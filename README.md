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
```

## 2. Selection Sort

**Function**: `selection_sort(arr)`

Selection Sort repeatedly finds the minimum element from the unsorted portion and moves it to the beginning. It maintains two subarrays in a given array: the subarray which is already sorted and the remaining subarray which is unsorted. It is not efficient for large lists as it performs O(n^2) comparisons.

**Usage:**
```python
sorted_array = selection_sort([64, 25, 12, 22, 11])
```

## 3. Insertion Sort

**Function**: `insertion_sort(arr)`

Insertion Sort builds the final sorted array one item at a time. 
It is much less efficient on large lists than more advanced algorithms like quicksort, heapsort, or merge sort. 
However, it performs well on small or mostly sorted datasets, making it useful for certain scenarios.

**Usage:**
```python
sorted_array = insertion_sort([12, 11, 13, 5, 6])
```


## 4. Merge Sort
**Function**: `merge_sort(arr)`

Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. 
It works by dividing the unsorted list into n sublists, each containing one element, 
and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. 
This results in a time complexity of O(n log n).


**Usage:**
```python
sorted_array = merge_sort([12, 11, 13, 5, 6, 7]
```

## 5. Quick Sort

**Function**: `quick_sort(arr)`

Quick Sort is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. 
It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
This process is recursively applied to the sub-arrays, resulting in a time complexity of O(n log n) on average.

**Usage:**
```python
sorted_array = quick_sort([10, 7, 8, 9, 1, 5])
```


## 6. Heap Sort
**Function**: `heap_sort(arr)`

Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure.
It is similar to selection sort where we first find the maximum element and place it at the end. 
The heap data structure is used to find the maximum element efficiently, making it a reliable sorting algorithm with a time complexity of O(n log n).

**Usage:**
```python
sorted_array = heap_sort([12, 11, 13, 5, 6, 7])
```


## 7. Shell Sort
**Function**: `shell_sort(arr)`

Shell Sort is an in-place comparison sort. It is mainly a variation of Insertion Sort. 
In Shell Sort, we start by sorting elements that are far apart from each other and progressively reduce the gap between elements to be compared. 
This allows the algorithm to move some out-of-place elements into position faster than a simple nearest-neighbor exchange.

**Usage:**
```python
sorted_array = shell_sort([12, 34, 54, 2, 3])
```


## 8. Counting Sort
**Function**: `counting_sort(arr)`

Counting Sort is a stable sorting technique that works by counting the number of objects having distinct key values. 
Then it performs some arithmetic to calculate the position of each object in the output sequence. 
It is efficient for sorting integers within a known range and has a time complexity of O(n + k), where n is the number of elements and k is the range of input.

**Usage:**
```python
sorted_array = counting_sort([1, 4, 1, 2, 7, 5, 2])
```


## 9. Radix Sort
**Function**: `radix_sort(arr)`

Radix Sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. 
For elements with more than one significant digit, this bucketing process is repeated for each digit. 
This results in a time complexity of O(nk), where n is the number of elements and k is the number of digits.

**Usage:**
```python
sorted_array = radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
```


## 10. Bucket Sort
**Function**: `bucket_sort(arr)`

Bucket Sort is mainly useful when the input is uniformly distributed over a range. 
It works by distributing the elements into a number of buckets, then sorting these buckets individually (using another sorting algorithm or recursively applying bucket sort). 
Finally, the sorted buckets are concatenated to form the final sorted array. It has an average time complexity of O(n + k).

**Usage:**
```python
sorted_array = bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68])
```


## Time Complexities

| Algorithm       | Best Case       | Average Case    | Worst Case     | Space Complexity  |
|-----------------|-----------------|-----------------|----------------|-------------------|
| Bubble Sort     | O(n)            | O(n^2)          | O(n^2)         | O(1)              |
| Selection Sort  | O(n^2)          | O(n^2)          | O(n^2)         | O(1)              |
| Insertion Sort  | O(n)            | O(n^2)          | O(n^2)         | O(1)              |
| Merge Sort      | O(n log n)      | O(n log n)      | O(n log n)     | O(n)              |
| Quick Sort      | O(n log n)      | O(n log n)      | O(n^2)         | O(log n)          |
| Heap Sort       | O(n log n)      | O(n log n)      | O(n log n)     | O(1)              |
| Shell Sort      | O(n log n)      | O(n (log n)^2)  | O(n (log n)^2) | O(1)              |
| Counting Sort   | O(n + k)        | O(n + k)        | O(n + k)       | O(k)              |
| Radix Sort      | O(nk)           | O(nk)           | O(nk)          | O(n + k)          |
| Bucket Sort     | O(n + k)        | O(n + k)        | O(n^2)         | O(n)              |

### Notes:
- `n` is the number of elements in the array.
- `k` is the range of the input (for Counting Sort and Radix Sort).
- `log n` is the logarithm of `n` (base 2, typically).

