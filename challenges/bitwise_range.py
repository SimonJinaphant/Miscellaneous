def generate_bitwise_ones(n):
    """Generate a binary number with n amounts of '1's

    :param n: The amount of '1's to generate
    :return: A binary of only '1's that is of size n
    """
    return (1 << n) - 1


def generate_bitwise_range(n, m):
    """Generate a binary number with '1's between the bit index of n and m
    Precondition: n >= m

    :param n: The upper bit index (inclusive)
    :param m: The lower bit index (inclusive)
    :return: A binary with (n - m) '1's shifted by m bits
    """
    return generate_bitwise_ones(n) & ~generate_bitwise_ones(m)


def set_bits(n, m, i, j):
    """Given two binary numbers, set the first binary's bits between i and j to be m
    Precondition: m just have (j - i) digits and ||n|| > ||m||

    :param n: The larger binary to be changed
    :param m: The smaller binary to be set
    :param i: The lower bit index (inclusive)
    :param j: The upper bit index (inclusive)
    :return:
    """
    n &= ~generate_bitwise_range(j+1, i)
    m <<= i
    return n | m


print bin(set_bits(0b10000001000, 0b10101, 2, 6))