import unittest


def subarray_sums(numbers, sum):
    """Determine the contiguous sub-array which adds up to the given sum

    :param numbers: The array of positive integer numbers which can add up to the sum
    :param sum: The given sum to add upto
    :return: The first contiguous sub-array which adds to the given sum
    """
    lookup = [-1] * len(numbers)
    lookup[0] = numbers[0]

    if lookup[0] >= sum:
            return [lookup[0]] if lookup[0] == sum else None

    end = None

    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] >= sum and end is None:
            end = i
  
    assert end is not None, "Sum is larger than given numbers"

    for i2 in xrange(end, len(numbers)):
        if (lookup[i2]-sum) in lookup[:end]:
            return numbers[lookup.index(lookup[i2]-sum)+1:end+1]
        end += 1
    
    return None


class TestSubarraySums(unittest.TestCase):
    def test_valid(self):
        self.assertEquals(subarray_sums([1, 4, 20, 3, 10, 5], 33), [20, 3, 10])
        self.assertEquals(subarray_sums([1, 4, 0, 0, 3, 10, 5], 7), [4, 0, 0, 3])
        self.assertEqual(subarray_sums([1, 3, 10, 5, 1, 6], 16), [10, 5, 1])

    def test_invalid(self):
        self.assertEquals(subarray_sums([1, 4], 0), None)

if __name__ == "__main__":
    unittest.main()

