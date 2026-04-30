"""
Name - Valid Palindrom
Topics - Two Pointers, Stringss 
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = list()
        for i in s:
            if i.isalnum():
                d.append(i.lower())
        
        d_str = "".join(d)
        print(d_str)
        return d_str == d_str[::-1]
    

sol = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
print(sol)


"""
1. Convert all the letters to lowercase.
2. remove all characters other than alphanumeric


we can check if a character is alpha numeric by 2 ways
1. using isalnum() method
2. using ASCII values of 'A-Z', 'a-z' and '0-9' and using ord() fuction
"""