from solution import TimeMap

def test_time_based_key_value_store():
    print("Testing Time Based Key-Value Store Solution...")
    print("=" * 50)
    
    # Test Case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    timeMap1 = TimeMap()
    timeMap1.set("alice", "happy", 1)
    result1_1 = timeMap1.get("alice", 1)
    result1_2 = timeMap1.get("alice", 2)
    timeMap1.set("alice", "sad", 3)
    result1_3 = timeMap1.get("alice", 3)
    
    expected1 = ["happy", "happy", "sad"]
    actual1 = [result1_1, result1_2, result1_3]
    print(f"Expected: {expected1}")
    print(f"Actual: {actual1}")
    print(f"✓ Passed: {actual1 == expected1}\n")
    
    # Test Case 2: Non-existent key
    print("Test 2: Non-existent key")
    timeMap2 = TimeMap()
    result2 = timeMap2.get("nonexistent", 1)
    expected2 = ""
    print(f"get('nonexistent', 1) = '{result2}'")
    print(f"Expected: '{expected2}'")
    print(f"✓ Passed: {result2 == expected2}\n")
    
    # Test Case 3: Timestamp before any set operation
    print("Test 3: Timestamp before any set operation")
    timeMap3 = TimeMap()
    timeMap3.set("key1", "value1", 5)
    result3 = timeMap3.get("key1", 3)
    expected3 = ""
    print(f"set('key1', 'value1', 5) then get('key1', 3) = '{result3}'")
    print(f"Expected: '{expected3}'")
    print(f"✓ Passed: {result3 == expected3}\n")
    
    # Test Case 4: Multiple keys
    print("Test 4: Multiple keys")
    timeMap4 = TimeMap()
    timeMap4.set("key1", "value1", 1)
    timeMap4.set("key2", "value2", 2)
    timeMap4.set("key1", "value3", 3)
    
    result4_1 = timeMap4.get("key1", 1)
    result4_2 = timeMap4.get("key2", 2)
    result4_3 = timeMap4.get("key1", 3)
    result4_4 = timeMap4.get("key2", 3)
    
    expected4 = ["value1", "value2", "value3", "value2"]
    actual4 = [result4_1, result4_2, result4_3, result4_4]
    print(f"Expected: {expected4}")
    print(f"Actual: {actual4}")
    print(f"✓ Passed: {actual4 == expected4}\n")
    
    # Test Case 5: Same timestamp (edge case)
    print("Test 5: Exact timestamp match")
    timeMap5 = TimeMap()
    timeMap5.set("exact", "match", 10)
    result5 = timeMap5.get("exact", 10)
    expected5 = "match"
    print(f"set('exact', 'match', 10) then get('exact', 10) = '{result5}'")
    print(f"Expected: '{expected5}'")
    print(f"✓ Passed: {result5 == expected5}\n")
    
    # Test Case 6: Large timestamp values (boundary)
    print("Test 6: Large timestamp values")
    timeMap6 = TimeMap()
    timeMap6.set("large", "value999", 999)
    timeMap6.set("large", "value1000", 1000)
    result6_1 = timeMap6.get("large", 999)
    result6_2 = timeMap6.get("large", 1000)
    
    expected6 = ["value999", "value1000"]
    actual6 = [result6_1, result6_2]
    print(f"Expected: {expected6}")
    print(f"Actual: {actual6}")
    print(f"✓ Passed: {actual6 == expected6}\n")
    
    # Test Case 7: Sequential updates to same key
    print("Test 7: Sequential updates to same key")
    timeMap7 = TimeMap()
    timeMap7.set("seq", "v1", 1)
    timeMap7.set("seq", "v2", 2)
    timeMap7.set("seq", "v3", 3)
    timeMap7.set("seq", "v4", 4)
    
    result7_1 = timeMap7.get("seq", 1)
    result7_2 = timeMap7.get("seq", 2)
    result7_3 = timeMap7.get("seq", 3)
    result7_4 = timeMap7.get("seq", 4)
    result7_5 = timeMap7.get("seq", 5)  # Future timestamp
    
    expected7 = ["v1", "v2", "v3", "v4", "v4"]
    actual7 = [result7_1, result7_2, result7_3, result7_4, result7_5]
    print(f"Expected: {expected7}")
    print(f"Actual: {actual7}")
    print(f"✓ Passed: {actual7 == expected7}\n")
    
    # Test Case 8: Mixed operations with gaps
    print("Test 8: Mixed operations with timestamp gaps")
    timeMap8 = TimeMap()
    timeMap8.set("gap", "start", 1)
    timeMap8.set("gap", "middle", 50)
    timeMap8.set("gap", "end", 100)
    
    result8_1 = timeMap8.get("gap", 25)   # Should get "start"
    result8_2 = timeMap8.get("gap", 75)   # Should get "middle"
    result8_3 = timeMap8.get("gap", 150)  # Should get "end"
    
    expected8 = ["start", "middle", "end"]
    actual8 = [result8_1, result8_2, result8_3]
    print(f"Expected: {expected8}")
    print(f"Actual: {actual8}")
    print(f"✓ Passed: {actual8 == expected8}\n")
    
    print("All test cases completed!")

# Problem constraints for reference:
"""
Time Based Key-Value Store Problem Constraints:
- 1 <= key.length, value.length <= 100
- key and value only include lowercase English letters and digits
- 1 <= timestamp <= 1000
- For all calls to set, the timestamps are in strictly increasing order
"""

if __name__ == "__main__":
    test_time_based_key_value_store() 