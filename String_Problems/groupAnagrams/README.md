# Group Anagrams

## Problem Description

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Examples

**Example 1:**
```
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

**Example 2:**
```
Input: strs = ["x"]
Output: [["x"]]
```

**Example 3:**
```
Input: strs = [""]
Output: [[""]]
```

## Constraints

- `1 <= strs.length <= 1000`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters

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

The solution uses a hash map approach with sorted strings as keys:

1. **Key Generation**: For each string, sort its characters to create a unique key for all anagrams
2. **Grouping**: Use the sorted string as a dictionary key to group anagram indices
3. **Result Building**: Construct the final result by collecting all strings for each anagram group

**Algorithm Steps:**
- Iterate through input strings
- Sort each string's characters to create anagram signature
- Group indices by their anagram signature
- Build result by collecting original strings for each group

**Note**: The output order may vary since "any order" is acceptable according to the problem statement.

## Complexity Analysis

**Time Complexity**: O(N × M × log M) where:
- N = number of strings
- M = maximum length of a string
- log M factor comes from sorting each string

**Space Complexity**: O(N × M) for storing the hash map and result

## Alternative Approaches

1. **Character Count**: Instead of sorting, use character frequency as key (O(N × M) time)
2. **Prime Number Mapping**: Assign prime numbers to each character and use product as key

## LeetCode Link

[Group Anagrams - LeetCode](https://leetcode.com/problems/group-anagrams/) 