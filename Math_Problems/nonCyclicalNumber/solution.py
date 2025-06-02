# Time complexity: O(log n) where n is the input number
# Space complexity: O(1) - bounded by the finite set of possible intermediate values
class Solution:
    def isHappy(self, n: int) -> bool:


        foundCycle = False

        foundNumbs = {}

        currentNumber = n

        while not foundCycle:

            currentSum = 0

            while currentNumber>0:

                currentSum = currentSum + ((currentNumber % 10)**2)

                currentNumber = currentNumber // 10
            
            if currentSum == 1:
                return True
            else:
                if currentSum in foundNumbs:
                    foundCycle = True
                else:
                    foundNumbs[currentSum] = 0
                    currentNumber = currentSum
        
        return False

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Non-Cyclical Number (Happy Number)...")
    print("=" * 45)
    
    # Test case 1: n = 100 -> True
    n = 100
    result = solution.isHappy(n)
    
    print(f"Input: n = {n}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print(f"Explanation: 1² + 0² + 0² = 1")
    print(f"Verification: {'✓ Correct' if result == True else '✗ Incorrect'}")
    
    # Test case 2: n = 101 -> False
    print(f"\nInput: n = 101")
    result2 = solution.isHappy(101)
    print(f"Output: {result2}")
    print(f"Expected: False")
    print(f"Explanation: 1² + 0² + 1² = 2 → 2² = 4 → 4² = 16 → 1² + 6² = 37 → ... → cycle detected")
    print(f"Verification: {'✓ Correct' if result2 == False else '✗ Incorrect'}") 