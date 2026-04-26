class Solution:
    def isPalindrome(self, s: str) -> bool:    
        # Initialize 2 pointers
        p1 = 0 # First element
        p2 = len(s) - 1 # Last element

        # Loop through to see if is palindrome
        while p1 < p2:
            # Check right pointer
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            
            # Check left pointer
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            
            if s[p1].lower() != s[p2].lower():
                return False
            
            # Increment p1 and p2 for next iteration
            p1 += 1
            p2 -= 1
        
        return True


        