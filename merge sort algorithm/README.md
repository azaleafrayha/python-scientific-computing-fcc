# Merge Sort Algorithm
Merge Sort is a classic Divide and Conquer algorithm used to sort collections of data efficiently. The logic follows three main steps:
1. **Divide**: Splitting the array into smaller sub-arrays.
2. **Conquer**: Sorting these sub-arrays recursively.
3. **Combine**: Merging the sorted sub-arrays back into a single sorted array.


## Implementation Features
This project is part of my journey in learning Python and Algorithms through freeCodeCamp Scientific Computing with Python curriculum. It was a great challenge, and it gave me the chance to really dig into how these mechanisms work under the hood:
* **Recursive Divide and Conquer**: A core part of the algorithm where the array is split into smaller pieces and then sorted step-by-step using self-referential functions.

* **In-place Index Tracking**: Keeping track of data movement with `left_array_index`, `right_array_index`, and `sorted_index`. It’s a clean way to manage how values are shifted without creating unnecessary extra lists.

* **Modular Design**: By wrapping the test logic inside an `if __name__ == '__main__':` block, the code stays flexible. This way, the `merge_sort` function can be imported into other scripts as a module without running the demo code automatically.