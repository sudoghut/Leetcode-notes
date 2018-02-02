class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        index = []
        for i in nums_sorted:
            print(target - i)
            if (target - i) in nums_sorted:
                index_1 = nums.index(i)
                index.append(index_1)
                nums[index_1] = ""
                index_2 = nums.index(target - i)
                return [index_1, index_2]     


a = Solution()
print(a.twoSum([3,3],6))

"""
NOTES:
right the index function by myself will be better than just using index
"""
