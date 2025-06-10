#Time complexity: O(n) where n is the length of the string s. We only need to do one main pass through the string to identify the longest "unique" substring within our string.
#Space complexity: O(1) because it is a fixed amount of characters. The maximum is all the possible printable ASCII characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentDict = set()
        bestLength = 0
        initPointer = 0
        endPointer = 0
        while endPointer < len(s):

            if s[endPointer] not in currentDict:
                currentDict.add(s[endPointer])
                if len(currentDict) > bestLength:
                    bestLength = len(currentDict)
            elif s[endPointer] in currentDict:
                while s[endPointer] in currentDict:
                    currentDict.remove(s[initPointer])
                    initPointer+=1
                currentDict.add(s[endPointer])
            endPointer+= 1

        if len(currentDict) > bestLength:
            bestLength = len(currentDict)
        return bestLength

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Longest Substring Without Repeating Characters...")
    print("=" * 55)
    
    # Test case 1: s = "zxyzxyz" -> 3
    s = "zxyzxyz"
    result = solution.lengthOfLongestSubstring(s)
    
    print(f"Input: s = \"{s}\"")
    print(f"Output: {result}")
    print(f"Expected: 3")
    print(f"Explanation: The substring \"xyz\" is the longest without duplicate characters")
    print(f"Verification: {'✓ Correct' if result == 3 else '✗ Incorrect'}")
    
    # Test case 2: s = "xxxx" -> 1
    print(f"\nInput: s = \"xxxx\"")
    s2 = "xxxx"
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Explanation: The longest substring is \"x\" with length 1")
    print(f"Verification: {'✓ Correct' if result2 == 1 else '✗ Incorrect'}") 