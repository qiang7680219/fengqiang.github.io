class Solution:
    def maxArea(self, height: list) -> int:
        n = len(height)
        left = 0
        right = n - 1
        area = 0

        while left <= right:
            #tmpArea = max(area,(right - left) * min(height[left],height[right]))
            if height[left] < height[right]:
                tmpArea = (right - left) * height[left]
                left += 1
            else:
                tmpArea = (right - left) * height[right]
                right -= 1

            #print('tmpArea=',tmpArea)
            area = max(area,tmpArea)

        return area

    def test(self):
        print(self.maxArea([1,8,6,2,5,4,8,3,7]))


solution = Solution()
solution.test()