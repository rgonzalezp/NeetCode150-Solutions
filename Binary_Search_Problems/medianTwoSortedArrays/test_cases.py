from solution import Solution

def test_median_two_sorted_arrays():
    solution = Solution()
    
    print("Testing Median of Two Sorted Arrays Solution...")
    print("=" * 50)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example nums1=[1,2], nums2=[3]")
    nums1_1 = [1, 2]
    nums2_1 = [3]
    result1 = solution.findMedianSortedArrays(nums1_1, nums2_1)
    expected1 = 2.0
    print(f"Input: nums1={nums1_1}, nums2={nums2_1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: Even total length
    print("Test 2: Even total length nums1=[1,3], nums2=[2,4]")
    nums1_2 = [1, 3]
    nums2_2 = [2, 4]
    result2 = solution.findMedianSortedArrays(nums1_2, nums2_2)
    expected2 = 2.5
    print(f"Input: nums1={nums1_2}, nums2={nums2_2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: One empty array
    print("Test 3: One empty array nums1=[], nums2=[1,2,3,4]")
    nums1_3 = []
    nums2_3 = [1, 2, 3, 4]
    result3 = solution.findMedianSortedArrays(nums1_3, nums2_3)
    expected3 = 2.5
    print(f"Input: nums1={nums1_3}, nums2={nums2_3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Other empty array
    print("Test 4: Other empty array nums1=[1,2,3], nums2=[]")
    nums1_4 = [1, 2, 3]
    nums2_4 = []
    result4 = solution.findMedianSortedArrays(nums1_4, nums2_4)
    expected4 = 2.0
    print(f"Input: nums1={nums1_4}, nums2={nums2_4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Single elements
    print("Test 5: Single elements nums1=[1], nums2=[2]")
    nums1_5 = [1]
    nums2_5 = [2]
    result5 = solution.findMedianSortedArrays(nums1_5, nums2_5)
    expected5 = 1.5
    print(f"Input: nums1={nums1_5}, nums2={nums2_5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Identical arrays
    print("Test 6: Identical arrays nums1=[1,2,3], nums2=[1,2,3]")
    nums1_6 = [1, 2, 3]
    nums2_6 = [1, 2, 3]
    result6 = solution.findMedianSortedArrays(nums1_6, nums2_6)
    expected6 = 2.0
    print(f"Input: nums1={nums1_6}, nums2={nums2_6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Different sizes
    print("Test 7: Different sizes nums1=[1,3,8], nums2=[7,9,10,11]")
    nums1_7 = [1, 3, 8]
    nums2_7 = [7, 9, 10, 11]
    result7 = solution.findMedianSortedArrays(nums1_7, nums2_7)
    expected7 = 8.0  # Merged: [1,3,7,8,9,10,11], median is 8
    print(f"Input: nums1={nums1_7}, nums2={nums2_7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Negative numbers
    print("Test 8: Negative numbers nums1=[-5,-3,-1], nums2=[-2,0,4]")
    nums1_8 = [-5, -3, -1]
    nums2_8 = [-2, 0, 4]
    result8 = solution.findMedianSortedArrays(nums1_8, nums2_8)
    expected8 = -1.5  # Merged: [-5,-3,-2,-1,0,4], median = (-2 + -1)/2 = -1.5
    print(f"Input: nums1={nums1_8}, nums2={nums2_8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Large numbers
    print("Test 9: Large numbers nums1=[1000000], nums2=[999999]")
    nums1_9 = [1000000]
    nums2_9 = [999999]
    result9 = solution.findMedianSortedArrays(nums1_9, nums2_9)
    expected9 = 999999.5
    print(f"Input: nums1={nums1_9}, nums2={nums2_9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: All elements in one array smaller
    print("Test 10: All elements in first array smaller nums1=[1,2], nums2=[3,4]")
    nums1_10 = [1, 2]
    nums2_10 = [3, 4]
    result10 = solution.findMedianSortedArrays(nums1_10, nums2_10)
    expected10 = 2.5
    print(f"Input: nums1={nums1_10}, nums2={nums2_10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Overlapping ranges
    print("Test 11: Overlapping ranges nums1=[1,4,6], nums2=[2,3,5]")
    nums1_11 = [1, 4, 6]
    nums2_11 = [2, 3, 5]
    result11 = solution.findMedianSortedArrays(nums1_11, nums2_11)
    expected11 = 3.5  # Merged: [1,2,3,4,5,6], median = (3+4)/2 = 3.5
    print(f"Input: nums1={nums1_11}, nums2={nums2_11}")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Boundary values (constraints)
    print("Test 12: Boundary values nums1=[-1000000], nums2=[1000000]")
    nums1_12 = [-1000000]
    nums2_12 = [1000000]
    result12 = solution.findMedianSortedArrays(nums1_12, nums2_12)
    expected12 = 0.0
    print(f"Input: nums1={nums1_12}, nums2={nums2_12}")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Median of Two Sorted Arrays Problem Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

if __name__ == "__main__":
    test_median_two_sorted_arrays() 