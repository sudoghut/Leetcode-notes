class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        count = -1
        for i in nums:
            count+=1
            if i >= target:
                index = count
                break
        if index == -1:
            index = len(nums)
        return index
