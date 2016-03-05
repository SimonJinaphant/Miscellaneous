import unittest


def generate_bitwise_ones(n):
    """Generate a binary number with n amounts of '1's

    :param n: The amount of '1's to generate
    :return: A binary of only '1's that is of size n
    """

    return (1 << n) - 1


def generate_bitwise_range(upper, lower):
    """Generate a binary number with '1's between the bit index range
    Precondition: upper > lower

    :param upper: The upper bit index (inclusive)
    :param lower: The lower bit index (inclusive)
    :return: A binary with (:upper - :lower + 1) amount of '1's shifted by :lower bits
    """

    return generate_bitwise_ones(upper+1) & ~generate_bitwise_ones(lower)


def set_bits(n, m, upper, lower):
    """Given two binary numbers, set the first binary's bits between i and j to that of m
    Precondition: ||n|| > ||m||

    :param n: The larger binary to be changed
    :param m: The smaller binary to be set
    :param upper: The lower bit index (inclusive)
    :param lower: The upper bit index (inclusive)
    :return: n with its :upper and :lower bits (both inclusive) matching that of m
    """

    n &= ~generate_bitwise_range(upper, lower)
    m <<= lower

    return n | m


class BitwiseRangeTest(unittest.TestCase):

    def test_normals(self):
        self.assertEqual(set_bits(0b10000000000, 0b111, 3, 1), 0b10000001110)
        self.assertEqual(set_bits(0b10000001000, 0b10101, 6, 2), 0b10001010100)

if __name__ == "__main__":
    unittest.main()