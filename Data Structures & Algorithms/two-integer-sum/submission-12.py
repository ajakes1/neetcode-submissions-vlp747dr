class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i in range(len(nums)):
            num = nums[i]
            difference_needed = target - num
            if (j_index := value_index.get(difference_needed)) is not None and j_index != i:
                return list(sorted([i, j_index]))
            value_index[num] = i
            
            