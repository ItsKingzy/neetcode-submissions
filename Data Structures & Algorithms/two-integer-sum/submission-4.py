class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, val in enumerate(nums):
            remainder = target - val
            if remainder not in hash.keys():
                hash[val] = i
            else:
                return [hash[remainder], i]

                

