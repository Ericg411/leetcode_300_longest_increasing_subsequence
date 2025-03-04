from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            count = 1
            prev = 0
            for j in range(i):
                print(f"prev: {prev}, nums[j]: {nums[j]}, nums[i]: {nums[i]}")
                if prev < nums[j] < nums[i]:
                    print("Entered")
                    prev = nums[j]
                    count += 1
            if count > result:
                result = count
                print(f"Updated result: {result}")


        return result