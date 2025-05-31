from typing import List

class Solution:
    # Time complexity: O(n) - at worst we have to check all values and either find no duplicates, or find a duplicate at the end
    # Space complexity: O(n) - at worst we have to store all values (if they are all unique)
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    nums = [1, 2, 3, 3]
    result = solution.hasDuplicate(nums)
    
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print(f"Verification: {'✓ Correct' if result == True else '✗ Incorrect'}") 