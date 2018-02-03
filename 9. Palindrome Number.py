class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (str(x)[::-1] == str(x))!=True:
            return False
        
        if str(x)[::-1] == str(x):
            return True
        else:
            False