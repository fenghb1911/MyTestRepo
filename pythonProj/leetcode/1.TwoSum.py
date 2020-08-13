from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        seen_values = {}
        for index, value in enumerate(nums):
            if target - value in seen_values:
                return [seen_values[target-value], index]
            else:
                seen_values[value] = index

        return None

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    findlist = s.twoSum(nums, target)
    print(findlist)
