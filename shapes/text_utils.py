def is_palindrome(text):
    # make lowercase & remove spaces
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

