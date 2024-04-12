class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1  
        left_max, right_max = 0, 0  
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        
        return water

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
sol = Solution()
print(sol.trap(height1))  # 6
print(sol.trap(height2))  # 9
