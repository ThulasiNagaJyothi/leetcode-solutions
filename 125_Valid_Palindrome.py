class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        empty = ""
        for i in s:
            if i.isalnum() :
                empty = empty + i
        return empty == empty[: : -1]