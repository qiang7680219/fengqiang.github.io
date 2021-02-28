class Solution:
    def singleNumber(self, nums: list):
        n = len(nums)
        nums.sort()
        i = -1
        print(nums)

        while i < n:
            #i += 2
            print('i = ',i)



            if i == -1 or nums[i] == nums[i - 1]:
                i += 2
                #continue
            else:
                return nums[i - 1]

            #i += 2
        if i == n:
            return nums[-1]


        """
        for item in nums:
            if nums.count(item) == 1:
                return item
        """


    def test(self):
        #print(self.lengthOfLongestSubstring('pwwkew'))
        print(self.singleNumber([4,2,1,2,1]))


solution = Solution()
solution.test()