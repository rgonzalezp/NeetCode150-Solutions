from solution import Solution

def test_non_cyclical_number():
    solution = Solution()
    
    print("Testing Non-Cyclical Number (Happy Number) Solution...")
    print("=" * 55)
    
    # Test Case 1: Basic happy number example
    print("Test 1: Basic happy number n = 100")
    n1 = 100
    result1 = solution.isHappy(n1)
    expected1 = True
    print(f"Input: {n1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Explanation: 1² + 0² + 0² = 1")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: Basic unhappy number example
    print("Test 2: Basic unhappy number n = 101")
    n2 = 101
    result2 = solution.isHappy(n2)
    expected2 = False
    print(f"Input: {n2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Explanation: 1² + 0² + 1² = 2 → ... → cycle detected")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Single digit happy number
    print("Test 3: Single digit happy number n = 1")
    n3 = 1
    result3 = solution.isHappy(n3)
    expected3 = True
    print(f"Input: {n3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Explanation: 1² = 1 (already happy)")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Another single digit happy number
    print("Test 4: Single digit happy number n = 7")
    n4 = 7
    result4 = solution.isHappy(n4)
    expected4 = True
    print(f"Input: {n4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Explanation: 7² = 49 → 4² + 9² = 97 → 9² + 7² = 130 → 1² + 3² + 0² = 10 → 1² + 0² = 1")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: Single digit unhappy number
    print("Test 5: Single digit unhappy number n = 2")
    n5 = 2
    result5 = solution.isHappy(n5)
    expected5 = False
    print(f"Input: {n5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Explanation: 2² = 4 → 4² = 16 → 1² + 6² = 37 → ... → cycle")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Two digit happy number
    print("Test 6: Two digit happy number n = 19")
    n6 = 19
    result6 = solution.isHappy(n6)
    expected6 = True
    print(f"Input: {n6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Explanation: 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Two digit unhappy number
    print("Test 7: Two digit unhappy number n = 20")
    n7 = 20
    result7 = solution.isHappy(n7)
    expected7 = False
    print(f"Input: {n7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Explanation: 2² + 0² = 4 → 4² = 16 → ... → cycle")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Three digit happy number
    print("Test 8: Three digit happy number n = 130")
    n8 = 130
    result8 = solution.isHappy(n8)
    expected8 = True
    print(f"Input: {n8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Explanation: 1² + 3² + 0² = 10 → 1² + 0² = 1")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Three digit unhappy number
    print("Test 9: Three digit unhappy number n = 145")
    n9 = 145
    result9 = solution.isHappy(n9)
    expected9 = False
    print(f"Input: {n9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Explanation: 1² + 4² + 5² = 42 → 4² + 2² = 20 → 2² + 0² = 4 → ... → cycle")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Boundary value (maximum constraint)
    print("Test 10: Boundary value n = 1000")
    n10 = 1000
    result10 = solution.isHappy(n10)
    expected10 = True
    print(f"Input: {n10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Explanation: 1² + 0² + 0² + 0² = 1")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Happy number with all same digits
    print("Test 11: All same digits n = 111")
    n11 = 111
    result11 = solution.isHappy(n11)
    expected11 = False
    print(f"Input: {n11}")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"Explanation: 1² + 1² + 1² = 3 → 3² = 9 → 9² = 81 → 8² + 1² = 65 → ... → cycle")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Another happy number
    print("Test 12: Happy number n = 23")
    n12 = 23
    result12 = solution.isHappy(n12)
    expected12 = True
    print(f"Input: {n12}")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"Explanation: 2² + 3² = 13 → 1² + 3² = 10 → 1² + 0² = 1")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Non-Cyclical Number (Happy Number) Problem Constraints:
- 1 <= n <= 1000
"""

if __name__ == "__main__":
    test_non_cyclical_number() 