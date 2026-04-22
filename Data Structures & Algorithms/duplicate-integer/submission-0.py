class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i, val in enumerate(nums):
            if (val not in hash):
                hash[val] = 1
            else:
                return True
        
        return False
