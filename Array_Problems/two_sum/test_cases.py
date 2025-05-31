from solution import Solution

def test_two_sum():
    solution = Solution()
    
    print("Testing Two Sum Solution...")
    print("=" * 40)
    
    # Test Case 1: Basic example from LeetCode
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    expected1 = [0, 1]
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {sorted(result1) == sorted(expected1)}\n")
    
    # Test Case 2: Different order
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    expected2 = [1, 2]
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {sorted(result2) == sorted(expected2)}\n")
    
    # Test Case 3: Same number used twice
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    expected3 = [0, 1]
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {sorted(result3) == sorted(expected3)}\n")
    
    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = solution.twoSum(nums4, target4)
    expected4 = [2, 4]  # -3 + -5 = -8
    print(f"Test 4: nums={nums4}, target={target4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {sorted(result4) == sorted(expected4)}\n")
    
    # Test Case 5: Mixed positive and negative
    nums5 = [-3, 4, 3, 90]
    target5 = 0
    result5 = solution.twoSum(nums5, target5)
    expected5 = [0, 2]  # -3 + 3 = 0
    print(f"Test 5: nums={nums5}, target={target5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {sorted(result5) == sorted(expected5)}\n")
    
    # Test Case 6: Large numbers
    nums6 = [1000000000, 999999999, 1]
    target6 = 1999999999
    result6 = solution.twoSum(nums6, target6)
    expected6 = [0, 1]
    print(f"Test 6: nums={nums6}, target={target6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {sorted(result6) == sorted(expected6)}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Two Sum Problem Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9  
- -10^9 <= target <= 10^9
- Only one valid answer exists
- You may not use the same element twice
"""

if __name__ == "__main__":
    test_two_sum() 