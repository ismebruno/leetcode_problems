class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = 0
        temp_x = abs(x)
        while temp_x != 0:
            reverse_x *= 10
            reverse_x += temp_x % 10
            temp_x //= 10

        if reverse_x == x:
            return True
        else:
            return False


# Wanted to do it without converting to string
