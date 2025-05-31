from solution import Solution

def test_contains_duplicate():
    solution = Solution()
    
    print("Testing Contains Duplicate Solution...")
    print("=" * 45)
    
    # Test Case 1: Basic example with duplicates
    nums1 = [1, 2, 3, 3]
    result1 = solution.hasDuplicate(nums1)
    expected1 = True
    print(f"Test 1: nums = {nums1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    result2 = solution.hasDuplicate(nums2)
    expected2 = False
    print(f"Test 2: nums = {nums2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Single element (edge case)
    nums3 = [1]
    result3 = solution.hasDuplicate(nums3)
    expected3 = False
    print(f"Test 3: nums = {nums3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Two identical elements
    nums4 = [1, 1]
    result4 = solution.hasDuplicate(nums4)
    expected4 = True
    print(f"Test 4: nums = {nums4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Negative numbers with duplicates
    nums5 = [-1, -2, -3, -1]
    result5 = solution.hasDuplicate(nums5)
    expected5 = True
    print(f"Test 5: nums = {nums5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Large array with no duplicates
    nums6 = list(range(1000))  # [0, 1, 2, ..., 999]
    result6 = solution.hasDuplicate(nums6)
    expected6 = False
    print(f"Test 6: nums = [0, 1, 2, ..., 999] (1000 elements)")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Large array with duplicates at the end
    nums7 = list(range(1000)) + [999]  # [0, 1, 2, ..., 999, 999]
    result7 = solution.hasDuplicate(nums7)
    expected7 = True
    print(f"Test 7: nums = [0, 1, 2, ..., 999, 999] (1001 elements)")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Mixed positive and negative numbers
    nums8 = [1, -1, 2, -2, 3, -3, 4, -4, 1]
    result8 = solution.hasDuplicate(nums8)
    expected8 = True
    print(f"Test 8: nums = {nums8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Zero with duplicates
    nums9 = [0, 1, 2, 0]
    result9 = solution.hasDuplicate(nums9)
    expected9 = True
    print(f"Test 9: nums = {nums9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Contains Duplicate Problem Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

if __name__ == "__main__":
    test_contains_duplicate() 