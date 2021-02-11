def conv_bin(n: int) -> tuple:
    bits = []
    while n > 0:
        bits.append(n % 2)
        n //= 2

    bits.reverse()
    return bits, len(bits)


print(conv_bin(9))
print(conv_bin(42))
