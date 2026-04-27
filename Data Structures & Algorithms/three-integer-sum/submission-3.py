class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort() # Sorting the nums array

        for i in range(len(nums)):
            # if i is positive, return
            if nums[i] > 0:
                return answer

            # Check for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip

            else:
                left = i+1
                right = len(nums) - 1
                while left < right:
                    currSum = nums[i] + nums[left] + nums[right]
                    if currSum < 0:
                        left += 1
                    elif currSum > 0:
                        right -= 1
                    elif currSum == 0:
                        triplet = [nums[i], nums[left], nums[right]]
                        answer.append(triplet)

                        # Increment pointers
                        left += 1
                        right -= 1

                        # Check for duplicates
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        
        return answer
