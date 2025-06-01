class TimeMap:

    def __init__(self):
        self.data = {}
        self.mostRecentKey = None
        self.mostRecentValue = None
        self.mostRecentTimestamp = None
    
    #Time complexity of set function is O(nLogN) bounded by the sorting operation which is mandatory to maintain the expected order of the timestamps of the array. Insertion into the array is O(1) because we just append at the end of the list.
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value,timestamp))
            self.mostRecentKey = key
            self.mostRecentValue = value
            self.mostRecentTimeStamp = timestamp
        else:
            self.data[key] = [(value,timestamp)]
            self.mostRecentKey = key
            self.mostRecentValue = value
            self.mostRecentTimeStamp = timestamp
        
        self.data[key] = sorted(self.data[key], key = lambda item: item[1])
    
    ##Time complexity of get function is O(n) where N is equal to the size of the array we are exploring, at worst we need to go through all the values for the array with the corresponding key. O(1) space complexity, self explanatory. The reversed() function is an O(1) operation that creates an iterator object that knows how to loop backwards… it doesn't literally create a copy of the list reversed.
    
    def get(self, key: str, timestamp: int) -> str:
        foundStamp = ""
        
        ## run in reverse and then return the first one that is lower.
        if key in self.data:
            for tuples in reversed(self.data[key]):
                if tuples[1] <= timestamp:
                    return tuples[0]
        
        return foundStamp

# Single test case for debugging
if __name__ == "__main__":
    timeMap = TimeMap()
    
    # Test case for debugging - Example from problem
    print("Testing Time Based Key-Value Store...")
    print("=" * 40)
    
    # Operations from the example
    timeMap.set("alice", "happy", 1)
    print("set('alice', 'happy', 1)")
    
    result1 = timeMap.get("alice", 1)
    print(f"get('alice', 1) = '{result1}' (Expected: 'happy')")
    
    result2 = timeMap.get("alice", 2)
    print(f"get('alice', 2) = '{result2}' (Expected: 'happy')")
    
    timeMap.set("alice", "sad", 3)
    print("set('alice', 'sad', 3)")
    
    result3 = timeMap.get("alice", 3)
    print(f"get('alice', 3) = '{result3}' (Expected: 'sad')")
    
    print("\nVerification:")
    print(f"✓ Test 1: {result1 == 'happy'}")
    print(f"✓ Test 2: {result2 == 'happy'}")
    print(f"✓ Test 3: {result3 == 'sad'}") 