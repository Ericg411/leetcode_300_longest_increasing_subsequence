from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        dp = []

        for num in nums:
            pos = bisect.bisect_left(dp, num)
            if pos < len(dp):
                dp[pos] = num
            else:
                dp.append(num)

        return len(dp)