"""
problem URL - https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None




"""
# Working

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                num_sum = nums[i] + nums[j]
                if num_sum == target:
                    return [i, j]
        return None

This approach is BRUTE FORCE Approach where I iterate through arrays multiple times to get to the solution.
Time Complexity - O(n^2)
# Learn how to calculate space complexity

"""



"""
# Failed Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1
            for j in range(len(nums)):
                num_sum = nums[i] + nums[j]
                if num_sum == target:
                    return [i, j]
        return None
        
I have defined j here above thinking the loop will start from 1 but in a iteration it starts from 0 to range
ques - how to iterate arrary from any position like not from 0 like 1 to that range       
"""


nums = [3,2,4]
target = 6
sol = Solution().twoSum(nums=nums, target=target)

print(sol)