def findStrIndex(letter, index, s):
    output = []
    for i in range(len(s)):
        if letter == s[i]:
            output.append(i+index)
    return output

def palindromeStrFound(index, candidate, s):
    str = s[index:candidate+1]
    revStr = str[::-1]
    if str == revStr and len(str)>1:
        return str
    else:
        return ""
        
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromicStr = ""

        for i in range(len(s)):
            currentLetter = s[i]
            indexFound = findStrIndex(currentLetter,i, s[i:])
            for j in indexFound:
                strFound = palindromeStrFound(i, j, s)
                if strFound!="" and len(palindromicStr)<len(strFound):
                    palindromicStr = strFound
        if palindromicStr == "":
            if len(s)<2:
                palindromicStr = s
            else:
                palindromicStr = s[0]
        return palindromicStr

a = Solution()
print(a.longestPalindrome("ababba"))