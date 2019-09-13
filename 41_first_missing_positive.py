from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        nums = [n for n in nums if n > 0]

        if len(nums) == 0:
            return 1

        for idx, actual_num in enumerate(nums):
            expected_num = idx + 1
            if actual_num != expected_num:
                return expected_num

        return nums[-1] + 1
