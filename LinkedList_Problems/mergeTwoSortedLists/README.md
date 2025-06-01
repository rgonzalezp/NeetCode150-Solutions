# Merge Two Sorted Linked Lists

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

## Examples

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]
```

**Example 2:**
```
Input: list1 = [], list2 = [1,2]
Output: [1,2]
```

**Example 3:**
```
Input: list1 = [], list2 = []
Output: []
```

## Constraints

- `0 <= The length of each list <= 100`
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order

## Files

- `solution.py`: Contains the solution implementation with ListNode definition, helper functions, and debugging test case
- `test_cases.py`: Contains comprehensive test cases covering edge cases and boundary conditions
- `README.md`: This problem description

## Usage

```bash
# Debug the solution directly
python solution.py

# Run comprehensive test cases
python test_cases.py
```

## Implementation Notes

The solution includes helper functions:
- `create_linked_list(arr)`: Creates a linked list from an array for testing
- `linked_list_to_array(head)`: Converts a linked list back to an array for verification

The algorithm merges the two sorted lists by comparing values and connecting nodes appropriately.

## LeetCode Link

[Merge Two Sorted Lists - LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) 