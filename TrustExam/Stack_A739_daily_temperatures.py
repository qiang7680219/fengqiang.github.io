class Solution:
    def dailyTemperatures(self, T):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        res = [0] * len(T)
        for i, tempe in enumerate(T):
            while stack and tempe > T[stack[-1]]:
                index = stack[-1]
                res[index] = i - stack.pop()
            stack.append(i)
        return res

    def dailyTemperatures2(self, T: list):
        res = list()
        n = len(T)


        for first in range(n):
            second = first + 1
            tmp = 0

            #for j in n
            while second != n and  T[first] >= T[second]:
                tmp += 1
                second += 1

            if second == n:
                tmp = 0
            else:
                tmp += 1


            res.append(tmp)

        return res



    def test(self):
        #print(self.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
        print(self.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

solution = Solution()
solution.test()

