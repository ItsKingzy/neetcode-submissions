class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums) # Removes duplicates
        longestSequence = 0

        for num in numsSet:
            # Check if num is beginning of sequence
            if (num - 1) not in numsSet:
                length = 1  # Consider the first num in the sequence
                while ((num + length) in numsSet):
                    length += 1
                longestSequence = max(longestSequence, length) # O(n)
        
        return longestSequence


