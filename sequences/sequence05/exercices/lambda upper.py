def upper(word): return "".join([chr(ord(c) + (ord('A') - ord('a'))) for c in word])


print(upper("test"))
