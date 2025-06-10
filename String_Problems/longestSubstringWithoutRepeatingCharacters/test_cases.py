from solution import Solution

def test_longest_substring_without_repeating_characters():
    solution = Solution()
    
    print("Testing Longest Substring Without Repeating Characters Solution...")
    print("=" * 65)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example \"zxyzxyz\"")
    s1 = "zxyzxyz"
    result1 = solution.lengthOfLongestSubstring(s1)
    expected1 = 3
    print(f"Input: \"{s1}\"")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Explanation: \"xyz\" is the longest substring without repeating characters")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: All same characters
    print("Test 2: All same characters \"xxxx\"")
    s2 = "xxxx"
    result2 = solution.lengthOfLongestSubstring(s2)
    expected2 = 1
    print(f"Input: \"{s2}\"")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Explanation: \"x\" is the longest substring")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Empty string
    print("Test 3: Empty string \"\"")
    s3 = ""
    result3 = solution.lengthOfLongestSubstring(s3)
    expected3 = 0
    print(f"Input: \"{s3}\"")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Explanation: Empty string has no characters")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Single character
    print("Test 4: Single character \"a\"")
    s4 = "a"
    result4 = solution.lengthOfLongestSubstring(s4)
    expected4 = 1
    print(f"Input: \"{s4}\"")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Explanation: Single character has length 1")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: All unique characters
    print("Test 5: All unique characters \"abcdef\"")
    s5 = "abcdef"
    result5 = solution.lengthOfLongestSubstring(s5)
    expected5 = 6
    print(f"Input: \"{s5}\"")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Explanation: All characters are unique")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Palindrome pattern
    print("Test 6: Palindrome pattern \"abccba\"")
    s6 = "abccba"
    result6 = solution.lengthOfLongestSubstring(s6)
    expected6 = 3
    print(f"Input: \"{s6}\"")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Explanation: \"abc\" or \"cb\" are longest substrings")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Numbers and letters
    print("Test 7: Numbers and letters \"a1b2c3a\"")
    s7 = "a1b2c3a"
    result7 = solution.lengthOfLongestSubstring(s7)
    expected7 = 6
    print(f"Input: \"{s7}\"")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Explanation: \"1b2c3a\" is the longest substring")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Special characters
    print("Test 8: Special characters \"a!@#a\"")
    s8 = "a!@#a"
    result8 = solution.lengthOfLongestSubstring(s8)
    expected8 = 4
    print(f"Input: \"{s8}\"")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Explanation: \"!@#a\" is the longest substring")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Repeated pattern
    print("Test 9: Repeated pattern \"abcabcbb\"")
    s9 = "abcabcbb"
    result9 = solution.lengthOfLongestSubstring(s9)
    expected9 = 3
    print(f"Input: \"{s9}\"")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Explanation: \"abc\" is the longest substring")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Spaces and characters
    print("Test 10: Spaces and characters \"a b c a\"")
    s10 = "a b c a"
    result10 = solution.lengthOfLongestSubstring(s10)
    expected10 = 4
    print(f"Input: \"{s10}\"")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Explanation: \"b c a\" or \"a b c\" is the longest substring")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Long string with pattern
    print("Test 11: Long string \"pwwkew\"")
    s11 = "pwwkew"
    result11 = solution.lengthOfLongestSubstring(s11)
    expected11 = 3
    print(f"Input: \"{s11}\"")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"Explanation: \"wke\" is the longest substring")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Boundary case - maximum length
    print("Test 12: Mixed case \"ABCDEFGabcdefg123!@#\"")
    s12 = "ABCDEFGabcdefg123!@#"
    result12 = solution.lengthOfLongestSubstring(s12)
    expected12 = 20
    print(f"Input: \"{s12}\"")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"Explanation: All characters are unique")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Longest Substring Without Repeating Characters Problem Constraints:
- 0 <= s.length <= 1000
- s may consist of printable ASCII characters
"""

if __name__ == "__main__":
    test_longest_substring_without_repeating_characters() 