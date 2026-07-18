class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        s= s.lower()
        for ch in s:
            if ch.isalnum():
                clean +=ch

        if clean == clean[::-1]:
            return True
        else:
            return False
                   
        