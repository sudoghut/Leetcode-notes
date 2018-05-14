class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumList = []
        ans = nums[0]
        sumNum = 0
        for i in nums:
            print("i:%d"%i)
            sumNum+=i
            print("sumNumi:%d"%sumNum)
            print("ans:%d"%ans)
            ans = max(sumNum, ans)
            print("Final Ans:%d"%ans)
            print()
            sumNum = max(sumNum, 0)
        return ans

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
