#贪心算法，对孩子胃口和饼干大小排序，优先满足胃口小的孩子
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child=0
        biscuit=0
        while(child<len(g) and biscuit<len(s)):
            if(g[child]<=s[biscuit]):
                child+=1
            biscuit+=1
        return child
