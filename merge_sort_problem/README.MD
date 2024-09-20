This problem requires building a Sort algorithm that sorts an array by merging it into smaller pieces.

## Full Logic of Merge Sort Explained

Merge sort is indeed a "divide and conquer" sorting algorithm that consists of three main steps: dividing the list, conquering (sorting each piece), and combining (merging them back into a sorted list). Here’s a detailed breakdown:

### Step 1: Divide
You start by splitting the full list into two smaller sublists. This is done recursively until each sublist has only one element or no elements (an empty list or a single-element list is already sorted by definition).

### Step 2: Conquer
Once you have broken down the list into sublists of one element each, you begin to sort and merge them back together. Since each sublist is initially of size one, they are trivially sorted. The sorting happens implicitly as part of the merge process in the next step.

### Step 3: Combine (Merge)
The merge process is where the actual sorting happens during the recombination. Here's how it works:

- **Compare and Merge**: You take two sorted sublists and merge them into a single sorted list. You do this by comparing the smallest (unmerged) elements of each sublist and adding the smaller one to the new merged list. This is repeated until all elements from both sublists are in the merged list.

- **Recursive Merging**: This merging is done recursively:
  - You merge very small sublists first (initially of size one).
  - As you move up the recursion tree, you merge larger and larger sublists, which are sorted during the merge until the entire array is reassembled and sorted.

#### Example with [5, 6, 4, 2]:
- **Initial List**: [5, 6, 4, 2]
- **Divide**:
  - Split into [5, 6] and [4, 2].
- **Further Divide**:
  - Split [5, 6] into [5] and [6].
  - Split [4, 2] into [4] and [2].
- **Conquer (by trivial sorting)**:
  - Each of [5], [6], [4], [2] is already sorted because all are single elements.
- **Combine (Merge)**:
  - Merge [5] and [6] to get [5, 6] (they are already in order).
  - Merge [4] and [2] but since 2 < 4, the merge result is [2, 4].
- **Final Merge**:
  - Merge [5, 6] and [2, 4] using the merge logic. Start with comparing the first elements (5 from left and 2 from right). Since 2 < 5, 2 is placed first, followed by 4 (since 4 < 5), and then the remaining elements of [5, 6] are appended to get [2, 4, 5, 6].

This step-by-step approach through splitting, trivial sorting, and merging through recursive combination efficiently sorts the entire original list. Each step ensures that the lists are combined in a sorted manner, maintaining the order throughout the process.
