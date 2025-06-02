from solution import Solution

def test_daily_temperatures():
    solution = Solution()
    
    print("Testing Daily Temperatures Solution...")
    print("=" * 45)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example [30,38,30,36,35,40,28]")
    temperatures1 = [30,38,30,36,35,40,28]
    result1 = solution.dailyTemperatures(temperatures1)
    expected1 = [1,4,1,2,1,0,0]
    print(f"Input: {temperatures1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"✓ Passed: {result1 == expected1}\n")
    
    # Test Case 2: Decreasing temperatures
    print("Test 2: Decreasing temperatures [22,21,20]")
    temperatures2 = [22,21,20]
    result2 = solution.dailyTemperatures(temperatures2)
    expected2 = [0,0,0]
    print(f"Input: {temperatures2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Single temperature
    print("Test 3: Single temperature [73]")
    temperatures3 = [73]
    result3 = solution.dailyTemperatures(temperatures3)
    expected3 = [0]
    print(f"Input: {temperatures3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Increasing temperatures
    print("Test 4: Increasing temperatures [30,40,50,60]")
    temperatures4 = [30,40,50,60]
    result4 = solution.dailyTemperatures(temperatures4)
    expected4 = [1,1,1,0]
    print(f"Input: {temperatures4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"✓ Passed: {result4 == expected4}\n")
    
    # Test Case 5: All same temperatures
    print("Test 5: All same temperatures [50,50,50,50]")
    temperatures5 = [50,50,50,50]
    result5 = solution.dailyTemperatures(temperatures5)
    expected5 = [0,0,0,0]
    print(f"Input: {temperatures5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Two temperatures
    print("Test 6: Two temperatures [30,60]")
    temperatures6 = [30,60]
    result6 = solution.dailyTemperatures(temperatures6)
    expected6 = [1,0]
    print(f"Input: {temperatures6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"✓ Passed: {result6 == expected6}\n")
    
    # Test Case 7: Two temperatures - reverse
    print("Test 7: Two temperatures reverse [60,30]")
    temperatures7 = [60,30]
    result7 = solution.dailyTemperatures(temperatures7)
    expected7 = [0,0]
    print(f"Input: {temperatures7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"✓ Passed: {result7 == expected7}\n")
    
    # Test Case 8: Peak in middle
    print("Test 8: Peak in middle [40,35,32,36,39]")
    temperatures8 = [40,35,32,36,39]
    result8 = solution.dailyTemperatures(temperatures8)
    expected8 = [0,2,1,1,0]
    print(f"Input: {temperatures8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"✓ Passed: {result8 == expected8}\n")
    
    # Test Case 9: Large gap between warmer days
    print("Test 9: Large gap [55,38,35,36,40,60]")
    temperatures9 = [55,38,35,36,40,60]
    result9 = solution.dailyTemperatures(temperatures9)
    expected9 = [5,3,1,1,1,0]
    print(f"Input: {temperatures9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"✓ Passed: {result9 == expected9}\n")
    
    # Test Case 10: Boundary values (min temp)
    print("Test 10: Boundary values with min temp [1,2,3]")
    temperatures10 = [1,2,3]
    result10 = solution.dailyTemperatures(temperatures10)
    expected10 = [1,1,0]
    print(f"Input: {temperatures10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"✓ Passed: {result10 == expected10}\n")
    
    # Test Case 11: Boundary values (max temp)
    print("Test 11: Boundary values with max temp [98,99,100]")
    temperatures11 = [98,99,100]
    result11 = solution.dailyTemperatures(temperatures11)
    expected11 = [1,1,0]
    print(f"Input: {temperatures11}")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"✓ Passed: {result11 == expected11}\n")
    
    # Test Case 12: Complex pattern
    print("Test 12: Complex pattern [34,80,80,34,34,80,34]")
    temperatures12 = [34,80,80,34,34,80,34]
    result12 = solution.dailyTemperatures(temperatures12)
    expected12 = [1,0,0,2,1,0,0]
    print(f"Input: {temperatures12}")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"✓ Passed: {result12 == expected12}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Daily Temperatures Problem Constraints:
- 1 <= temperatures.length <= 1000
- 1 <= temperatures[i] <= 100
"""

if __name__ == "__main__":
    test_daily_temperatures() 