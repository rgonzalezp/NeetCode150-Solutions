from solution import Solution

def test_valid_anagram():
    solution = Solution()
    
    print("Testing Valid Anagram Solution...")
    print("=" * 40)
    
    # Test Case 1: Basic example - valid anagram
    s1 = "racecar"
    t1 = "carrace"
    result1 = solution.isAnagram(s1, t1)
    expected1 = True
    print(f"Test 1: s = '{s1}', t = '{t1}'")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: Not an anagram - different characters
    s2 = "jar"
    t2 = "jam"
    result2 = solution.isAnagram(s2, t2)
    expected2 = False
    print(f"Test 2: s = '{s2}', t = '{t2}'")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Different lengths
    s3 = "hello"
    t3 = "bello"
    result3 = solution.isAnagram(s3, t3)
    expected3 = False
    print(f"Test 3: s = '{s3}', t = '{t3}'")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Same strings
    s4 = "listen"
    t4 = "listen"
    result4 = solution.isAnagram(s4, t4)
    expected4 = True
    print(f"Test 4: s = '{s4}', t = '{t4}'")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Empty strings
    s5 = ""
    t5 = ""
    result5 = solution.isAnagram(s5, t5)
    expected5 = True
    print(f"Test 5: s = '{s5}', t = '{t5}'")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Single character - anagram
    s6 = "a"
    t6 = "a"
    result6 = solution.isAnagram(s6, t6)
    expected6 = True
    print(f"Test 6: s = '{s6}', t = '{t6}'")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Single character - not anagram
    s7 = "a"
    t7 = "b"
    result7 = solution.isAnagram(s7, t7)
    expected7 = False
    print(f"Test 7: s = '{s7}', t = '{t7}'")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Different character counts
    s8 = "aab"
    t8 = "aaa"
    result8 = solution.isAnagram(s8, t8)
    expected8 = False
    print(f"Test 8: s = '{s8}', t = '{t8}'")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Classic anagram example
    s9 = "listen"
    t9 = "silent"
    result9 = solution.isAnagram(s9, t9)
    expected9 = True
    print(f"Test 9: s = '{s9}', t = '{t9}'")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Longer strings - valid anagram
    s10 = "conversation"
    t10 = "voices rant on"
    # Remove spaces for testing
    s10_clean = s10.replace(" ", "")
    t10_clean = t10.replace(" ", "")
    result10 = solution.isAnagram(s10_clean, t10_clean)
    expected10 = True
    print(f"Test 10: s = '{s10_clean}', t = '{t10_clean}'")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Different lengths
    s11 = "abc"
    t11 = "ab"
    result11 = solution.isAnagram(s11, t11)
    expected11 = False
    print(f"Test 11: s = '{s11}', t = '{t11}'")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Valid Anagram Problem Constraints:
- s and t consist of lowercase English letters
- 1 <= s.length, t.length <= 5 * 10^4
"""

if __name__ == "__main__":
    test_valid_anagram() 