class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        quene = []
        for i in s:
            if i in ["(","{","["]:
                quene.append(i)
            elif i in [")","}","]"]:
                if len(quene)==0:
                    return False
                if i==")" and quene[-1]=="(":
                    quene = quene[:-1]
                elif i=="}" and quene[-1]=="{":
                    quene = quene[:-1]
                elif i=="]" and quene[-1]=="[":
                    quene = quene[:-1]
                else:
                    return False
        if len(quene)>0:
            return False
        else:
            return True
test = Solution()
print(test.isValid("[(])"))
