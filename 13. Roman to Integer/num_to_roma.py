class Solution:
    def st_10(self, s):
        if s==0: return ""
        elif s==1: return "I"
        elif s==2: return "II"        
        elif s==3: return "III"
        elif s==4: return "IV"
        elif s==5: return "V"
        elif s==6: return "VI"
        elif s==7: return "VII"
        elif s==8: return "VIII"
        elif s==9: return "IX"
        elif s==10: return "X"
    def st_100(self, s):
        if s==0: return "" 
        elif s==2: return "XX"        
        elif s==3: return "XXX"
        elif s==4: return "XL"
        elif s==5: return "L"
        elif s==6: return "LX"
        elif s==7: return "LXX"
        elif s==8: return "LXXX"
        elif s==9: return "XC"
        elif s==10: return "C"
    def st_1000(self, s):
        if s==2: return "CC"        
        elif s==3: return "CCC"
        elif s==4: return "CD"
        elif s==5: return "D"
        elif s==6: return "DC"
        elif s==7: return "DCC"
        elif s==8: return "DCCC"
        elif s==9: return "CM"
        elif s==10: return "M"          
    def st_3999(self, s):
        if s==2: return "MM"        
        elif s==3: return "MMM"

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s<=10:
            return self.st_10(s)
        elif s<=100:
            ten_num = self.st_100(int(str(s)[0]))
            digit_num = self.st_10(int(str(s)[1]))
            return ten_num+digit_num
        elif s<1000:
            hun_num = self.st_1000(int(str(s)[0]))
            ten_num = self.st_100(int(str(s)[1]))
            digit_num = self.st_10(int(str(s)[2]))
            return hun_num+ten_num+digit_num
        elif s<=3999:
            thr_num = self.st_3999(int(str(s)[0]))
            hun_num = self.st_1000(int(str(s)[1]))
            ten_num = self.st_100(int(str(s)[2]))
            digit_num = self.st_10(int(str(s)[3]))
            return thr_num+hun_num+ten_num+digit_num
            
test = Solution()
print(test.romanToInt(3990))
