def trim(s):
    for i in s:
        if i == " ":
            s = s[1:]
        else:
            break
    countBlank = 0
    for i in range(1, len(s)):
        index = -i
        if s[index] == " ":
            countBlank+=1
        else:
            break
    if countBlank!= 0:
        s = s[:-countBlank]
    return s

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        output = 0
        hasBlank = 0
        s = trim(s)
        length = len(s)
        if s == "":
            return 0
        for i in range(1, length):
            index = -i
            if s[index]==" ":
                hasBlank = 1
                output = count
                break
            else:
                count+=1
        if hasBlank == 0:
            output = length
        return output
