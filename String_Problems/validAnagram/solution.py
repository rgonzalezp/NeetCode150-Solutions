class Solution:
    # Time complexity: O(N+M) - we need to go over all characters in both strings at least once. Additionally we go again over all keys of the dictionaries
    # Space complexity: O(1) - at most 26 unique characters each in both dictionaries (lowercase English letters only), otherwise the space complexity is O(N+M) for an arbitrary number of unique characters.
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_s = {}
        my_dict_t = {}

        for i in range(len(s)):
            if s[i] not in my_dict_s:
                my_dict_s[s[i]] = 1
            else:
                my_dict_s[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in my_dict_t:
                my_dict_t[t[i]] = 1
            else:
                my_dict_t[t[i]] += 1

        for key in my_dict_s:
            if key not in my_dict_t:
                return False
            else:
                if my_dict_t[key] != my_dict_s[key]:
                    return False
        for key in my_dict_t:
            if key not in my_dict_s:
                return False
            else:
                if my_dict_s[key] != my_dict_t[key]:
                    return False
        
        return True

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    s = "racecar"
    t = "carrace"
    result = solution.isAnagram(s, t)
    
    print(f"Input: s = '{s}', t = '{t}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print(f"Verification: {'✓ Correct' if result == True else '✗ Incorrect'}") 