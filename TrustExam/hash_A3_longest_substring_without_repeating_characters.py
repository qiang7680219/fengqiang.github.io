class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = list()
        n = len(s)
        left,right = 0,0
        res = 0

        #except process
        if n == 0:
            return res

        for left in range(n):
            if left != 0:
                subString.remove(s[left -1])

            while right < n  and s[right] not in subString:
                subString.append(s[right])
                right += 1

            res = max(res,len(subString))


        return res



        """
        hashTable = list()

        n =  len(s)
        j = 0

        for i in range(n):
            if s[i] in hashTable[j]:
                j += 1

            else:
                hashTable[j].append(s[i])


        return max(hashTable)
       """

    def test(self):
        #print(self.lengthOfLongestSubstring('pwwkew'))
        print(self.lengthOfLongestSubstring('p'))


solution = Solution()
solution.test()