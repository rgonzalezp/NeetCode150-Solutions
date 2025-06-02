# Non-Cyclical Number (Happy Number)

## Problem Description

A **non-cyclical number** is an integer defined by the following algorithm:

1. Given a positive integer, replace it with the sum of the squares of its digits.
2. Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
3. If it stops at 1, then the number is a non-cyclical number.

Given a positive integer `n`, return `true` if it is a non-cyclical number, otherwise return `false`.

## Examples

**Example 1:**
```
Input: n = 100
Output: true
Explanation: 1² + 0² + 0² = 1
```

**Example 2:**
```
Input: n = 101
Output: false
Explanation:
1² + 0² + 1² = 2
2² = 4
4² = 16
1² + 6² = 37
3² + 7² = 58
5² + 8² = 89
8² + 9² = 145
1² + 4² + 5² = 42
4² + 2² = 20
2² + 0² = 4 (This number has already been seen - cycle detected)
```

## Constraints

- `1 <= n <= 1000`

## Files

- `solution.py`: Contains the solution implementation with debugging test case
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

The solution uses a hash set approach to detect cycles:

1. **Sum of Squares**: For each number, extract digits and compute sum of their squares
2. **Cycle Detection**: Use a dictionary to track previously seen numbers
3. **Termination**: Return `True` if we reach 1, `False` if we detect a cycle

**Algorithm Steps:**
- Start with the given number
- While not in a cycle:
  - Calculate sum of squares of digits
  - If sum equals 1, return `True` (happy number)
  - If sum was seen before, cycle detected, return `False`
  - Otherwise, continue with the new sum

**Time Complexity**: O(k) where k is the total number of digits processed until reaching 1 or detecting a cycle  
**Space Complexity**: O(m) where m is the number of unique values encountered before cycle detection

## Mathematical Insight

For any starting number, the sequence will either:
1. **Converge to 1** (making it a happy/non-cyclical number)
2. **Enter a cycle** that doesn't include 1 (making it unhappy/cyclical)

Common cycles include: `4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4`

## LeetCode Link

[Happy Number - LeetCode](https://leetcode.com/problems/happy-number/) 