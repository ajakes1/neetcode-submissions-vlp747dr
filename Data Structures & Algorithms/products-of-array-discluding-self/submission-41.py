from functools import reduce
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        postfixes = []
        output = []

        product = 1
        for i in range(1,len(nums)):
            product*=nums[i-1]
            prefixes.append(product)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            if not postfixes:
                postfixes.append(1)
            else:
                product*=nums[i+1]
                postfixes.insert(0, product)
        for i in range(len(nums)):
            output.append(prefixes[i]*postfixes[i])
        return output
