#287 寻找重复数
#解法一：
#使用同向双指针的思路，一个指针快，一个指针慢，第一个指针左边都是处理过的数据，第二个指针右边是待处理的数据，两指针之间为不需要的数据。
#对应到本题，第一个指针左边就是未重复的，何时两个指针的值无差异即相同了，循环终止。
#写法一：这个写法有点多余，其实一个指针应该就够了，因为排序后重复一定是前后两个重复，不需要两个指针
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
  
#写法二：
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #如果发现有数据重复一定是前后两个相连的数据
        #所以其实一个指针就够了
        #首先对数据排序
        i=0
        nums.sort()
        while(i<len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
            i+=1
