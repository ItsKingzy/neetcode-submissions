class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

# -4 -1 -1 0 1 2

        for i in range(len(nums)):
            # if num is positive 
            if nums[i] > 0:
                return answer
            
            # Skip all duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            else:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    currSum = nums[i] + nums[left] + nums[right]
                    if currSum > 0:
                        right -= 1
                    if currSum < 0:
                        left += 1
                    if currSum == 0:
                        answer.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Duplicates
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        
        return answer
                        