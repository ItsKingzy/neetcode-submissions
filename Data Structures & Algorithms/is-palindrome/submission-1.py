class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Make alnum arr (O(n) space complexity)
        alnumArr = []
        for char in s:
            if char.isalnum():
                alnumArr.append(char.lower())
        
        # Initialize 2 pointers
        p1 = 0 # First element
        p2 = len(alnumArr) - 1 # Last element

        # Loop through to see if is palindrome
        for i in range(len(alnumArr)):
            if (p1 != p2 or p2 - p1 != 1):
                if (alnumArr[p1] != alnumArr[p2]):
                    return False
                # Increment pointers
                p1 += 1
                p2 -= 1
        
        return True


        