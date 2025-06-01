from solution import Solution, ListNode, create_linked_list, linked_list_to_array

def test_reverse_linked_list():
    solution = Solution()
    
    print("Testing Reverse Linked List Solution...")
    print("=" * 40)
    
    # Test Case 1: Basic example [0,1,2,3] -> [3,2,1,0]
    print("Test 1: Basic example [0,1,2,3]")
    input1 = [0, 1, 2, 3]
    head1 = create_linked_list(input1)
    result1 = solution.reverseList(head1)
    output1 = linked_list_to_array(result1)
    expected1 = [3, 2, 1, 0]
    print(f"Input: {input1}")
    print(f"Expected: {expected1}, Got: {output1}")
    print(f"✓ Passed: {output1 == expected1}\n")
    
    # Test Case 2: Empty list [] -> []
    print("Test 2: Empty list")
    input2 = []
    head2 = create_linked_list(input2)
    result2 = solution.reverseList(head2)
    output2 = linked_list_to_array(result2)
    expected2 = []
    print(f"Input: {input2}")
    print(f"Expected: {expected2}, Got: {output2}")
    print(f"✓ Passed: {output2 == expected2}\n")
    
    # Test Case 3: Single element [1] -> [1]
    print("Test 3: Single element")
    input3 = [1]
    head3 = create_linked_list(input3)
    result3 = solution.reverseList(head3)
    output3 = linked_list_to_array(result3)
    expected3 = [1]
    print(f"Input: {input3}")
    print(f"Expected: {expected3}, Got: {output3}")
    print(f"✓ Passed: {output3 == expected3}\n")
    
    # Test Case 4: Two elements [1,2] -> [2,1]
    print("Test 4: Two elements")
    input4 = [1, 2]
    head4 = create_linked_list(input4)
    result4 = solution.reverseList(head4)
    output4 = linked_list_to_array(result4)
    expected4 = [2, 1]
    print(f"Input: {input4}")
    print(f"Expected: {expected4}, Got: {output4}")
    print(f"✓ Passed: {output4 == expected4}\n")
    
    # Test Case 5: Negative numbers [-1,-2,-3] -> [-3,-2,-1]
    print("Test 5: Negative numbers")
    input5 = [-1, -2, -3]
    head5 = create_linked_list(input5)
    result5 = solution.reverseList(head5)
    output5 = linked_list_to_array(result5)
    expected5 = [-3, -2, -1]
    print(f"Input: {input5}")
    print(f"Expected: {expected5}, Got: {output5}")
    print(f"✓ Passed: {output5 == expected5}\n")
    
    # Test Case 6: Mixed positive and negative [1,-2,3,-4]
    print("Test 6: Mixed positive and negative")
    input6 = [1, -2, 3, -4]
    head6 = create_linked_list(input6)
    result6 = solution.reverseList(head6)
    output6 = linked_list_to_array(result6)
    expected6 = [-4, 3, -2, 1]
    print(f"Input: {input6}")
    print(f"Expected: {expected6}, Got: {output6}")
    print(f"✓ Passed: {output6 == expected6}\n")
    
    # Test Case 7: Longer list [1,2,3,4,5,6,7]
    print("Test 7: Longer list")
    input7 = [1, 2, 3, 4, 5, 6, 7]
    head7 = create_linked_list(input7)
    result7 = solution.reverseList(head7)
    output7 = linked_list_to_array(result7)
    expected7 = [7, 6, 5, 4, 3, 2, 1]
    print(f"Input: {input7}")
    print(f"Expected: {expected7}, Got: {output7}")
    print(f"✓ Passed: {output7 == expected7}\n")
    
    # Test Case 8: All same values [5,5,5,5]
    print("Test 8: All same values")
    input8 = [5, 5, 5, 5]
    head8 = create_linked_list(input8)
    result8 = solution.reverseList(head8)
    output8 = linked_list_to_array(result8)
    expected8 = [5, 5, 5, 5]
    print(f"Input: {input8}")
    print(f"Expected: {expected8}, Got: {output8}")
    print(f"✓ Passed: {output8 == expected8}\n")
    
    # Test Case 9: Boundary values [-1000, 1000]
    print("Test 9: Boundary values")
    input9 = [-1000, 1000]
    head9 = create_linked_list(input9)
    result9 = solution.reverseList(head9)
    output9 = linked_list_to_array(result9)
    expected9 = [1000, -1000]
    print(f"Input: {input9}")
    print(f"Expected: {expected9}, Got: {output9}")
    print(f"✓ Passed: {output9 == expected9}\n")
    
    # Test Case 10: Maximum length (close to constraint limit)
    print("Test 10: Larger list (10 elements)")
    input10 = list(range(10))  # [0,1,2,3,4,5,6,7,8,9]
    head10 = create_linked_list(input10)
    result10 = solution.reverseList(head10)
    output10 = linked_list_to_array(result10)
    expected10 = list(range(9, -1, -1))  # [9,8,7,6,5,4,3,2,1,0]
    print(f"Input: {input10}")
    print(f"Expected: {expected10}, Got: {output10}")
    print(f"✓ Passed: {output10 == expected10}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Reverse Linked List Problem Constraints:
- 0 <= The length of the list <= 1000
- -1000 <= Node.val <= 1000
"""

if __name__ == "__main__":
    test_reverse_linked_list() 