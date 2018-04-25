class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        output = ""
        leftBlank = 1
        isMinus = 0
        while leftBlank==1:
            if len(str)<=0:
                break
            if str[0] == " ":
                str = str[1:]
            else:
                if str[0] == "-":
                    isMinus = 1
                    str = str[1:]
                elif str[0] == "+":
                    str = str[1:]
                leftBlank = 0
                
        for i in str:
            if i in ["0","1","2","3","4","5","6","7","8","9"]:
                output+=i
            else:
                break
        if output == "":
            output = "0"
        numOutPut = int(output)
        if numOutPut >= 2147483648:
            if isMinus == 0:
                numOutPut = 2147483647
            else:
                numOutPut = 2147483648
        if isMinus == 1:
            numOutPut = -numOutPut
        return numOutPut
a = Solution()
print(a.myAtoi("2147483648"))
