class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        arr = []
        for i,v in enumerate(str(x)):
                arr.append(v)
        arr_rev = arr[::-1]
        output = ""
        for i in arr_rev:
            output+=i
        if output[-1] == "-":
            output = "-"+output[:-1]
        int_output = int(output)
        if abs(int_output)<=2147483647:
            return int_output
        else:
            return 0

a = Solution()
print(a.reverse(147483647))
