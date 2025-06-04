from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resp = []

        anagrams = {}

        for i,string in enumerate(strs):
            sorted_string = "".join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(i)
            else:
                anagrams[sorted_string] = [i]

        for i in range(len(anagrams)):
            resp.append([])

        for i,anagramkey in enumerate(anagrams):
            for indexes in anagrams[anagramkey]:
                resp[i].append(strs[indexes])
                    
        return resp

# Single test case for debugging
if __name__ == "__main__":
    solution = Solution()
    
    # Test case for debugging
    print("Testing Group Anagrams...")
    print("=" * 30)
    
    # Test case 1: ["act","pots","tops","cat","stop","hat"]
    strs = ["act","pots","tops","cat","stop","hat"]
    result = solution.groupAnagrams(strs)
    
    print(f"Input: strs = {strs}")
    print(f"Output: {result}")
    expected = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
    print(f"Expected (one possible grouping): {expected}")
    print(f"Note: Output order may vary as any order is acceptable")
    
    # Verify correctness by checking if each group contains anagrams
    print("\nVerification:")
    for i, group in enumerate(result):
        if len(group) > 1:
            sorted_chars = ["".join(sorted(word)) for word in group]
            all_same = all(chars == sorted_chars[0] for chars in sorted_chars)
            print(f"Group {i+1} {group}: {'✓ All anagrams' if all_same else '✗ Not all anagrams'}")
        else:
            print(f"Group {i+1} {group}: ✓ Single word group") 