import unittest


def odd_even_occurrence(numbers):
    """Challenge: Given an array of positive integers; all numbers occur an
    even number of times except one number which occurs an odd number of times.

    Find the number in O(n) time & constant space.

    :param numbers: A list of integers where only 1 number occurs an odd amount of times
    :return: the number which occurs an odd amount of times
    """

    total = 0

    for num in numbers:
        total = total ^ num

    return total


class TestOddEvenOccurrence(unittest.TestCase):
    def test_normals(self):
        self.assertEquals(odd_even_occurrence([3, 3, 1, 0, 0, 5, 1, 0, 8, 8, 0]), 5)
        self.assertEqual(odd_even_occurrence([1, 0, 1, 0, 1]), 1)
        self.assertEqual(odd_even_occurrence([1, 2, 3, 4, 5, 5, 4, 3, 2, 2, 2]), 1)


if __name__ == "__main__":
    unittest.main()