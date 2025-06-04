from solution import Solution

def verify_anagram_groups(result):
    """Helper function to verify that each group contains only anagrams"""
    for group in result:
        if len(group) > 1:
            # Check if all words in the group are anagrams
            sorted_chars = ["".join(sorted(word)) for word in group]
            if not all(chars == sorted_chars[0] for chars in sorted_chars):
                return False
    return True

def test_group_anagrams():
    solution = Solution()
    
    print("Testing Group Anagrams Solution...")
    print("=" * 40)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example [\"act\",\"pots\",\"tops\",\"cat\",\"stop\",\"hat\"]")
    strs1 = ["act","pots","tops","cat","stop","hat"]
    result1 = solution.groupAnagrams(strs1)
    print(f"Input: {strs1}")
    print(f"Output: {result1}")
    print(f"✓ Passed: {verify_anagram_groups(result1) and len(result1) == 3}\n")
    
    # Test Case 2: Single string
    print("Test 2: Single string [\"x\"]")
    strs2 = ["x"]
    result2 = solution.groupAnagrams(strs2)
    expected2 = [["x"]]
    print(f"Input: {strs2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Empty string
    print("Test 3: Empty string [\"\"]")
    strs3 = [""]
    result3 = solution.groupAnagrams(strs3)
    expected3 = [[""]]
    print(f"Input: {strs3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: All strings are anagrams
    print("Test 4: All strings are anagrams [\"abc\",\"bca\",\"cab\"]")
    strs4 = ["abc","bca","cab"]
    result4 = solution.groupAnagrams(strs4)
    print(f"Input: {strs4}")
    print(f"Output: {result4}")
    print(f"✓ Passed: {verify_anagram_groups(result4) and len(result4) == 1}\n")
    
    # Test Case 5: No anagrams (all unique)
    print("Test 5: No anagrams [\"a\",\"b\",\"c\"]")
    strs5 = ["a","b","c"]
    result5 = solution.groupAnagrams(strs5)
    print(f"Input: {strs5}")
    print(f"Output: {result5}")
    print(f"✓ Passed: {verify_anagram_groups(result5) and len(result5) == 3}\n")
    
    # Test Case 6: Mixed empty and non-empty strings
    print("Test 6: Mixed empty and non-empty [\"\",\"a\",\"\"]")
    strs6 = ["","a",""]
    result6 = solution.groupAnagrams(strs6)
    print(f"Input: {strs6}")
    print(f"Output: {result6}")
    print(f"✓ Passed: {verify_anagram_groups(result6) and len(result6) == 2}\n")
    
    # Test Case 7: Single character anagrams
    print("Test 7: Single character anagrams [\"a\",\"a\",\"a\"]")
    strs7 = ["a","a","a"]
    result7 = solution.groupAnagrams(strs7)
    print(f"Input: {strs7}")
    print(f"Output: {result7}")
    print(f"✓ Passed: {verify_anagram_groups(result7) and len(result7) == 1}\n")
    
    # Test Case 8: Different length strings
    print("Test 8: Different length strings [\"ab\",\"ba\",\"abc\",\"bca\"]")
    strs8 = ["ab","ba","abc","bca"]
    result8 = solution.groupAnagrams(strs8)
    print(f"Input: {strs8}")
    print(f"Output: {result8}")
    print(f"✓ Passed: {verify_anagram_groups(result8) and len(result8) == 2}\n")
    
    # Test Case 9: Longer anagrams
    print("Test 9: Longer anagrams [\"listen\",\"silent\",\"hello\",\"world\"]")
    strs9 = ["listen","silent","hello","world"]
    result9 = solution.groupAnagrams(strs9)
    print(f"Input: {strs9}")
    print(f"Output: {result9}")
    print(f"✓ Passed: {verify_anagram_groups(result9) and len(result9) == 3}\n")
    
    # Test Case 10: Repeated characters
    print("Test 10: Repeated characters [\"aab\",\"aba\",\"baa\",\"ab\"]")
    strs10 = ["aab","aba","baa","ab"]
    result10 = solution.groupAnagrams(strs10)
    print(f"Input: {strs10}")
    print(f"Output: {result10}")
    print(f"✓ Passed: {verify_anagram_groups(result10) and len(result10) == 2}\n")
    
    # Test Case 11: Case sensitivity (all lowercase as per constraints)
    print("Test 11: All lowercase [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]")
    strs11 = ["eat","tea","tan","ate","nat","bat"]
    result11 = solution.groupAnagrams(strs11)
    print(f"Input: {strs11}")
    print(f"Output: {result11}")
    print(f"✓ Passed: {verify_anagram_groups(result11) and len(result11) == 3}\n")
    
    # Test Case 12: Maximum length strings (boundary test)
    print("Test 12: Boundary test with longer strings")
    strs12 = ["abcdefghij","jihgfedcba","hello","olleh"]
    result12 = solution.groupAnagrams(strs12)
    print(f"Input: {strs12}")
    print(f"Output: {result12}")
    print(f"✓ Passed: {verify_anagram_groups(result12) and len(result12) == 3}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Group Anagrams Problem Constraints:
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters
"""

if __name__ == "__main__":
    test_group_anagrams() 