# Container With Most Water
# Medium
# Topics
# Company Tags
# Hints
# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.


# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.


# Example 2:

# Input: height = [2,2,2]

# Output: 4

# Constraints:

# 2 <= height.length <= 100,000
# 0 <= height[i] <= 10,000


from typing import List
class Solution:
    def container_with_most_water(self, heights:List[int]):
        res = 0
        l , r= 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return res

soln = Solution()
print(soln.container_with_most_water(heights = [1,7,2,5,4,7,3,6]))