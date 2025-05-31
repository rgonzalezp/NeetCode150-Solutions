# NeetCode150 + LeetCode Solutions

## Description

The purpose of this repository is to document my solutions to **NeetCode 150** and **LeetCode** problems. This repository should be useful for anyone trying to prepare software engineering coding interviews. The repository contains realistic solutions made by a real software engineer seeking to understand how to approach interview coding problems in a realistic time frame (most solutions were developed in 5 minutes to 1 hour).

I want to record each solution script and make the repository as simple as possible. My goal is to share a repository where other people seeking to prepare for software engineering interview can observe and debug the code of my solutions scripts and test against them.

## Repository Structure

The repository is organized by problem categories:

```
NeetCode150-Solutions/
├── Array_Problems/
├── Binary_Search_Problems/
├── Math_Problems/
├── Matrix_Problems/
├── String_Problems/
└── etc...
```

Each problem category contains individual problem folders with:
- Solution script (`solution.py`) with a quick test to allow you to debug the execution of my solution
- Test cases (`test_cases.py`) with  typical edge case tests to validate the solution
- Problem description (if applicable) copied from original problem statement.

### Running Solutions

```bash
# Navigate to a specific problem directory
cd Array_Problems/two_sum/

# Debug the solution directly and use print statements or anything else you want
python solution.py

# Run the solution with test cases
python test_cases.py
```

## Solution Format

Each solution follows this structure:

```python
class Solution:
    def problemName(self, params) -> return_type:
        # Solution implementation
        pass
```

## Test Cases Format

Test cases are generated based on problem constraints and include:
- Edge cases
- Normal cases
- Boundary conditions
- Expected outputs

Example:
```python
def test_solution():
    solution = Solution()
    
    # Test case 1: Normal case
    assert solution.twoSum([2,7,11,15], 9) == [0,1]
    
    # Test case 2: Edge case
    assert solution.twoSum([3,2,4], 6) == [1,2]
```

## Contributing

Feel free to:
- Suggest optimizations
- Report bugs
- Add alternative solutions
- Improve test cases

## Problem Sources

- [NeetCode 150](https://neetcode.io/practice)
- [LeetCode](https://leetcode.com/)

---

