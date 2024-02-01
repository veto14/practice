class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        tam = len(nums)
        min = nums[0]*nums[1]
        max = nums[tam-1]*nums[tam-2]
        return (max-min)
