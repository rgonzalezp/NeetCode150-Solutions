from solution import MinStack

def test_minimum_stack():
    print("Testing Minimum Stack Solution...")
    print("=" * 45)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    minStack1 = MinStack()
    minStack1.push(1)
    minStack1.push(2)
    minStack1.push(0)
    
    result1_1 = minStack1.getMin()  # Should be 0
    minStack1.pop()
    result1_2 = minStack1.top()     # Should be 2
    result1_3 = minStack1.getMin()  # Should be 1
    
    expected1 = [0, 2, 1]
    actual1 = [result1_1, result1_2, result1_3]
    print(f"Expected: {expected1}")
    print(f"Actual: {actual1}")
    print(f"✓ Passed: {actual1 == expected1}\n")
    
    # Test Case 2: Single element operations
    print("Test 2: Single element operations")
    minStack2 = MinStack()
    minStack2.push(5)
    
    result2_1 = minStack2.top()     # Should be 5
    result2_2 = minStack2.getMin()  # Should be 5
    minStack2.pop()
    # After pop, stack is empty (but we won't call operations on empty stack as per constraints)
    
    expected2 = [5, 5]
    actual2 = [result2_1, result2_2]
    print(f"Expected: {expected2}")
    print(f"Actual: {actual2}")
    print(f"✓ Passed: {actual2 == expected2}\n")
    
    # Test Case 3: Decreasing sequence
    print("Test 3: Decreasing sequence [5,4,3,2,1]")
    minStack3 = MinStack()
    sequence = [5, 4, 3, 2, 1]
    
    for val in sequence:
        minStack3.push(val)
    
    mins = []
    for i in range(len(sequence)):
        mins.append(minStack3.getMin())
        if i < len(sequence) - 1:  # Don't pop the last element
            minStack3.pop()
    
    expected3 = [1, 2, 3, 4, 5]  # Min should be current smallest as we pop
    print(f"Expected: {expected3}")
    print(f"Actual: {mins}")
    print(f"✓ Passed: {mins == expected3}\n")
    
    # Test Case 4: Increasing sequence
    print("Test 4: Increasing sequence [1,2,3,4,5]")
    minStack4 = MinStack()
    sequence4 = [1, 2, 3, 4, 5]
    
    for val in sequence4:
        minStack4.push(val)
    
    mins4 = []
    for i in range(len(sequence4)):
        mins4.append(minStack4.getMin())
        if i < len(sequence4) - 1:
            minStack4.pop()
    
    expected4 = [1, 1, 1, 1, 1]  # Min should always be 1
    print(f"Expected: {expected4}")
    print(f"Actual: {mins4}")
    print(f"✓ Passed: {mins4 == expected4}\n")
    
    # Test Case 5: Negative numbers
    print("Test 5: Negative numbers [-3, -1, -5, -2]")
    minStack5 = MinStack()
    sequence5 = [-3, -1, -5, -2]
    
    for val in sequence5:
        minStack5.push(val)
    
    result5_1 = minStack5.getMin()  # Should be -5
    minStack5.pop()  # Remove -2
    result5_2 = minStack5.getMin()  # Should be -5
    minStack5.pop()  # Remove -5
    result5_3 = minStack5.getMin()  # Should be -3
    
    expected5 = [-5, -5, -3]
    actual5 = [result5_1, result5_2, result5_3]
    print(f"Expected: {expected5}")
    print(f"Actual: {actual5}")
    print(f"✓ Passed: {actual5 == expected5}\n")
    
    # Test Case 6: Same values
    print("Test 6: Same values [3,3,3,3]")
    minStack6 = MinStack()
    
    for _ in range(4):
        minStack6.push(3)
    
    mins6 = []
    for i in range(4):
        mins6.append(minStack6.getMin())
        if i < 3:
            minStack6.pop()
    
    expected6 = [3, 3, 3, 3]
    print(f"Expected: {expected6}")
    print(f"Actual: {mins6}")
    print(f"✓ Passed: {mins6 == expected6}\n")
    
    # Test Case 7: Boundary values
    print("Test 7: Boundary values [-2^31, 2^31-1]")
    minStack7 = MinStack()
    min_val = -2**31
    max_val = 2**31 - 1
    
    minStack7.push(max_val)
    minStack7.push(min_val)
    
    result7_1 = minStack7.getMin()  # Should be min_val
    result7_2 = minStack7.top()     # Should be min_val
    minStack7.pop()
    result7_3 = minStack7.getMin()  # Should be max_val
    result7_4 = minStack7.top()     # Should be max_val
    
    expected7 = [min_val, min_val, max_val, max_val]
    actual7 = [result7_1, result7_2, result7_3, result7_4]
    print(f"Expected: {expected7}")
    print(f"Actual: {actual7}")
    print(f"✓ Passed: {actual7 == expected7}\n")
    
    # Test Case 8: Mixed operations
    print("Test 8: Mixed operations")
    minStack8 = MinStack()
    
    minStack8.push(10)
    minStack8.push(5)
    result8_1 = minStack8.getMin()  # 5
    minStack8.push(15)
    result8_2 = minStack8.getMin()  # 5
    minStack8.push(2)
    result8_3 = minStack8.getMin()  # 2
    minStack8.pop()  # Remove 2
    result8_4 = minStack8.getMin()  # 5
    minStack8.pop()  # Remove 15
    result8_5 = minStack8.getMin()  # 5
    
    expected8 = [5, 5, 2, 5, 5]
    actual8 = [result8_1, result8_2, result8_3, result8_4, result8_5]
    print(f"Expected: {expected8}")
    print(f"Actual: {actual8}")
    print(f"✓ Passed: {actual8 == expected8}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Minimum Stack Problem Constraints:
- -2^31 <= val <= 2^31 - 1
- pop, top and getMin will always be called on non-empty stacks
- Each function should run in O(1) time
"""

if __name__ == "__main__":
    test_minimum_stack() 