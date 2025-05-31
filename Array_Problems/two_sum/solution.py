from typing import List

class Solution:

    # Time complexity: O(nsquared) - Two for loops, checking all pairs
    # Space complexity: O(1) - no variables stored
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j-1]+ nums[i] == target and (j-1) != i:
                    if i < j-1:
                        
                        return [i,j-1]
                    else:
                        
                        return [j-1,i]

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Verification: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}") 