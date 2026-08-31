class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        s1="".join(i.lower() for i in s if i.isalnum())
        r=len(s1)-1
        while l<r:
            if s1[l]!=s1[r]:
                return False
            l+=1
            r-=1
        return True

        