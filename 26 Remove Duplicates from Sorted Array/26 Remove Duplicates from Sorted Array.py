class Solution:
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<2:
            return len(nums)
        for i in range(len(nums)):
            print(nums)
            if i>0 and len(nums)>1:
                if nums[0] != nums[1]:
                    nums.append(nums[0])                    
                del nums[0]
        nums.append(nums[0])
        del nums[0]
        return len(nums)
    
a = Solution
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
