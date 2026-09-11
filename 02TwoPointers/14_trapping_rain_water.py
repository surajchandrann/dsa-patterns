# Trapping Rain Water
# Hard
# Topics
# Company Tags
# Hints
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the total amount of water that can be trapped between the bars.


# Example 1:



# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
# Constraints:

# 1 <= height.length <= 20,000
# 0 <= height[i] <= 100,000

from typing import List
class Solution:
    def trapping_rain_water(self,height:List[int]):
        if not height:return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                res+=left_max - height[l]
            else:
                r-=1
                right_max = max(right_max,height[r])
                res += right_max - height[r]

        return res


soln = Solution()
print(soln.trapping_rain_water([0,2,0,3,1,0,1,3,2,1]))