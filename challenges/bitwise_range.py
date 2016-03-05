def generate_bitwise_ones(n):
    return (1 << n) - 1


def generate_bitwise_range(n, m):
    return generate_bitwise_ones(n) & ~generate_bitwise_ones(m)


def set_bits(n, m, i, j):
    n &= ~generate_bitwise_range(j+1, i)
    m <<= i
    return n | m

print bin(set_bits(0b10000001000, 0b10101, 2, 6))