
def isPalindrome(x):
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x

def isPalindromeHash(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    tmp = x
    reversed_num = 0
    
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    tmp = x == reversed_num or x == reversed_num // 10

    return tmp


if __name__ == '__main__':

    nums = 121
    # nums = -121

    target = 'yes'

    k= isPalindrome(nums)
    print("é palindromo a:",k)
    
    k= isPalindromeHash(nums)
    print("é palindromo a:",k)

# 9. Palindrome Number