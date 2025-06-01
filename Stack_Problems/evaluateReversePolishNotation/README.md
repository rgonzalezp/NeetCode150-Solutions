# Evaluate Reverse Polish Notation

## Problem Description

You are given an array of strings `tokens` that represents a valid arithmetic expression in **Reverse Polish Notation**.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always **truncates toward zero**.

## Examples

**Example 1:**
```
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
```

## Constraints

- `1 <= tokens.length <= 1000`
- `tokens[i]` is `"+"`, `"-"`, `"*"`, or `"/"`, or a string representing an integer in the range `[-100, 100]`
- Division between integers always **truncates toward zero**

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

The solution uses a stack-based approach:
1. Iterate through tokens
2. If token is a number, push to stack
3. If token is an operator, pop two operands, perform operation, and push result back
4. Return the final result from the stack

**Important**: For division, `int(a/b)` truncates toward zero as required by the problem.

## About Reverse Polish Notation (RPN)

RPN is a mathematical notation where operators follow their operands. For example:
- Infix: `(1 + 2) * 3`
- RPN: `1 2 + 3 *`

## LeetCode Link

[Evaluate Reverse Polish Notation - LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) 