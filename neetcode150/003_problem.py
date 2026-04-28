"""
Name - Contains Duplicate
Type - Arrays and Hashing
https://leetcode.com/problems/contains-duplicate/
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()

        for num in nums:
            if num in unique_elements:
                return True
            else:
                unique_elements.add(num)
        return False