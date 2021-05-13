#287 寻找重复数
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=0
        while(j<len(nums)):
            if(i==0 or nums[i-1]!=nums[j]):
                nums[i]=nums[j]
                i=i+1
                j=j+1
            else:
                return nums[j]
