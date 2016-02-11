import unittest


def max_subarray(numbers):
    """Determine the largest contiguous sub-array which has the largest sum
    :param numbers: An array of integer numbers
    :return: An sub-array of numbers which produces the largest sum
    """
    lookup = [None] * len(numbers)
    lookup[0] = numbers[0]

    end = 0
    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] > lookup[end]:
            end = i

    start = lookup.index(min(lookup)) + 1

    return numbers[start:end+1]


class TestMaxSubarray(unittest.TestCase):
    def test_normal(self):
        self.assertEquals(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])
        self.assertEquals(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]), [4, -1, -2, 1, 5])

if __name__ == "__main__":
    unittest.main()