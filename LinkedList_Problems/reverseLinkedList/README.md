# Reverse Linked List

## Problem Description

Given the beginning of a singly linked list `head`, reverse the list, and return the new beginning of the list.

## Examples

**Example 1:**
```
Input: head = [0,1,2,3]
Output: [3,2,1,0]
```

**Example 2:**
```
Input: head = []
Output: []
```

## Constraints

- `0 <= The length of the list <= 1000`
- `-1000 <= Node.val <= 1000`

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

## LeetCode Link

[Reverse Linked List - LeetCode](https://leetcode.com/problems/reverse-linked-list/) 