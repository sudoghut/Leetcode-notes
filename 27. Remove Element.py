class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        output = 0
        token = 0
        if len(nums)<1:
            return 0
        while token==0:
            if nums[index]==val:
                del nums[index]
            else:
                output+=1
                index+=1
            if index>len(nums)-1:
                token = 1
        return output