# Daily Temperatures

## Problem Description

You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the ith day.

Return an array `result` where `result[i]` is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set `result[i]` to 0 instead.

## Examples

**Example 1:**
```
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]
Explanation:
- Day 0 (30°): Next warmer day is day 1 (38°), so 1 day later
- Day 1 (38°): Next warmer day is day 5 (40°), so 4 days later  
- Day 2 (30°): Next warmer day is day 3 (36°), so 1 day later
- Day 3 (36°): Next warmer day is day 5 (40°), so 2 days later
- Day 4 (35°): Next warmer day is day 5 (40°), so 1 day later
- Day 5 (40°): No warmer day ahead, so 0
- Day 6 (28°): No warmer day ahead, so 0
```

**Example 2:**
```
Input: temperatures = [22,21,20]
Output: [0,0,0]
Explanation: There are no warmer days ahead for any day.
```

## Constraints

- `1 <= temperatures.length <= 1000`
- `1 <= temperatures[i] <= 100`

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

The provided solution uses a brute force approach:
1. For each day, scan forward through the remaining days
2. Count days until a warmer temperature is found
3. If no warmer day exists, return 0 for that position

**Time Complexity**: O(n²) - for each element, we potentially scan all remaining elements  
**Space Complexity**: O(n) - for storing the result array

## Alternative Approaches

While this solution works correctly, a more efficient O(n) solution exists using a **monotonic stack** to track indices of days with decreasing temperatures, achieving better time complexity for larger inputs.

## LeetCode Link

[Daily Temperatures - LeetCode](https://leetcode.com/problems/daily-temperatures/) 