class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i, val in enumerate(nums):
            remainder = target - val
            if (remainder in hash):
                return sorted([hash[remainder], i])
            else:
                hash[val] = i
                

