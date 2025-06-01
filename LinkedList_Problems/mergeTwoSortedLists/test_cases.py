from solution import Solution, ListNode, create_linked_list, linked_list_to_array

def test_merge_two_sorted_lists():
    solution = Solution()
    
    print("Testing Merge Two Sorted Linked Lists Solution...")
    print("=" * 50)
    
    # Test Case 1: Basic example [1,2,4] and [1,3,5] -> [1,1,2,3,4,5]
    print("Test 1: Basic example [1,2,4] and [1,3,5]")
    list1_1 = create_linked_list([1, 2, 4])
    list2_1 = create_linked_list([1, 3, 5])
    result1 = solution.mergeTwoLists(list1_1, list2_1)
    output1 = linked_list_to_array(result1)
    expected1 = [1, 1, 2, 3, 4, 5]
    print(f"Input: list1 = [1,2,4], list2 = [1,3,5]")
    print(f"Expected: {expected1}, Got: {output1}")
    print(f"✓ Passed: {output1 == expected1}\n")
    
    # Test Case 2: One empty list [] and [1,2] -> [1,2]
    print("Test 2: One empty list [] and [1,2]")
    list1_2 = create_linked_list([])
    list2_2 = create_linked_list([1, 2])
    result2 = solution.mergeTwoLists(list1_2, list2_2)
    output2 = linked_list_to_array(result2)
    expected2 = [1, 2]
    print(f"Input: list1 = [], list2 = [1,2]")
    print(f"Expected: {expected2}, Got: {output2}")
    print(f"✓ Passed: {output2 == expected2}\n")
    
    # Test Case 3: Both empty lists [] and [] -> []
    print("Test 3: Both empty lists [] and []")
    list1_3 = create_linked_list([])
    list2_3 = create_linked_list([])
    result3 = solution.mergeTwoLists(list1_3, list2_3)
    output3 = linked_list_to_array(result3)
    expected3 = []
    print(f"Input: list1 = [], list2 = []")
    print(f"Expected: {expected3}, Got: {output3}")
    print(f"✓ Passed: {output3 == expected3}\n")
    
    # Test Case 4: [5] and [] -> [5]
    print("Test 4: [5] and [] -> [5]")
    list1_4 = create_linked_list([5])
    list2_4 = create_linked_list([])
    result4 = solution.mergeTwoLists(list1_4, list2_4)
    output4 = linked_list_to_array(result4)
    expected4 = [5]
    print(f"Input: list1 = [5], list2 = []")
    print(f"Expected: {expected4}, Got: {output4}")
    print(f"✓ Passed: {output4 == expected4}\n")
    
    # Test Case 5: All elements from first list come first
    print("Test 5: All elements from first list come first [1,2,3] and [4,5,6]")
    list1_5 = create_linked_list([1, 2, 3])
    list2_5 = create_linked_list([4, 5, 6])
    result5 = solution.mergeTwoLists(list1_5, list2_5)
    output5 = linked_list_to_array(result5)
    expected5 = [1, 2, 3, 4, 5, 6]
    print(f"Input: list1 = [1,2,3], list2 = [4,5,6]")
    print(f"Expected: {expected5}, Got: {output5}")
    print(f"✓ Passed: {output5 == expected5}\n")
    
    # Test Case 6: All elements from second list come first
    print("Test 6: All elements from second list come first [4,5,6] and [1,2,3]")
    list1_6 = create_linked_list([4, 5, 6])
    list2_6 = create_linked_list([1, 2, 3])
    result6 = solution.mergeTwoLists(list1_6, list2_6)
    output6 = linked_list_to_array(result6)
    expected6 = [1, 2, 3, 4, 5, 6]
    print(f"Input: list1 = [4,5,6], list2 = [1,2,3]")
    print(f"Expected: {expected6}, Got: {output6}")
    print(f"✓ Passed: {output6 == expected6}\n")
    
    # Test Case 7: Single elements [1] and [2]
    print("Test 7: Single elements [1] and [2]")
    list1_7 = create_linked_list([1])
    list2_7 = create_linked_list([2])
    result7 = solution.mergeTwoLists(list1_7, list2_7)
    output7 = linked_list_to_array(result7)
    expected7 = [1, 2]
    print(f"Input: list1 = [1], list2 = [2]")
    print(f"Expected: {expected7}, Got: {output7}")
    print(f"✓ Passed: {output7 == expected7}\n")
    
    # Test Case 8: Negative numbers [-10, -5, 0] and [-8, -3, 2]
    print("Test 8: Negative numbers [-10,-5,0] and [-8,-3,2]")
    list1_8 = create_linked_list([-10, -5, 0])
    list2_8 = create_linked_list([-8, -3, 2])
    result8 = solution.mergeTwoLists(list1_8, list2_8)
    output8 = linked_list_to_array(result8)
    expected8 = [-10, -8, -5, -3, 0, 2]
    print(f"Input: list1 = [-10,-5,0], list2 = [-8,-3,2]")
    print(f"Expected: {expected8}, Got: {output8}")
    print(f"✓ Passed: {output8 == expected8}\n")
    
    # Test Case 9: Same values [1,3,5] and [1,3,5]
    print("Test 9: Same values [1,3,5] and [1,3,5]")
    list1_9 = create_linked_list([1, 3, 5])
    list2_9 = create_linked_list([1, 3, 5])
    result9 = solution.mergeTwoLists(list1_9, list2_9)
    output9 = linked_list_to_array(result9)
    expected9 = [1, 1, 3, 3, 5, 5]
    print(f"Input: list1 = [1,3,5], list2 = [1,3,5]")
    print(f"Expected: {expected9}, Got: {output9}")
    print(f"✓ Passed: {output9 == expected9}\n")
    
    # Test Case 10: Boundary values [-100] and [100]
    print("Test 10: Boundary values [-100] and [100]")
    list1_10 = create_linked_list([-100])
    list2_10 = create_linked_list([100])
    result10 = solution.mergeTwoLists(list1_10, list2_10)
    output10 = linked_list_to_array(result10)
    expected10 = [-100, 100]
    print(f"Input: list1 = [-100], list2 = [100]")
    print(f"Expected: {expected10}, Got: {output10}")
    print(f"✓ Passed: {output10 == expected10}\n")
    
    # Test Case 11: Different lengths [1,2,3,4,5] and [10,20]
    print("Test 11: Different lengths [1,2,3,4,5] and [10,20]")
    list1_11 = create_linked_list([1, 2, 3, 4, 5])
    list2_11 = create_linked_list([10, 20])
    result11 = solution.mergeTwoLists(list1_11, list2_11)
    output11 = linked_list_to_array(result11)
    expected11 = [1, 2, 3, 4, 5, 10, 20]
    print(f"Input: list1 = [1,2,3,4,5], list2 = [10,20]")
    print(f"Expected: {expected11}, Got: {output11}")
    print(f"✓ Passed: {output11 == expected11}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Merge Two Sorted Linked Lists Problem Constraints:
- 0 <= The length of each list <= 100
- -100 <= Node.val <= 100
- Both lists are sorted in non-decreasing order
"""

if __name__ == "__main__":
    test_merge_two_sorted_lists() 