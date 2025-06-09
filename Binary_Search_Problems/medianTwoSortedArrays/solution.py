from typing import List

class Solution:
    #Time Complexity: O(n+m) where n is the size of one list and m is the size of the other list.
    # build an ordered list in O(n+m) using two pointers, adding smaller items and advancing through the corresponding array. 
    #Space Complexity: O(n+m) because we only have pointers and a newly formed list that is the size of the two lists we need to explore
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArrayOrdered = []

        pointer1 = 0
        pointer2 = 0
        #Append numbers as we can until we reach the end of one of the two list
        while pointer1< len(nums1) and pointer2< len(nums2):

            if(nums1[pointer1]<= nums2[pointer2]):
                newArrayOrdered.append(nums1[pointer1])
                pointer1+=1
            else:
                newArrayOrdered.append(nums2[pointer2])
                pointer2+=1

        #Append unfinished list to the end
        if pointer1< len(nums1):
            #append rest
            while pointer1< len(nums1):
                newArrayOrdered.append(nums1[pointer1])
                pointer1+=1
        elif pointer2< len(nums2):
            #append rest
            while pointer2< len(nums2):
                newArrayOrdered.append(nums2[pointer2])
                pointer2+=1
            



        #Get the number in the center if uneven. Get the two numbers in the center if even and /2

        if len(newArrayOrdered) % 2 == 0:
            return (newArrayOrdered[len(newArrayOrdered)//2] + newArrayOrdered[(len(newArrayOrdered)//2)-1])/2
        else:
            return newArrayOrdered[((len(newArrayOrdered)-1)//2)]

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Median of Two Sorted Arrays...")
    print("=" * 40)
    
    # Test case 1: nums1 = [1,2], nums2 = [3] -> 2.0
    nums1 = [1, 2]
    nums2 = [3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")
    print(f"Expected: 2.0")
    print(f"Verification: {'✓ Correct' if result == 2.0 else '✗ Incorrect'}")
    
    # Test case 2: nums1 = [1,3], nums2 = [2,4] -> 2.5
    print(f"\nInput: nums1 = [1,3], nums2 = [2,4]")
    nums1_2 = [1, 3]
    nums2_2 = [2, 4]
    result2 = solution.findMedianSortedArrays(nums1_2, nums2_2)
    print(f"Output: {result2}")
    print(f"Expected: 2.5")
    print(f"Explanation: Merged array [1,2,3,4], median = (2+3)/2 = 2.5")
    print(f"Verification: {'✓ Correct' if result2 == 2.5 else '✗ Incorrect'}") 