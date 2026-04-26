class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        sortedNums = sorted(set(nums)) # O(nlogn)
        
        count = 1
        LCS = []

        for i in range(1, len(sortedNums)):
            if sortedNums[i-1] == sortedNums[i] - 1:
                count += 1
            else:
                LCS.append(count)
                count = 1
        
        LCS.append(count)

        return max(LCS)

