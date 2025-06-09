# Trapping Rain Water

## Problem Description

You are given an array of non-negative integers `height` which represent an elevation map. Each value `height[i]` represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

## Examples

**Example 1:**
```
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
Explanation: The elevation map is represented by the array [0,2,0,3,1,0,1,3,2,1]. 
In this case, 9 units of rain water can be trapped.
```

**Visual representation:**
```
    |
|   ||  |
||_||||_||
```

## Constraints

- `1 <= height.length <= 1000`
- `0 <= height[i] <= 1000`

## Files

- `solution.py`: Contains the solution implementation with debugging test case and visualization
- `test_cases.py`: Contains comprehensive test cases covering edge cases and boundary conditions
- `README.md`: This problem description

## Usage

```bash
# Debug the solution directly with visualization
python solution.py

# Run comprehensive test cases
python test_cases.py
```

## Implementation Notes

The solution uses a **prefix-suffix array approach**:

1. **Prefix Array**: For each position, store the maximum height seen so far from the left
2. **Suffix Array**: For each position, store the maximum height seen so far from the right  
3. **Water Calculation**: At each position, water trapped = min(left_max, right_max) - current_height

**Algorithm Steps:**
- Build prefix array by scanning left to right
- Build suffix array by scanning right to left
- For each position, calculate trapped water using the minimum of prefix and suffix values
- Sum all positive water values

**Key Insight**: Water at any position is determined by the minimum of the highest bars to its left and right, minus the current bar height.

## Complexity Analysis

**Time Complexity**: O(n) - Three separate passes through the array
- One pass for prefix calculation
- One pass for suffix calculation  
- One pass for final water calculation

**Space Complexity**: O(n) - Storage for prefix and suffix arrays

## Alternative Approaches

1. **Two Pointer Technique**: O(1) space using left and right pointers
2. **Stack-based Solution**: Using a monotonic stack to track indices
3. **Dynamic Programming**: Similar to current approach but with memoization

## LeetCode Link

[Trapping Rain Water - LeetCode](https://leetcode.com/problems/trapping-rain-water/) 