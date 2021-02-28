class Solution:
    def twoSum(self, nums: list, target: int):

        res = []
        dic = dict()

        #hashTable =

        for i,item in enumerate(nums):
            dic[target - item] = i

        for i,item in enumerate(nums):
            if item in dic and i != dic[item]:
                #res.append(i,index(dic[target - item])
                #res.append(i)
                #res.append(dic[item])
                return [i,dic[item]]

        #return res

    def test(self):
        print(self.twoSum([3, 2, 4], 6))

solution = Solution()
solution.test()