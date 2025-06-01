# All operations timecomplexity are O(1) since we do not do any iterations over the stacks
# The data structure itself is O(n) for the stack and O(2n) which is O(n) for the ministack that keeps track of the min value for each insertion
class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack =[]
        self.mini = None
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.mini is None):
            self.mini = val
            self.miniStack.append(val)
            self.miniStack.append(self.mini)
        elif val < self.mini:
            self.mini = val
            self.miniStack.append(val)
            self.miniStack.append(val)
        else:
            self.miniStack.append(val)
            self.miniStack.append(self.mini)
            


    def pop(self) -> None:
        del self.stack[len(self.stack)-1]

        if len(self.miniStack) >2:
            del self.miniStack[len(self.miniStack)-1]
            del self.miniStack[len(self.miniStack)-1]
            self.mini = self.miniStack[len(self.miniStack)-1]
        elif len(self.miniStack)> 1:
            del self.miniStack[len(self.miniStack)-1]
            del self.miniStack[len(self.miniStack)-1]
            self.mini = None
            

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.miniStack[len(self.miniStack)-1]

# Single test case for debugging
if __name__ == "__main__":
    print("Testing Minimum Stack...")
    print("=" * 30)
    
    # Test case from the example
    minStack = MinStack()
    
    print("push(1)")
    minStack.push(1)
    
    print("push(2)")
    minStack.push(2)
    
    print("push(0)")
    minStack.push(0)
    
    min_val = minStack.getMin()
    print(f"getMin() = {min_val} (Expected: 0)")
    
    print("pop()")
    minStack.pop()
    
    top_val = minStack.top()
    print(f"top() = {top_val} (Expected: 2)")
    
    min_val2 = minStack.getMin()
    print(f"getMin() = {min_val2} (Expected: 1)")
    
    print("\nVerification:")
    print(f"✓ Test 1 (getMin): {min_val == 0}")
    print(f"✓ Test 2 (top): {top_val == 2}")
    print(f"✓ Test 3 (getMin after pop): {min_val2 == 1}") 