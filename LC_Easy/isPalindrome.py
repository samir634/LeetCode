class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        str_x = str(x)
        
        # Compare the string with its reverse
        return str_x == str_x[::-1]

# Create an instance of the Solution class
sol = Solution()

# Call the isPalindrome method with a palindrome number
print(sol.isPalindrome(121))  # Should print: True

# Call the isPalindrome method with a non-palindrome number
print(sol.isPalindrome(123))  # Should print: False