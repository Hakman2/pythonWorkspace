def is_palindrome(text):
    # make lowercase & remove spaces
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Examples
print(is_palindrome("madam"))       # True
print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("Nurses run"))  # True
