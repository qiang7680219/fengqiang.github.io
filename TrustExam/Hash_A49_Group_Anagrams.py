#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guanglinzhou(z00522822)
# @Version : $Id$

"""
思路：单个字符串排序，作为字典键，将字符串作为字典值存储
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for st in strs:
            key = tuple(sorted(st))
            dic[key] = dic.get(key, []) + [st]
            #dic[key] = dic.get(key, []).append(st)
        return list(dic.values())



    def test(self):
        #print(self.lengthOfLongestSubstring('pwwkew'))
        print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


solution = Solution()
solution.test()
