from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Sort keys based on frequency in descending order
        sorted_keys = sorted(freq, key=freq.get, reverse=True)
        
        # Return the top k frequent elements
        return sorted_keys[:k]

solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3,3], k=2))
