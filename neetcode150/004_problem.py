"""
Name - Valid Anagram
Type - Arrays and Hashing
https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter

# Second Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)







"""
# First Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length is not same return False
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for i in range(len(s)):
            if s_dict.get(s[i]):
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1


        t_dict = dict()
        for i in range(len(t)):
            if t_dict.get(t[i]):
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1


        for k, v  in s_dict.items():
            if k not in t_dict.keys():
                return False
            
            if t_dict[k] != v:
                return False

        return True

"""

s = "rat"
t = "car"
sol = Solution().isAnagram(s,t)
print(sol)

"""
1. How to iterate through 2 dictionaries to comapre their values - Hint (use zip)
2. s_dict[s[i]] += 1 will increment the value.
3. Best way check if both dictionaries have same keys and values
4. what is the time and space complexity.
5. Learn Counter
6. How are both solutions differ from each other like Counter took 6ms and dict iteration took 19ms
"""