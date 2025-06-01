from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n) - We need to go through the entire list to update the pointers
    # Space complexity: O(1) - We do not store any additional data to tackle the problem
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        if current == None:
            return head
        nextObject = current
        previousObject = None

        while nextObject != None:

            if current.next is not None:
                nextObject = current.next
                current.next = previousObject
                previousObject = current
                current = nextObject
            else:
                nextObject = None
            
        current.next = previousObject
        return current

# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Reverse Linked List...")
    print("=" * 30)
    
    # Test case 1: [0,1,2,3] -> [3,2,1,0]
    input_arr = [0, 1, 2, 3]
    head = create_linked_list(input_arr)
    
    print(f"Input: {input_arr}")
    
    reversed_head = solution.reverseList(head)
    output_arr = linked_list_to_array(reversed_head)
    
    print(f"Output: {output_arr}")
    print(f"Expected: [3, 2, 1, 0]")
    print(f"Verification: {'✓ Correct' if output_arr == [3, 2, 1, 0] else '✗ Incorrect'}") 