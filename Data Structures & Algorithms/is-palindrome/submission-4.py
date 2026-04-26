class Solution:
    def isPalindrome(self, s: str) -> bool:    
        # Initialize 2 pointers
        left = 0 # First element
        right = len(s) - 1 # Last element

        # Loop through to see if is palindrome
        while left < right:
            # Check right pointer
            while left < right and not s[left].isalnum():
                left += 1
            
            # Check left pointer
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[right].lower() != s[left].lower():
                return False
            
            # Increment and decrement right pointer and left pointer, respectively, for next iteration
            left += 1
            right -= 1
        
        return True


        