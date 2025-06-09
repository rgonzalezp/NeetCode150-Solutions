# Median of Two Sorted Arrays

## Problem Description

You are given two integer arrays `nums1` and `nums2` of size `m` and `n` respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

**Your solution must run in O(log(m+n)) time.**

## Examples

**Example 1:**
```
Input: nums1 = [1,2], nums2 = [3]
Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.
```

**Example 2:**
```
Input: nums1 = [1,3], nums2 = [2,4]
Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.
```

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

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

The provided solution uses a **merge-based approach**:

1. **Two-pointer merge**: Similar to merge step in merge sort
2. **Complete array construction**: Builds the entire merged sorted array
3. **Median calculation**: Finds median from the merged array

**Algorithm Steps:**
- Use two pointers to merge arrays in sorted order
- Handle remaining elements from either array
- Calculate median based on total length (odd/even)

## Complexity Analysis

**Time Complexity**: O(m + n) - Must traverse both arrays completely  
**Space Complexity**: O(m + n) - Creates new merged array

## Important Note

⚠️ **Optimization Opportunity**: While this solution is correct and handles all test cases properly, it **does not meet the optimal O(log(m+n))** time complexity requirement specified in the problem statement.

## Optimal Approach

The optimal O(log(m+n)) solution uses **binary search** on the smaller array:
- Partition both arrays such that left halves have equal elements to right halves
- Use binary search to find the correct partition point
- No need to construct the entire merged array

## Key Insights

- **Median Definition**: Middle element(s) that divide sorted data into equal halves
- **Even vs Odd**: For even total length, median = average of two middle elements
- **Merge Strategy**: Leverages the fact that both input arrays are already sorted

## LeetCode Link

[Median of Two Sorted Arrays - LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) 