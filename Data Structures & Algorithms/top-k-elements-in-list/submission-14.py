from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store counts for each
        num_counts = defaultdict(int)
        # list where index is the count and item = list of values for that count
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            num_counts[num] += 1
        for n,c in num_counts.items():
            freq[c].append(n)
        top_k = []
        for i in range(len(freq)-1, 0, -1):
            for number in freq[i]:
                top_k.append(number)
                if len(top_k) == k:
                    return top_k
        

