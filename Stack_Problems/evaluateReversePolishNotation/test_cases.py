from solution import Solution

def test_evaluate_reverse_polish_notation():
    solution = Solution()
    
    print("Testing Evaluate Reverse Polish Notation Solution...")
    print("=" * 55)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example [\"1\",\"2\",\"+\",\"3\",\"*\",\"4\",\"-\"]")
    tokens1 = ["1","2","+","3","*","4","-"]
    result1 = solution.evalRPN(tokens1)
    expected1 = 5  # ((1 + 2) * 3) - 4 = 5
    print(f"Input: {tokens1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Explanation: ((1 + 2) * 3) - 4 = {expected1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: Single number
    print("Test 2: Single number [\"42\"]")
    tokens2 = ["42"]
    result2 = solution.evalRPN(tokens2)
    expected2 = 42
    print(f"Input: {tokens2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Simple addition
    print("Test 3: Simple addition [\"2\",\"3\",\"+\"]")
    tokens3 = ["2","3","+"]
    result3 = solution.evalRPN(tokens3)
    expected3 = 5  # 2 + 3 = 5
    print(f"Input: {tokens3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Simple subtraction
    print("Test 4: Simple subtraction [\"5\",\"2\",\"-\"]")
    tokens4 = ["5","2","-"]
    result4 = solution.evalRPN(tokens4)
    expected4 = 3  # 5 - 2 = 3
    print(f"Input: {tokens4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Simple multiplication
    print("Test 5: Simple multiplication [\"4\",\"3\",\"*\"]")
    tokens5 = ["4","3","*"]
    result5 = solution.evalRPN(tokens5)
    expected5 = 12  # 4 * 3 = 12
    print(f"Input: {tokens5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Simple division
    print("Test 6: Simple division [\"6\",\"2\",\"/\"]")
    tokens6 = ["6","2","/"]
    result6 = solution.evalRPN(tokens6)
    expected6 = 3  # 6 / 2 = 3
    print(f"Input: {tokens6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Division with truncation towards zero
    print("Test 7: Division with truncation [\"7\",\"3\",\"/\"]")
    tokens7 = ["7","3","/"]
    result7 = solution.evalRPN(tokens7)
    expected7 = 2  # 7 / 3 = 2.33... -> 2 (truncate towards zero)
    print(f"Input: {tokens7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Negative division with truncation
    print("Test 8: Negative division [\"-7\",\"3\",\"/\"]")
    tokens8 = ["-7","3","/"]
    result8 = solution.evalRPN(tokens8)
    expected8 = -2  # -7 / 3 = -2.33... -> -2 (truncate towards zero)
    print(f"Input: {tokens8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Negative numbers
    print("Test 9: Negative numbers [\"-1\",\"2\",\"+\"]")
    tokens9 = ["-1","2","+"]
    result9 = solution.evalRPN(tokens9)
    expected9 = 1  # -1 + 2 = 1
    print(f"Input: {tokens9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Complex expression
    print("Test 10: Complex expression [\"15\",\"7\",\"1\",\"1\",\"+\",\"-\",\"/\",\"3\",\"*\",\"2\",\"1\",\"1\",\"+\",\"+\",\"-\"]")
    tokens10 = ["15","7","1","1","+","-","/","3","*","2","1","1","+","+","-"]
    result10 = solution.evalRPN(tokens10)
    # Step by step: 15 / (7 - (1 + 1)) * 3 - (2 + (1 + 1))
    # = 15 / (7 - 2) * 3 - (2 + 2)
    # = 15 / 5 * 3 - 4
    # = 3 * 3 - 4
    # = 9 - 4 = 5
    expected10 = 5
    print(f"Input: {tokens10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Zero operations
    print("Test 11: Operations with zero [\"0\",\"3\",\"+\"]")
    tokens11 = ["0","3","+"]
    result11 = solution.evalRPN(tokens11)
    expected11 = 3  # 0 + 3 = 3
    print(f"Input: {tokens11}")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Boundary values
    print("Test 12: Boundary values [\"100\",\"-100\",\"+\"]")
    tokens12 = ["100","-100","+"]
    result12 = solution.evalRPN(tokens12)
    expected12 = 0  # 100 + (-100) = 0
    print(f"Input: {tokens12}")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Evaluate Reverse Polish Notation Problem Constraints:
- 1 <= tokens.length <= 1000
- tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100]
- Division between integers always truncates toward zero
"""

if __name__ == "__main__":
    test_evaluate_reverse_polish_notation() 