from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in heapq.nsmallest(k, Counter(nums).items(), key=lambda x: -x[1])]

