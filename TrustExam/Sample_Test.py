class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for st in strs:
            #key = tuple(sorted(st))
            key = sorted(st)
            dic[key] = dic.get(key, []) + ['mm']
            #dic[key] = dic.get(key, []).append(st)
        return list(dic.values())



    def test(self):
        #print(self.lengthOfLongestSubstring('pwwkew'))
        print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


solution = Solution()
solution.test()
