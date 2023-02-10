def palindrome(s):
    if(s == s[::-1]):
        return True
    else:
        return False


print(palindrome('hello'))
print(palindrome('madam'))