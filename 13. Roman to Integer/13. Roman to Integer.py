class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_before = 0
        num_now = 0
        result = 0
        for i in s:
            if i=="I": num_now = 1
            if i=="V": num_now = 5
            if i=="X": num_now = 10
            if i=="L": num_now = 50
            if i=="C": num_now = 100
            if i=="D": num_now = 500
            if i=="M": num_now = 1000
            if num_before==0:
                result = 0
            elif num_before!=0:
                if num_now<=num_before:
                    result+=num_before
                else:
                    result-=num_before
            num_before=num_now
            print(result)
        if num_now<=num_before:
            result+=num_now
        else:
            result-=num_before
        return result
test = Solution()
print(test.romanToInt("DCXXI"))
