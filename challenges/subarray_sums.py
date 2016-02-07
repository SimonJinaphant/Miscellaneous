import unittest


def subarray_sums(numbers, sum):
    lookup = [-1] * len(numbers)
    lookup[0] = numbers[0]

    end = None
    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] >= sum: 
            end = i
            break
  
    assert end is not None, "Sum is larger than given numbers"
  
    start = lookup.index(lookup[end]-sum)
    
    return numbers[start+1:end+1]


class TestSubarraySums(unittest.TestCase):
    def test_valid(self):
        self.assertEquals(subarray_sums([1,4,20,3,10,5], 33), [20, 3, 10])
        self.assertEquals(subarray_sums([1,4,0,0,3,10,5], 7), [4,0,0,3])

    def test_invalid(self):
        self.assertEquals(subarray_sums([1,4], 0), [])

if __name__ == "__main__":
    unittest.main()

