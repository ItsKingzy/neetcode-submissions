class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        topK = [[] for i in range(len(nums) + 1)] # +1 since we need the last index to be the size of the arr

        # O(n)
        for i, val in enumerate(nums):
            if val not in hash:
                hash[val] = 1
            else:
                hash[val] += 1
        
        # O(n)
        for num, val in hash.items():
            topK[val].append(num)
        
        answer = []
        # O(n) since we only need to loop through the elements at most O(n + N) times or just O(n)
        for i in range(len(topK) - 1, 0, -1):
            if topK[i] == []:
                continue
            else:
                for j in topK[i]:
                    answer.append(j)
                    if len(answer) == k:
                        return answer
        

            
        



