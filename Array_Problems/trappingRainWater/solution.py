from typing import List

class Solution:
    # Time Complexity: O(n) where n is the size of height. We just need to iterate the array 3 times at most to find the solution
    # One time from left to right, one time from right to left, and one time to calculate the water trapped on each cel
    # Space Complexity: O(n) where n is the size of height. We need to store n prefixes and n suffixes.
    def trap(self, height: List[int]) -> int:

        total = 0

        suffix = [-1] * len(height)
        preffix = [-1] * len(height)

        # Prefix calculation
        preffixTop = -1
        for i,h in enumerate(height):
            preffix[i] = preffixTop 
            if(h > preffixTop):
                preffixTop = h
             

        # Suffix calculation
        suffixTop = -1
        size = len(height)
        for i,h in enumerate(reversed(height)):   
            orig_i = size - 1 - i 
            suffix[orig_i] = suffixTop 
            if(h > suffixTop):
                suffixTop = h
            

        for i in range(len(height)):
 
            calc = min(suffix[i],preffix[i]) - height[i]

            if calc > 0:
                 total = calc + total

        return total

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Trapping Rain Water...")
    print("=" * 35)
    
    # Test case 1: [0,2,0,3,1,0,1,3,2,1] -> 9
    height = [0,2,0,3,1,0,1,3,2,1]
    result = solution.trap(height)
    
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 9")
    print(f"Verification: {'✓ Correct' if result == 9 else '✗ Incorrect'}")
    
    # Visualize the solution
    print("\nVisualization:")
    print("Heights: ", height)
    print("Water trapped at each position:")
    
    # Recalculate to show water at each position
    suffix = [-1] * len(height)
    preffix = [-1] * len(height)
    
    preffixTop = -1
    for i, h in enumerate(height):
        preffix[i] = preffixTop 
        if h > preffixTop:
            preffixTop = h
    
    suffixTop = -1
    size = len(height)
    for i, h in enumerate(reversed(height)):   
        orig_i = size - 1 - i 
        suffix[orig_i] = suffixTop 
        if h > suffixTop:
            suffixTop = h
    
    for i in range(len(height)):
        calc = min(suffix[i], preffix[i]) - height[i]
        water = max(0, calc)
        print(f"Position {i}: height={height[i]}, water={water}") 