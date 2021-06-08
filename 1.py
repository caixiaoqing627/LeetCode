#双指针解法

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #
        #将数组按大小排序，因为答案只存在一种组合的可能，
        #当确定一个元素的时候，想求另外一个，也可以看成是对元素的搜索
        #用双指针破坏了原来的数组，所以还需要留个备份，用来查找原来的编号，
        #当代码长的时候，一定要注意循环的范围，是不是两段本来应该并列的代码，写到另外一个循环里了，然后今天还学到了就是python里面复制数组不能直接用赋值的形式，用赋值形式复制的只是多了一个指针，但是两个数组实际是一个对象，如果修改其中一个，另外一个也会被修改，需要用list()创建,才是新的数组,在查找的时候还有一个点要注意，就是相同的元素不能用两次，在最后设置那个标签的时候，可以调节，设了-1的最先赋值，尽管j在同一次循环中也被赋值，但是由于后面还会有机会再匹配，j的值会再次被更新为正确的值，所以两个数的赋值写法有差别
        #想投个懒可太不容易了，这道题里各种坑
        nums_copy=list(nums)
        nums.sort()
        i=0
        j=len(nums)-1
        x=0
        y=0
        while(i<j):
            if(nums[i]+nums[j]==target):
                x=nums[i]
                y=nums[j]
                break
            elif(nums[i]+nums[j]<target):
                i=i+1
            else:
                j=j-1

        i,j=-1,-1
        k=0
        #print('nums个数',nums_copy)
        while(k<len(nums_copy)):
            if(nums_copy[k]==x and i==-1):
                i=k
            if(nums_copy[k]==y):   
                j=k
            k=k+1
        return i,j
