from solution import Solution

def test_trapping_rain_water():
    solution = Solution()
    
    print("Testing Trapping Rain Water Solution...")
    print("=" * 45)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example [0,2,0,3,1,0,1,3,2,1]")
    height1 = [0,2,0,3,1,0,1,3,2,1]
    result1 = solution.trap(height1)
    expected1 = 9
    print(f"Input: {height1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: No water can be trapped
    print("Test 2: Increasing heights [1,2,3,4,5]")
    height2 = [1,2,3,4,5]
    result2 = solution.trap(height2)
    expected2 = 0
    print(f"Input: {height2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Decreasing heights
    print("Test 3: Decreasing heights [5,4,3,2,1]")
    height3 = [5,4,3,2,1]
    result3 = solution.trap(height3)
    expected3 = 0
    print(f"Input: {height3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Single element
    print("Test 4: Single element [5]")
    height4 = [5]
    result4 = solution.trap(height4)
    expected4 = 0
    print(f"Input: {height4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Two elements
    print("Test 5: Two elements [3,2]")
    height5 = [3,2]
    result5 = solution.trap(height5)
    expected5 = 0
    print(f"Input: {height5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Perfect valley
    print("Test 6: Perfect valley [3,0,2,0,4]")
    height6 = [3,0,2,0,4]
    result6 = solution.trap(height6)
    expected6 = 7  # 3+1+2+1 = 7
    print(f"Input: {height6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: All zeros
    print("Test 7: All zeros [0,0,0,0]")
    height7 = [0,0,0,0]
    result7 = solution.trap(height7)
    expected7 = 0
    print(f"Input: {height7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Flat plateau
    print("Test 8: Flat plateau [5,5,5,5]")
    height8 = [5,5,5,5]
    result8 = solution.trap(height8)
    expected8 = 0
    print(f"Input: {height8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Multiple peaks
    print("Test 9: Multiple peaks [4,2,0,3,2,5]")
    height9 = [4,2,0,3,2,5]
    result9 = solution.trap(height9)
    expected9 = 9  # 0+1+3+0+1+0 = 5, let me recalculate: at pos 1: min(4,5)-2=2, pos 2: min(4,5)-0=4, pos 3: min(4,5)-3=1, pos 4: min(4,5)-2=2, total = 2+4+1+2=9
    print(f"Input: {height9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Valley at the beginning
    print("Test 10: Valley at beginning [0,1,0,2,1,0,1,3,2,1,2,1]")
    height10 = [0,1,0,2,1,0,1,3,2,1,2,1]
    result10 = solution.trap(height10)
    expected10 = 6  # This needs manual calculation
    print(f"Input: {height10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Valley at the end
    print("Test 11: Valley at end [3,2,1,2,0]")
    height11 = [3,2,1,2,0]
    result11 = solution.trap(height11)
    expected11 = 1  # Only position 3 can trap: min(3,2)-1=1
    print(f"Input: {height11}")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Boundary values (max height)
    print("Test 12: Boundary values [1000,0,1000]")
    height12 = [1000,0,1000]
    result12 = solution.trap(height12)
    expected12 = 1000
    print(f"Input: {height12}")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Trapping Rain Water Problem Constraints:
- 1 <= height.length <= 1000
- 0 <= height[i] <= 1000
"""

if __name__ == "__main__":
    test_trapping_rain_water() 