def is_palindrome(n):
    return n and str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1,1000))
print('1~1000:',list(output))