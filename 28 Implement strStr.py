class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLen = len(needle)
        if needleLen < 1:
            return 0
        for i in range(len(haystack)):
            if len(haystack[i:])>=needleLen:
                if haystack[i:i+needleLen]==needle:
                    return i
        return -1
        
    
