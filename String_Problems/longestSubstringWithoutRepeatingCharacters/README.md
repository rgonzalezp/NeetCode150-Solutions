# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

A **substring** is a contiguous sequence of characters within a string.

## Examples

**Example 1:**
```
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.
```

**Example 2:**
```
Input: s = "xxxx"
Output: 1
Explanation: The longest substring is "x" with length 1.
```

## Constraints

- `0 <= s.length <= 1000`
- `s` may consist of printable ASCII characters

## Files

- `solution.py`: Contains the solution implementation with debugging test cases
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

The solution uses a **sliding window approach** with two pointers:

1. **Expand Phase**: Move the end pointer and add characters to the window
2. **Contract Phase**: When a duplicate is found, shrink the window from the left
3. **Track Maximum**: Keep track of the longest valid window seen

**Algorithm Steps:**
- Use a set to track characters in the current window
- Expand window by moving end pointer
- When duplicate found, contract window from left until duplicate is removed
- Track the maximum window size throughout the process

**Key Insight**: The sliding window technique ensures we only traverse the string once, making it optimal for this type of substring problem.

## Complexity Analysis

**Time Complexity**: O(n) where n is the length of the string
- Single pass through the string with the end pointer
- Each character is added and removed at most once

**Space Complexity**: O(1) - bounded by the number of printable ASCII characters
- The set can contain at most all printable ASCII characters (constant space)
- Independent of input string length

## Algorithm Pattern

This problem demonstrates the **sliding window pattern**, which is useful for:
- Substring problems with constraints
- Finding optimal contiguous sequences
- Problems requiring tracking of elements in a moving window

## Alternative Approaches

1. **HashMap with Last Index**: Track last seen index of each character for more efficient jumping
2. **Array as Hash Table**: Use ASCII values as indices for even faster lookups
3. **Brute Force**: Check all possible substrings (O(n³) time complexity)

## LeetCode Link

[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) 