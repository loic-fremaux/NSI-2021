def palindrome(word: str):
    """
    check if a given word is a palindrome
    :param word: to check
    :return: True if the word is a palindrome or else False
    """
    palindrome = ""
    n = len(word) - 1
    for i in range(len(word)):
        palindrome += word[n - i]
    return word == palindrome


print(palindrome("test"))
print(palindrome("tenet"))
