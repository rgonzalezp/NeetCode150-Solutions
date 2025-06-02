from typing import List

class Solution:

    #Time Complexity: O(nsquared) because we are checking all the list elements once for every element in the list (approximately)
    #Space Complexity: O(n) where n is the size of the initial list. We store one value per temperature in results.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []
        for i in range(len(temperatures)):
            daysCooler = 0
            foundWarmer = False
            for j in range(len(temperatures)-i):
                if j+i != i and temperatures[j+i] <= temperatures[i]:
                    daysCooler +=1
                    continue
                elif j+i == i and temperatures[j+i] <= temperatures[i]:
                    daysCooler +=1
                    continue
                elif temperatures[j+i] > temperatures[i]:
                    foundWarmer = True
                    break
            if foundWarmer:
                result.append(daysCooler)
            else:
                result.append(0)
            


        return result

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Daily Temperatures...")
    print("=" * 35)
    
    # Test case 1: [30,38,30,36,35,40,28] -> [1,4,1,2,1,0,0]
    temperatures = [30,38,30,36,35,40,28]
    result = solution.dailyTemperatures(temperatures)
    
    print(f"Input: temperatures = {temperatures}")
    print(f"Output: {result}")
    print(f"Expected: [1, 4, 1, 2, 1, 0, 0]")
    print(f"Verification: {'✓ Correct' if result == [1, 4, 1, 2, 1, 0, 0] else '✗ Incorrect'}")
    
    # Show step-by-step explanation
    print("\nStep-by-step explanation:")
    for i, temp in enumerate(temperatures):
        days = result[i]
        if days > 0:
            warmer_temp = temperatures[i + days]
            print(f"Day {i} (temp {temp}): {days} days until warmer temp {warmer_temp}")
        else:
            print(f"Day {i} (temp {temp}): No warmer day ahead") 