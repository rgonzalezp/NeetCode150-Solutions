from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity O(n+m) for the size of each list because we have to go over both lists at worst. N is the size of the first list and M is the size of the second list
# Space O(n+m) because we are merging two lists. N is the size of the first list and M is the size of the second list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        l1 = list1
        l2 = list2
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if list1.val <= list2.val:
            head = list1
            if list1 is not None:
                l1 = list1.next
        else:
            head = list2
            if list2 is not None:
                l2 = list2.next

        

        current = head
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
        
        if l1 is None:
            while l2 is not None:
                current.next = l2
                current = current.next
                l2 = l2.next
        elif l2 is None:
            while l1 is not None:
                current.next = l1
                current = current.next
                l1 = l1.next


        return head

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
    print("Testing Merge Two Sorted Linked Lists...")
    print("=" * 40)
    
    # Test case 1: [1,2,4] and [1,3,5] -> [1,1,2,3,4,5]
    list1_arr = [1, 2, 4]
    list2_arr = [1, 3, 5]
    
    list1 = create_linked_list(list1_arr)
    list2 = create_linked_list(list2_arr)
    
    print(f"Input: list1 = {list1_arr}, list2 = {list2_arr}")
    
    merged = solution.mergeTwoLists(list1, list2)
    output_arr = linked_list_to_array(merged)
    
    print(f"Output: {output_arr}")
    print(f"Expected: [1, 1, 2, 3, 4, 5]")
    print(f"Verification: {'✓ Correct' if output_arr == [1, 1, 2, 3, 4, 5] else '✗ Incorrect'}") 