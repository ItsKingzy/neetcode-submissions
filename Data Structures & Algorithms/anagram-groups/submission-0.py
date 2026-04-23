class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        anagrams = []

        for i, val in enumerate(strs):
            str = "".join(sorted(val))
            if (str not in hash):
                hash.setdefault(str, [])
            
            hash[str].append(val)
        
        for arr in hash.values():
            anagrams.append(arr)
        
        return anagrams

