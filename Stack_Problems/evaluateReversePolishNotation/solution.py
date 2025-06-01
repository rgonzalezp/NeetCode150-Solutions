from typing import List

class Solution:

    # Time Complexity: O(N) where N is the number of tokens. Need to go through the entire list to process the operation
    # Space Complexity: O(N) where N is the number of tokens. Although it may seem at first to be O(1), the stack can grow as the array of tokens grow even if it is up to half its size.
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []

        for token in tokens:

            if token == '*':
                o2 = numberStack.pop()
                o1 = numberStack.pop()
                res = o1 * o2
                numberStack.append(res)
            elif token == '-':
                o2 = numberStack.pop()
                o1 = numberStack.pop()
                res = o1 - o2
                numberStack.append(res)
            elif token == '+':
                o2 = numberStack.pop()
                o1 = numberStack.pop()
                res = o1 + o2
                numberStack.append(res)
            elif token == '/':
                o2 = numberStack.pop()
                o1 = numberStack.pop()
                res = int(o1 / o2)
                numberStack.append(res)
            else:
                numberStack.append(int(token))


        return numberStack.pop()

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Evaluate Reverse Polish Notation...")
    print("=" * 45)
    
    # Test case 1: ["1","2","+","3","*","4","-"] -> 5
    tokens = ["1","2","+","3","*","4","-"]
    result = solution.evalRPN(tokens)
    
    print(f"Input: tokens = {tokens}")
    print(f"Output: {result}")
    print(f"Expected: 5")
    print(f"Explanation: ((1 + 2) * 3) - 4 = {((1 + 2) * 3) - 4}")
    print(f"Verification: {'✓ Correct' if result == 5 else '✗ Incorrect'}") 